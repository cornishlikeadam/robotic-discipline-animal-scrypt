# ASSUMPTIONS & EPISTEMIC LEDGER — Robotic Discipline

**Purpose:** Prevent older brainstorming notes, AI-generated drafts, or repeated documents from being mistaken for verified facts, working implementations, or customer traction.

---

## 1. Epistemic Classification Key

* **`[VERIFIED_FACT]`**: Confirmed directly by the founder, inspected source code execution, or dated external primary sources.
* **`[INSPECTED_SKELETON]`**: Present and executable in [`skeleton/interfaces.py`](./skeleton/interfaces.py), [`skeleton/schema.sql`](./skeleton/schema.sql), and verified by [`tests/test_kernel.py`](./tests/test_kernel.py), using synthetic demo data.
* **`[FOUNDER_HYPOTHESIS]`**: Core product or business assumption held by the founder that requires empirical customer or technical testing.
* **`[UNVALIDATED_PROPOSAL]`**: Idea present in earlier notes (`Madken space fort 2.pdf`, `DUNA_MAdken.pdf`, `More_madken_university.pdf`) that has **not** been built, legally verified, or customer-tested.

---

## 2. Master Assumption Register

| ID | Statement / Claim | Classification | Current Evidence / Reality Check | Cheapest Verification Experiment |
| :--- | :--- | :--- | :--- | :--- |
| **A-01** | MADKEN, Animal Scrypt, Disciple, and Space Fort are parts of one unified venture (**Robotic Discipline**). | `[VERIFIED_FACT]` | Confirmed directly by founder KJ Cornish in Master Prompt v2.0. | N/A (Settled founder directive). |
| **A-02** | The Stage-1 SQLite memory ledger, bilateral fragment exchange, ritual object progression, and capability flash-lease work in code. | `[INSPECTED_SKELETON]` | Inspected and executed via `python3 skeleton/interfaces.py --demo` and `tests/test_kernel.py`. Uses synthetic data (`synthetic_demo_data: true`), not live LLM inference or real users yet. | Wire `AnimalScryptKernel` to a live local Ollama or cloud LLM endpoint and run 5 real user sessions. |
| **A-03** | Creative students and solo builders prefer tapping a physical character figure to open a specialized workspace over clicking a standard web bookmark or chat tab. | `[FOUNDER_HYPOTHESIS]` | Supported by analogy to Tonies (€630M FY25 revenue) and Amiibo (77M+ units), but **unproven for adult productivity/AI workspaces**. | A/B Wizard-of-Oz test with 10 SCAD students: compare engagement with an NFC-triggered character workspace vs. a plain web tab over 5 days. |
| **A-04** | Explicit memory approval (`PROPOSED -> APPROVED`) increases user trust without causing annoying UI fatigue. | `[FOUNDER_HYPOTHESIS]` | Implemented in `skeleton/interfaces.py`, but not yet measured on independent human users. | Measure approval rate, edit rate, and user annoyance score across 10 15-minute user tests. |
| **A-05** | Shared Ritual Objects and 15-minute silent parallel presence blocks reduce perceived isolation among students/remote creators. | `[FOUNDER_HYPOTHESIS]` | Grounded in social facilitation literature, but zero empirical human-subject trials have been conducted on Animal Scrypt yet. | Run a 7-day pilot with 5 pairs of SCAD students completing daily 15-minute parallel build blocks; log retention and pre/post survey. |
| **A-06** | `madken1.jpeg` is an original Robotic Discipline hardware prototype. | `[UNVALIDATED_PROPOSAL]` (False if claimed as original IP) | Visual inspection of [`madken1.jpeg`](./madken1.jpeg) shows "wave corporation" decals and an "amiami" watermark (a commercial Japanese mecha figure). It is a **visual proportion and material reference only**, not founder-owned IP. | Create original 3D character CAD/sculpts (or commission SCAD industrial design/animation assets) before public commercial sale. |
| **A-07** | Launching 12 founding characters across 4 factions with new waves every 6 months toward ~1,100 skills in 6 years is achievable by a solo founder. | `[UNVALIDATED_PROPOSAL]` | Proposed in `DUNA_MAdken.pdf` and `More_madken_university.pdf`. Building 12 distinct hardware + software characters at launch would bankrupt a bootstrapped founder in tooling and inventory costs. | Constrain Launch Wave 0 to **1 to 3 characters** (e.g., Engineer, Scholar, Athlete) using 3D-printed shells + $0.50 NFC tags until unit economics are proven. |
| **A-08** | Every physical figure can ship with preconfigured emails, phone numbers, social accounts, and paid subscriptions with 20–60 minute onboarding (`DUNA_MAdken.pdf` p. 6). | `[UNVALIDATED_PROPOSAL]` | Automated provisioning of phone numbers/emails/socials per figure triggers severe anti-spam/KYC blocks (Twilio A2P 10DLC, Google/Meta bot bans) and recurring monthly burn even if a user stops paying. | Replace per-figure phone numbers/socials in MVP with local workspace tools and opt-in user-linked webhooks. |
| **A-09** | A Delaware PBC + Founder Trust + Wyoming DUNA + Litecoin/LitVM smart contract stack should be formed right now. | `[UNVALIDATED_PROPOSAL]` | Proposed in `DUNA_MAdken.pdf` and `Madken space fort 2.pdf`. Multi-entity crypto structures prior to revenue incur high legal costs and deter traditional accelerators. | Keep a single clean entity (LLC or Delaware PBC/C-Corp) and SQLite/PostgreSQL provenance until >100 paying users exist. |
| **A-10** | Consumer companion profits will fund neighborhood wet-labs, robotic arms, a sustainable data center, and orbital space biology (`Madken space fort 2.pdf` p. 9–10). | `[UNVALIDATED_PROPOSAL]` | Inspiring long-term moonshot narrative, but wet-labs and data centers require millions in capex and biosafety regulation. | Frame strictly as the multi-decade "Phase 6/7 North Star Vision" while keeping 100% of current execution on the Stage-1 companion and workspace. |
