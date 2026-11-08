#!/usr/bin/env python3
"""
TDD test suite for the unified Vercel deployment gateway (api/index.py).
Verifies that a single Vercel deployment serves:
- `/` (Section 19 Portfolio Front Page + Navigation Bar to all apps)
- `/workspace` & `/api/workspace/*` (Build 1: Interactive Creature Workspace & 20% Royalty Simulator)
- `/dataroom` & `/api/dataroom/*` (Build 2: Self-Hosted Investor Data Room with Stage 1 / Stage 2 NDA Gate)
- `/directory` & `/api/directory/*` (Build 3: Open-Source VC & Startup Tools Directory)
- `/zine` (Stage-1 Zine Terminal View)
- `/seed` (Seed Repository Index `00-context.md` through `29-white-paper.md`)
"""

import json
import unittest

from api.index import route_request


class TestVercelGateway(unittest.TestCase):
    def test_all_primary_views_render_200(self) -> None:
        for path in ["/", "/workspace", "/dataroom", "/directory", "/zine", "/seed"]:
            status, headers, body = route_request("GET", path)
            self.assertEqual(status, 200, f"Failed on {path}")
            self.assertIn("text/html", headers["Content-Type"])
            self.assertTrue(len(body) > 200)

    def test_workspace_and_dataroom_and_directory_apis_on_gateway(self) -> None:
        # Workspace state API
        status, _, body = route_request("GET", "/api/state")
        self.assertEqual(status, 200)
        data = json.loads(body)
        self.assertEqual(data["companion_manifest"]["id"], "mk-08-wave")

        # Data room Stage 2 room returns 403 before NDA
        status, _, _ = route_request("GET", "/api/rooms/cap-table")
        self.assertEqual(status, 403)

        # VC Directory API returns 15 tools
        status, _, tools_body = route_request("GET", "/api/tools")
        self.assertEqual(status, 200)
        self.assertEqual(len(json.loads(tools_body)), 15)


if __name__ == "__main__":
    unittest.main()
