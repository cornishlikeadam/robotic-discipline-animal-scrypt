#!/usr/bin/env python3
"""
Robotic Discipline (Animal Scrypt × Disciple × Madken)
Visual Design Studio, Interactive Hardware Blueprint & Formatted White Paper Reader/Editor.
"""

from __future__ import annotations
import html
import json
import pathlib
import re
import sqlite3
import urllib.parse
from typing import Dict, Any, List, Tuple, Optional

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SEED_DIR = REPO_ROOT / "seed"


def markdown_to_rich_html(md_text: str) -> str:
    """Converts Markdown (headings, tables, blockquotes, lists, bold, code, links) into publication-grade HTML."""
    lines = md_text.splitlines()
    out: List[str] = []
    in_code = False
    in_ul = False
    in_ol = False
    in_table = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol, in_table
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False
        if in_table:
            out.append("</tbody></table></div>")
            in_table = False

    def inline_fmt(text: str) -> str:
        t = html.escape(text)
        # inline code
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        # bold
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        # italic
        t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
        # checkboxes
        t = t.replace("[ ]", "<input type='checkbox' class='blueprint-check' />")
        t = t.replace("[x]", "<input type='checkbox' class='blueprint-check' checked />")
        # links [label](url)
        t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', t)
        return t

    for raw_line in lines:
        line = raw_line.rstrip()

        if line.strip().startswith("```"):
            close_lists()
            if not in_code:
                in_code = True
                out.append("<pre class='code-block'><code>")
            else:
                in_code = False
                out.append("</code></pre>")
            continue

        if in_code:
            out.append(html.escape(raw_line))
            continue

        # Table rows
        if line.strip().startswith("|") and line.strip().endswith("|"):
            if in_ul or in_ol:
                if in_ul:
                    out.append("</ul>")
                    in_ul = False
                if in_ol:
                    out.append("</ol>")
                    in_ol = False
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            if not in_table:
                in_table = True
                out.append("<div class='table-wrap'><table class='wp-table'><thead><tr>")
                for c in cells:
                    out.append(f"<th>{inline_fmt(c)}</th>")
                out.append("</tr></thead><tbody>")
            else:
                out.append("<tr>")
                for c in cells:
                    out.append(f"<td>{inline_fmt(c)}</td>")
                out.append("</tr>")
            continue
        elif in_table:
            close_lists()

        if not line.strip():
            close_lists()
            continue

        if line.strip() == "---":
            close_lists()
            out.append("<hr class='wp-rule' />")
            continue

        if line.startswith("# "):
            close_lists()
            out.append(f"<h1 class='wp-h1'>{inline_fmt(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_lists()
            out.append(f"<h2 class='wp-h2'>{inline_fmt(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            close_lists()
            out.append(f"<h3 class='wp-h3'>{inline_fmt(line[4:].strip())}</h3>")
        elif line.startswith("#### "):
            close_lists()
            out.append(f"<h4 class='wp-h4'>{inline_fmt(line[5:].strip())}</h4>")
        elif line.strip().startswith("> "):
            close_lists()
            out.append(f"<blockquote class='wp-quote'>{inline_fmt(line.strip()[2:])}</blockquote>")
        elif re.match(r"^\s*[-*]\s+", line):
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                in_ul = True
                out.append("<ul class='wp-list'>")
            item_text = re.sub(r"^\s*[-*]\s+", "", line)
            out.append(f"<li>{inline_fmt(item_text)}</li>")
        elif re.match(r"^\s*\d+\.\s+", line):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                in_ol = True
                out.append("<ol class='wp-list'>")
            item_text = re.sub(r"^\s*\d+\.\s+", "", line)
            out.append(f"<li>{inline_fmt(item_text)}</li>")
        else:
            close_lists()
            out.append(f"<p class='wp-p'>{inline_fmt(line)}</p>")

    close_lists()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


class StudioBlueprintApp:
    """Interactive Visual Design Studio, Hardware Blueprint CAD Preview & White Paper Reader/Editor."""

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS studio_design (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                paper_hex TEXT NOT NULL,
                ink_hex TEXT NOT NULL,
                lime_hex TEXT NOT NULL,
                blush_hex TEXT NOT NULL,
                shell_tint TEXT NOT NULL,
                optic_hex TEXT NOT NULL,
                nfc_slot_mm INTEGER NOT NULL,
                wall_thickness_mm REAL NOT NULL,
                creature_name TEXT NOT NULL,
                worker_role TEXT NOT NULL,
                font_mode TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS studio_docs (
                doc_id TEXT PRIMARY KEY,
                content TEXT NOT NULL
            );
            """
        )
        self.conn.execute(
            """
            INSERT OR IGNORE INTO studio_design (
                id, paper_hex, ink_hex, lime_hex, blush_hex,
                shell_tint, optic_hex, nfc_slot_mm, wall_thickness_mm,
                creature_name, worker_role, font_mode
            ) VALUES (
                1, '#EFE6D4', '#141413', '#D8FF3E', '#FF5E8E',
                '#0e62d1', '#16c784', 28, 2.4,
                'WAVE-08 (Cobalt Scout)', 'Engineer', 'editorial'
            )
            """
        )
        self.conn.commit()

    def get_design(self) -> Dict[str, Any]:
        row = self.conn.execute("SELECT * FROM studio_design WHERE id = 1").fetchone()
        return dict(row)

    def save_design(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        current = self.get_design()
        updated = {
            "paper_hex": payload.get("paper_hex", current["paper_hex"]),
            "ink_hex": payload.get("ink_hex", current["ink_hex"]),
            "lime_hex": payload.get("lime_hex", current["lime_hex"]),
            "blush_hex": payload.get("blush_hex", current["blush_hex"]),
            "shell_tint": payload.get("shell_tint", current["shell_tint"]),
            "optic_hex": payload.get("optic_hex", current["optic_hex"]),
            "nfc_slot_mm": int(payload.get("nfc_slot_mm", current["nfc_slot_mm"])),
            "wall_thickness_mm": float(payload.get("wall_thickness_mm", current["wall_thickness_mm"])),
            "creature_name": payload.get("creature_name", current["creature_name"]),
            "worker_role": payload.get("worker_role", current["worker_role"]),
            "font_mode": payload.get("font_mode", current["font_mode"]),
        }
        self.conn.execute(
            """
            UPDATE studio_design
            SET paper_hex = ?, ink_hex = ?, lime_hex = ?, blush_hex = ?,
                shell_tint = ?, optic_hex = ?, nfc_slot_mm = ?, wall_thickness_mm = ?,
                creature_name = ?, worker_role = ?, font_mode = ?
            WHERE id = 1
            """,
            (
                updated["paper_hex"],
                updated["ink_hex"],
                updated["lime_hex"],
                updated["blush_hex"],
                updated["shell_tint"],
                updated["optic_hex"],
                updated["nfc_slot_mm"],
                updated["wall_thickness_mm"],
                updated["creature_name"],
                updated["worker_role"],
                updated["font_mode"],
            ),
        )
        self.conn.commit()
        return self.get_design()

    def list_available_docs(self) -> List[Tuple[str, str]]:
        """Returns ordered list of (doc_id, display_title) across the White Paper, Master Blueprint, and /seed/."""
        docs: List[Tuple[str, str]] = [
            ("MASTER_BOOK", "★ THE WHOLE THING (Unified White Paper + Blueprint + Seed Book)"),
            ("29-white-paper.md", "White Paper: Identity, Embodiment & Royalties"),
            ("28-case-study.md", "Build Case 01: Kernel, Shell & 7-Day Memory Protocol"),
            ("00-context.md", "00 — Master Venture Context & 7-Point MVP"),
            ("ROOT:PRODUCT-VISION.md", "Blueprint: 8-Layer Product Architecture (10yo / 24yo / Professor)"),
            ("ROOT:ARCHITECTURE.md", "Blueprint: Software, SQLite Kernel & Hybrid AI Architecture"),
            ("ROOT:COMPANY-IDENTITY.md", "Blueprint: Robotic Discipline × Animal Scrypt × Disciple × Madken"),
            ("ROOT:FEATURE-REGISTRY.md", "Blueprint: Complete 20-Field Feature Registry"),
        ]
        for p in sorted(SEED_DIR.glob("*.md")):
            if p.name not in ("00-context.md", "28-case-study.md", "29-white-paper.md"):
                docs.append((p.name, f"Seed / {p.name}"))
        return docs

    def load_doc_markdown(self, doc_id: str) -> str:
        # Check if overridden in studio_docs
        row = self.conn.execute("SELECT content FROM studio_docs WHERE doc_id = ?", (doc_id,)).fetchone()
        if row:
            return row["content"]

        if doc_id == "MASTER_BOOK":
            parts: List[str] = []
            ordered_files = [
                SEED_DIR / "29-white-paper.md",
                SEED_DIR / "00-context.md",
                REPO_ROOT / "COMPANY-IDENTITY.md",
                REPO_ROOT / "PRODUCT-VISION.md",
                REPO_ROOT / "ARCHITECTURE.md",
                SEED_DIR / "01-board.md",
                SEED_DIR / "02-competitors.md",
                SEED_DIR / "04-offer.md",
                SEED_DIR / "05-pricing.md",
                SEED_DIR / "06-cfo.md",
                SEED_DIR / "07-canvas.md",
                SEED_DIR / "08-business-plan.md",
                SEED_DIR / "09-market.md",
                SEED_DIR / "11-deck-investor.md",
                SEED_DIR / "22-legal-menu.md",
                SEED_DIR / "28-case-study.md",
            ]
            for fp in ordered_files:
                if fp.exists():
                    parts.append(fp.read_text(encoding="utf-8"))
            return "\n\n---\n\n".join(parts)

        if doc_id.startswith("ROOT:"):
            fname = doc_id.split("ROOT:", 1)[1]
            fp = REPO_ROOT / fname
            if fp.exists():
                return fp.read_text(encoding="utf-8")

        fp = SEED_DIR / doc_id
        if fp.exists():
            return fp.read_text(encoding="utf-8")

        return self.load_doc_markdown("29-white-paper.md")

    def save_doc_markdown(self, doc_id: str, content: str) -> Dict[str, str]:
        self.conn.execute(
            "INSERT OR REPLACE INTO studio_docs (doc_id, content) VALUES (?, ?)",
            (doc_id, content),
        )
        self.conn.commit()
        return {"doc_id": doc_id, "content": content}

    def handle_request(
        self, method: str, path: str, body: Optional[str] = None
    ) -> Tuple[int, Dict[str, str], str]:
        parsed = urllib.parse.urlparse(path)
        clean_path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if method == "POST" and clean_path == "/api/studio/design":
            payload = json.loads(body or "{}")
            saved = self.save_design(payload)
            return 200, {"Content-Type": "application/json"}, json.dumps(saved)

        if method == "POST" and clean_path == "/api/studio/doc":
            payload = json.loads(body or "{}")
            doc_id = payload.get("doc_id", "29-white-paper.md")
            content = payload.get("content", "")
            saved = self.save_doc_markdown(doc_id, content)
            return 200, {"Content-Type": "application/json"}, json.dumps(saved)

        if method == "GET" and clean_path == "/api/studio/doc":
            doc_id = query.get("doc", ["MASTER_BOOK"])[0]
            md = self.load_doc_markdown(doc_id)
            return 200, {"Content-Type": "application/json"}, json.dumps(
                {"doc_id": doc_id, "markdown": md, "html": markdown_to_rich_html(md)}
            )

        selected_doc = query.get("doc", query.get("file", ["MASTER_BOOK"]))[0]
        return 200, {"Content-Type": "text/html; charset=utf-8"}, self.render_studio_html(selected_doc)

    def render_studio_html(self, selected_doc: str = "MASTER_BOOK") -> str:
        d = self.get_design()
        docs = self.list_available_docs()
        valid_ids = {doc_id for doc_id, _ in docs}
        if selected_doc not in valid_ids:
            selected_doc = "MASTER_BOOK"
        md_content = self.load_doc_markdown(selected_doc)
        rendered_html = markdown_to_rich_html(md_content)

        doc_options = "".join(
            f"<option value='{html.escape(doc_id)}' {'selected' if doc_id == selected_doc else ''}>{html.escape(label)}</option>"
            for doc_id, label in docs
        )
        chapter_pills = "".join(
            f"<a href='/studio?doc={urllib.parse.quote(doc_id)}' class='chap-pill {'active' if doc_id == selected_doc else ''}'>{html.escape(label)}</a>"
            for doc_id, label in docs[:10]
        )

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Robotic Discipline × Animal Scrypt — Visual Design Studio, Blueprint &amp; White Paper</title>
<style>
  :root {{
    --paper: {d['paper_hex']};
    --ink: {d['ink_hex']};
    --lime: {d['lime_hex']};
    --blush: {d['blush_hex']};
    --shell-tint: {d['shell_tint']};
    --optic-hex: {d['optic_hex']};
    --body-font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --head-font: Georgia, "Times New Roman", serif;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    background: var(--paper);
    color: var(--ink);
    font-family: var(--body-font);
    margin: 0;
    padding: 0;
    line-height: 1.6;
  }}
  .studio-shell {{
    display: grid;
    grid-template-columns: 330px 1fr;
    min-height: calc(100vh - 50px);
  }}
  @media (max-width: 960px) {{
    .studio-shell {{ grid-template-columns: 1fr; }}
  }}
  /* Left Visual Design & Blueprint Inspector */
  .inspector {{
    border-right: 2px solid var(--ink);
    padding: 1.25rem;
    background: rgba(255,255,255,0.45);
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
  }}
  .inspector h2 {{
    font-family: var(--head-font);
    font-size: 1.05rem;
    margin: 0 0 0.75rem 0;
    padding-bottom: 0.35rem;
    border-bottom: 2px solid var(--ink);
  }}
  .control-group {{
    margin-bottom: 0.9rem;
  }}
  .control-group label {{
    display: block;
    font-family: "Courier New", monospace;
    font-size: 0.78rem;
    font-weight: bold;
    margin-bottom: 0.25rem;
  }}
  .color-row {{
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }}
  .color-row input[type="color"] {{
    width: 38px;
    height: 32px;
    border: 2px solid var(--ink);
    padding: 0;
    cursor: pointer;
    background: none;
  }}
  .color-row input[type="text"], .inspector input[type="text"], .inspector input[type="number"], .inspector select {{
    width: 100%;
    padding: 0.4rem 0.5rem;
    border: 2px solid var(--ink);
    background: #fff;
    font-family: "Courier New", monospace;
    font-size: 0.82rem;
  }}
  .btn {{
    display: inline-block;
    background: var(--ink);
    color: var(--paper);
    border: 2px solid var(--ink);
    padding: 0.5rem 0.85rem;
    font-weight: bold;
    font-size: 0.82rem;
    cursor: pointer;
    text-decoration: none;
    margin-right: 0.35rem;
    margin-bottom: 0.35rem;
  }}
  .btn-lime {{
    background: var(--lime);
    color: var(--ink);
  }}
  .btn-blush {{
    background: var(--blush);
    color: #fff;
  }}
  /* Main Canvas: Blueprint Schematic + White Paper Book */
  .main-stage {{
    padding: 1.5rem 2.25rem 4rem;
    max-width: 1060px;
  }}
  .blueprint-box {{
    border: 2px solid var(--ink);
    background: #101419;
    color: #e2e8f0;
    padding: 1.25rem;
    box-shadow: 6px 6px 0 var(--ink);
    margin-bottom: 2rem;
  }}
  .blueprint-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px dashed #3b82f6;
    padding-bottom: 0.6rem;
    margin-bottom: 1rem;
    font-family: "Courier New", monospace;
    font-size: 0.82rem;
  }}
  .blueprint-grid {{
    display: grid;
    grid-template-columns: 1.15fr 1fr;
    gap: 1.25rem;
    align-items: center;
  }}
  @media (max-width: 760px) {{
    .blueprint-grid {{ grid-template-columns: 1fr; }}
  }}
  .chap-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1.25rem;
  }}
  .chap-pill {{
    border: 1.5px solid var(--ink);
    padding: 0.25rem 0.6rem;
    font-family: "Courier New", monospace;
    font-size: 0.76rem;
    text-decoration: none;
    color: var(--ink);
    background: rgba(255,255,255,0.5);
  }}
  .chap-pill.active {{
    background: var(--lime);
    font-weight: bold;
  }}
  /* White Paper & Master Book Publication Sheet */
  .paper-sheet {{
    border: 2px solid var(--ink);
    background: rgba(255,255,255,0.72);
    padding: 2.5rem 3rem;
    box-shadow: 6px 6px 0 var(--ink);
  }}
  @media (max-width: 760px) {{
    .paper-sheet {{ padding: 1.25rem; }}
  }}
  .paper-sheet[contenteditable="true"] {{
    outline: 3px dashed var(--blush);
    background: #fff;
  }}
  .wp-h1 {{
    font-family: var(--head-font);
    font-size: 2.2rem;
    line-height: 1.15;
    border-bottom: 3px solid var(--ink);
    padding-bottom: 0.6rem;
    margin-top: 1.5rem;
  }}
  .wp-h2 {{
    font-family: var(--head-font);
    font-size: 1.5rem;
    margin-top: 2rem;
    border-bottom: 1.5px solid var(--ink);
    padding-bottom: 0.3rem;
  }}
  .wp-h3 {{
    font-family: var(--head-font);
    font-size: 1.2rem;
    margin-top: 1.4rem;
  }}
  .wp-p, .wp-list li {{
    font-size: 1.02rem;
    line-height: 1.68;
  }}
  .wp-quote {{
    border-left: 4px solid var(--blush);
    background: rgba(0,0,0,0.04);
    margin: 1rem 0;
    padding: 0.75rem 1rem;
    font-style: italic;
  }}
  .table-wrap {{
    overflow-x: auto;
    margin: 1.25rem 0;
  }}
  .wp-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
  }}
  .wp-table th, .wp-table td {{
    border: 1.5px solid var(--ink);
    padding: 0.5rem 0.65rem;
    text-align: left;
    vertical-align: top;
  }}
  .wp-table th {{
    background: var(--lime);
    font-family: "Courier New", monospace;
    font-size: 0.82rem;
  }}
  .code-block {{
    background: #141413;
    color: #EFE6D4;
    padding: 1rem;
    overflow-x: auto;
    font-family: "Courier New", monospace;
    font-size: 0.84rem;
    border: 2px solid var(--ink);
  }}
  code {{
    font-family: "Courier New", monospace;
    background: rgba(0,0,0,0.08);
    padding: 0.1rem 0.3rem;
    font-size: 0.88em;
  }}
  .code-block code {{ background: none; padding: 0; }}
  .wp-rule {{
    border: none;
    border-top: 2px solid var(--ink);
    margin: 2.25rem 0;
  }}
  #raw-md-editor {{
    display: none;
    width: 100%;
    min-height: 600px;
    font-family: "Courier New", monospace;
    font-size: 0.9rem;
    padding: 1.25rem;
    border: 2px solid var(--ink);
    background: #141413;
    color: #EFE6D4;
    margin-bottom: 1rem;
  }}
</style>
</head>
<body>
  <div class="studio-shell">
    <!-- LEFT PANEL: VISUAL DESIGN & HARDWARE BLUEPRINT INSPECTOR -->
    <aside class="inspector">
      <h2>1. Visual Design &amp; Brand Inspector</h2>
      <div class="control-group">
        <label>Cream Paper Background</label>
        <div class="color-row">
          <input type="color" id="pick-paper" value="{d['paper_hex']}" oninput="syncColor('paper', this.value)" />
          <input type="text" id="hex-paper" value="{d['paper_hex']}" oninput="syncColor('paper', this.value)" />
        </div>
      </div>
      <div class="control-group">
        <label>Deep Ink Text &amp; Borders</label>
        <div class="color-row">
          <input type="color" id="pick-ink" value="{d['ink_hex']}" oninput="syncColor('ink', this.value)" />
          <input type="text" id="hex-ink" value="{d['ink_hex']}" oninput="syncColor('ink', this.value)" />
        </div>
      </div>
      <div class="control-group">
        <label>Acid Lime Accent</label>
        <div class="color-row">
          <input type="color" id="pick-lime" value="{d['lime_hex']}" oninput="syncColor('lime', this.value)" />
          <input type="text" id="hex-lime" value="{d['lime_hex']}" oninput="syncColor('lime', this.value)" />
        </div>
      </div>
      <div class="control-group">
        <label>Hot Blush Accent (Test &amp; Lock Hex)</label>
        <div class="color-row">
          <input type="color" id="pick-blush" value="{d['blush_hex']}" oninput="syncColor('blush', this.value)" />
          <input type="text" id="hex-blush" value="{d['blush_hex']}" oninput="syncColor('blush', this.value)" />
        </div>
      </div>
      <div class="control-group">
        <label>Typography Mode</label>
        <select id="font-mode" onchange="changeFontMode(this.value)">
          <option value="editorial" {'selected' if d['font_mode']=='editorial' else ''}>Editorial Zine (Georgia + Sans)</option>
          <option value="technical" {'selected' if d['font_mode']=='technical' else ''}>Technical Blueprint (Monospace)</option>
          <option value="modern" {'selected' if d['font_mode']=='modern' else ''}>Clean Studio Sans</option>
        </select>
      </div>

      <h2 style="margin-top:1.5rem;">2. Creature Shell CAD Parameters</h2>
      <div class="control-group">
        <label>Creature Designation</label>
        <input type="text" id="creature-name" value="{html.escape(d['creature_name'])}" oninput="updateBlueprint()" />
      </div>
      <div class="control-group">
        <label>Primary Worker Role</label>
        <select id="worker-role" onchange="updateBlueprint()">
          <option value="Engineer" {'selected' if d['worker_role']=='Engineer' else ''}>Engineer (V1 Active)</option>
          <option value="Artist" {'selected' if d['worker_role']=='Artist' else ''}>Artist (Planned)</option>
          <option value="Musician" {'selected' if d['worker_role']=='Musician' else ''}>Musician (Planned)</option>
          <option value="Researcher" {'selected' if d['worker_role']=='Researcher' else ''}>Researcher (Planned)</option>
        </select>
      </div>
      <div class="control-group">
        <label>Translucent Shell Tint</label>
        <div class="color-row">
          <input type="color" id="pick-shell" value="{d['shell_tint']}" oninput="syncColor('shell', this.value)" />
          <input type="text" id="hex-shell" value="{d['shell_tint']}" oninput="syncColor('shell', this.value)" />
        </div>
      </div>
      <div class="control-group">
        <label>Optic / Core Accent Color</label>
        <div class="color-row">
          <input type="color" id="pick-optic" value="{d['optic_hex']}" oninput="syncColor('optic', this.value)" />
          <input type="text" id="hex-optic" value="{d['optic_hex']}" oninput="syncColor('optic', this.value)" />
        </div>
      </div>
      <div class="control-group">
        <label>NFC Base Slot Diameter (mm)</label>
        <input type="number" id="nfc-slot" value="{d['nfc_slot_mm']}" min="18" max="45" oninput="updateBlueprint()" />
      </div>
      <div class="control-group">
        <label>Shell Wall Thickness (mm)</label>
        <input type="number" id="wall-thick" value="{d['wall_thickness_mm']}" step="0.2" min="1.2" max="5.0" oninput="updateBlueprint()" />
      </div>

      <button class="btn btn-lime" style="width:100%;margin-top:0.5rem;" onclick="saveDesignState()">Save Visual Design &amp; Blueprint</button>
      <button class="btn" style="width:100%;margin-top:0.35rem;" onclick="window.print()">Print / Export PDF Zine</button>
      <div id="design-status" style="font-family:'Courier New',monospace;font-size:0.76rem;margin-top:0.4rem;"></div>
    </aside>

    <!-- RIGHT STAGE: INTERACTIVE BLUEPRINT + WHITE PAPER / MASTER BOOK READER & EDITOR -->
    <main class="main-stage">
      <!-- TOP SCHEMATIC: INTERACTIVE HARDWARE & SHELL BLUEPRINT -->
      <section class="blueprint-box">
        <div class="blueprint-header">
          <div><strong>Interactive Hardware &amp; Shell Blueprint</strong> // ROBOTIC DISCIPLINE &times; ANIMAL SCRYPT CAD SHEET</div>
          <div id="bp-meta-tag">UNIT: {html.escape(d['creature_name'])} | ROLE: {html.escape(d['worker_role'])}</div>
        </div>
        <div class="blueprint-grid">
          <div>
            <svg id="creature-svg" viewBox="0 0 420 260" width="100%" style="background:#0b0f17;border:1px solid #1e293b;">
              <!-- Technical Blueprint Grid Lines -->
              <defs>
                <pattern id="bp-grid" width="20" height="20" patternUnits="userSpaceOnUse">
                  <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.8"/>
                </pattern>
              </defs>
              <rect width="420" height="260" fill="url(#bp-grid)" />
              <!-- Articulated Head / Ears (Translucent Shell) -->
              <polygon id="svg-ears" points="145,55 165,20 185,55" fill="{d['shell_tint']}" fill-opacity="0.55" stroke="#93c5fd" stroke-width="1.5"/>
              <polygon id="svg-ears-r" points="235,55 255,20 275,55" fill="{d['shell_tint']}" fill-opacity="0.55" stroke="#93c5fd" stroke-width="1.5"/>
              <rect id="svg-head" x="140" y="50" width="140" height="78" rx="14" fill="{d['shell_tint']}" fill-opacity="0.65" stroke="#bfdbfe" stroke-width="2"/>
              <!-- Visor & Optic Accents -->
              <rect x="156" y="68" width="108" height="34" rx="6" fill="#090d14" stroke="#60a5fa" stroke-width="1.2"/>
              <circle id="svg-optic-l" cx="182" cy="85" r="8" fill="{d['optic_hex']}" />
              <circle id="svg-optic-r" cx="238" cy="85" r="8" fill="{d['optic_hex']}" />
              <!-- Torso & Core -->
              <rect id="svg-torso" x="152" y="134" width="116" height="74" rx="10" fill="{d['shell_tint']}" fill-opacity="0.6" stroke="#bfdbfe" stroke-width="2"/>
              <circle id="svg-core" cx="210" cy="170" r="14" fill="{d['optic_hex']}" fill-opacity="0.35" stroke="{d['optic_hex']}" stroke-width="2"/>
              <!-- Recessed NTAG215 NFC Base Slot -->
              <rect x="135" y="212" width="150" height="22" rx="4" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
              <rect id="svg-nfc" x="170" y="216" width="80" height="14" rx="2" fill="none" stroke="{d['lime_hex']}" stroke-width="1.8" stroke-dasharray="4,2"/>
              <!-- Callout Labels -->
              <text x="14" y="30" fill="#93c5fd" font-family="Courier New" font-size="10">FIG 1. ARTICULATED SHELL CHASSIS</text>
              <text id="svg-wall-label" x="14" y="155" fill="#cbd5e1" font-family="Courier New" font-size="10">WALL: {d['wall_thickness_mm']}mm PLA/RESIN</text>
              <text id="svg-nfc-label" x="14" y="226" fill="{d['lime_hex']}" font-family="Courier New" font-size="10">NTAG215 SLOT: {d['nfc_slot_mm']}mm</text>
              <text id="svg-blush-tag" x="295" y="88" fill="{d['blush_hex']}" font-family="Courier New" font-size="10">OPTIC + LORE CORE</text>
            </svg>
          </div>
          <div style="font-family:'Courier New',monospace;font-size:0.82rem;line-height:1.55;">
            <div style="color:var(--lime);font-weight:bold;margin-bottom:0.4rem;">SYSTEM ARCHITECTURE BLUEPRINT</div>
            <div>1. <strong>Physical Layer:</strong> 3D-printed shell (<span id="spec-wall">{d['wall_thickness_mm']}</span>mm wall) + <span id="spec-nfc">{d['nfc_slot_mm']}</span>mm recessed NTAG215 NFC tag.</div>
            <div>2. <strong>Identity Layer:</strong> Immutable <code>authored_lore</code> separated from user conversation.</div>
            <div>3. <strong>Memory Layer:</strong> Explicit 3-state SQLite ledger (<code>PROPOSED &rarr; APPROVED &rarr; DELETED</code>).</div>
            <div>4. <strong>Royalty Layer:</strong> Single-hop 20% creator royalty in <code>royalty_ledger</code> on child mint.</div>
            <div style="margin-top:0.65rem;padding-top:0.5rem;border-top:1px dashed #334155;">
              <strong>Price Growth Ladder:</strong><br/>
              Tier 1: $45 + $9/mo (SCAD V1)<br/>
              Tier 2: $129-$199 + $19-$29/mo<br/>
              Tier 3: $249 + $39-$49/mo<br/>
              Tier 4: $2,500 Founding Cohort
            </div>
          </div>
        </div>
      </section>

      <!-- WHITE PAPER & MASTER BLUEPRINT READER / VISUAL EDITOR -->
      <section>
        <div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:0.75rem;margin-bottom:0.85rem;">
          <h2 style="font-family:var(--head-font);margin:0;">White Paper &amp; Master Blueprint Reader / Editor</h2>
          <div>
            <select id="doc-selector" onchange="window.location.href='/studio?doc='+encodeURIComponent(this.value)" style="padding:0.45rem;border:2px solid var(--ink);font-family:'Courier New',monospace;font-weight:bold;background:#fff;">
              {doc_options}
            </select>
          </div>
        </div>

        <div class="chap-bar">{chapter_pills}</div>

        <div style="margin-bottom:1rem;display:flex;flex-wrap:wrap;gap:0.4rem;align-items:center;">
          <button class="btn btn-lime" id="btn-visual-edit" onclick="toggleVisualEdit()">Click to Visually Edit Text On Page</button>
          <button class="btn" id="btn-md-edit" onclick="toggleMarkdownEdit()">Edit Raw Markdown</button>
          <button class="btn btn-blush" onclick="saveDocumentEdits()">Save Document Edits</button>
          <button class="btn" onclick="downloadMarkdown()">Download .md</button>
          <span id="doc-save-msg" style="font-family:'Courier New',monospace;font-size:0.8rem;font-weight:bold;"></span>
        </div>

        <textarea id="raw-md-editor">{html.escape(md_content)}</textarea>

        <article id="paper-sheet" class="paper-sheet" contenteditable="false">
          {rendered_html}
        </article>
      </section>
    </main>
  </div>

  <script>
    const currentDocId = {json.dumps(selected_doc)};

    function syncColor(kind, val) {{
      if (kind === 'paper') {{
        document.documentElement.style.setProperty('--paper', val);
        document.getElementById('pick-paper').value = val;
        document.getElementById('hex-paper').value = val;
      }} else if (kind === 'ink') {{
        document.documentElement.style.setProperty('--ink', val);
        document.getElementById('pick-ink').value = val;
        document.getElementById('hex-ink').value = val;
      }} else if (kind === 'lime') {{
        document.documentElement.style.setProperty('--lime', val);
        document.getElementById('pick-lime').value = val;
        document.getElementById('hex-lime').value = val;
        document.getElementById('svg-nfc').setAttribute('stroke', val);
        document.getElementById('svg-nfc-label').setAttribute('fill', val);
      }} else if (kind === 'blush') {{
        document.documentElement.style.setProperty('--blush', val);
        document.getElementById('pick-blush').value = val;
        document.getElementById('hex-blush').value = val;
        document.getElementById('svg-blush-tag').setAttribute('fill', val);
      }} else if (kind === 'shell') {{
        document.documentElement.style.setProperty('--shell-tint', val);
        document.getElementById('pick-shell').value = val;
        document.getElementById('hex-shell').value = val;
        ['svg-head', 'svg-torso', 'svg-ears', 'svg-ears-r'].forEach(id => {{
          document.getElementById(id).setAttribute('fill', val);
        }});
      }} else if (kind === 'optic') {{
        document.documentElement.style.setProperty('--optic-hex', val);
        document.getElementById('pick-optic').value = val;
        document.getElementById('hex-optic').value = val;
        document.getElementById('svg-optic-l').setAttribute('fill', val);
        document.getElementById('svg-optic-r').setAttribute('fill', val);
        document.getElementById('svg-core').setAttribute('fill', val);
        document.getElementById('svg-core').setAttribute('stroke', val);
      }}
    }}

    function changeFontMode(mode) {{
      if (mode === 'technical') {{
        document.documentElement.style.setProperty('--body-font', '"Courier New", Courier, monospace');
        document.documentElement.style.setProperty('--head-font', '"Courier New", Courier, monospace');
      }} else if (mode === 'modern') {{
        document.documentElement.style.setProperty('--body-font', '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif');
        document.documentElement.style.setProperty('--head-font', '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif');
      }} else {{
        document.documentElement.style.setProperty('--body-font', '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif');
        document.documentElement.style.setProperty('--head-font', 'Georgia, "Times New Roman", serif');
      }}
    }}

    function updateBlueprint() {{
      const name = document.getElementById('creature-name').value;
      const role = document.getElementById('worker-role').value;
      const nfc = document.getElementById('nfc-slot').value;
      const wall = document.getElementById('wall-thick').value;
      document.getElementById('bp-meta-tag').textContent = `UNIT: ${{name}} | ROLE: ${{role}}`;
      document.getElementById('svg-wall-label').textContent = `WALL: ${{wall}}mm PLA/RESIN`;
      document.getElementById('svg-nfc-label').textContent = `NTAG215 SLOT: ${{nfc}}mm`;
      document.getElementById('spec-wall').textContent = wall;
      document.getElementById('spec-nfc').textContent = nfc;
    }}

    async function saveDesignState() {{
      const payload = {{
        paper_hex: document.getElementById('hex-paper').value,
        ink_hex: document.getElementById('hex-ink').value,
        lime_hex: document.getElementById('hex-lime').value,
        blush_hex: document.getElementById('hex-blush').value,
        shell_tint: document.getElementById('hex-shell').value,
        optic_hex: document.getElementById('hex-optic').value,
        nfc_slot_mm: parseInt(document.getElementById('nfc-slot').value || '28', 10),
        wall_thickness_mm: parseFloat(document.getElementById('wall-thick').value || '2.4'),
        creature_name: document.getElementById('creature-name').value,
        worker_role: document.getElementById('worker-role').value,
        font_mode: document.getElementById('font-mode').value
      }};
      localStorage.setItem('animal_scrypt_design', JSON.stringify(payload));
      const res = await fetch('/api/studio/design', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify(payload)
      }});
      if (res.ok) {{
        document.getElementById('design-status').textContent = '✓ Saved visual design & shell blueprint.';
      }}
    }}

    function toggleVisualEdit() {{
      const sheet = document.getElementById('paper-sheet');
      const btn = document.getElementById('btn-visual-edit');
      const isEditing = sheet.getAttribute('contenteditable') === 'true';
      sheet.setAttribute('contenteditable', isEditing ? 'false' : 'true');
      btn.textContent = isEditing ? 'Click to Visually Edit Text On Page' : '✓ Visual Editing Active (Click any text below)';
      if (!isEditing) sheet.focus();
    }}

    function toggleMarkdownEdit() {{
      const mdBox = document.getElementById('raw-md-editor');
      const sheet = document.getElementById('paper-sheet');
      const showingMd = mdBox.style.display === 'block';
      mdBox.style.display = showingMd ? 'none' : 'block';
      sheet.style.display = showingMd ? 'block' : 'none';
    }}

    async function saveDocumentEdits() {{
      const mdBox = document.getElementById('raw-md-editor');
      const sheet = document.getElementById('paper-sheet');
      const content = mdBox.style.display === 'block' ? mdBox.value : sheet.innerText;
      localStorage.setItem('animal_scrypt_doc_' + currentDocId, content);
      const res = await fetch('/api/studio/doc', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{doc_id: currentDocId, content}})
      }});
      if (res.ok) {{
        document.getElementById('doc-save-msg').textContent = '✓ Saved edits to ' + currentDocId;
      }}
    }}

    function downloadMarkdown() {{
      const mdBox = document.getElementById('raw-md-editor');
      const sheet = document.getElementById('paper-sheet');
      const content = mdBox.style.display === 'block' ? mdBox.value : sheet.innerText;
      const blob = new Blob([content], {{type: 'text/markdown;charset=utf-8'}});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = currentDocId === 'MASTER_BOOK' ? 'Robotic-Discipline-Animal-Scrypt-Master-Book.md' : currentDocId;
      a.click();
    }}
  </script>
</body>
</html>"""
