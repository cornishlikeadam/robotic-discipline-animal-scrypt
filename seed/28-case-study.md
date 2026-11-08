replaced 2026-11-08 because founder approved and executed Builds 1, 2, and 3 (royalty_ledger + workspace server, self-hosted dataroom, and VC tools directory).

# 28 — Build Case Study: One Animal, One Kernel, and the 7-Day Memory Test Plan (`/case`)

**Context read:** [`00-context.md`](./00-context.md), [`skeleton/interfaces.py`](../skeleton/interfaces.py), [`skeleton/schema.sql`](../skeleton/schema.sql)  
**Epistemic Status:** **BUILD CASE (Pre-User).** Per Section 17 of the Master Prompt, we have **0 real users yet**, so this document records only dated, inspectable build artifacts that exist today and the exact protocol for the 3-adult test. We do not call synthetic demo rows "user results."

---

## 1. Title
**Build Case 01 (November 8, 2026): Enforcing User-Approved Memory and Portable Identity in a Local SQLite Kernel Before Printing Shell #1**

---

## 2. Context (Who, Where, When)
* **Builder:** Kendren "KJ" Cornish (solo founder, rising sophomore and resident assistant at SCAD).
* **Location:** Savannah, Georgia.
* **Date of Inspected Build Artifacts:** November 7–8, 2026.
* **Problem Targeted:** Standard LLM chat interfaces either lose project context across sessions or silently store hallucinated chat turns in opaque cloud memory. Before printing our first physical Animal Scrypt shell at SCAD, we needed a deterministic local state kernel where:
  1. Character biography (`authored_lore`) can never be overwritten by chat dialogue.
  2. Candidate facts require explicit human approval (`PROPOSED -> APPROVED`) before entering long-term memory.
  3. Approved memories survive process restarts and export cleanly as a single user-owned JSON file.

---

## 3. What We Built and Tried (Inspected Code Only)

In [`skeleton/schema.sql`](../skeleton/schema.sql) and [`skeleton/interfaces.py`](../skeleton/interfaces.py), we implemented `AnimalScryptKernel` (497 lines of zero-dependency Python 3 + SQLite3):

1. **Companion Registration (`register_companion`):** Stores `id` (`mk-08-wave`), `owner_id`, `name`, `chassis_spec_json` (translucent cobalt-08 articulated proportions), immutable `authored_lore`, and `voice_constraints_json` (`max_sentences: 3`, `clinical_claims_allowed: false`).
2. **Explicit Memory Approval State Machine (`propose_memory` & `review_memory`):**
   * New facts are inserted into `memory_records` with `status = 'PROPOSED'`.
   * Only calling `review_memory(memory_id, approve=True)` transitions the record to `APPROVED` and stamps `approved_at` (UTC ISO-8601). Rejecting transitions it to `DELETED`.
3. **Bilateral Fragment & Ritual State Machines (`propose_fragment_exchange`, `tend_ritual_object`, `grant_capability_lease`):** Enforces dual sign-off (`sender_approved = 1 AND recipient_approved = 1`) and time-bounded worker role leases without exposing `PRIVATE` memories.
4. **Portable Identity Bundle & Zine UI Generator (`export_portable_bundle` & `render_zine_html`):** Exports `skeleton/portable_identity_export.json` ( explicitly stamped `"synthetic_demo_data": true`) and renders `skeleton/zine_demo_view.html`.

---

## 4. What the Animal Remembered in the Local Verification Run (vs. What Is Not Yet Tested)

* **Verified in Local Execution (November 8, 2026):**
  * When `memory_records` is queried for export or context injection (`SELECT * FROM memory_records WHERE companion_id = ? AND status = 'APPROVED'`), `PROPOSED` and `DELETED` records are strictly excluded.
  * When persisted to a file-backed SQLite database (instead of `:memory:`), closing the connection and re-instantiating `AnimalScryptKernel(db_path)` preserves 100% of `APPROVED` memories across restarts.
* **What Is `not yet` Completed (Human 7-Day Test):**
  * The 15-minute session note inside `portable_identity_export.json` is a **scripted synthetic demo entry**, not a real human test.
  * **0 of 3 consenting adults** have completed the 7-day elapsed calendar recall test (`00-context.md` checkboxes #3 and #7).

---

## 5. What the Person Did With the Shell (`not yet`)
* **Current Status:** We have a third-party visual reference image ([`madken1.jpeg`](../madken1.jpeg)) used to set the translucent blue panel and amber-green optic palette in `zine_demo_view.html`, but **Shell #1 has not been 3D-printed or handed to a human tester yet**.

---

## 6. What Broke During Inspection

During our November 8, 2026 audit of `skeleton/interfaces.py` and the workspace documents, three real flaws surfaced:

1. **In-Memory Default (`:memory:`):** Line 46 of `skeleton/interfaces.py` defaulted `db_path: str = ":memory:"`. An in-memory SQLite database wipes itself when the Python process exits, which would fail MVP done-condition #3 (*"accurately recalls at least three user-approved details after seven days, including after an application restart"*).
2. **Missing Parent-to-Child Royalty Table in `schema.sql`:** While `interfaces.py` implemented `capability_leases` (temporary worker borrowing), it did not yet have a dedicated `royalty_ledger` table recording the 20% creator-to-owner transfer required by MVP done-condition #6.
3. **Three-Way Customer Split in Early Notes:** Earlier drafts mixed lonely consumers, homestead cooperatives, and K–12 schools without locking a single testable v1 group.

---

## 7. What We Changed

1. **Locked the 7-Checkbox MVP & V1 Beachhead (`00-context.md` & `01-board.md`):** Narrowed v1 testing to 18–30 SCAD makers and collectors in Savannah, with a 4-tier price growth ladder (`05-pricing.md`).
2. **Shipped `royalty_ledger` & Interactive Workspace (`skeleton/schema.sql`, `skeleton/interfaces.py`, `skeleton/workspace_server.py`):** Added the `royalty_ledger` table (`20%` creator royalty, `10%` platform fee, `70%` net in `SIMULATED_TEST_LEDGER` mode) and built the Section 19 Portfolio Front Page (`/`) + Interactive Browser Workspace (`/workspace`).
3. **Shipped Self-Hosted Data Room (`apps/dataroom/server.py`) & VC Tools Directory (`apps/vc_directory/server.py`):** Implemented the 9-room investor data room with hard server-side NDA gating, CSV audit logging, and `en`/`de`/`fr` i18n, plus the Markdown-driven directory of 15 open-source VC repositories (`content/tools/tools-directory.md`).
4. **Verified 12 Automated TDD Tests (`tests/`):** Executed `python3 -m unittest discover -s tests -v` (`Ran 12 tests in 0.176s — OK`).

---

## 8. What We Still Do Not Know (To Be Measured in Week 6)

1. Will 3 independent SCAD adults remember to scan the physical shell on Day 7 without the founder standing next to them?
2. How many proposed memory cards per conversation feel helpful versus annoying?
3. What is the exact print time and filament cost (`assumption: $5.50`) of our first original 3D shell on a SCAD printer?

---

## 9. Sources & Local Artifacts
* [`skeleton/interfaces.py`](../skeleton/interfaces.py) — Python state & permission kernel.
* [`skeleton/schema.sql`](../skeleton/schema.sql) — SQLite / PostgreSQL table definitions.
* [`skeleton/portable_identity_export.json`](../skeleton/portable_identity_export.json) — Synthetic portable identity bundle (`synthetic_demo_data: true`).
* [`skeleton/zine_demo_view.html`](../skeleton/zine_demo_view.html) — Generated zine workspace preview.
* [`PROJECT_BRIEF.md`](../PROJECT_BRIEF.md) — November 8, 2026 audit notes.
