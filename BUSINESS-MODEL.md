# BUSINESS MODEL — Robotic Discipline

**Company:** Robotic Discipline  
**Stage:** Pre-Revenue / Customer Discovery & Prototype Validation  
**Epistemic Note:** All prices, conversion rates, and cost figures below are **explicitly labeled hypotheses and benchmark estimates** for experimentation, not realized historical revenue.

---

## 1. Business Model Canvas (with Founder Guiding Questions)

### 1. Customer Segments
*Who needs this most right now, and who will actually pay first?*
* **Beachhead Segment (Primary MVP Target):** **Creative University Students & Solo Makers/Founders** (starting at SCAD: industrial design, animation, game development, interactive design, and student entrepreneurs) who spend 6–10 hours/day building projects at a desk, collect character figures, use AI tools daily, and experience solo-studio isolation.
* **Adjacent Segment A (Collectible & Mecha Enthusiasts):** Young adults (ages 18–34) who already buy desk figures (Pop Mart, Bandai/Gundam, MechatroWeGo, Amiibo) and want their collectibles to have a living digital identity and utility.
* **Adjacent Segment B (Intentional Study Groups / Makerspaces):** Small cohorts of 2–6 friends, dormmates, or studio collaborators using shared docks and parallel-presence rituals.
* *Guiding Question for KJ:* Which specific group of 10 people at SCAD can you sit down with this week to watch them use the prototype for 15 minutes?

### 2. Value Propositions
*What concrete job does Robotic Discipline do better than a plain chatbot or an inert plastic toy?*
* **Tangible Focus & Context Switching:** Place your physical character on your desk dock to immediately open your project workspace (*Spaceport*), pre-loaded with your role-specific AI agent (Engineer, Scholar, Athlete) and files.
* **Inspectable, User-Owned Memory:** Zero creepy cloud surveillance or amnesia—you approve every memory your character keeps and can export your character's mind as a portable file (`ORBIT` JSON).
* **Low-Pressure Human Connection:** Work alongside friends in 15-minute silent **Parallel Presence** blocks that evolve a **Shared Ritual Object**, taking the social exhaustion out of staying connected.
* *Guiding Question for KJ:* When a customer finishes their first 15-minute session, what tangible output do they have that makes them glad they showed up?

### 3. Channels
*How do first customers discover, test, and buy Robotic Discipline?*
* **Campus & Maker Direct (Phase 1–3):** Live table demos at SCAD entrepreneurship events, SCAD Pro studios, and capstone showcases.
* **The Book & Content Flywheel (`The Book of Robotic Discipline`):** Publishing the 18 Laws as free essays + the 10 downloadable founder worksheets, converting readers into beta testers of the workspace.
* **Viral Pair Invites:** Every **Shared Ritual Object** and **Bilateral Memory Fragment Exchange** naturally requires a second participant, turning 1 user into 2.
* *Guiding Question for KJ:* Can a new user try the software workspace in 60 seconds using a printable QR/NFC card before buying a 3D-printed figure?

### 4. Customer Relationships
*How do users stay engaged across weeks and waves?*
* **Personal Ownership & Continuity:** The user owns their character's memory ledger and progression record.
* **Zero-Shame Dormancy:** Unlike punitive streak apps, if a user misses a week during finals, their character and ritual object wait patiently in `DORMANT` state without guilt-tripping notifications.
* **Wave-Based Collectible Progression:** Optional seasonal lore missions, workshop verification stamps, and new character classes.

### 5. Revenue Streams (Hypotheses to Test)
*What will people actually pay for, and how do we test willingness to pay?*

| Revenue Stream | Proposed Offer | Target Price Range (To Test) | Margin Profile | Stage |
| :--- | :--- | :--- | :--- | :--- |
| **1. Starter Physical-Digital Character Kit** | 3D-printed / small-batch articulated figure (or NFC collector card) + Portable Identity Code + Local Spaceport Workspace | **$29 – $49** (Card/Mini) / **$69 – $99** (Articulated Figure + USB-C Dock) | ~60%–75% gross margin at small batch | **MVP / Phase 3** |
| **2. Cloud Sync, Multi-Agent & Managed Inference Tier** | Optional monthly subscription for hosted cloud LLM routing, cross-device sync, and multi-user ritual rooms (local/BYO-model stays free!) | **$9 – $15 / month** | ~75%–80% gross margin | **Phase 4** |
| **3. Additional Character Archetypes & Skill Packs** | Expanding from 1 figure (e.g., Engineer) to a 3-figure Dock Council (+ Scholar, + Commander) | **$24 – $39 per figure** | ~70% gross margin | **V2** |
| **4. *The Book of Robotic Discipline* & Workbook** | Field manual e-book / print-on-demand + 10 startup worksheets | **$0 (Lead magnet essays) → $19–$29 (Book)** | ~85% digital / ~50% print | **Parallel Channel** |
| **5. Creator Marketplace & Studio Licenses** | Third-party character shells, custom agent roles, and educational/makerspace kits | **10%–15% marketplace fee** or **$250+/seat studio kit** | High software margin | **Future (Phase 6+)** |

### 6. Key Resources
* **Existing:** Stage-1 Python/SQLite state & permission kernel (`skeleton/`), SCAD prototyping & 3D-printing lab access, founder creative/design/system architecture IP, *The Book of Robotic Discipline* manuscript plan.
* **Needed:** Original 3D character CAD/sculpt for the first founding character (replacing the third-party `madken1.jpeg` reference image), USB-C NFC dock housing prototype, local Ollama/LangGraph connector.

### 7. Key Activities
1. Running 10 structured customer discovery & usability sessions at SCAD.
2. Iterating the local-first character workspace and NFC dock pairing loop using strict TDD.
3. Documenting real weekly progress in the Friday review cadence (feeding both the SCAD Accelerator coach meetings and *The Book of Robotic Discipline*).

### 8. Key Partnerships
* **SCAD Ecosystem:** SCAD Accelerator coaches (e.g., David Chang, Adrian Gill), SCAD Pro branding studio (Oscar Bettenker), and SCAD digital fabrication/3D printing labs.
* **Open-Source AI Stack:** Ollama, LangGraph, SQLite, PostgreSQL.

### 9. Cost Structure (Estimated Prototype & Early Unit Economics)

| Cost Category | Prototype / Bootstrap Estimate (1–50 Units) | Assumptions & Notes |
| :--- | :--- | :--- |
| **Physical Figure Shell (3D Printed PLA/Resin)** | **$3.50 – $8.00 / unit** | Printed via SCAD fabrication lab or desktop Bambu/Elegoo printer. |
| **NFC Tag (NTAG215 or NTAG424 DNA)** | **$0.25 – $0.85 / unit** | Passive 13.56 MHz sticker embedded in figure base or removable cartridge. |
| **Desktop USB-C NFC Dock (Gen-1)** | **$12.00 – $18.00 / unit** | Off-the-shelf PN532 / ACR122U PCB module inside a 3D-printed dock shell. |
| **Packaging & Collector Zine Insert** | **$1.50 – $3.00 / unit** | Printed editorial zine quick-start guide + QR backup code. |
| **Total Hardware Prototype BOM (Figure + Dock)** | **~$17.25 – $29.85 / kit** | Supports a **$59–$79** pilot kit price with >50% gross margin even at 10-unit hand-built scale. |
| **AI Inference Cost per Active User** | **$0.00 / mo (Local Ollama)** or **~$0.80 – $2.50 / mo (Cloud API)** | Using small/medium models (Llama 3.2 / Qwen 2.5 / Gemini Flash) with strict 3-sentence zine output constraints. |
| **Web / Database Hosting (MVP)** | **$0 – $20 / mo** | Local-first SQLite requires $0 hosting; optional Supabase/Vercel free-to-pro tier for shared ritual rooms. |

---

## 2. The "First Million Math" (From *The Book of Robotic Discipline*, Law 16)

Rather than inventing speculative multi-billion-dollar hockey sticks, Robotic Discipline uses transparent arithmetic to evaluate revenue paths:
* **Path A (Consumer Hardware + Companion Subscription):**
  * 1,000 active owners paying an average of **$84/month** (or **5,000 owners** spending **$200/year** across a $79 starter dock kit + two $35 expansion figures + $9/mo cloud/council pass) = **$1,000,000 ARR**.
* **Path B (Immediate 90-Day Accelerator Milestone):**
  * Conduct **10 customer interviews**, build **3 working NFC figure + dock prototypes**, and secure **your first 10 paying pilot users** at **$39–$79 per kit** ($390–$790 in verified Day-1 customer revenue).
