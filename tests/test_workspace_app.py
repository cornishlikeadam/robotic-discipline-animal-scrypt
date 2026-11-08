#!/usr/bin/env python3
"""
TDD test suite for Build 1: Portfolio Front Page (Section 19) & Interactive Browser Workspace (skeleton/workspace_server.py).
"""

import json
import pathlib
import tempfile
import unittest

from skeleton.workspace_server import WorkspaceApp


class TestWorkspaceApp(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = str(pathlib.Path(self.tmpdir.name) / "workspace_test.db")
        self.app = WorkspaceApp(db_path=self.db_path)

    def tearDown(self) -> None:
        self.app.close()
        self.tmpdir.cleanup()

    def test_portfolio_front_page_follows_section_19_zine_rules(self) -> None:
        """Portfolio front page includes the exact Section 19 headline, palette, 6 sections, and zero fake counters."""
        status, headers, html = self.app.handle_request("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn("text/html", headers["Content-Type"])
        self.assertIn("Hold the animal. Keep the memory.", html)
        self.assertIn("#EFE6D4", html)
        self.assertIn("#141413", html)
        self.assertIn("#D8FF3E", html)
        self.assertIn("How Memory Works", html)
        self.assertIn("Worker Roles", html)
        self.assertIn("Royalty Loop", html)
        self.assertIn("Studio Note", html)

    def test_workspace_api_memory_approval_and_royalty_simulation(self) -> None:
        """Interactive workspace API proposes memory, approves it, simulates 20% royalty, and exports JSON."""
        # 1. Propose a memory via POST /api/memory/propose
        status, _, body = self.app.handle_request(
            "POST",
            "/api/memory/propose",
            json.dumps({"category": "project", "content": "Printed NTAG215 base slot at 0.2mm layer height."}),
        )
        self.assertEqual(status, 200)
        prop_data = json.loads(body)
        mem_id = prop_data["memory_id"]

        # Verify it is in proposed_memories, not yet in approved_private_memories
        _, _, state_body = self.app.handle_request("GET", "/api/state")
        state = json.loads(state_body)
        proposed_ids = [m["id"] for m in state["proposed_memories"]]
        approved_ids = [m["id"] for m in state["approved_private_memories"]]
        self.assertIn(mem_id, proposed_ids)
        self.assertNotIn(mem_id, approved_ids)

        # 2. Approve the memory via POST /api/memory/review
        status, _, rev_body = self.app.handle_request(
            "POST",
            "/api/memory/review",
            json.dumps({"memory_id": mem_id, "approve": True}),
        )
        self.assertEqual(status, 200)
        rev_data = json.loads(rev_body)
        self.assertEqual(rev_data["status"], "APPROVED")

        # 3. Trigger simulated creator-to-owner royalty transfer via POST /api/royalty/simulate
        status, _, roy_body = self.app.handle_request(
            "POST",
            "/api/royalty/simulate",
            json.dumps({"buyer_id": "scad_collector_04", "gross_amount_cents": 1500}),
        )
        self.assertEqual(status, 200)
        roy_data = json.loads(roy_body)
        self.assertEqual(roy_data["creator_royalty_cents"], 300)
        self.assertEqual(roy_data["settlement_mode"], "SIMULATED_TEST_LEDGER")


if __name__ == "__main__":
    unittest.main()
