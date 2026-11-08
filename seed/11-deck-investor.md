# 11 — Investor Deck (`/deck` — Laptop Read)

**Context read:** [`00-context.md`](./00-context.md) through [`10-investor-match.md`](./10-investor-match.md)  
**How it is seen:** Alone, on a laptop, skimmed in 2 minutes.  
**Design Rules:** Cream paper background (`#EFE6D4`), dark ink (`#101419`), acid lime highlights (`#D8FF3E`). Hot blush is unset—do not use a made-up pink hex. 18–24 pt type minimum. Zero paragraphs.

---

## Slide 1 — Title & The Moment
* **Headline:** **ANIMAL SCRYPT** *(Robotic Discipline)*
* **Sub-line:** You collect an animal that remembers you, and it can grow up into a worker. If someone copies it, the original maker still gets paid.
* **Specific Moment:** Last Tuesday at 1 a.m. in a SCAD studio, I opened a new chat tab to check my CAD joint tolerances—and the AI had forgotten every measurement from Monday.
* **Visual:** Photo of a 3D-printed animal shell next to a laptop running the cream-and-lime zine workspace.

---

## Slide 2 — The Animal That Remembers (In One Picture)
* **Visual (Full Slide):** Split photo:
  * **Left:** A 3D-printed animal shell held in a hand, showing the NFC/QR tag on its base.
  * **Right:** The browser workspace showing three green `[APPROVED]` memory cards from 7 days ago and the creature using them in a new answer.
* **Caption (20 pt):** Scan the shell. Approve what it keeps. Come back a week later and it still knows your work.

---

## Slide 3 — What Is Broken About Chatbots and Toys
* **Chatbots forget or hallucinate:**
  * Character.ai charges `$9.99/mo` and Replika charges `$19.99/mo`, yet users complain every day on Reddit that bots forget plot and project facts after a short chat (https://www.reddit.com/r/CharacterAI/, https://replika.com).
* **Collectible toys sit on a shelf and do nothing:**
  * Pop Mart sold `~$5.1B+ USD` (RMB 37.12B) of vinyl figures in 2025 with zero digital memory (https://www.popmart.com).
  * Tonies sold `EUR 630M` in FY 2025 across 173M+ NFC figures that only play static audio tracks (https://ir.tonies.com).
  * Desktop robots like Living.AI EMO (`$279`) die in 2 hours and fail on dorm Wi-Fi (https://living.ai).

---

## Slide 4 — The Product: Memory, Role, Shell
* **1. Inspectable Memory:** The animal never silently saves chat noise. It proposes a fact; you click **Approve**, **Edit**, or **Delete**.
* **2. Worker Role:** Each animal takes a job—**engineer, artist, musician, or researcher**—and builds a domain memory bank over weeks.
* **3. 3D-Printed Shell:** A physical twin printed at SCAD with a passive QR/NFC tag. Zero batteries to charge, zero Wi-Fi chips to break.

---

## Slide 5 — How the Royalty Works (One Diagram)
```mermaid
flowchart LR
    A["Maker A trains Parent Animal\n(Approves 20 CAD & Print Facts)"] -->|Publishes Worker Template\n(Private notes stripped)| B["Buyer B forks Child Animal\nPays $45 (V1) -> $149 (Pro)"]
    B -->|20% Creator Royalty| A
    B -->|80% Net Revenue| C["Animal Scrypt\n(Prints shell + hosts workspace)"]
```
* **Rule for v1:** One parent, one child, one payout event (paid child mint). No multi-level pyramid, no payout on free test forks.

---

## Slide 6 — Why We Can Build the Shell (SCAD as Factory)
* **Built in Savannah at SCAD:** 18,550 art, design, and engineering students in one ecosystem (https://www.scad.edu/about/scad-glance).
* **Zero injection-mold capex:** We print shells on campus, embed a `$0.30` (`assumption:`) NFC/QR tag, and film the build process as our organic marketing channel.
* **Unit cost (`assumption:` from `06-cfo.md`):** `~$7.50` physical shell + packaging, `~$1.50` Month-1 model tokens = `~$10.61` total Day-1 cost with payment fees.

---

## Slide 7 — What Is True Today (No Fake Traction)
* **Paid users & revenue today:** **$0** (0 of 3 consenting adult MVP tests completed; `00-context.md`).
* **What already runs locally:** Python + SQLite state kernel (`skeleton/interfaces.py`) implementing companion registration, `PROPOSED -> APPROVED -> DELETED` memory gates, portable JSON identity export, and simulated ledger records.
* **Adjacent empirical work:** Founder's SCADpro research thread on AI sensing for horses (equine telehealth, gait, vocalization)—same core question: giving an animal a longitudinal record a human can trust.

---

## Slide 8 — What the Next 8 Weeks Prove (The 7-Box MVP Checklist)
1. `[ ]` **1 Physical Creature:** 3D-printed shell with QR/NFC tag linked to digital identity.
2. `[ ]` **1 Persistent Personality:** Name, biography, voice, and chat UI.
3. `[ ]` **7-Day Memory:** Recalls $\ge 3$ user-approved facts after 7 days and an app restart.
4. `[ ]` **1 Digital Workspace:** Browser dashboard with profile, chat, and memory controls.
5. `[ ]` **1 Ownership Record:** Verified owner views and controls pairing.
6. `[ ]` **1 Royalty Demonstration:** Simulated creator-to-owner transfer records royalty split in a test ledger.
7. `[ ]` **3 Consenting Adults:** Independently complete activation, conversation, and Day-7 return tasks.

---

## Slide 9 — How Prices and Customers Grow (`05-pricing.md`)
* **Phase 1 (Weeks 1–8 — SCAD Makers & Collectors, 18–30):** `assumption: $45` shell + `$9/mo` memory workspace (`278` SCAD buyers at 1.5% conversion = `~$60k` campus beachhead; `09-market.md`).
* **Phase 2 (Months 3–6 — Pro Worker & Studios):** `assumption: $129–$199` multi-part shell/dock + `$19–$29/mo`.
* **Phase 3 (Months 6–12 — Accessible Companions & Self-Directed Learning):** `assumption: $249` kit + `$39–$49/mo` for assistive users and parents seeking Alpha School-style adaptive project tools (`$40,000/yr` benchmark; https://alpha.school).
* **Phase 4 (Post-Proof Cohort):** Planned `~300 × $2,500` Founding Cohort (`$750k` gross scenario; opened only after Day-14 retention is measured).

---

## Slide 10 — Team & The Ask
* **Founder:** **Kendren "KJ" Cornish** — Rising sophomore at SCAD (Savannah). U.S. military veteran (~8 months served, diver path). Resident assistant. Helps run family nonprofit and church conference. Builds both the software kernel and the physical shells.
* **The Ask:**
  * **SCAD Accelerator:** Cohort admission + mentorship from David Chang and Adrian Gill to ship the first 50 shells by May Demo Day.
  * **Pre-Seed / Accelerator Round (Post-MVP Gate):** **$150,000 – $500,000** (`assumption:` standard YC/Techstars/pre-seed SAFE) to fund:
    1. **40% (`~$60k–$200k`):** Small-batch shell fabrication, NFC dock tooling, and shipping for the first 1,500 units.
    2. **35% (`~$52k–$175k`):** Next.js + Supabase + Litecoin royalty ledger engineering and security audit.
    3. **25% (`~$38k–$125k`):** 18 months of founder runway and campus pilot operations in Savannah.

---

## Appendix Slides (Included in File for Skeptical Readers)
* **Appendix A — Founding Cohort Scenario Math (`05-pricing.md`):** `300 × $2,500 = $750,000` gross $\to$ `~$604,580` net after `10%` refund reserve, `$35` shell/shipping, 12-month compute reserve, and legal (`assumption:`).
* **Appendix B — Competitor Matrix (`02-competitors.md`):** Head-to-head vs. Character.ai, Replika, Tonies, Living.AI EMO, Pop Mart, Sintra/Relevance AI, and why we avoid CryptoZoo's mistakes.
* **Appendix C — Risk Register (`08-business-plan.md`):** Day-7 novelty drop-off, memory pollution, crypto stigma, and SCAD IP verification.
