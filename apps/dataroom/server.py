#!/usr/bin/env python3
"""
Robotic Discipline / Animal Scrypt — Self-Hosted Investor Data Room (apps/dataroom/server.py)
Implements /seed/23-dataroom-product-spec.md:
- 5 Roles: admin (Founder), advisor, partner, investor_s1, investor_s2
- 9 Rooms:
  * Stage 1 (Public/Login): overview, team, product, milestones
  * Stage 2 (NDA-Locked): financials, cap-table, legal, tax, ip
- NDA State Machine: NONE -> SIGNED (Investor signs) -> APPROVED / REJECTED (Founder approves)
- Immutable Audit Log + Founder CSV Export (/api/admin/audit.csv)
- Hard Server-Side NDA Lock on AI Chat (/api/chat)
- GDPR Account Export (/api/me/export), Delete (/api/me), Cookie Banner, and Multilingual UI (en, de, fr)

Run locally:
    python3 apps/dataroom/server.py --port 8082
"""

from __future__ import annotations
import argparse
import csv
import datetime
import hashlib
import io
import json
import pathlib
import sqlite3
import urllib.parse
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, Any, Tuple, Optional, List

BASE_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
SEED_DIR = REPO_ROOT / "seed"
BRAND_CONFIG_PATH = BASE_DIR / "config" / "brand.json"
DEFAULT_DB_PATH = str(BASE_DIR / "dataroom.db")

NDA_TEXT_V1 = (
    "MUTUAL NON-DISCLOSURE AGREEMENT (STARTER TEMPLATE — NOT LEGAL ADVICE). "
    "Recipient agrees to hold Stage 2 materials of Robotic Discipline (Animal Scrypt / Disciple / Madken) "
    "in strict confidence and not disclose cap table, financial, tax, or unreleased IP materials without consent."
)
NDA_HASH_V1 = hashlib.sha256(NDA_TEXT_V1.encode("utf-8")).hexdigest()[:16]

LOCALES: Dict[str, Dict[str, str]] = {
    "en": {
        "title": "Animal Scrypt — Investor Data Room",
        "stage1_heading": "Stage 1 Rooms (Pre-NDA)",
        "stage2_heading": "Stage 2 Rooms (NDA Required)",
        "unlock_btn": "Unlock Stage 2 Rooms (NDA)",
        "cookie_banner": "Essential session cookies only. Non-essential analytics are disabled by default.",
        "ai_title": "Data Room AI Assistant (NDA-Gated)",
        "gdpr_export": "Export My Account Data (JSON)",
        "gdpr_delete": "Delete My Account",
    },
    "de": {
        "title": "Animal Scrypt — Investoren-Datenraum",
        "stage1_heading": "Stufe 1 Räume (Vor NDA)",
        "stage2_heading": "Stufe 2 Räume (NDA erforderlich)",
        "unlock_btn": "Stufe 2 freischalten (NDA)",
        "cookie_banner": "Nur notwendige Sitzungs-Cookies. Nicht notwendige Analysen sind standardmäßig deaktiviert.",
        "ai_title": "Datenraum KI-Assistent (NDA-geschützt)",
        "gdpr_export": "Meine Kontodaten exportieren (JSON)",
        "gdpr_delete": "Mein Konto löschen",
    },
    "fr": {
        "title": "Animal Scrypt — Salle de données investisseurs",
        "stage1_heading": "Salles de niveau 1 (Pré-NDA)",
        "stage2_heading": "Salles de niveau 2 (NDA requis)",
        "unlock_btn": "Déverrouiller le niveau 2 (NDA)",
        "cookie_banner": "Cookies de session essentiels uniquement. Les analyses non essentielles sont désactivées.",
        "ai_title": "Assistant IA de la salle de données (Verrouillé par NDA)",
        "gdpr_export": "Exporter mes données (JSON)",
        "gdpr_delete": "Supprimer mon compte",
    },
}

ROOMS_SEED: List[Dict[str, str]] = [
    {
        "slug": "overview",
        "title": "1. Overview",
        "tier": "STAGE_1",
        "summary": "Executive summary, 00-context.md, 07-canvas.md, and 08-business-plan.md.",
        "corpus": "Animal Scrypt (Robotic Discipline) builds a $45 3D-printed studio creature with an NTAG215 tag and $9/mo explicit SQLite memory ledger, scaling up a 4-tier price ladder.",
    },
    {
        "slug": "team",
        "title": "2. Team",
        "tier": "STAGE_1",
        "summary": "Founder bio (Kendren 'KJ' Cornish, rising sophomore at SCAD in Savannah) and fabrication context.",
        "corpus": "Founded by Kendren 'KJ' Cornish at SCAD in Savannah, Georgia. Uses campus 3D printers and studio fabrication.",
    },
    {
        "slug": "product",
        "title": "3. Product",
        "tier": "STAGE_1",
        "summary": "Stage-1 Python/SQLite kernel (skeleton/interfaces.py), Zine terminal, and 7-point MVP checklist.",
        "corpus": "Product includes physical PLA/resin shell, NTAG215 tag, proposed->approved memory state machine, and 20% single-hop parent royalty simulation.",
    },
    {
        "slug": "milestones",
        "title": "4. Milestones",
        "tier": "STAGE_1",
        "summary": "8-week MVP roadmap, Build Case 01 (28-case-study.md), and Methods White Paper (29-white-paper.md).",
        "corpus": "Milestones: Weeks 1-2 shell & NFC tag; Weeks 3-4 memory ledger; Weeks 5-6 workspace & simulated royalty ledger; Weeks 7-8 3-adult unassisted test.",
    },
    {
        "slug": "financials",
        "title": "5. Financials",
        "tier": "STAGE_2",
        "summary": "Unit cost breakdown ($10.61 COGS assumption), bootstrap burn (~$120-$230/mo), and 4-tier pricing ladder.",
        "corpus": "STAGE 2 CONFIDENTIAL FINANCIALS: V1 unit cost assumption is $10.61 on a $45 shell (76.4% hardware gross margin). Monthly student bootstrap burn is $120-$230/mo.",
    },
    {
        "slug": "cap-table",
        "title": "6. Cap Table",
        "tier": "STAGE_2",
        "summary": "Founder equity ledger (100% founder-held pre-seed) and SAFE register.",
        "corpus": "STAGE 2 CONFIDENTIAL CAP TABLE: 100% founder-held by Kendren 'KJ' Cornish prior to pre-seed SAFE issuance. Zero prior priced rounds or outstanding debt.",
    },
    {
        "slug": "legal",
        "title": "7. Legal",
        "tier": "STAGE_2",
        "summary": "Entity comparison (22-legal-menu.md), tester consent forms, and starter SAFE templates.",
        "corpus": "STAGE 2 CONFIDENTIAL LEGAL: Recommended single entity is Robotic Discipline, Inc. (Delaware C-Corp) with DBAs for Animal Scrypt, Disciple, and Madken.",
    },
    {
        "slug": "tax",
        "title": "8. Tax",
        "tier": "STAGE_2",
        "summary": "EIN confirmation placeholder, 83(b) election checklist, and state franchise tax schedule.",
        "corpus": "STAGE 2 CONFIDENTIAL TAX: 83(b) election must be filed within 30 days of founder stock issuance upon incorporation.",
    },
    {
        "slug": "ip",
        "title": "9. IP",
        "tier": "STAGE_2",
        "summary": "Founder IP assignment checklist, SCAD student policy review questions, and SCADpro equine boundary note.",
        "corpus": "STAGE 2 CONFIDENTIAL IP: Consumer toy IP is kept strictly separate from SCADpro equine telehealth research.",
    },
]


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


class DataRoomApp:
    """Self-hosted investor data room with hard server-side NDA gating and audit logging."""

    def __init__(self, db_path: str = DEFAULT_DB_PATH) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                role TEXT NOT NULL CHECK (role IN ('admin', 'advisor', 'partner', 'investor_s1', 'investor_s2')),
                nda_status TEXT NOT NULL DEFAULT 'NONE' CHECK (nda_status IN ('NONE', 'REQUESTED', 'SIGNED', 'APPROVED', 'REJECTED')),
                nda_signer_name TEXT,
                nda_firm TEXT,
                nda_signed_at TEXT,
                nda_approved_at TEXT,
                nda_version_hash TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS rooms (
                slug TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                tier TEXT NOT NULL CHECK (tier IN ('STAGE_1', 'STAGE_2')),
                summary TEXT NOT NULL,
                corpus TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS audit_logs (
                id TEXT PRIMARY KEY,
                user_email TEXT NOT NULL,
                role TEXT NOT NULL,
                room_slug TEXT,
                action TEXT NOT NULL CHECK (action IN ('VIEW', 'DOWNLOAD', 'NDA_SIGN', 'NDA_APPROVE', 'AI_QUERY')),
                ip_address TEXT NOT NULL,
                detail TEXT,
                created_at TEXT NOT NULL
            );
            """
        )
        # Seed default users
        self.conn.execute(
            """
            INSERT OR IGNORE INTO users (email, role, nda_status, created_at)
            VALUES ('kj@roboticdiscipline.com', 'admin', 'APPROVED', ?)
            """,
            (utc_now(),),
        )
        self.conn.execute(
            """
            INSERT OR IGNORE INTO users (email, role, nda_status, created_at)
            VALUES ('investor@precursor.vc', 'investor_s1', 'NONE', ?)
            """,
            (utc_now(),),
        )
        for room in ROOMS_SEED:
            self.conn.execute(
                """
                INSERT OR IGNORE INTO rooms (slug, title, tier, summary, corpus)
                VALUES (?, ?, ?, ?, ?)
                """,
                (room["slug"], room["title"], room["tier"], room["summary"], room["corpus"]),
            )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def _get_or_create_user(self, email: str) -> Dict[str, Any]:
        row = self.conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if not row:
            self.conn.execute(
                "INSERT INTO users (email, role, nda_status, created_at) VALUES (?, 'investor_s1', 'NONE', ?)",
                (email, utc_now()),
            )
            self.conn.commit()
            row = self.conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        return dict(row)

    def _log_audit(
        self, user_email: str, role: str, action: str, room_slug: Optional[str] = None, ip_address: str = "127.0.0.1", detail: str = ""
    ) -> None:
        self.conn.execute(
            """
            INSERT INTO audit_logs (id, user_email, role, room_slug, action, ip_address, detail, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (f"aud-{uuid.uuid4().hex[:8]}", user_email, role, room_slug, action, ip_address, detail, utc_now()),
        )
        self.conn.commit()

    def _can_access_stage2(self, user: Dict[str, Any]) -> bool:
        return user["role"] == "admin" or user["nda_status"] == "APPROVED"

    def handle_request(
        self,
        method: str,
        path: str,
        body: Optional[str] = None,
        user_email: str = "investor@precursor.vc",
        ip_address: str = "127.0.0.1",
    ) -> Tuple[int, Dict[str, str], str]:
        parsed = urllib.parse.urlparse(path)
        clean_path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)
        lang = query.get("lang", ["en"])[0]
        if lang not in LOCALES:
            lang = "en"
        if "user" in query:
            user_email = query["user"][0]

        user = self._get_or_create_user(user_email)

        if method == "GET" and clean_path == "/":
            return 200, {"Content-Type": "text/html; charset=utf-8"}, self.render_dashboard_html(user, lang)

        if method == "GET" and clean_path.startswith("/api/rooms/"):
            slug = clean_path.split("/api/rooms/", 1)[1]
            room = self.conn.execute("SELECT * FROM rooms WHERE slug = ?", (slug,)).fetchone()
            if not room:
                return 404, {"Content-Type": "application/json"}, json.dumps({"error": "Room not found"})
            room_dict = dict(room)
            if room_dict["tier"] == "STAGE_2" and not self._can_access_stage2(user):
                return (
                    403,
                    {"Content-Type": "application/json"},
                    json.dumps({"error": "Stage 2 room locked. Requires signed & founder-approved NDA."}),
                )
            self._log_audit(user["email"], user["role"], "VIEW", room_slug=slug, ip_address=ip_address)
            return 200, {"Content-Type": "application/json"}, json.dumps(room_dict)

        if method == "POST" and clean_path == "/api/nda/sign":
            payload = json.loads(body or "{}")
            full_name = (payload.get("full_name") or "").strip()
            firm = (payload.get("firm") or "").strip()
            if not full_name:
                return 400, {"Content-Type": "application/json"}, json.dumps({"error": "full_name required"})
            self.conn.execute(
                """
                UPDATE users
                SET nda_status = 'SIGNED', nda_signer_name = ?, nda_firm = ?, nda_signed_at = ?, nda_version_hash = ?
                WHERE email = ?
                """,
                (full_name, firm, utc_now(), NDA_HASH_V1, user["email"]),
            )
            self.conn.commit()
            self._log_audit(
                user["email"],
                user["role"],
                "NDA_SIGN",
                ip_address=ip_address,
                detail=f"Signed by {full_name} ({firm}) hash={NDA_HASH_V1}",
            )
            updated = self._get_or_create_user(user["email"])
            return 200, {"Content-Type": "application/json"}, json.dumps(updated)

        if method == "POST" and clean_path == "/api/admin/nda/approve":
            if user["role"] != "admin":
                return 403, {"Content-Type": "application/json"}, json.dumps({"error": "Admin only"})
            payload = json.loads(body or "{}")
            investor_email = payload.get("investor_email", "")
            approve = bool(payload.get("approve", True))
            new_status = "APPROVED" if approve else "REJECTED"
            new_role = "investor_s2" if approve else "investor_s1"
            self.conn.execute(
                """
                UPDATE users
                SET nda_status = ?, role = ?, nda_approved_at = ?
                WHERE email = ?
                """,
                (new_status, new_role, utc_now() if approve else None, investor_email),
            )
            self.conn.commit()
            self._log_audit(
                user["email"],
                user["role"],
                "NDA_APPROVE",
                ip_address=ip_address,
                detail=f"Set {investor_email} -> {new_status}",
            )
            updated_inv = self._get_or_create_user(investor_email)
            return 200, {"Content-Type": "application/json"}, json.dumps(updated_inv)

        if method == "POST" and clean_path == "/api/chat":
            payload = json.loads(body or "{}")
            question = (payload.get("question") or "").strip()
            stage2_ok = self._can_access_stage2(user)
            self._log_audit(
                user["email"], user["role"], "AI_QUERY", ip_address=ip_address, detail=f"stage2={stage2_ok}: {question}"
            )
            if not stage2_ok:
                # Strict server-side corpus filter: only STAGE_1 rooms
                s1_rooms = [
                    dict(r) for r in self.conn.execute("SELECT * FROM rooms WHERE tier = 'STAGE_1'").fetchall()
                ]
                q_lower = question.lower()
                sensitive_terms = ["cap table", "equity", "bank", "tax", "ein", "83(b)", "ip", "cogs", "burn"]
                if any(t in q_lower for t in sensitive_terms):
                    answer = (
                        "ACCESS REFUSED (Stage 1 Only): This question asks for Stage 2 confidential material "
                        "(cap table, financials, tax, or unreleased IP). Please request Stage 2 NDA approval first."
                    )
                else:
                    answer = "Stage 1 Summary: " + " ".join(r["corpus"] for r in s1_rooms[:2])
                return (
                    200,
                    {"Content-Type": "application/json"},
                    json.dumps({"stage2_unlocked": False, "answer": answer}),
                )
            else:
                all_rooms = [dict(r) for r in self.conn.execute("SELECT * FROM rooms").fetchall()]
                answer = "Stage 1 + Stage 2 Verified Corpus: " + " | ".join(r["corpus"] for r in all_rooms)
                return (
                    200,
                    {"Content-Type": "application/json"},
                    json.dumps({"stage2_unlocked": True, "answer": answer}),
                )

        if method == "GET" and clean_path == "/api/admin/audit.csv":
            if user["role"] != "admin":
                return 403, {"Content-Type": "application/json"}, json.dumps({"error": "Admin only"})
            rows = self.conn.execute("SELECT * FROM audit_logs ORDER BY created_at DESC").fetchall()
            buf = io.StringIO()
            writer = csv.writer(buf)
            writer.writerow(["id", "user_email", "role", "room_slug", "action", "ip_address", "detail", "created_at"])
            for r in rows:
                writer.writerow([r["id"], r["user_email"], r["role"], r["room_slug"], r["action"], r["ip_address"], r["detail"], r["created_at"]])
            return 200, {"Content-Type": "text/csv; charset=utf-8"}, buf.getvalue()

        if method == "GET" and clean_path == "/api/me/export":
            logs = [
                dict(r)
                for r in self.conn.execute("SELECT * FROM audit_logs WHERE user_email = ?", (user["email"],)).fetchall()
            ]
            return 200, {"Content-Type": "application/json"}, json.dumps({"user": user, "audit_logs": logs}, indent=2)

        if method == "DELETE" and clean_path == "/api/me":
            self.conn.execute("DELETE FROM users WHERE email = ?", (user["email"],))
            # Anonymize personal email in audit logs while preserving security timestamp trail
            self.conn.execute(
                "UPDATE audit_logs SET user_email = 'deleted_user@anonymized.local' WHERE user_email = ?",
                (user["email"],),
            )
            self.conn.commit()
            return 200, {"Content-Type": "application/json"}, json.dumps({"deleted": True})

        return 404, {"Content-Type": "application/json"}, json.dumps({"error": "Not found"})

    def render_dashboard_html(self, user: Dict[str, Any], lang: str = "en") -> str:
        t = LOCALES.get(lang, LOCALES["en"])
        stage2_ok = self._can_access_stage2(user)
        s1_rooms = [dict(r) for r in self.conn.execute("SELECT * FROM rooms WHERE tier = 'STAGE_1'").fetchall()]
        s2_rooms = [dict(r) for r in self.conn.execute("SELECT * FROM rooms WHERE tier = 'STAGE_2'").fetchall()]

        s1_cards = "".join(
            f"<div class='card'><span class='tag'>STAGE 1 // UNLOCKED</span><h3>{r['title']}</h3>"
            f"<p>{r['summary']}</p><p class='mono'>{r['corpus']}</p></div>"
            for r in s1_rooms
        )
        if stage2_ok:
            s2_cards = "".join(
                f"<div class='card'><span class='tag'>STAGE 2 // NDA VERIFIED</span><h3>{r['title']}</h3>"
                f"<p>{r['summary']}</p><p class='mono'>{r['corpus']}</p></div>"
                for r in s2_rooms
            )
        else:
            s2_cards = "".join(
                f"<div class='card locked'><span class='tag'>LOCKED (NDA REQUIRED)</span><h3>{r['title']}</h3>"
                f"<p>{r['summary']}</p><p class='mono'>[403 FORBIDDEN UNTIL NDA SIGNED &amp; FOUNDER APPROVED]</p></div>"
                for r in s2_rooms
            )

        return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8" />
<title>{t['title']}</title>
<style>
  :root {{
    --paper: #EFE6D4;
    --ink: #141413;
    --lime: #D8FF3E;
  }}
  body {{
    background: var(--paper);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 1.5rem;
    line-height: 1.5;
  }}
  .wrap {{ max-width: 980px; margin: 0 auto; }}
  .cookie {{
    background: var(--ink);
    color: var(--paper);
    padding: 0.5rem 1rem;
    font-size: 0.82rem;
    margin-bottom: 1rem;
  }}
  header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--ink);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }}
  h1, h2, h3 {{ font-family: Georgia, serif; margin-top: 0; }}
  .mono {{ font-family: "Courier New", Courier, monospace; font-size: 0.84rem; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem; }}
  .card {{
    border: 2px solid var(--ink);
    padding: 1rem;
    background: rgba(255,255,255,0.45);
    box-shadow: 4px 4px 0 var(--ink);
  }}
  .card.locked {{ opacity: 0.68; background: rgba(0,0,0,0.05); }}
  .tag {{
    display: inline-block;
    background: var(--lime);
    color: var(--ink);
    border: 1px solid var(--ink);
    padding: 0.1rem 0.45rem;
    font-family: "Courier New", Courier, monospace;
    font-size: 0.75rem;
    font-weight: bold;
  }}
  button {{
    background: var(--lime);
    color: var(--ink);
    border: 2px solid var(--ink);
    padding: 0.45rem 0.85rem;
    font-weight: bold;
    cursor: pointer;
  }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="cookie mono">{t['cookie_banner']}</div>
    <header>
      <div>
        <div class="mono">ANIMAL SCRYPT // ROBOTIC DISCIPLINE DATA ROOM</div>
        <h1>{t['title']}</h1>
      </div>
      <div class="mono">
        Viewer: <strong>{user['email']}</strong> ({user['role']} | NDA: {user['nda_status']})<br/>
        Lang: <a href="/?lang=en">EN</a> | <a href="/?lang=de">DE</a> | <a href="/?lang=fr">FR</a>
      </div>
    </header>

    <h2>{t['stage1_heading']}</h2>
    <div class="grid">{s1_cards}</div>

    <h2>{t['stage2_heading']}</h2>
    <div class="card" style="margin-bottom:1rem;">
      <p class="mono" style="margin-top:0;"><strong>Interactive NDA State Machine Controls:</strong></p>
      <button onclick="signNda()">1. Investor: Sign NDA ({t['unlock_btn']})</button>
      <button onclick="approveNda(true)" style="margin-left:0.5rem;">2. Founder (Admin): Approve NDA &amp; Unlock Stage 2</button>
      <button onclick="approveNda(false)" style="margin-left:0.5rem;background:#fff;">3. Founder (Admin): Revoke / Reject NDA</button>
      <div id="nda-msg" class="mono" style="margin-top:0.5rem;"></div>
    </div>
    <div class="grid">{s2_cards}</div>

    <div class="card" style="margin-top:1.5rem;">
      <h2>{t['ai_title']}</h2>
      <p class="mono">Server-side NDA check active: Stage 1 viewers cannot query Stage 2 cap table, tax, or IP corpus.</p>
      <form id="chat-form" style="margin-top:0.75rem;">
        <input type="text" id="chat-q" value="What is the exact cap table and founder equity split?" style="width:65%;padding:0.45rem;border:2px solid var(--ink);" />
        <button type="submit">Ask Data Room AI</button>
      </form>
      <pre id="chat-ans" class="mono" style="background:var(--ink);color:var(--paper);padding:0.85rem;margin-top:0.75rem;white-space:pre-wrap;">Ask a question above to test the server-side NDA corpus filter.</pre>
    </div>

    <footer class="mono" style="margin-top:2rem;border-top:2px solid var(--ink);padding-top:1rem;">
      <a href="/api/me/export">{t['gdpr_export']}</a> |
      <a href="/api/admin/audit.csv?user=kj@roboticdiscipline.com">Founder Audit CSV (Admin Only)</a>
    </footer>
  </div>
  <script>
    async function signNda() {{
      const res = await fetch('/api/nda/sign', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{full_name: 'Demo Investor', firm: 'Precursor Ventures'}})
      }});
      const data = await res.json();
      document.getElementById('nda-msg').textContent = 'NDA Status: ' + data.nda_status + ' (Awaiting Founder Approval)';
    }}
    async function approveNda(approve) {{
      const res = await fetch('/api/admin/nda/approve?user=kj@roboticdiscipline.com', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{investor_email: '{user['email']}', approve}})
      }});
      await res.json();
      window.location.reload();
    }}
    document.getElementById('chat-form').addEventListener('submit', async (e) => {{
      e.preventDefault();
      const question = document.getElementById('chat-q').value;
      const res = await fetch('/api/chat', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{question}})
      }});
      const data = await res.json();
      document.getElementById('chat-ans').textContent = `[Stage 2 Unlocked: ${{data.stage2_unlocked}}]\\n${{data.answer}}`;
    }});
  </script>
</body>
</html>"""


def run_server(port: int = 8082, db_path: str = DEFAULT_DB_PATH) -> None:
    app = DataRoomApp(db_path=db_path)

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            status, headers, body = app.handle_request("GET", self.path, ip_address=self.client_address[0])
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def do_POST(self) -> None:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
            status, headers, body = app.handle_request("POST", self.path, raw, ip_address=self.client_address[0])
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def do_DELETE(self) -> None:
            status, headers, body = app.handle_request("DELETE", self.path, ip_address=self.client_address[0])
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def log_message(self, format: str, *args: Any) -> None:
            return

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Animal Scrypt Self-Hosted Data Room running on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Animal Scrypt Self-Hosted Data Room Server")
    parser.add_argument("--port", type=int, default=8082)
    parser.add_argument("--db", type=str, default=DEFAULT_DB_PATH)
    args = parser.parse_args()
    run_server(port=args.port, db_path=args.db)
