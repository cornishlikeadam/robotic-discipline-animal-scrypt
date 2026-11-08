# 25 — Software Factory & Founder Skills (`/factory`)

**Context read:** [`00-context.md`](./00-context.md), [`23-dataroom-product-spec.md`](./23-dataroom-product-spec.md), [`24-vc-directory-spec.md`](./24-vc-directory-spec.md)  
**Purpose:** Separate the **Engineering Software Factory** (which builds and tests code) from the **Founder Operating Skills** (which run the business), while keeping both anchored to `00-context.md`.

---

## Layer 1: The Engineering Software Factory (`gstack` + Strict TDD)

No feature is coded from a vague prompt. Every build runs through five slash commands in order:

| Slash Command | Role | What It Does | Output Artifact |
|---|---|---|---|
| **`/plan-ceo-review`** | **CEO** | Restates the feature in plain user language. Cuts anything not needed for the 7-checkbox MVP (`00-context.md`). Names the single riskiest assumption. **Allowed to say "do not build this."** Zero code. | 1-paragraph user story + cut list |
| **`/plan-design`** | **Designer** | Maps one screen flow using the zine brand (`#EFE6D4` cream, `#D8FF3E` lime, `#101419` ink; hot blush unset). Defines loading, empty, and error states. Flags anything that looks like generic SaaS-purple AI UI. | Wireframe flow + state table |
| **`/plan-eng-review`** | **Eng Manager** | Defines the SQLite/PostgreSQL tables, permission boundaries, NDA lock (`nda-status.md`), and failure cases. Slices the build into small tasks where **every task names the automated test that proves it**. | Task list + test names |
| **`/qa`** | **QA Engineer** | Opens the local/staging URL in a real browser (or runs headless browser + CLI verification). Clicks every flow. Files bugs with exact reproduction steps. Never "imagines" a click. | Bug report + screenshot/DOM log |
| **`/ship`** | **Release Manager** | Runs the full test suite, prepares the commit/PR summary, and writes an honest release note listing both **what passed** and **what was not tested**. | Release note + green test log |

---

### The Non-Negotiable Pre-Code & TDD Loop

1. **Clarify:** Ask until the user story fits in one paragraph.
2. **Approve Spec:** Write the spec (`23` or `24` or `/seed/prd/`) and wait for the founder's `"yes"` or `"go"`.
3. **Red-Green-Refactor TDD:**
   * **Step A (Red):** Write a failing automated test (`tests/test_*.py` or `*.test.ts`) that tests the exact requirement.
   * **Step B (Green):** Write the smallest code change that makes the test pass.
   * **Step C (Refactor):** Clean up duplication only while all tests stay green.

---

### Six Composable Factory Skills (`/skills/`)

We install six modular `SKILL.md` files in [`/skills/`](../skills/) so any compatible coding agent (Claude Code, Cursor, Antigravity, Codex) follows this loop automatically:
1. [`skills/factory-brainstorm/SKILL.md`](../skills/factory-brainstorm/SKILL.md) — `/plan-ceo-review`: Cut scope & lock 1-paragraph user story.
2. [`skills/factory-spec/SKILL.md`](../skills/factory-spec/SKILL.md) — `/plan-design` + `/plan-eng-review`: Write the spec & pause for founder approval.
3. [`skills/factory-slice-tdd/SKILL.md`](../skills/factory-slice-tdd/SKILL.md) — Slice into small tasks with Red-Green-Refactor TDD enforcement.
4. [`skills/factory-debug/SKILL.md`](../skills/factory-debug/SKILL.md) — Systematic debugging: Reproduce → Hypothesize → Instrument → Fix → Regression Test.
5. [`skills/factory-subagent-review/SKILL.md`](../skills/factory-subagent-review/SKILL.md) — One task, one owner, second-pass diff review checking `00-context.md` and `nda-status.md`.
6. [`skills/factory-ship-qa/SKILL.md`](../skills/factory-ship-qa/SKILL.md) — `/qa` and `/ship`: Real execution check + honest "what was not tested" log.

---

## Layer 2: Founder Operating Skills (What the Factory Is Not)

Every operating skill below reads [`00-context.md`](./00-context.md) first and **must echo back five fields** at the top of its output (`Stage`, `Product`, `Market`, `Team`, `Goal This Month`). If an output could fit any random SaaS startup without mentioning **the animal, the 3D-printed shell, or the parent-child royalty**, delete it and rewrite it.

| Operating Skill | Reads First | Writes or Updates | Current Status |
|---|---|---|---|
| **Pitch Deck** (`/deck`) | `00`–`10` | `11-deck-investor.md` & `12-deck-stage.md` | Written in `/seed/` |
| **Investor Research** (`/investors`) | `00`, `08`, `09` | `10-investor-match.md` | Written in `/seed/` |
| **Cold Outreach** (`/outreach`) | `00`, `10` | `17-outreach.md` | Written in `/seed/` |
| **Sales / User Call** (`/calls`) | `00`, `03`, `04` | `18-call-coach.md` + `/seed/call-notes/` | Written in `/seed/` |
| **PRD Writer** | `00`, `01` | `/seed/prd/<feature>.md` | Ready on demand |
| **User Research Script** (`/customers`) | `00`, `03` | `03-customers-100.md` (Mom Test questions) | Written in `/seed/` |
| **Job Description & Interview Kit** | `00`, `06` | `/seed/hiring/` *(Use ONLY when hiring is real; solo right now)* | Parked (`solo founder`) |
| **Architecture Review** | `00`, `nda-status.md` | Checks data room lock & 20% single-event royalty rule | Active in `skeleton/` & `23` |
| **Contract Review Checklist** | `00`, `19`, `22` | Flags traps in `19-term-sheet.md` (not legal advice) | Written in `/seed/` |
| **Privacy & Terms Checklist** | `00`, `22` | Questions for counsel + plain-language draft stamped `DRAFT` | Written in `PRIVACY.md` & `22` |
| **Growth Note** | `00`, `07` | One channel (SCAD campus prints), one week, one metric | Active in `21-investor-update.md` |
