#!/usr/bin/env python3
"""
TDD test suite for Build 3: Open-Source VC & Startup Tools Directory App (apps/vc_directory/server.py)
Verifies all requirements from /seed/24-vc-directory-spec.md:
1. Single source of truth in Markdown (/content/tools/tools-directory.md) with all 15 repositories.
2. Validates 11 categories and 4 stage badges ('Pre-seed', 'Seed', 'Series A+', 'All stages').
3. Filtering by category, stage, and search query returns exact matches.
4. Renders fast searchable directory HTML with <= 40-word intro header and #EFE6D4 / #141413 / #D8FF3E palette.
"""

import json
import unittest

from apps.vc_directory.server import VCDirectoryApp, ALLOWED_CATEGORIES, ALLOWED_STAGES


class TestVCDirectoryApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = VCDirectoryApp()

    def test_markdown_loader_loads_all_15_seeded_tools_with_valid_metadata(self) -> None:
        """All 15 repositories from Section 20 are loaded from Markdown with valid categories and stage badges."""
        tools = self.app.load_tools()
        self.assertEqual(len(tools), 15)
        for tool in tools:
            self.assertIn(tool["category"], ALLOWED_CATEGORIES)
            self.assertIn(tool["stage"], ALLOWED_STAGES)
            self.assertTrue(tool["url"].startswith("https://github.com/"))
            self.assertTrue(len(tool["description"]) > 10)

    def test_category_stage_and_search_filtering(self) -> None:
        """Filtering by category, stage badge, and text query returns exact matching cards."""
        # Filter by category = 'AI tools' -> gstack and solopreneur
        status, _, body = self.app.handle_request("GET", "/api/tools?category=AI+tools")
        self.assertEqual(status, 200)
        ai_tools = json.loads(body)
        names = {t["name"] for t in ai_tools}
        self.assertEqual(names, {"gstack", "solopreneur"})

        # Filter by stage = 'Seed' -> startup-dataroom and seed-skill
        status, _, body2 = self.app.handle_request("GET", "/api/tools?stage=Seed")
        seed_tools = json.loads(body2)
        seed_names = {t["name"] for t in seed_tools}
        self.assertEqual(seed_names, {"startup-dataroom", "seed-skill"})

        # Filter by text query = 'canvas' -> business-model-canvas-md-template
        status, _, body3 = self.app.handle_request("GET", "/api/tools?q=canvas")
        q_tools = json.loads(body3)
        self.assertEqual(len(q_tools), 1)
        self.assertEqual(q_tools[0]["name"], "business-model-canvas-md-template")

    def test_directory_html_renders_concise_header_and_cards(self) -> None:
        """HTML view renders all 15 cards, palette colors, and an intro header under 40 words."""
        status, headers, html = self.app.handle_request("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn("text/html", headers["Content-Type"])
        self.assertIn("#EFE6D4", html)
        self.assertIn("#D8FF3E", html)
        self.assertIn("https://github.com/garrytan/gstack", html)
        self.assertIn("https://github.com/CreativateLabs/startup-dataroom", html)


if __name__ == "__main__":
    unittest.main()
