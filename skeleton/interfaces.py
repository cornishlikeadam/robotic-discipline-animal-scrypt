#!/usr/bin/env python3
"""
Space Fort PBC / Animal Scrypt / Madken — Minimal Accelerator Skeleton & Interfaces
Implements the 4 Stage-1 verifiable primitives:
1. User-Approved Memory Ledger (PROPOSED -> APPROVED -> DELETED)
2. Bilateral Memory Fragment Exchange (requires both humans' explicit approval; supports revocation)
3. Parallel-Presence Shared Ritual Object (DORMANT -> RESONATING -> CRYSTALLIZED)
4. Capability Flash-Lease (time-bounded worker role token without exposing private memories)

Run:
    python3 skeleton/interfaces.py --demo
"""

from __future__ import annotations
import argparse
import datetime
import json
import pathlib
import sqlite3
import uuid
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

BASE_DIR = pathlib.Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR / "schema.sql"
EXPORT_PATH = BASE_DIR / "portable_identity_export.json"
HTML_DEMO_PATH = BASE_DIR / "zine_demo_view.html"


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


@dataclass
class ChassisSpec:
    proportion_class: str = "compact-articulated-mk1"
    translucent_tint: str = "cobalt-blue-08"
    optic_accent: str = " phosphor-amber-green"
    visible_joints: bool = True
    progression_stage: int = 1


class AnimalScryptKernel:
    """Minimal, model-agnostic state & permission kernel for Animal Scrypt / Madken."""

    def __init__(self, db_path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))

    # --- 1. Companion Identity Manifest ---
    def register_companion(
        self,
        companion_id: str,
        owner_id: str,
        name: str,
        authored_lore: str,
        chassis: Optional[ChassisSpec] = None,
    ) -> Dict[str, Any]:
        spec = asdict(chassis or ChassisSpec())
        voice = {
            "aesthetic": "editorial-zine",
            "max_sentences": 3,
            "clinical_claims_allowed": False,
        }
        now = utc_now()
        self.conn.execute(
            """
            INSERT INTO companions (id, owner_id, name, chassis_spec_json, authored_lore, voice_constraints_json, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (companion_id, owner_id, name, json.dumps(spec), authored_lore, json.dumps(voice), now),
        )
        self.conn.commit()
        return self.get_companion(companion_id)

    def get_companion(self, companion_id: str) -> Dict[str, Any]:
        row = self.conn.execute("SELECT * FROM companions WHERE id = ?", (companion_id,)).fetchone()
        if not row:
            raise KeyError(f"Companion {companion_id} not found")
        return dict(row)

    # --- 2. Explicit Memory Ledger (Never Silently Stored) ---
    def propose_memory(
        self,
        companion_id: str,
        category: str,
        content: str,
        visibility: str = "PRIVATE",
    ) -> str:
        memory_id = f"mem-{uuid.uuid4().hex[:8]}"
        self.conn.execute(
            """
            INSERT INTO memory_records (id, companion_id, category, content, status, visibility, created_at)
            VALUES (?, ?, ?, ?, 'PROPOSED', ?, ?)
            """,
            (memory_id, companion_id, category, content, visibility, utc_now()),
        )
        self.conn.commit()
        return memory_id

    def review_memory(self, memory_id: str, approve: bool, updated_content: Optional[str] = None) -> Dict[str, Any]:
        new_status = "APPROVED" if approve else "DELETED"
        if updated_content is not None:
            self.conn.execute(
                "UPDATE memory_records SET content = ?, status = ?, approved_at = ? WHERE id = ?",
                (updated_content, new_status, utc_now() if approve else None, memory_id),
            )
        else:
            self.conn.execute(
                "UPDATE memory_records SET status = ?, approved_at = ? WHERE id = ?",
                (new_status, utc_now() if approve else None, memory_id),
            )
        self.conn.commit()
        row = self.conn.execute("SELECT * FROM memory_records WHERE id = ?", (memory_id,)).fetchone()
        return dict(row)

    # --- 3. Bilateral Memory Fragment Exchange ---
    def propose_fragment_exchange(
        self,
        memory_id: str,
        sender_companion_id: str,
        recipient_companion_id: str,
        shared_summary: str,
    ) -> str:
        mem = self.conn.execute("SELECT * FROM memory_records WHERE id = ?", (memory_id,)).fetchone()
        if not mem or mem["status"] != "APPROVED":
            raise PermissionError("Only user-APPROVED memories can be proposed for fragment exchange.")
        exchange_id = f"fx-{uuid.uuid4().hex[:8]}"
        self.conn.execute(
            """
            INSERT INTO fragment_exchanges
            (id, memory_id, sender_companion_id, recipient_companion_id, shared_summary, sender_approved, recipient_approved, created_at)
            VALUES (?, ?, ?, ?, ?, 0, 0, ?)
            """,
            (exchange_id, memory_id, sender_companion_id, recipient_companion_id, shared_summary, utc_now()),
        )
        self.conn.commit()
        return exchange_id

    def approve_fragment_exchange(self, exchange_id: str, party: str) -> Dict[str, Any]:
        if party == "sender":
            self.conn.execute("UPDATE fragment_exchanges SET sender_approved = 1 WHERE id = ?", (exchange_id,))
        elif party == "recipient":
            self.conn.execute("UPDATE fragment_exchanges SET recipient_approved = 1 WHERE id = ?", (exchange_id,))
        else:
            raise ValueError("party must be 'sender' or 'recipient'")

        row = self.conn.execute("SELECT * FROM fragment_exchanges WHERE id = ?", (exchange_id,)).fetchone()
        if row["sender_approved"] and row["recipient_approved"] and not row["approved_at"]:
            self.conn.execute("UPDATE fragment_exchanges SET approved_at = ? WHERE id = ?", (utc_now(), exchange_id))
        self.conn.commit()
        return dict(self.conn.execute("SELECT * FROM fragment_exchanges WHERE id = ?", (exchange_id,)).fetchone())

    def revoke_fragment_exchange(self, exchange_id: str) -> Dict[str, Any]:
        self.conn.execute("UPDATE fragment_exchanges SET revoked_at = ? WHERE id = ?", (utc_now(), exchange_id))
        self.conn.commit()
        return dict(self.conn.execute("SELECT * FROM fragment_exchanges WHERE id = ?", (exchange_id,)).fetchone())

    # --- 4. Parallel-Presence Shared Ritual Object ---
    def create_ritual_object(self, ritual_id: str, title: str, participant_ids: List[str]) -> Dict[str, Any]:
        self.conn.execute(
            """
            INSERT INTO ritual_objects (id, title, participants_json, state, vitality_points, continuity_log_json, updated_at)
            VALUES (?, ?, ?, 'DORMANT', 0, '[]', ?)
            """,
            (ritual_id, title, json.dumps(participant_ids), utc_now()),
        )
        self.conn.commit()
        return dict(self.conn.execute("SELECT * FROM ritual_objects WHERE id = ?", (ritual_id,)).fetchone())

    def tend_ritual_object(self, ritual_id: str, active_participants: List[str], shared_action_note: str) -> Dict[str, Any]:
        row = self.conn.execute("SELECT * FROM ritual_objects WHERE id = ?", (ritual_id,)).fetchone()
        expected = set(json.loads(row["participants_json"]))
        if not expected.issubset(set(active_participants)):
            raise PermissionError("Parallel presence requires all paired participants to check in together.")

        vitality = int(row["vitality_points"]) + 1
        new_state = "RESONATING" if vitality == 1 else ("CRYSTALLIZED" if vitality >= 2 else "DORMANT")
        log = json.loads(row["continuity_log_json"])
        log.append(
            {
                "timestamp": utc_now(),
                "participants": active_participants,
                "vitality_points": vitality,
                "state": new_state,
                "continuity_note": shared_action_note,
            }
        )
        self.conn.execute(
            """
            UPDATE ritual_objects
            SET state = ?, vitality_points = ?, continuity_log_json = ?, updated_at = ?
            WHERE id = ?
            """,
            (new_state, vitality, json.dumps(log), utc_now(), ritual_id),
        )
        self.conn.commit()
        return dict(self.conn.execute("SELECT * FROM ritual_objects WHERE id = ?", (ritual_id,)).fetchone())

    # --- 5. Capability Flash-Lease (Scoped Temporary Worker Role) ---
    def grant_capability_lease(
        self,
        granter_companion_id: str,
        grantee_user_id: str,
        worker_role: str,
        scope_description: str,
        duration_minutes: int = 60,
    ) -> Dict[str, Any]:
        lease_id = f"lease-{uuid.uuid4().hex[:8]}"
        expires = (
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=duration_minutes)
        ).replace(microsecond=0).isoformat()
        self.conn.execute(
            """
            INSERT INTO capability_leases (id, granter_companion_id, grantee_user_id, worker_role, scope_description, expires_at, revoked)
            VALUES (?, ?, ?, ?, ?, ?, 0)
            """,
            (lease_id, granter_companion_id, grantee_user_id, worker_role, scope_description, expires),
        )
        self.conn.commit()
        return dict(self.conn.execute("SELECT * FROM capability_leases WHERE id = ?", (lease_id,)).fetchone())

    # --- 6. Portable Identity Export (Garry Tan "Own Your Intelligence" Bundle) ---
    def export_portable_bundle(self, companion_id: str) -> Dict[str, Any]:
        companion = self.get_companion(companion_id)
        memories = [
            dict(r)
            for r in self.conn.execute(
                "SELECT * FROM memory_records WHERE companion_id = ? AND status = 'APPROVED'",
                (companion_id,),
            ).fetchall()
        ]
        exchanges = [
            dict(r)
            for r in self.conn.execute(
                """
                SELECT * FROM fragment_exchanges
                WHERE (sender_companion_id = ? OR recipient_companion_id = ?)
                  AND sender_approved = 1 AND recipient_approved = 1 AND revoked_at IS NULL
                """,
                (companion_id, companion_id),
            ).fetchall()
        ]
        leases = [
            dict(r)
            for r in self.conn.execute(
                "SELECT * FROM capability_leases WHERE granter_companion_id = ? AND revoked = 0",
                (companion_id,),
            ).fetchall()
        ]
        royalties = [
            dict(r)
            for r in self.conn.execute(
                "SELECT * FROM royalty_ledger WHERE parent_companion_id = ? OR child_companion_id = ? ORDER BY created_at DESC",
                (companion_id, companion_id),
            ).fetchall()
        ]
        return {
            "schema_version": "spacefort.orbit.portable_identity.v0.1",
            "synthetic_demo_data": True,
            "exported_at": utc_now(),
            "companion_manifest": {
                **companion,
                "chassis_spec": json.loads(companion["chassis_spec_json"]),
                "voice_constraints": json.loads(companion["voice_constraints_json"]),
            },
            "approved_private_memories": memories,
            "active_bilateral_exchanges": exchanges,
            "active_capability_leases": leases,
            "royalty_ledger": royalties,
        }

    # --- 7. Simulated Creator-to-Owner Royalty Ledger (20% Single-Hop Parent Rule) ---
    def record_royalty_transfer(
        self,
        parent_companion_id: str,
        child_companion_id: str,
        creator_id: str,
        buyer_id: str,
        gross_amount_cents: int = 1500,
        creator_royalty_bps: int = 2000,
        platform_fee_bps: int = 1000,
    ) -> Dict[str, Any]:
        if gross_amount_cents < 0:
            raise ValueError("gross_amount_cents must be non-negative")
        # Verify both companions exist
        self.get_companion(parent_companion_id)
        self.get_companion(child_companion_id)

        creator_royalty_cents = (gross_amount_cents * creator_royalty_bps) // 10000
        platform_fee_cents = (gross_amount_cents * platform_fee_bps) // 10000
        net_settlement_cents = gross_amount_cents - creator_royalty_cents - platform_fee_cents

        tx_id = f"roy-{uuid.uuid4().hex[:8]}"
        self.conn.execute(
            """
            INSERT INTO royalty_ledger (
                id, parent_companion_id, child_companion_id, creator_id, buyer_id,
                gross_amount_cents, creator_royalty_cents, platform_fee_cents,
                net_settlement_cents, settlement_mode, created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'SIMULATED_TEST_LEDGER', ?)
            """,
            (
                tx_id,
                parent_companion_id,
                child_companion_id,
                creator_id,
                buyer_id,
                gross_amount_cents,
                creator_royalty_cents,
                platform_fee_cents,
                net_settlement_cents,
                utc_now(),
            ),
        )
        self.conn.commit()
        return dict(self.conn.execute("SELECT * FROM royalty_ledger WHERE id = ?", (tx_id,)).fetchone())


def render_zine_html(bundle_a: Dict[str, Any], ritual: Dict[str, Any]) -> str:
    """Renders a self-contained Editorial Zine + Translucent Blue Hardware HTML preview for YC Demo Video."""
    continuity = json.loads(ritual["continuity_log_json"])
    memories_html = "".join(
        f"<li><span class='badge'>{m['category'].upper()}</span> {m['content']} "
        f"<span class='meta'>[STATUS: {m['status']}]</span></li>"
        for m in bundle_a["approved_private_memories"]
    )
    exchanges_html = "".join(
        f"<li><strong>{fx['sender_companion_id']} &harr; {fx['recipient_companion_id']}</strong>: "
        f"“{fx['shared_summary']}” <span class='meta'>[BILATERAL SIGN-OFF VERIFIED]</span></li>"
        for fx in bundle_a["active_bilateral_exchanges"]
    )
    ritual_html = "".join(
        f"<li><code>{entry['timestamp']}</code> — <strong>{entry['state']}</strong> "
        f"(Vitality: {entry['vitality_points']}): {entry['continuity_note']}</li>"
        for entry in continuity
    )
    royalty_html = "".join(
        f"<li><code>{r['id']}</code> — Parent <strong>{r['parent_companion_id']}</strong> &rarr; Child <strong>{r['child_companion_id']}</strong> | "
        f"Gross: ${r['gross_amount_cents']/100:.2f} | Creator Royalty (20%): <strong>${r['creator_royalty_cents']/100:.2f}</strong> "
        f"<span class='meta'>[{r['settlement_mode']}]</span></li>"
        for r in bundle_a.get("royalty_ledger", [])
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>ANIMAL SCRYPT // MADKEN STAGE-1 ZINE TERMINAL (DEMO)</title>
<style>
  :root {{
    --paper: #f4f1ea;
    --ink: #101419;
    --cobalt-glass: rgba(14, 98, 209, 0.14);
    --cobalt-border: #0e62d1;
    --optic-green: #16c784;
  }}
  body {{
    background: var(--paper);
    color: var(--ink);
    font-family: "Courier New", Courier, monospace;
    margin: 2rem auto;
    max-width: 920px;
    padding: 0 1.5rem;
    line-height: 1.5;
  }}
  header {{
    border-bottom: 3px solid var(--ink);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .zine-tag {{
    background: var(--ink);
    color: var(--paper);
    padding: 0.2rem 0.6rem;
    font-size: 0.8rem;
    font-weight: bold;
  }}
  .grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
  }}
  .panel {{
    background: var(--cobalt-glass);
    border: 2px solid var(--cobalt-border);
    padding: 1rem 1.25rem;
    box-shadow: 4px 4px 0px var(--ink);
  }}
  h2 {{
    margin-top: 0;
    font-size: 1.05rem;
    text-transform: uppercase;
    border-bottom: 1px dashed var(--cobalt-border);
    padding-bottom: 0.4rem;
  }}
  .badge {{
    background: var(--cobalt-border);
    color: white;
    padding: 0.1rem 0.4rem;
    font-size: 0.75rem;
  }}
  .optic {{
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--optic-green);
    box-shadow: 0 0 8px var(--optic-green);
    margin-right: 6px;
  }}
  .meta {{
    font-size: 0.78rem;
    color: #0b4a9e;
  }}
  pre {{
    background: #101419;
    color: #d8e6ff;
    padding: 1rem;
    overflow-x: auto;
    font-size: 0.8rem;
  }}
</style>
</head>
<body>
  <header>
    <div>
      <span class="zine-tag">SPACE FORT PBC // ISSUE 01</span>
      <h1 style="margin:0.4rem 0 0 0;">ANIMAL SCRYPT &times; MADKEN</h1>
      <small>SYNTHETIC DEMO VIEW — PORTABLE IDENTITY &amp; PARALLEL PRESENCE</small>
    </div>
    <div>
      <span class="optic"></span><strong>UNIT: {bundle_a['companion_manifest']['name']}</strong>
    </div>
  </header>

  <div class="grid">
    <section class="panel">
      <h2>1. Madken Chassis &amp; Authored Lore</h2>
      <p><strong>ID:</strong> <code>{bundle_a['companion_manifest']['id']}</code></p>
      <p><strong>Shell Spec:</strong> Translucent Cobalt-08 / Articulated MK1</p>
      <p><strong>Immutable Lore:</strong> {bundle_a['companion_manifest']['authored_lore']}</p>
    </section>

    <section class="panel">
      <h2>2. Shared Ritual Object ({ritual['state']})</h2>
      <p><strong>Artifact:</strong> {ritual['title']}</p>
      <p><strong>Vitality Points:</strong> {ritual['vitality_points']} (Zero-Shame Dormancy Enabled)</p>
      <ul>{ritual_html}</ul>
    </section>

    <section class="panel">
      <h2>3. User-Approved Private Memories</h2>
      <ul>{memories_html}</ul>
    </section>

    <section class="panel">
      <h2>4. Bilateral Fragment Exchanges</h2>
      <ul>{exchanges_html}</ul>
    </section>
  </div>

  <section class="panel" style="margin-top: 1.25rem;">
    <h2>5. Simulated Creator-to-Owner Royalty Ledger (20% Parent Rule)</h2>
    <ul>{royalty_html}</ul>
  </section>

  <section class="panel" style="margin-top: 1.25rem;">
    <h2>6. Portable Identity Export (User-Owned JSON State)</h2>
    <pre>{json.dumps(bundle_a, indent=2)}</pre>
  </section>
</body>
</html>
"""


def run_demo() -> None:
    kernel = AnimalScryptKernel()

    # Step 1: Register two companions (User A & User B)
    kernel.register_companion(
        companion_id="mk-08-wave",
        owner_id="user_alpha",
        name="WAVE-08 (Cobalt Scout)",
        authored_lore="Compact articulated field archivist with translucent cobalt plates and amber-green optics.",
    )
    kernel.register_companion(
        companion_id="mk-12-orbit",
        owner_id="user_beta",
        name="ORBIT-12 (Quiet Botanist)",
        authored_lore="Low-power atmospheric listener designed to log parallel study habitats.",
    )

    # Step 2: Companion A proposes a memory; User A explicitly approves it
    mem_id = kernel.propose_memory(
        companion_id="mk-08-wave",
        category="project",
        content="Prototyping low-pressure co-working habitats and OpenSCAD shell joints.",
        visibility="FRAGMENT_CANDIDATE",
    )
    kernel.review_memory(mem_id, approve=True)

    # Step 3: Bilateral Memory Fragment Exchange between WAVE-08 and ORBIT-12
    fx_id = kernel.propose_fragment_exchange(
        memory_id=mem_id,
        sender_companion_id="mk-08-wave",
        recipient_companion_id="mk-12-orbit",
        shared_summary="Both humans are building hardware-software prototypes late at night this week.",
    )
    kernel.approve_fragment_exchange(fx_id, party="sender")
    kernel.approve_fragment_exchange(fx_id, party="recipient")

    # Step 4: Create & Advance a Shared Ritual Object via Parallel Presence
    kernel.create_ritual_object(
        ritual_id="ritual-cobalt-core-01",
        title="Translucent Signal Core #01",
        participant_ids=["mk-08-wave", "mk-12-orbit"],
    )
    kernel.tend_ritual_object(
        ritual_id="ritual-cobalt-core-01",
        active_participants=["mk-08-wave", "mk-12-orbit"],
        shared_action_note="Completed 15-minute silent parallel build block.",
    )
    ritual = kernel.tend_ritual_object(
        ritual_id="ritual-cobalt-core-01",
        active_participants=["mk-08-wave", "mk-12-orbit"],
        shared_action_note="Logged mutual evening observation; core crystallized to Stage 2.",
    )

    # Step 5: Issue a scoped 60-minute Capability Flash-Lease (worker role only, no private memory access)
    kernel.grant_capability_lease(
        granter_companion_id="mk-08-wave",
        grantee_user_id="user_beta",
        worker_role="archivist",
        scope_description="Temporary read/write access to shared ritual log only; zero access to private memories.",
        duration_minutes=60,
    )

    # Step 6: Simulated Creator-to-Owner Royalty Rule Demonstration (20% single-hop parent allocation)
    kernel.record_royalty_transfer(
        parent_companion_id="mk-08-wave",
        child_companion_id="mk-12-orbit",
        creator_id="user_alpha",
        buyer_id="user_beta",
        gross_amount_cents=1500,
    )

    # Step 7: Export Portable Identity JSON & Zine HTML Preview
    bundle = kernel.export_portable_bundle("mk-08-wave")
    EXPORT_PATH.write_text(json.dumps(bundle, indent=2), encoding="utf-8")
    HTML_DEMO_PATH.write_text(render_zine_html(bundle, ritual), encoding="utf-8")

    print("=== SPACE FORT // ANIMAL SCRYPT YC DEMO SKELETON COMPLETE ===")
    print(f"1. Portable Identity Export saved to: {EXPORT_PATH}")
    print(f"2. Visual Zine Demo View saved to:    {HTML_DEMO_PATH}")
    print(f"3. Ritual Object State:               {ritual['state']} (Vitality: {ritual['vitality_points']})")
    print(f"4. Approved Memories Count:           {len(bundle['approved_private_memories'])}")
    print(f"5. Bilateral Exchanges Verified:      {len(bundle['active_bilateral_exchanges'])}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Animal Scrypt / Madken Stage-1 Demo Kernel")
    parser.add_argument("--demo", action="store_true", help="Run the 60-second YC verification scenario")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        parser.print_help()
