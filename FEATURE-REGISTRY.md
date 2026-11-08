# FEATURE REGISTRY — Robotic Discipline

**Standard Compliance:** Every feature in this registry follows the 20-point Feature Development Standard defined in Section 04 of the Unified Master Prompt, including status classification (`[FOUNDER_CONFIRMED]`, `[HISTORICAL_PROPOSAL]`, `[IMPLEMENTED_SKELETON]`, `[NEW_SUGGESTION]`), three-audience explanations, technical architecture, costs, privacy/security, test plans, and priority (`MVP`, `V2`, `Future`, `Experimental`).

---

## Feature Summary Table across All 8 Architectural Layers

| Feature ID | Feature Name | Layer | Origin Concept | Status | Priority | Score (/100) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **F-01** | **User-Approved Memory Ledger** | L3: Intelligence & Memory | Animal Scrypt / MADKEN | `[IMPLEMENTED_SKELETON]` & `[FOUNDER_CONFIRMED]` | **MVP** | **88/100 (Build)** |
| **F-02** | **NFC Figure-to-Dock Workspace Pairing** | L1: Physical & L4: Workspace | MADKEN | `[FOUNDER_CONFIRMED]` | **MVP** | **84/100 (Build)** |
| **F-03** | **Parallel-Presence Shared Ritual Objects** | L4: Workspace & L5: Social | Animal Scrypt | `[IMPLEMENTED_SKELETON]` & `[HISTORICAL_PROPOSAL]` | **MVP** | **83/100 (Build)** |
| **F-04** | **Bilateral Memory Fragment Exchange** | L3: Memory & L7: Messaging | Animal Scrypt | `[IMPLEMENTED_SKELETON]` & `[HISTORICAL_PROPOSAL]` | **MVP** | **80/100 (Build)** |
| **F-05** | **Portable Character Identity Bundle (`ORBIT`)** | L2: Digital Identity | Space Fort / MADKEN | `[IMPLEMENTED_SKELETON]` & `[FOUNDER_CONFIRMED]` | **MVP** | **85/100 (Build)** |
| **F-06** | **Archetypal Character Workspaces (Engineer/Scholar/Athlete)** | L4: Operating Environment | MADKEN (`StarNetOS`) | `[FOUNDER_CONFIRMED]` | **MVP** | **82/100 (Build)** |
| **F-07** | **Multi-Figure Dock Council (2–3 Figures Collaborating)** | L1, L3, L5 | MADKEN | `[HISTORICAL_PROPOSAL]` | **V2** | **76/100 (Test First)** |
| **F-08** | **Capability Flash-Lease (Temporary Worker Role Token)** | L6: Ownership & Economy | Animal Scrypt | `[IMPLEMENTED_SKELETON]` & `[HISTORICAL_PROPOSAL]` | **V2** | **74/100 (Test First)** |
| **F-09** | **Removable Hardware Intelligence Cartridge** | L1: Physical & L2: Identity | MADKEN | `[HISTORICAL_PROPOSAL]` | **V2 / Future** | **65/100 (Defer)** |
| **F-10** | **Local Civilization Event Engine & Faction Treaties** | L5: Connected Civilization | MADKEN | `[HISTORICAL_PROPOSAL]` | **V2** | **71/100 (Test First)** |
| **F-11** | **SMS / iMessage-Style Async Companion Check-Ins** | L7: Messaging | Space Fort / MADKEN | `[HISTORICAL_PROPOSAL]` | **V2** | **72/100 (Test First)** |
| **F-12** | **Litecoin / LitVM On-Chain Registry & Parent-Child Royalties** | L6: Ownership & Economy | Animal Scrypt / DUNA | `[HISTORICAL_PROPOSAL]` | **Future** | **52/100 (Defer)** |
| **F-13** | **Founder Operating System & Investor Data Room** | Internal Infrastructure | Disciple / Master Prompt | `[FOUNDER_CONFIRMED]` | **MVP (Internal)** | **81/100 (Build)** |
| **F-14** | **Neighborhood Wet-Lab, Sustainable Data Center & Space Twins** | L8: Real-World Expansion | Animal Scrypt Stage 2–4 | `[HISTORICAL_PROPOSAL]` | **Experimental** | **45/100 (Defer)** |

---

## Detailed 20-Point Specifications for Core MVP & V2 Features

### F-01: User-Approved Memory Ledger (`PROPOSED -> APPROVED -> DELETED`)
1. **Feature ID & Name:** `F-01` — User-Approved Memory Ledger
2. **Status:** `[FOUNDER_CONFIRMED]` & `[IMPLEMENTED_SKELETON]` (in [`skeleton/interfaces.py`](./skeleton/interfaces.py))
3. **Description:** A deterministic state machine that prevents AI characters from silently storing hallucinated or sensitive personal facts. Any candidate memory extracted during conversation enters a `PROPOSED` queue; only memories explicitly clicked `APPROVED` by the user are persisted and retrieved in future sessions.
4. **Explain to a 10-year-old:** When you tell your character something about yourself, it writes it on a sticky note and asks, "Should I keep this in my memory book?" It only glues the note into the book if you press "Yes," and you can rip any page out whenever you want.
5. **Explain to a 24-year-old:** Chatbots either forget everything in a new tab or creepy-stalk you with hidden cloud profiles. Here, your character proposes structured memory cards (`project`, `interest`, `routine`, `observation`) that you approve, edit, or delete in one click—giving you a clean, accurate project brain you control.
6. **Explain to a professor:** An explicit human-in-the-loop (HITL) epistemic gate over episodic agent memory. Rather than unvalidated RAG ingestion of raw conversational transcripts, candidate tuples $(c_{\text{id}}, \text{cat}, \text{text}, t)$ are staged with $\text{status}=\texttt{PROPOSED}$ in a relational ledger and excluded from prompt injection until a user-authenticated transition sets $\text{status}=\texttt{APPROVED}$.
7. **Problem Solved:** Eliminates silent AI hallucination persistence, privacy anxiety, and context pollution across long-term companion interactions.
8. **User Story:** *As a creative founder or student working with an AI companion over weeks, I want to approve or edit every fact my character saves about my work so that it remembers my real context without storing private vent sessions or AI mistakes.*
9. **User Interaction:** User chats or logs a note → Companion displays a translucent blue "Proposed Memory" card → User clicks **Approve**, **Edit & Approve**, or **Discard** → Approved memory appears in the inspectable Vault panel with a **Delete** button.
10. **Dependencies:** Local SQLite or PostgreSQL database (`memory_records` table in [`skeleton/schema.sql`](./skeleton/schema.sql)).
11. **Technical Architecture:** Python/FastAPI or Next.js API layer wrapping SQLite/PostgreSQL; strict query filter `WHERE status = 'APPROVED'` on all context-retrieval calls.
12. **Required Hardware/Software:** Runs on any laptop, phone browser, or Raspberry Pi (Python 3.10+, SQLite3).
13. **Estimated Implementation Cost:** $0 external software cost (core logic already built in `skeleton/interfaces.py`; ~$0–$5/mo hosting if deployed to cloud).
14. **Privacy & Security Requirements:** Local-first storage by default; hard deletion (`DELETE` or tombstone scrub) on user command; strict separation between `authored_lore` and `memory_records`.
15. **Acceptance Criteria:** (a) Unapproved memories never appear in exported bundles or retrieval context; (b) User can edit text prior to approval; (c) Rejected memories transition to `DELETED` and are excluded from queries.
16. **Test Plan:** Automated unit tests in [`tests/test_kernel.py`](./tests/test_kernel.py) verifying proposal, approval, editing, rejection, and exclusion of unapproved records from portable exports.
17. **Success Metrics:** >70% of test users successfully review and approve at least 2 memories in their first 10-minute session; 100% of surveyed testers can accurately explain what the character remembers about them.
18. **Risks:** UI friction if the agent proposes too many memories per turn (mitigated by limiting to at most 1 high-salience proposal per session block).
19. **Alternatives:** Fully automatic background memory extraction (Mem0 default) — rejected for MVP because it violates the founder's explicit consent and accuracy rules.
20. **Priority:** **MVP** (Build Now).

---

### F-02: NFC Figure-to-Dock Workspace Pairing
1. **Feature ID & Name:** `F-02` — NFC Figure-to-Dock Workspace Pairing
2. **Status:** `[FOUNDER_CONFIRMED]` (Core physical-digital bridge in `More_madken_university.pdf` and Master Prompt Layer 1)
3. **Description:** Placing a physical character figure (embedded with an NTAG215/NTAG424 NFC tag) onto a desktop dock (or tapping a smartphone) reads the character's unique hardware UID/cryptographic signature and opens its specific character workspace (*Spaceport / Zine Terminal*).
4. **Explain to a 10-year-old:** Your toy has a tiny invisible magic sticker inside its foot. When you set the toy on its special coaster plugged into your computer, the computer immediately knows which character just arrived and opens up its home on your screen!
5. **Explain to a 24-year-old:** It's like Nintendo Amiibo or Toniebox, except instead of unlocking a static costume or audio track, placing your figure on your USB-C desk dock switches your computer into that character's dedicated AI workspace—loading your engineering CAD assistant, study partner, or workout coach instantly.
6. **Explain to a professor:** A Tangible User Interface (TUI) physical-digital binding mechanism utilizing ISO/IEC 14443 Type A NFC tags (13.56 MHz). In Generation 1a, an NDEF URI/UID payload triggers a local WebUSB/WebNFC or HID reader daemon to resolve the corresponding `CharacterManifest` from the local SQLite ledger; in Generation 1b (NTAG424 DNA), SUN (Secure Unique NFC) AES-128 cryptographic challenge-response prevents tag cloning.
7. **Problem Solved:** Turns abstract software agents into tangible, zero-friction physical objects that anchor attention and make switching workflows tactile and memorable.
8. **User Story:** *As a designer or builder, I want to place my physical Engineer figure on my desk dock to immediately open my engineering workspace and project memory without navigating menus.*
9. **User Interaction:** User places figure on USB-C dock (or taps phone) → LED/screen optic pulses amber-green → Browser/desktop app transitions to that character's active workspace and greets the user with their last approved continuity note.
10. **Dependencies:** `F-01` (Memory Ledger), `F-05` (Portable Identity Manifest), off-the-shelf USB-C NFC reader (e.g., ACR122U / PN532) or smartphone WebNFC/NDEF URL.
11. **Technical Architecture:** NDEF URL `http://localhost:8000/dock?uid=<tag_id>&sig=<cmac>` or small Python USB HID listener dispatching a WebSocket event to the local Spaceport Zine UI.
12. **Required Hardware/Software:** 3D-printed figure shell (PLA/resin), NTAG215 ($0.25) or NTAG424 DNA ($0.80) sticker, USB-C NFC reader module ($12–$25) inside a 3D-printed dock shell.
13. **Estimated Implementation Cost:** ~$15–$30 per prototype kit in unit 1 BOM using SCAD 3D-printing labs.
14. **Privacy & Security Requirements:** Tag stores **only** the public Character UID and cryptographic nonce—**never** raw personal conversations or private memories (per `More_madken_university.pdf` Page 2).
15. **Acceptance Criteria:** Placing Figure A loads Companion A's manifest within <1.5 seconds; swapping to Figure B cleanly switches the active workspace context to Companion B.
16. **Test Plan:** Hardware-in-the-loop test with 3 NFC tags (Engineer, Scholar, Athlete) verifying workspace switching and clone rejection.
17. **Success Metrics:** <2 second pairing latency; 90%+ of live demo viewers immediately understand the physical-to-digital connection without verbal explanation.
18. **Risks:** iOS Safari restricts raw WebNFC API (mitigated by using standard NDEF URLs that iOS reads natively via background tag reading, plus a USB-C desktop reader for laptop docks).
19. **Alternatives:** QR codes printed on the figure base (kept as a $0 fallback for webcam/phone scanning when NFC hardware is absent).
20. **Priority:** **MVP** (Phase 3 Physical-Digital Prototype).

---

### F-03: Parallel-Presence Shared Ritual Objects
1. **Feature ID & Name:** `F-03` — Parallel-Presence Shared Ritual Objects
2. **Status:** `[IMPLEMENTED_SKELETON]` & `[HISTORICAL_PROPOSAL]` (`Madken space fort 2.pdf` Pages 5–6, `skeleton/interfaces.py`)
3. **Description:** A shared digital (and optionally 3D-printed) artifact linked between two or more users' characters that only advances state (`DORMANT -> RESONATING -> CRYSTALLIZED`) when participants complete a brief simultaneous or daily parallel activity (e.g., a 15-minute silent study/build timer or shared observation). Missed days result in gentle dormancy, never destructive loss or guilt notifications.
4. **Explain to a 10-year-old:** You and your best friend get a special digital crystal or cyber-plant that your characters take care of together. Whenever you both do your homework or build something at the same time for 15 minutes, the crystal glows and grows to the next level! If you miss a day, it just takes a nap until you're back.
5. **Explain to a 24-year-old:** Social media demands constant witty texting, while working alone gets isolating. A Shared Ritual Object lets you and a studio mate or friend co-work in silence for 15 minutes; your characters log the session together and evolve a shared collectible artifact—giving you human connection with zero social exhaustion.
6. **Explain to a professor:** A cooperative state-machine mechanism designed to foster *ambient co-presence* and *social facilitation* (Zajonc, 1965) while avoiding the negative reinforcement loops of punitive streak mechanics (e.g., Duolingo/Snapchat streaks). State transitions require a conjunctive participation predicate $\forall u \in P: \text{active}(u, \Delta t)$ to increment `vitality_points`, while inactivity triggers a non-punitive $\texttt{DORMANT}$ state.
7. **Problem Solved:** Reduces solo-builder / student isolation without requiring high-energy conversation or performative social media posting.
8. **User Story:** *As a solo founder or SCAD student working late in my room, I want to do a 15-minute silent build block alongside a friend so we both feel less alone and build a shared record of our progress.*
9. **User Interaction:** Users A and B select a shared ritual object (*"Translucent Signal Core #01"*) → Both start a 15-minute parallel block and log a 1-line note → Object state advances from `DORMANT` to `RESONATING` (and `CRYSTALLIZED` on repeat sessions) → Both characters record the signed continuity note.
10. **Dependencies:** `F-01` (Memory Ledger), `ritual_objects` table in [`skeleton/schema.sql`](./skeleton/schema.sql).
11. **Technical Architecture:** Implemented in `AnimalScryptKernel.create_ritual_object` and `tend_ritual_object` (`skeleton/interfaces.py` L161–199).
12. **Required Hardware/Software:** Web/Desktop UI + SQLite/PostgreSQL backend.
13. **Estimated Implementation Cost:** Core state machine already built ($0); real-time WebSocket room sync adds ~2 days of engineering.
14. **Privacy & Security Requirements:** Only paired participants see the shared continuity log; private memories remain isolated in each user's local vault.
15. **Acceptance Criteria:** Single-user check-in raises `PermissionError` (cannot advance alone); dual check-in increments `vitality_points` and updates state to `RESONATING` / `CRYSTALLIZED`.
16. **Test Plan:** Verified by automated test `test_ritual_object_requires_parallel_presence` in [`tests/test_kernel.py`](./tests/test_kernel.py).
17. **Success Metrics:** Repeat completion rate (percentage of pairs who complete $\ge 3$ parallel sessions within 7 days).
18. **Risks:** Coordination friction if two users cannot align schedules synchronously (mitigated by allowing a configurable time window, e.g., same evening, or drop-in silent habitat rooms).
19. **Alternatives:** Traditional voice/video chat rooms — rejected as primary wedge because high social anxiety users avoid camera/mic calls.
20. **Priority:** **MVP**.

---

### F-04: Bilateral Memory Fragment Exchange
1. **Feature ID & Name:** `F-04` — Bilateral Memory Fragment Exchange
2. **Status:** `[IMPLEMENTED_SKELETON]` & `[HISTORICAL_PROPOSAL]` (`Madken space fort 2.pdf` Page 6, `skeleton/interfaces.py`)
3. **Description:** Two companions can propose sharing a short, sanitized continuity note (`shared_summary`) derived from an `APPROVED` memory, but the exchange only completes when **both** the sender human and the recipient human explicitly approve it (`sender_approved = 1 AND recipient_approved = 1`). Either party can later revoke the exchange (`revoked_at`), removing it from active views and exports while honestly noting that prior human viewing cannot be erased from human memory.
4. **Explain to a 10-year-old:** If your character wants to tell your friend's character what game you're building, it shows you the exact sentence first. Both you AND your friend have to press "Okay" before the characters share the note.
5. **Explain to a 24-year-old:** Instead of manually texting updates or letting an AI overshare your private chat, your companion drafts a 1-sentence bridge note (*"Both of you are prototyping 3D-printed joints this week"*). It only shares after both humans click approve, and you can revoke access anytime.
6. **Explain to a professor:** A bilateral discretionary access control (DAC) protocol over agent-mediated information disclosure. It enforces two invariants: (1) $\text{status}(m) = \texttt{APPROVED}$ is a precondition for proposal, and (2) visibility in the recipient's active context requires $\text{sender\_approved} \land \text{recipient\_approved} \land (\text{revoked\_at} = \varnothing)$.
7. **Problem Solved:** Prevents agent-to-agent prompt injection leakage and unauthorized disclosure of private user context in multi-agent rooms.
8. **User Story:** *As a user in a shared studio or study group, I want my character to help break the ice around shared interests without ever leaking my private notes without my permission.*
9. **User Interaction:** Companion A drafts a 1-line `shared_summary` from an approved `FRAGMENT_CANDIDATE` memory → User A clicks **Approve Send** → User B sees the preview and clicks **Approve Receive** → Both companions can now reference the shared fragment.
10. **Dependencies:** `F-01` (`memory_records`), `fragment_exchanges` table in [`skeleton/schema.sql`](./skeleton/schema.sql).
11. **Technical Architecture:** Implemented in `propose_fragment_exchange`, `approve_fragment_exchange`, and `revoke_fragment_exchange` (`skeleton/interfaces.py` L119–158).
12. **Required Hardware/Software:** SQLite/PostgreSQL + Web UI.
13. **Estimated Implementation Cost:** $0 (already implemented in `skeleton/interfaces.py`).
14. **Privacy & Security Requirements:** Raw private memory content is never transmitted automatically; only the user-inspected `shared_summary` is exchanged; revocation immediately filters the record from `export_portable_bundle`.
15. **Acceptance Criteria:** Attempting to propose an unapproved memory raises `PermissionError`; exchange remains inactive until both parties approve; revoking excludes the exchange from portable exports.
16. **Test Plan:** Automated tests in [`tests/test_kernel.py`](./tests/test_kernel.py).
17. **Success Metrics:** Zero unintended data disclosures; >60% bilateral approval rate on proposed fragments in paired user tests.
18. **Risks:** Users may confuse revoking a digital record with erasing what another person already read on screen (mitigated by explicit UI copy explaining what revocation does and does not undo).
19. **Alternatives:** Open multi-agent chat rooms where bots freely talk to each other — rejected due to severe privacy and prompt-injection leakage risks.
20. **Priority:** **MVP**.

---

### F-05: Portable Character Identity Bundle (`ORBIT` Manifest)
1. **Feature ID & Name:** `F-05` — Portable Character Identity Bundle (`spacefort.orbit.portable_identity.v0.1`)
2. **Status:** `[IMPLEMENTED_SKELETON]` & `[FOUNDER_CONFIRMED]` (`Madken space fort 2.pdf` Page 12–13, `More_madken_university.pdf` Page 3)
3. **Description:** A self-contained, user-owned JSON/SQLite identity package containing the character's immutable `authored_lore`, `chassis_spec`, `voice_constraints`, `approved_private_memories`, `active_bilateral_exchanges`, and `active_capability_leases`. Enables moving a character between a laptop, a desktop dock, a removable cartridge, or a different LLM runtime without moving heavy model weights.
4. **Explain to a 10-year-old:** It's like a digital backpack for your character. Everything your character is allowed to remember fits inside one tiny file that belongs to you, so your character can visit a different computer or a robot body and still be the exact same friend.
5. **Explain to a 24-year-old:** If OpenAI, Anthropic, or a companion startup shuts down or changes a model, your character doesn't die or get lobotomized. You own a portable JSON identity manifest that plugs into local Ollama models or cloud APIs interchangeably.
6. **Explain to a professor:** Decouples persistent agent state from parametric model weights ($W_{\theta}$). By serializing the non-parametric state $\langle \mathcal{L}, \mathcal{M}_{\text{approved}}, \mathcal{P} \rangle$ into a versioned, schema-validated document (`spacefort.orbit.portable_identity.v0.1`), the architecture achieves runtime interoperability across heterogeneous local and cloud inference engines.
7. **Problem Solved:** Prevents vendor lock-in, model deprecation amnesia, and hardware tie-in.
8. **User Story:** *As an owner of a Robotic Discipline character, I want to export my character's identity and approved memories in one click so I truly own my data and can run my character on local models offline.*
9. **User Interaction:** User clicks **Export Portable Identity** → System generates `portable_identity_export.json` (and renders `zine_demo_view.html`).
10. **Dependencies:** `F-01`, `F-04`, `F-08`.
11. **Technical Architecture:** Implemented in `AnimalScryptKernel.export_portable_bundle` (`skeleton/interfaces.py` L225–264).
12. **Required Hardware/Software:** Standard JSON/SQLite runtime.
13. **Estimated Implementation Cost:** $0 (implemented in `skeleton/interfaces.py`).
14. **Privacy & Security Requirements:** Export includes only `APPROVED` memories and non-revoked exchanges/leases; optional AES-256-GCM passphrase encryption for file transport in V2.
15. **Acceptance Criteria:** Exported JSON validates against `spacefort.orbit.portable_identity.v0.1` schema and accurately reflects all approved state transitions.
16. **Test Plan:** Automated test in [`tests/test_kernel.py`](./tests/test_kernel.py).
17. **Success Metrics:** 100% lossless round-trip import/export across two separate local agent runtimes.
18. **Risks:** Unencrypted JSON exports stored on shared computers could be read if the user does not protect the file (mitigated by local encryption option).
19. **Alternatives:** Cloud-only proprietary account storage.
20. **Priority:** **MVP**.
