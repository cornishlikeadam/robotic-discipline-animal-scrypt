# 16 — Founder & Demo Video Scripts (`/video`)

**Context read:** [`00-context.md`](./00-context.md), [`13-talk-track.md`](./13-talk-track.md), [`15-applications.md`](./15-applications.md)  
**Rules:** Look straight at the camera lens. No background music. Normal room sound in your dorm or SCAD studio is fine. No slides behind you in the Founder Video. Every shot that cannot be filmed today is explicitly marked **`not yet`**.

---

## 1. Founder Video Script (~60 Seconds)
*(For YC, Techstars, a16z Speedrun, and SCAD Accelerator Video #1)*

* **0:00–0:05 (Name, City, One Line):**
  > "Hi, I'm Kendren 'KJ' Cornish in Savannah, Georgia. I'm building Animal Scrypt under Robotic Discipline: you collect an animal that remembers you, and it can grow up into a worker."
* **0:05–0:25 (The 10-Year-Old Explanation + One Adult Clause):**
  > "Imagine a pet that lives in your browser and also as a little 3D-printed figure you can hold. It remembers your name, what you're working on, and what you approved last time. One learns to help with engineering, one with art, one with research—and if someone forks a baby worker from the animal you trained, our ledger pays you a creator royalty."
* **0:25–0:45 (What We Built vs. What We Show This Month):**
  > "Today we are pre-revenue with zero paid users. I've built the local Python and SQLite memory and permission kernel that lets an owner approve facts, export their creature's identity, and log a simulated royalty split. This month, I'm printing our first QR- and NFC-tagged shell (`not yet` — *print shell before filming or hold current reference mockup and say it is a mockup*) and running three consenting adults at SCAD through a seven-day memory recall test."
* **0:45–1:00 (Why Me — Concrete Facts Only):**
  > "I'm a rising sophomore at SCAD, a U.S. military veteran on a diver path, and a resident assistant on campus. I have SCAD's 3D-printing labs right outside my door to fabricate the shells, and I also work on a SCADpro research thread studying AI signals for real horses. I'm building the animal and the shell myself."

---

## 2. Demo Video Script (~60–90 Seconds)
*(For Accelerator Video #2 — Screen + Hand Cutaways)*

### Checklist Before Recording
* **Filmable right now (`exists today`):**
  * Running `python3 skeleton/interfaces.py --demo` in terminal.
  * Opening `skeleton/zine_demo_view.html` in the browser showing the cream/cobalt zine UI, `[APPROVED]` memories, bilateral exchange, and portable JSON export.
* **Must be built/printed before filming as live (`not yet`):**
  * Holding the physical 3D-printed Animal Scrypt shell with a working QR/NFC sticker on its base (`not yet`).
  * Live Day-1 vs. Day-7 timestamped recall screen from an independent adult tester (`not yet`).
  * Live interactive browser button for the simulated creator-to-owner royalty transfer (`not yet` — currently runs via CLI script).

### Shot-by-Shot Script

* **0:00–0:15 — Shot 1: The Shell in a Hand (`not yet` for final printed shell; if filming today, show the CAD/reference model and state clearly it is the pre-print shell):**
  * *Visual:* KJ's hand holding the 3D-printed shell, flipping it over to show the QR/NFC tag on the bottom, and tapping it with a phone.
  * *Voiceover:* "This is an Animal Scrypt shell printed at SCAD. There is no battery to die and no Wi-Fi chip to break—just a tag tied to this creature's identity."
* **0:15–0:40 — Shot 2: Day 1 — Approving Three Facts (`exists today` in kernel / `not yet` for live chat form):**
  * *Visual:* Browser opens the zine workspace (`zine_demo_view.html`). The user tells the Engineer creature three facts about their project. The creature proposes three memory cards; the user clicks **Approve**.
  * *Voiceover:* "Unlike a chatbot that silently stuffs everything into a sliding window or forgets you tomorrow, the animal proposes a memory card. I click Approve on three facts about my OpenSCAD joints. Watch me restart the server right now."
* **0:40–0:60 — Shot 3: Day 7 — The Animal Remembers (`not yet` for real 7-day elapsed user log; label as simulated demo until Day 7 completes):**
  * *Visual:* Server restarts. Browser reloads the creature's workspace. The user asks, *"What are my joint tolerances from last week?"* The creature answers using the three approved memories from the SQLite database.
  * *Voiceover:* "Seven days later—and after a full application restart—the animal pulls from its approved memory ledger and recalls all three details accurately."
* **1:00–1:20 — Shot 4: The Royalty Ledger & Next Week (`exists today` as JSON/SQLite state / `not yet` as transfer button UI):**
  * *Visual:* Click **Fork Child Worker**. A single ledger line appears showing the creator-to-owner transfer and a 20% royalty allocation in the test ledger.
  * *Voiceover:* "When a second user forks a child worker from this trained engineer animal, our test ledger records a 20% royalty to the parent's maker—with private personal memories stripped out. Next week's change: handing three printed shells to three SCAD students to measure real Day-7 recall."
