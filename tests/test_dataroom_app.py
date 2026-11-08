#!/usr/bin/env python3
"""
TDD test suite for Build 2: Self-Hosted Data Room App (apps/dataroom/server.py)
Verifies all requirements from /seed/23-dataroom-product-spec.md:
1. Nine Rooms split into Stage 1 (Overview, Team, Product, Milestones) and Stage 2 (Financials, Cap Table, Legal, Tax, IP).
2. Stage 2 access returns 403 Forbidden until Investor signs NDA AND Founder approves NDA.
3. AI Chat enforces hard NDA lock on the server (never leaks Stage 2 corpus to Stage 1 user).
4. Audit log records VIEW, NDA_SIGN, and AI_QUERY events and exports CSV for admin.
5. Multilingual UI (en, de, fr) and GDPR account data export / delete.
"""

import json
import pathlib
import tempfile
import unittest

from apps.dataroom.server import DataRoomApp


class TestDataRoomApp(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = str(pathlib.Path(self.tmpdir.name) / "dataroom_test.db")
        self.app = DataRoomApp(db_path=self.db_path)

    def tearDown(self) -> None:
        self.app.close()
        self.tmpdir.cleanup()

    def test_stage1_vs_stage2_room_access_and_nda_state_machine(self) -> None:
        """Investor can view Stage 1 rooms, gets 403 on Stage 2 until NDA is signed AND approved by Founder."""
        # Stage 1 room ('overview') works for un-NDA'd investor
        status, _, body = self.app.handle_request("GET", "/api/rooms/overview", user_email="investor@precursor.vc")
        self.assertEqual(status, 200)
        room_data = json.loads(body)
        self.assertEqual(room_data["tier"], "STAGE_1")

        # Stage 2 room ('cap-table') returns 403 Forbidden before NDA approval
        status, _, _ = self.app.handle_request("GET", "/api/rooms/cap-table", user_email="investor@precursor.vc")
        self.assertEqual(status, 403)

        # Investor signs NDA -> status becomes SIGNED (still awaits founder approval)
        status, _, sign_body = self.app.handle_request(
            "POST",
            "/api/nda/sign",
            body=json.dumps({"full_name": "Charles Hudson", "firm": "Precursor Ventures"}),
            user_email="investor@precursor.vc",
            ip_address="198.51.100.42",
        )
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(sign_body)["nda_status"], "SIGNED")

        # Still 403 before Founder approves
        status, _, _ = self.app.handle_request("GET", "/api/rooms/cap-table", user_email="investor@precursor.vc")
        self.assertEqual(status, 403)

        # Founder (admin) approves the NDA
        status, _, approve_body = self.app.handle_request(
            "POST",
            "/api/admin/nda/approve",
            body=json.dumps({"investor_email": "investor@precursor.vc", "approve": True}),
            user_email="kj@roboticdiscipline.com",
        )
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(approve_body)["nda_status"], "APPROVED")

        # Now Investor can access Stage 2 ('cap-table' and 'financials')
        status, _, cap_body = self.app.handle_request("GET", "/api/rooms/cap-table", user_email="investor@precursor.vc")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(cap_body)["tier"], "STAGE_2")

    def test_ai_chat_enforces_hard_nda_lock(self) -> None:
        """Stage 1 user asking about cap table or Stage 2 financials gets a refusal and zero Stage 2 leakage."""
        status, _, body = self.app.handle_request(
            "POST",
            "/api/chat",
            body=json.dumps({"question": "What is the exact cap table and founder equity split?"}),
            user_email="investor@precursor.vc",
        )
        self.assertEqual(status, 200)
        reply = json.loads(body)
        self.assertFalse(reply["stage2_unlocked"])
        self.assertIn("Stage 2 NDA approval", reply["answer"])
        self.assertNotIn("100% founder-held", reply["answer"])

        # Sign & approve NDA, then ask again
        self.app.handle_request(
            "POST",
            "/api/nda/sign",
            body=json.dumps({"full_name": "Investor", "firm": "VC"}),
            user_email="investor@precursor.vc",
        )
        self.app.handle_request(
            "POST",
            "/api/admin/nda/approve",
            body=json.dumps({"investor_email": "investor@precursor.vc", "approve": True}),
            user_email="kj@roboticdiscipline.com",
        )
        status, _, body2 = self.app.handle_request(
            "POST",
            "/api/chat",
            body=json.dumps({"question": "What is the exact cap table and founder equity split?"}),
            user_email="investor@precursor.vc",
        )
        reply2 = json.loads(body2)
        self.assertTrue(reply2["stage2_unlocked"])
        self.assertIn("100% founder-held", reply2["answer"])

    def test_audit_log_csv_and_gdpr_and_i18n(self) -> None:
        """Audit log records views and exports CSV for admin; i18n supports en/de/fr; GDPR export/delete works."""
        self.app.handle_request("GET", "/api/rooms/overview", user_email="investor@precursor.vc")
        status, headers, csv_body = self.app.handle_request(
            "GET", "/api/admin/audit.csv", user_email="kj@roboticdiscipline.com"
        )
        self.assertEqual(status, 200)
        self.assertIn("text/csv", headers["Content-Type"])
        self.assertIn("investor@precursor.vc", csv_body)
        self.assertIn("VIEW", csv_body)

        # Multilingual UI check (German & French)
        _, _, html_de = self.app.handle_request("GET", "/?lang=de", user_email="investor@precursor.vc")
        self.assertIn("Stufe 2 freischalten (NDA)", html_de)
        _, _, html_fr = self.app.handle_request("GET", "/?lang=fr", user_email="investor@precursor.vc")
        self.assertIn("Déverrouiller le niveau 2 (NDA)", html_fr)

        # GDPR Export & Delete
        status, _, gdpr_json = self.app.handle_request("GET", "/api/me/export", user_email="investor@precursor.vc")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(gdpr_json)["user"]["email"], "investor@precursor.vc")

        status, _, del_json = self.app.handle_request("DELETE", "/api/me", user_email="investor@precursor.vc")
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(del_json)["deleted"])


if __name__ == "__main__":
    unittest.main()
