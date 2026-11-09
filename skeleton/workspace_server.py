#!/usr/bin/env python3
"""
Robotic Discipline / Animal Scrypt — Portfolio Front Page & Interactive Browser Workspace
Implements:
1. Section 19 Portfolio Front Page (`GET /`):
   - Editorial zine palette: Cream paper (#EFE6D4), Deep ink (#141413), Acid lime (#D8FF3E)
   - Six sections: Hero, The Animal, How Memory Works, Worker Roles, Royalty Loop, Studio Note
   - Zero fake counters or invented traction numbers
2. Interactive Creature Workspace (`GET /workspace` & `/api/*`):
   - Backed by AnimalScryptKernel (SQLite)
   - Propose & approve/delete memories (7-day persistent memory ledger)
   - Trigger simulated creator-to-owner transfer (20% single-hop parent royalty in test ledger)
   - Export portable JSON identity bundle

Run locally:
    python3 skeleton/workspace_server.py --port 8081
"""

from __future__ import annotations
import argparse
import json
import pathlib
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, Any, Tuple, Optional

from skeleton.interfaces import AnimalScryptKernel, ChassisSpec

BASE_DIR = pathlib.Path(__file__).resolve().parent
DEFAULT_DB_PATH = str(BASE_DIR / "animal_scrypt_workspace.db")


class WorkspaceApp:
    """Testable HTTP application controller for the Animal Scrypt Portfolio & Workspace."""

    def __init__(self, db_path: str = DEFAULT_DB_PATH) -> None:
        self.db_path = db_path
        self.kernel = AnimalScryptKernel(db_path=db_path)
        self.primary_id = "mk-08-wave"
        self.child_id = "mk-12-orbit"
        self._seed_if_empty()

    def _seed_if_empty(self) -> None:
        try:
            self.kernel.get_companion(self.primary_id)
        except KeyError:
            self.kernel.register_companion(
                companion_id=self.primary_id,
                owner_id="kj_cornish",
                name="WAVE-08 (Cobalt Scout)",
                authored_lore="3D-printed studio engineer shell with recessed NTAG215 tag and explicit memory ledger.",
                chassis=ChassisSpec(),
            )
            self.kernel.register_companion(
                companion_id=self.child_id,
                owner_id="savannah_maker_02",
                name="ORBIT-12 (Child Fork)",
                authored_lore="Forked studio shell derived from WAVE-08 parent blueprint.",
                chassis=ChassisSpec(progression_stage=1),
            )
            # Seed 3 approved details + 1 proposed detail for immediate verification
            m1 = self.kernel.propose_memory(
                self.primary_id, "project", "Shell wall thickness set to 2.4mm in OpenSCAD for PLA print."
            )
            m2 = self.kernel.propose_memory(
                self.primary_id, "routine", "NTAG215 NFC sticker recessed into 28mm bottom cavity."
            )
            m3 = self.kernel.propose_memory(
                self.primary_id, "observation", "Owner prefers short 3-sentence status briefings before studio critiques."
            )
            self.kernel.review_memory(m1, approve=True)
            self.kernel.review_memory(m2, approve=True)
            self.kernel.review_memory(m3, approve=True)
            self.kernel.propose_memory(
                self.primary_id, "interest", "Testing brass heat-set inserts on neck joint tomorrow."
            )
            self.kernel.record_royalty_transfer(
                parent_companion_id=self.primary_id,
                child_companion_id=self.child_id,
                creator_id="kj_cornish",
                buyer_id="savannah_maker_02",
                gross_amount_cents=1500,
            )

    def close(self) -> None:
        self.kernel.conn.close()

    def get_state(self) -> Dict[str, Any]:
        bundle = self.kernel.export_portable_bundle(self.primary_id)
        proposed = [
            dict(r)
            for r in self.kernel.conn.execute(
                "SELECT * FROM memory_records WHERE companion_id = ? AND status = 'PROPOSED' ORDER BY created_at DESC",
                (self.primary_id,),
            ).fetchall()
        ]
        return {
            "companion_manifest": bundle["companion_manifest"],
            "proposed_memories": proposed,
            "approved_private_memories": bundle["approved_private_memories"],
            "royalty_ledger": bundle["royalty_ledger"],
            "portable_bundle": bundle,
        }

    def handle_request(
        self, method: str, path: str, body: Optional[str] = None
    ) -> Tuple[int, Dict[str, str], str]:
        if method == "GET" and path == "/":
            return 200, {"Content-Type": "text/html; charset=utf-8"}, self.render_portfolio_html()
        if method == "GET" and path == "/workspace":
            return 200, {"Content-Type": "text/html; charset=utf-8"}, self.render_workspace_html()
        if method == "GET" and path == "/api/state":
            return 200, {"Content-Type": "application/json"}, json.dumps(self.get_state(), indent=2)
        if method == "GET" and path == "/api/export":
            bundle = self.kernel.export_portable_bundle(self.primary_id)
            return 200, {"Content-Type": "application/json"}, json.dumps(bundle, indent=2)
        if method == "POST" and path == "/api/memory/propose":
            payload = json.loads(body or "{}")
            category = payload.get("category", "project")
            content = (payload.get("content") or "").strip()
            if not content:
                return 400, {"Content-Type": "application/json"}, json.dumps({"error": "content required"})
            mem_id = self.kernel.propose_memory(self.primary_id, category, content)
            return 200, {"Content-Type": "application/json"}, json.dumps({"memory_id": mem_id, "status": "PROPOSED"})
        if method == "POST" and path == "/api/memory/review":
            payload = json.loads(body or "{}")
            mem_id = payload.get("memory_id", "")
            approve = bool(payload.get("approve", True))
            updated_content = payload.get("updated_content")
            record = self.kernel.review_memory(mem_id, approve=approve, updated_content=updated_content)
            return 200, {"Content-Type": "application/json"}, json.dumps(record)
        if method == "POST" and path == "/api/royalty/simulate":
            payload = json.loads(body or "{}")
            buyer_id = (payload.get("buyer_id") or "scad_buyer_demo").strip()
            gross_cents = int(payload.get("gross_amount_cents", 1500))
            child_id = f"mk-fork-{uuid.uuid4().hex[:4]}"
            self.kernel.register_companion(
                companion_id=child_id,
                owner_id=buyer_id,
                name=f"FORK-{child_id.upper()}",
                authored_lore=f"Child creature minted from parent {self.primary_id}.",
            )
            tx = self.kernel.record_royalty_transfer(
                parent_companion_id=self.primary_id,
                child_companion_id=child_id,
                creator_id="kj_cornish",
                buyer_id=buyer_id,
                gross_amount_cents=gross_cents,
            )
            return 200, {"Content-Type": "application/json"}, json.dumps(tx)
        return 404, {"Content-Type": "application/json"}, json.dumps({"error": "Not found"})

    def render_portfolio_html(self) -> str:
        state = self.get_state()
        manifest = state["companion_manifest"]
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Animal Scrypt — Hold the animal. Keep the memory.</title>
<style>
  :root {{
    --paper: #EFE6D4;
    --ink: #141413;
    --lime: #D8FF3E;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    background: var(--paper);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.55;
  }}
  .wrap {{
    max-width: 960px;
    margin: 0 auto;
    padding: 2rem 1.5rem 4rem;
  }}
  header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--ink);
    padding-bottom: 1rem;
    margin-bottom: 2.5rem;
  }}
  .mono {{
    font-family: "Courier New", Courier, monospace;
    font-size: 0.85rem;
  }}
  h1, h2, h3 {{
    font-family: Georgia, "Times New Roman", serif;
    letter-spacing: -0.02em;
  }}
  .hero h1 {{
    font-size: 3.1rem;
    line-height: 1.08;
    margin: 0.5rem 0 1rem;
  }}
  .hero p {{
    font-size: 1.2rem;
    max-width: 660px;
    margin-bottom: 1.5rem;
  }}
  .btn {{
    display: inline-block;
    background: var(--ink);
    color: var(--paper);
    padding: 0.75rem 1.25rem;
    text-decoration: none;
    font-weight: 700;
    border: 2px solid var(--ink);
    margin-right: 0.75rem;
  }}
  .btn-lime {{
    background: var(--lime);
    color: var(--ink);
  }}
  section {{
    border-top: 2px solid var(--ink);
    padding-top: 2rem;
    margin-top: 2.5rem;
  }}
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
  }}
  .grid-4 {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
  }}
  .card {{
    border: 2px solid var(--ink);
    padding: 1.25rem;
    background: rgba(255,255,255,0.35);
    box-shadow: 4px 4px 0 var(--ink);
  }}
  .tag {{
    display: inline-block;
    background: var(--lime);
    color: var(--ink);
    border: 1px solid var(--ink);
    padding: 0.1rem 0.5rem;
    font-family: "Courier New", Courier, monospace;
    font-size: 0.78rem;
    font-weight: bold;
  }}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="mono"><strong>ANIMAL SCRYPT</strong> // ROBOTIC DISCIPLINE STUDIO</div>
      <nav class="mono">
        <a href="/workspace" style="color:var(--ink);font-weight:bold;">[OPEN WORKSPACE]</a>
      </nav>
    </header>

    <!-- 1. HERO -->
    <div class="hero">
      <span class="tag">ISSUE 01 // SAVANNAH, GA</span>
      <h1>Hold the animal. Keep the memory.</h1>
      <p>A 3D-printed studio creature with a recessed NFC tag and an explicit memory ledger you approve, edit, and export.</p>
      <div>
        <a class="btn btn-lime" href="/studio">Open Visual Blueprint &amp; White Paper Studio</a>
        <a class="btn" href="/workspace">Meet an animal</a>
        <a class="btn" href="#studio-note">Read the studio note</a>
      </div>
    </div>

    <!-- 2. THE ANIMAL -->
    <section id="the-animal">
      <h2>1. The Animal</h2>
      <div class="grid-2">
        <div class="card">
          <span class="tag">PHYSICAL SHELL</span>
          <h3>{manifest['name']}</h3>
          <p>{manifest['authored_lore']}</p>
          <p class="mono">ID: {manifest['id']} | Tag: NTAG215 (28mm base slot) | Shell: PLA / Resin</p>
        </div>
        <div class="card">
          <span class="tag">SOFTWARE TWIN</span>
          <h3>Owner-Controlled Workspace</h3>
          <p>Tap your phone to the base of the figure. The browser opens your creature's biography, conversation terminal, memory approval queue, and JSON export.</p>
          <p class="mono">Approved Memories Stored: {len(state['approved_private_memories'])}</p>
        </div>
      </div>
    </section>

    <!-- 3. HOW MEMORY WORKS -->
    <section id="how-memory-works">
      <h2>2. How Memory Works</h2>
      <p>Your animal never saves silent background logs. Every long-term memory moves through a three-state ledger you control:</p>
      <div class="card mono">
        [1. CONVERSATION] &rarr; [2. PROPOSED MEMORY] &rarr; [3. OWNER APPROVES OR DELETES] &rarr; [4. STORED IN SQLITE &amp; RECALLED ON DAY 7]
      </div>
    </section>

    <!-- 4. WORKER ROLES -->
    <section id="worker-roles">
      <h2>3. Worker Roles</h2>
      <div class="grid-4">
        <div class="card">
          <span class="tag">V1 ACTIVE</span>
          <h3>Engineer</h3>
          <p>Tracks OpenSCAD dimensions, print tolerances, and build logs across studio sessions.</p>
        </div>
        <div class="card">
          <span class="tag">PLANNED POST-MVP</span>
          <h3>Artist</h3>
          <p>Holds visual references, color palettes, and critique notes across projects.</p>
        </div>
        <div class="card">
          <span class="tag">PLANNED POST-MVP</span>
          <h3>Musician</h3>
          <p>Catalogs tempo notes, patch settings, and session stems.</p>
        </div>
        <div class="card">
          <span class="tag">PLANNED POST-MVP</span>
          <h3>Researcher</h3>
          <p>Organizes citations, field observations, and reading summaries.</p>
        </div>
      </div>
    </section>

    <!-- 5. ROYALTY LOOP -->
    <section id="royalty-loop">
      <h2>4. Royalty Loop</h2>
      <p>When a collector forks a child creature from a parent animal's public blueprint, a single-hop royalty pays the parent's maker.</p>
      <div class="card mono">
        [PARENT ANIMAL ({manifest['id']})] &rarr; [CHILD MINT ($15.00)] &rarr; [20% CREATOR ROYALTY ($3.00) TO PARENT MAKER | 10% PLATFORM | 70% NET]
      </div>
    </section>

    <!-- 6. STUDIO NOTE -->
    <section id="studio-note">
      <h2>5. Studio Note</h2>
      <div class="card">
        <p>Built by Kendren "KJ" Cornish at SCAD in Savannah, Georgia. Robotic Discipline (practiced as Disciple, shipping Animal Scrypt and Madken) is pre-seed and student-built. We print shells on campus, test memory persistence in SQLite, and ship one working creature before scaling.</p>
      </div>
    </section>
  </div>
</body>
</html>"""

    def render_workspace_html(self) -> str:
        return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Animal Scrypt Workspace — Memory & Royalty Ledger</title>
<style>
  :root {
    --paper: #EFE6D4;
    --ink: #141413;
    --lime: #D8FF3E;
  }
  * { box-sizing: border-box; }
  body {
    background: var(--paper);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 1.5rem;
    line-height: 1.5;
  }
  .wrap { max-width: 980px; margin: 0 auto; }
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--ink);
    padding-bottom: 1rem;
    margin-bottom: 1.5rem;
  }
  h1, h2 { font-family: Georgia, serif; margin-top: 0; }
  .mono { font-family: "Courier New", Courier, monospace; font-size: 0.85rem; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; }
  .panel {
    border: 2px solid var(--ink);
    padding: 1.25rem;
    background: rgba(255,255,255,0.45);
    box-shadow: 4px 4px 0 var(--ink);
    margin-bottom: 1.25rem;
  }
  button {
    background: var(--ink);
    color: var(--paper);
    border: 2px solid var(--ink);
    padding: 0.45rem 0.85rem;
    font-weight: bold;
    cursor: pointer;
    margin-right: 0.4rem;
  }
  button.lime { background: var(--lime); color: var(--ink); }
  input, select {
    padding: 0.45rem;
    border: 2px solid var(--ink);
    background: #fff;
    font-family: inherit;
    margin-right: 0.4rem;
  }
  pre {
    background: var(--ink);
    color: var(--paper);
    padding: 1rem;
    overflow-x: auto;
    font-size: 0.8rem;
  }
  li { margin-bottom: 0.6rem; }
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div>
        <div class="mono"><a href="/" style="color:var(--ink);">&larr; Back to Portfolio Front Page</a></div>
        <h1>Animal Scrypt Digital Workspace</h1>
      </div>
      <div class="mono" id="owner-badge">Loading owner...</div>
    </header>

    <div class="grid">
      <div class="panel">
        <h2>1. Creature Profile &amp; Pairing</h2>
        <div id="profile-box" class="mono"></div>
      </div>

      <div class="panel">
        <h2>2. Propose Memory Detail</h2>
        <form id="propose-form">
          <select id="mem-category">
            <option value="project">project</option>
            <option value="routine">routine</option>
            <option value="observation">observation</option>
            <option value="interest">interest</option>
          </select>
          <input type="text" id="mem-content" placeholder="e.g. Set nozzle temp to 210C" style="width:55%;" required />
          <button type="submit" class="lime">Propose</button>
        </form>
        <h3 style="margin-top:1rem;">Pending Owner Approval (`PROPOSED`)</h3>
        <ul id="proposed-list" class="mono"></ul>
      </div>
    </div>

    <div class="grid">
      <div class="panel">
        <h2>3. Seven-Day Approved Memory Ledger (`APPROVED`)</h2>
        <ul id="approved-list" class="mono"></ul>
      </div>

      <div class="panel">
        <h2>4. Simulated Royalty Ledger (20% Parent Rule)</h2>
        <p style="font-size:0.9rem;">Simulate a creator-to-owner child mint ($15.00 gross &rarr; $3.00 parent royalty in test ledger).</p>
        <form id="royalty-form">
          <input type="text" id="buyer-id" placeholder="Buyer ID (e.g. scad_peer_09)" required />
          <button type="submit" class="lime">Simulate Child Mint ($15.00)</button>
        </form>
        <ul id="royalty-list" class="mono" style="margin-top:1rem;"></ul>
      </div>
    </div>

    <div class="panel">
      <h2>5. Portable Ownership &amp; Identity Export (JSON)</h2>
      <pre id="export-box"></pre>
    </div>
  </div>

  <script>
    async function refreshState() {
      const res = await fetch('/api/state');
      const data = await res.json();
      const m = data.companion_manifest;
      document.getElementById('owner-badge').textContent = `VERIFIED OWNER: ${m.owner_id} // UNIT: ${m.id}`;
      document.getElementById('profile-box').innerHTML = `
        <p><strong>Name:</strong> ${m.name}</p>
        <p><strong>Lore:</strong> ${m.authored_lore}</p>
        <p><strong>Chassis:</strong> ${m.chassis_spec.proportion_class} (${m.chassis_spec.translucent_tint})</p>
      `;

      const propUl = document.getElementById('proposed-list');
      propUl.innerHTML = data.proposed_memories.length === 0 ? '<li>None pending.</li>' : '';
      data.proposed_memories.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `[${item.category.toUpperCase()}] ${item.content}
          <button class="lime" onclick="reviewMem('${item.id}', true)">Approve</button>
          <button onclick="reviewMem('${item.id}', false)">Delete</button>`;
        propUl.appendChild(li);
      });

      const appUl = document.getElementById('approved-list');
      appUl.innerHTML = '';
      data.approved_private_memories.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `[${item.category.toUpperCase()}] ${item.content} (Approved: ${item.approved_at})`;
        appUl.appendChild(li);
      });

      const royUl = document.getElementById('royalty-list');
      royUl.innerHTML = '';
      data.royalty_ledger.forEach(r => {
        const li = document.createElement('li');
        li.textContent = `${r.id}: Parent ${r.parent_companion_id} -> Child ${r.child_companion_id} (Buyer: ${r.buyer_id}) | Gross: $${(r.gross_amount_cents/100).toFixed(2)} | 20% Creator Royalty: $${(r.creator_royalty_cents/100).toFixed(2)} [${r.settlement_mode}]`;
        royUl.appendChild(li);
      });

      document.getElementById('export-box').textContent = JSON.stringify(data.portable_bundle, null, 2);
    }

    async function reviewMem(memory_id, approve) {
      await fetch('/api/memory/review', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({memory_id, approve})
      });
      refreshState();
    }

    document.getElementById('propose-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const category = document.getElementById('mem-category').value;
      const content = document.getElementById('mem-content').value;
      await fetch('/api/memory/propose', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({category, content})
      });
      document.getElementById('mem-content').value = '';
      refreshState();
    });

    document.getElementById('royalty-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const buyer_id = document.getElementById('buyer-id').value;
      await fetch('/api/royalty/simulate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({buyer_id, gross_amount_cents: 1500})
      });
      document.getElementById('buyer-id').value = '';
      refreshState();
    });

    refreshState();
  </script>
</body>
</html>"""


def run_server(port: int = 8081, db_path: str = DEFAULT_DB_PATH) -> None:
    app = WorkspaceApp(db_path=db_path)

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            status, headers, body = app.handle_request("GET", self.path)
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def do_POST(self) -> None:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
            status, headers, body = app.handle_request("POST", self.path, raw)
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def log_message(self, format: str, *args: Any) -> None:
            return

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Animal Scrypt Portfolio & Workspace running on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Animal Scrypt Portfolio & Workspace Server")
    parser.add_argument("--port", type=int, default=8081)
    parser.add_argument("--db", type=str, default=DEFAULT_DB_PATH)
    args = parser.parse_args()
    run_server(port=args.port, db_path=args.db)
