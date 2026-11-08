#!/usr/bin/env python3
"""
Unified Vercel Serverless Gateway for Robotic Discipline (Animal Scrypt / Disciple / Madken).
Serves all 3 approved builds + Zine Demo + /seed Repository Index from one URL:
- `/`          -> Section 19 Portfolio Front Page
- `/workspace` -> Build 1: Interactive Creature Workspace & 20% Royalty Simulator
- `/dataroom`  -> Build 2: Self-Hosted Investor Data Room (Stage 1 & Stage 2 NDA Gate)
- `/directory` -> Build 3: Open-Source VC & Startup Tools Directory (15 GitHub Repos)
- `/zine`      -> Stage-1 Zine Terminal View (`skeleton/zine_demo_view.html`)
- `/seed`      -> Interactive `/seed/` Operating Repository Index (`00-context.md` .. `29-white-paper.md`)
"""

from __future__ import annotations
import html
import json
import pathlib
import tempfile
import urllib.parse
from http.server import BaseHTTPRequestHandler
from typing import Dict, Tuple, Optional, Any

from skeleton.workspace_server import WorkspaceApp
from apps.dataroom.server import DataRoomApp
from apps.vc_directory.server import VCDirectoryApp

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED_DIR = REPO_ROOT / "seed"
ZINE_HTML_PATH = REPO_ROOT / "skeleton" / "zine_demo_view.html"

TMP_DIR = pathlib.Path(tempfile.gettempdir())
WORKSPACE_DB = str(TMP_DIR / "animal_scrypt_vercel_workspace.db")
DATAROOM_DB = str(TMP_DIR / "animal_scrypt_vercel_dataroom.db")

_workspace_app: Optional[WorkspaceApp] = None
_dataroom_app: Optional[DataRoomApp] = None
_directory_app: Optional[VCDirectoryApp] = None


def get_apps() -> Tuple[WorkspaceApp, DataRoomApp, VCDirectoryApp]:
    global _workspace_app, _dataroom_app, _directory_app
    if _workspace_app is None:
        _workspace_app = WorkspaceApp(db_path=WORKSPACE_DB)
    if _dataroom_app is None:
        _dataroom_app = DataRoomApp(db_path=DATAROOM_DB)
    if _directory_app is None:
        _directory_app = VCDirectoryApp()
    return _workspace_app, _dataroom_app, _directory_app


GLOBAL_NAV_BAR = """
<div style="background:#141413;color:#EFE6D4;padding:0.65rem 1.25rem;font-family:'Courier New',monospace;font-size:0.82rem;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:0.5rem;border-bottom:2px solid #D8FF3E;">
  <div><strong>ROBOTIC DISCIPLINE</strong> // ANIMAL SCRYPT &times; DISCIPLE &times; MADKEN</div>
  <div style="display:flex;flex-wrap:wrap;gap:0.85rem;">
    <a href="/" style="color:#D8FF3E;text-decoration:none;font-weight:bold;">[1. Portfolio]</a>
    <a href="/workspace" style="color:#EFE6D4;text-decoration:none;">[2. Creature Workspace]</a>
    <a href="/dataroom" style="color:#EFE6D4;text-decoration:none;">[3. Investor Data Room]</a>
    <a href="/directory" style="color:#EFE6D4;text-decoration:none;">[4. VC Tools Directory]</a>
    <a href="/zine" style="color:#EFE6D4;text-decoration:none;">[5. Zine Terminal]</a>
    <a href="/seed" style="color:#EFE6D4;text-decoration:none;">[6. /seed Docs (00-29)]</a>
  </div>
</div>
"""


def inject_nav(page_html: str) -> str:
    if "<body>" in page_html:
        return page_html.replace("<body>", "<body>\n" + GLOBAL_NAV_BAR, 1)
    return GLOBAL_NAV_BAR + page_html


def render_seed_viewer(selected_file: str = "00-context.md") -> str:
    files = sorted(p.name for p in SEED_DIR.glob("*.md"))
    if selected_file not in files:
        selected_file = "00-context.md"
    content = (SEED_DIR / selected_file).read_text(encoding="utf-8")
    links_html = "".join(
        f"<li style='margin-bottom:0.35rem;'><a href='/seed?file={urllib.parse.quote(fname)}' "
        f"style='color:#141413;font-weight:{'bold' if fname == selected_file else 'normal'};"
        f"background:{'#D8FF3E' if fname == selected_file else 'transparent'};padding:0.1rem 0.3rem;text-decoration:none;'>"
        f"{fname}</a></li>"
        for fname in files
    )
    return inject_nav(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>/seed/{selected_file} — Animal Scrypt Operating Repository</title>
<style>
  body {{ background:#EFE6D4; color:#141413; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; margin:0; line-height:1.55; }}
  .layout {{ display:grid; grid-template-columns: 280px 1fr; max-width:1280px; margin:0 auto; padding:1.5rem; gap:1.5rem; }}
  @media (max-width: 800px) {{ .layout {{ grid-template-columns: 1fr; }} }}
  .sidebar {{ border:2px solid #141413; padding:1rem; background:rgba(255,255,255,0.45); box-shadow:4px 4px 0 #141413; height:fit-content; }}
  .viewer {{ border:2px solid #141413; padding:1.5rem; background:rgba(255,255,255,0.65); box-shadow:4px 4px 0 #141413; overflow-x:auto; }}
  pre {{ white-space:pre-wrap; word-wrap:break-word; font-family:"Courier New",Courier,monospace; font-size:0.88rem; margin:0; }}
  h2 {{ font-family:Georgia,serif; margin-top:0; font-size:1.15rem; border-bottom:2px solid #141413; padding-bottom:0.4rem; }}
</style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <h2>/seed/ Files ({len(files)})</h2>
      <ul style="list-style:none;padding:0;margin:0;font-family:'Courier New',monospace;font-size:0.82rem;">
        {links_html}
      </ul>
    </aside>
    <main class="viewer">
      <h2>Viewing: <code>/seed/{html.escape(selected_file)}</code></h2>
      <pre>{html.escape(content)}</pre>
    </main>
  </div>
</body>
</html>""")


def route_request(
    method: str, path: str, body: Optional[str] = None, ip_address: str = "127.0.0.1"
) -> Tuple[int, Dict[str, str], str]:
    workspace_app, dataroom_app, directory_app = get_apps()
    parsed = urllib.parse.urlparse(path)
    clean_path = parsed.path
    query = urllib.parse.parse_qs(parsed.query)

    # 1. Portfolio & Creature Workspace routes
    if clean_path in ("/", "/workspace") or clean_path.startswith("/api/memory/") or clean_path.startswith("/api/royalty/") or clean_path in ("/api/state", "/api/export"):
        status, headers, resp_body = workspace_app.handle_request(method, clean_path, body)
        if "text/html" in headers.get("Content-Type", ""):
            resp_body = inject_nav(resp_body)
        return status, headers, resp_body

    # 2. Self-Hosted Investor Data Room routes
    if clean_path == "/dataroom":
        sub_query = f"?{parsed.query}" if parsed.query else ""
        status, headers, resp_body = dataroom_app.handle_request("GET", f"/{sub_query}", ip_address=ip_address)
        # Rewrite language switcher links inside dataroom view to stay on /dataroom
        resp_body = resp_body.replace('href="/?lang=', 'href="/dataroom?lang=')
        return status, headers, inject_nav(resp_body)

    if (
        clean_path.startswith("/api/rooms/")
        or clean_path.startswith("/api/nda/")
        or clean_path.startswith("/api/admin/")
        or clean_path == "/api/chat"
        or clean_path.startswith("/api/me")
    ):
        return dataroom_app.handle_request(method, path, body, ip_address=ip_address)

    # 3. Open-Source VC & Startup Tools Directory routes
    if clean_path == "/directory":
        sub_query = f"?{parsed.query}" if parsed.query else ""
        status, headers, resp_body = directory_app.handle_request("GET", f"/{sub_query}")
        resp_body = resp_body.replace("href='/?", "href='/directory?").replace('action="/"', 'action="/directory"').replace('href="/"', 'href="/directory"')
        return status, headers, inject_nav(resp_body)

    if clean_path == "/api/tools":
        return directory_app.handle_request(method, path)

    # 4. Stage-1 Zine Terminal View
    if clean_path == "/zine":
        zine_html = ZINE_HTML_PATH.read_text(encoding="utf-8")
        return 200, {"Content-Type": "text/html; charset=utf-8"}, inject_nav(zine_html)

    # 5. Interactive /seed Repository Viewer
    if clean_path == "/seed":
        selected = query.get("file", ["00-context.md"])[0]
        return 200, {"Content-Type": "text/html; charset=utf-8"}, render_seed_viewer(selected)

    return 404, {"Content-Type": "application/json"}, json.dumps({"error": f"Route {clean_path} not found"})


class handler(BaseHTTPRequestHandler):
    """Vercel Python Serverless Function entrypoint."""

    def do_GET(self) -> None:
        ip = self.headers.get("x-forwarded-for", self.client_address[0] if self.client_address else "127.0.0.1")
        status, headers, resp_body = route_request("GET", self.path, ip_address=ip)
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(resp_body.encode("utf-8"))

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        ip = self.headers.get("x-forwarded-for", self.client_address[0] if self.client_address else "127.0.0.1")
        status, headers, resp_body = route_request("POST", self.path, raw, ip_address=ip)
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(resp_body.encode("utf-8"))

    def do_DELETE(self) -> None:
        ip = self.headers.get("x-forwarded-for", self.client_address[0] if self.client_address else "127.0.0.1")
        status, headers, resp_body = route_request("DELETE", self.path, ip_address=ip)
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(resp_body.encode("utf-8"))

    def log_message(self, format: str, *args: Any) -> None:
        return
