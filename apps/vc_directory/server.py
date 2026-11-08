#!/usr/bin/env python3
"""
Robotic Discipline / Animal Scrypt — Open-Source VC & Startup Tools Directory (apps/vc_directory/server.py)
Implements /seed/24-vc-directory-spec.md:
- Single source of truth in Markdown (/content/tools/tools-directory.md), zero SQL database.
- 11 required categories + 4 required stage badges ('Pre-seed', 'Seed', 'Series A+', 'All stages').
- Search box + Category chips + Stage chips + Responsive Card Grid.
- Header strictly under 40 words.

Run locally:
    python3 apps/vc_directory/server.py --port 8083
"""

from __future__ import annotations
import argparse
import json
import pathlib
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import List, Dict, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
DEFAULT_MD_PATH = REPO_ROOT / "content" / "tools" / "tools-directory.md"

ALLOWED_CATEGORIES = [
    "deal sourcing",
    "due diligence",
    "valuation",
    "legal docs",
    "cap table management",
    "portfolio tracking",
    "fund ops",
    "startup metrics",
    "fundraising",
    "market research",
    "AI tools",
]

ALLOWED_STAGES = [
    "Pre-seed",
    "Seed",
    "Series A+",
    "All stages",
]


class VCDirectoryApp:
    """Markdown-backed searchable directory of open-source VC and startup tools."""

    def __init__(self, md_path: pathlib.Path = DEFAULT_MD_PATH) -> None:
        self.md_path = md_path

    def load_tools(self) -> List[Dict[str, str]]:
        raw = self.md_path.read_text(encoding="utf-8")
        blocks = [b.strip() for b in raw.split("---") if b.strip()]
        tools: List[Dict[str, str]] = []
        for block in blocks:
            item: Dict[str, str] = {}
            for line in block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    item[k.strip()] = v.strip().strip('"')
            if "name" in item and "url" in item:
                if item.get("category") not in ALLOWED_CATEGORIES:
                    raise ValueError(f"Invalid category '{item.get('category')}' in {item.get('name')}")
                if item.get("stage") not in ALLOWED_STAGES:
                    raise ValueError(f"Invalid stage '{item.get('stage')}' in {item.get('name')}")
                tools.append(item)
        return tools

    def filter_tools(
        self, category: str = "", stage: str = "", query: str = ""
    ) -> List[Dict[str, str]]:
        tools = self.load_tools()
        if category:
            tools = [t for t in tools if t["category"].lower() == category.lower()]
        if stage:
            tools = [t for t in tools if t["stage"].lower() == stage.lower()]
        if query:
            q = query.lower()
            tools = [
                t
                for t in tools
                if q in t["name"].lower()
                or q in t["description"].lower()
                or q in t["category"].lower()
                or q in t["language"].lower()
            ]
        return tools

    def handle_request(self, method: str, path: str) -> Tuple[int, Dict[str, str], str]:
        parsed = urllib.parse.urlparse(path)
        clean_path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)
        category = params.get("category", [""])[0]
        stage = params.get("stage", [""])[0]
        q = params.get("q", [""])[0]

        if method == "GET" and clean_path == "/api/tools":
            matched = self.filter_tools(category=category, stage=stage, query=q)
            return 200, {"Content-Type": "application/json; charset=utf-8"}, json.dumps(matched, indent=2)

        if method == "GET" and clean_path == "/":
            matched = self.filter_tools(category=category, stage=stage, query=q)
            return 200, {"Content-Type": "text/html; charset=utf-8"}, self.render_html(matched, category, stage, q)

        return 404, {"Content-Type": "application/json"}, json.dumps({"error": "Not found"})

    def render_html(
        self, tools: List[Dict[str, str]], active_category: str = "", active_stage: str = "", query: str = ""
    ) -> str:
        cat_chips = "".join(
            f"<a class='chip {'active' if c.lower() == active_category.lower() else ''}' "
            f"href='/?category={urllib.parse.quote_plus(c)}'>{c}</a>"
            for c in ALLOWED_CATEGORIES
        )
        stage_chips = "".join(
            f"<a class='chip {'active' if s.lower() == active_stage.lower() else ''}' "
            f"href='/?stage={urllib.parse.quote_plus(s)}'>{s}</a>"
            for s in ALLOWED_STAGES
        )
        cards_html = "".join(
            f"""
            <article class="card">
              <div class="card-top">
                <span class="badge stage">{t['stage']}</span>
                <span class="badge cat">{t['category']}</span>
              </div>
              <h3><a href="{t['url']}" target="_blank" rel="noopener noreferrer">{t['name']} &nearr;</a></h3>
              <p>{t['description']}</p>
              <div class="meta mono">Lang: {t['language']} | Stars: {t['stars']}</div>
            </article>
            """
            for t in tools
        )
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Open-Source VC &amp; Startup Tools Directory</title>
<style>
  :root {{
    --paper: #EFE6D4;
    --ink: #101419;
    --lime: #D8FF3E;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    background: var(--paper);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
    padding: 1.5rem;
    line-height: 1.5;
  }}
  .wrap {{ max-width: 1080px; margin: 0 auto; }}
  header {{
    border-bottom: 2px solid var(--ink);
    padding-bottom: 1rem;
    margin-bottom: 1.25rem;
  }}
  h1 {{ font-family: Georgia, serif; margin: 0 0 0.35rem 0; font-size: 1.9rem; }}
  .mono {{ font-family: "Courier New", Courier, monospace; font-size: 0.8rem; }}
  .controls {{ margin-bottom: 1.5rem; }}
  .chips {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.5rem 0; }}
  .chip {{
    display: inline-block;
    border: 1.5px solid var(--ink);
    padding: 0.2rem 0.6rem;
    text-decoration: none;
    color: var(--ink);
    font-size: 0.82rem;
    background: rgba(255,255,255,0.4);
  }}
  .chip.active {{ background: var(--lime); font-weight: bold; }}
  input[type="search"] {{
    padding: 0.5rem 0.75rem;
    border: 2px solid var(--ink);
    width: 280px;
    font-size: 0.95rem;
  }}
  button {{
    padding: 0.5rem 0.9rem;
    border: 2px solid var(--ink);
    background: var(--lime);
    font-weight: bold;
    cursor: pointer;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.1rem;
  }}
  .card {{
    border: 2px solid var(--ink);
    padding: 1rem;
    background: rgba(255,255,255,0.5);
    box-shadow: 4px 4px 0 var(--ink);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .card h3 {{ margin: 0.5rem 0; font-family: Georgia, serif; }}
  .card h3 a {{ color: var(--ink); text-decoration: none; }}
  .badge {{
    display: inline-block;
    padding: 0.1rem 0.45rem;
    border: 1px solid var(--ink);
    font-family: "Courier New", Courier, monospace;
    font-size: 0.74rem;
    font-weight: bold;
    margin-right: 0.3rem;
  }}
  .badge.stage {{ background: var(--lime); }}
  .badge.cat {{ background: #fff; }}
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>Open-Source VC &amp; Startup Tools Directory</h1>
      <!-- Under 40 words header -->
      <p style="margin:0;">Searchable index of open-source repositories for pre-seed founders, accelerators, and venture capital diligence. Rendered directly from <code>content/tools/tools-directory.md</code>.</p>
    </header>

    <div class="controls">
      <form method="GET" action="/">
        <input type="search" name="q" value="{query}" placeholder="Search tools, categories, languages..." />
        <button type="submit">Filter</button>
        <a href="/" class="mono" style="margin-left:0.5rem;color:var(--ink);">[Reset ({len(tools)} shown)]</a>
      </form>
      <div class="chips"><strong>Stage:</strong> {stage_chips}</div>
      <div class="chips"><strong>Category:</strong> {cat_chips}</div>
    </div>

    <div class="grid">{cards_html}</div>
  </div>
</body>
</html>"""


def run_server(port: int = 8083) -> None:
    app = VCDirectoryApp()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            status, headers, body = app.handle_request("GET", self.path)
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def log_message(self, format: str, *args: object) -> None:
            return

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"VC & Startup Tools Directory running on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open-Source VC & Startup Tools Directory Server")
    parser.add_argument("--port", type=int, default=8083)
    args = parser.parse_args()
    run_server(port=args.port)
