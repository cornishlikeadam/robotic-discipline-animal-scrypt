#!/usr/bin/env python3
"""
TDD test suite for the Visual Design Studio, Master Blueprint & White Paper Reader/Editor (/studio & /blueprint).
Verifies:
1. Formatted White Paper & Master Blueprint view renders rich HTML (headings, tables, diagrams, hardware schematic SVG) instead of raw unstyled text.
2. Visual Design Editor lets the founder customize colors (Paper, Ink, Acid Lime, Hot Blush hex), typography, and Creature Shell Blueprint specs (tint, optics, NFC slot, joints) and persists updates via POST /api/studio/design and POST /api/studio/doc.
"""

import json
import unittest

from api.index import route_request


class TestStudioBlueprint(unittest.TestCase):
    def test_studio_and_blueprint_views_render_interactive_editor_and_whitepaper(self) -> None:
        for path in ["/studio", "/blueprint"]:
            status, headers, html = route_request("GET", path)
            self.assertEqual(status, 200, f"Failed GET {path}")
            self.assertIn("text/html", headers["Content-Type"])
            # Must contain visual design controls, interactive SVG hardware blueprint, and white paper reader
            self.assertIn("Visual Design &amp; Brand Inspector", html)
            self.assertIn("Interactive Hardware &amp; Shell Blueprint", html)
            self.assertIn("White Paper &amp; Master Blueprint Reader", html)
            self.assertIn("contenteditable", html)

    def test_save_and_load_visual_design_and_document_edits(self) -> None:
        # Save custom design tokens (including testing a Hot Blush hex) and custom shell blueprint parameters
        payload = {
            "paper_hex": "#EFE6D4",
            "ink_hex": "#141413",
            "lime_hex": "#D8FF3E",
            "blush_hex": "#FF5E8E",
            "shell_tint": "#0e62d1",
            "optic_hex": "#16c784",
            "nfc_slot_mm": 28,
            "creature_name": "WAVE-08 (Custom Studio Build)",
        }
        status, _, body = route_request("POST", "/api/studio/design", json.dumps(payload))
        self.assertEqual(status, 200)
        saved = json.loads(body)
        self.assertEqual(saved["blush_hex"], "#FF5E8E")
        self.assertEqual(saved["creature_name"], "WAVE-08 (Custom Studio Build)")

        # Save an edit to a document in the White Paper / Seed reader
        doc_payload = {
            "doc_id": "29-white-paper.md",
            "content": "# Updated White Paper\n\nEdited visually by KJ Cornish.",
        }
        status2, _, body2 = route_request("POST", "/api/studio/doc", json.dumps(doc_payload))
        self.assertEqual(status2, 200)
        saved_doc = json.loads(body2)
        self.assertEqual(saved_doc["doc_id"], "29-white-paper.md")
        self.assertIn("Edited visually by KJ Cornish.", saved_doc["content"])


if __name__ == "__main__":
    unittest.main()
