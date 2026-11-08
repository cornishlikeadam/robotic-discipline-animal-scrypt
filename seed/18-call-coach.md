# 18 — Investor & Coach Call Guide (`/calls`)

**Context read:** [`00-context.md`](./00-context.md), [`06-cfo.md`](./06-cfo.md), [`13-talk-track.md`](./13-talk-track.md)

---

## 1. The 25-Minute Call Agenda

Do not ramble for 15 minutes at the start. Keep this clock in front of you:

* **Minutes 0–2 (Frame & Hallway Line):** Say who you are, where you are calling from (SCAD in Savannah), the hallway line, and propose the agenda: *"I'll take 3 minutes to show you the shell and the memory workspace, tell you honestly where we are today, and leave 20 minutes for your questions."*
* **Minutes 2–5 (Show the Animal & State the Truth):** Hold up the 3D-printed shell (`or CAD/mockup if pre-print`), screen-share the cream-and-lime zine workspace (`zine_demo_view.html`), and state: *"We have 0 paid users today. Our 6–8 week MVP is 7 checkboxes ending with 3 consenting adults completing a 7-day memory test."*
* **Minutes 5–22 (The 8 Questions Below):** Answer every question in under 45 seconds. Stop talking and let them push back.
* **Minutes 22–25 (The Ask & Clear Next Step):** Ask for a yes, a no, or the exact milestone they want to see in two weeks.

---

## 2. The 8 Questions They Will Ask (And Honest Answers With Our Real Gaps)

### Q1: "What stops a user from just opening ChatGPT or Claude for free instead of using your animal?"
* **Answer:** "ChatGPT mixes all your classes and projects into a scrolling sidebar and silently summarizes or drops old context. With Animal Scrypt, scanning your Engineer shell opens only that creature's workspace and injects only the facts you clicked Approve to save. Plus, if you train your animal to be a great OpenSCAD helper, ChatGPT pays you nothing when a friend copies your GPT—our ledger credits you a 20% royalty when someone forks your animal."
* **Real Gap to Admit:** "We haven't proven yet that 3D-printed shells beat browser bookmarks over 14 days—that is what our 3-adult MVP test and 10-shell `$45` test measure."

### Q2: "Why is there a physical 3D-printed shell if it doesn't have motors, cameras, or a microphone?"
* **Answer:** "Because putting batteries, motors, and 2.4GHz Wi-Fi chips inside a $279 toy is why Living.AI EMO gets crushed on Trustpilot—the battery dies in two hours and the Wi-Fi breaks in dorms (https://www.trustpilot.com/review/living.ai). A 3D-printed shell with a passive QR/NFC tag costs us about `$7.50` (`assumption:`), never runs out of battery, and gives the digital worker a physical body on your desk."
* **Real Gap to Admit:** "Right now our shell is a static physical twin with a tag. Dock electronics and removable cartridges are on the V2 roadmap after we prove people come back on Day 7."

### Q3: "How does the parent-child royalty actually work without becoming a pyramid scheme or a dead NFT project like CryptoZoo?"
* **Answer:** "First, we never sell 'mystery eggs' before the software works. Second, in v1 we lock the royalty to one single event (`05-pricing.md`): when User B pays `$45` (`assumption:`) to mint a Child Animal from User A's trained Parent Animal template, User A gets 20% (`$9`). There are zero payouts on free forks and zero multi-level grandchildren cuts."
* **Real Gap to Admit:** "In our 6–8 week MVP (`00-context.md` checkbox #6), the royalty transfer runs in a simulated test ledger with zero real money or live Litecoin smart contracts until a lawyer reviews the flow."

### Q4: "Who is your very first customer—students, disabled users, or parents?"
* **Answer:** "Long term, our price ladder grows from `$45` starter shells into `$129–$249` pro worker docks, accessible daily companions for people with disabilities, and Alpha School-style self-directed learning kits for parents (`05-pricing.md`). For the next 8 weeks, 100% of our testing is on one group I can reach without ads: 18–30 SCAD makers and figure collectors in Savannah."
* **Real Gap to Admit:** "We have completed 0 of our 10 Mom Test conversations and 0 of our 3 consenting adult user tests so far."

### Q5: "What happens to a user's private memories when someone forks a child animal from their parent animal?"
* **Answer:** "Private memories never transfer. In our database schema (`skeleton/schema.sql`), private user facts (`visibility = 'PRIVATE'`) are separated from shareable worker rules and authored lore. Forking a child animal copies only the public worker role and approved domain templates—never the parent owner's personal chat."
* **Real Gap to Admit:** "Right now a human has to manually mark which memories are private versus shareable template rules; we haven't built an automated PII scrubber yet."

### Q6: "You're a full-time college sophomore and an RA. How do you have time to build a company?"
* **Answer:** "Two ways. First, I served in the military on a diver path and know how to run a strict daily schedule. Second, at SCAD, my studio coursework, SCADpro research, and fabrication lab time are aligned directly with building Animal Scrypt—so school is my R&D shop and factory floor, not a distraction."
* **Real Gap to Admit:** "I am a solo founder right now. If print volume passes 30 shells a month during exams, my personal time breaks first (`07-canvas.md`), so I will need to hire a part-time student print tech."

### Q7: "What is this horse telehealth project in your background—are you building two companies?"
* **Answer:** "No. The equine gait and vocalization telehealth thread is a SCADpro research project I worked on. It asks the same research question—how to give an animal a longitudinal signal record a human can trust—which proves I can do applied AI sensing work, but we are not merging horse telehealth into the Animal Scrypt product (`00-context.md`)."
* **Real Gap to Admit:** "Keep them separate in diligence; the company you are investing in is Robotic Discipline (Animal Scrypt)."

### Q8: "Why do you mention 300 founders at $2,500 in your notes?"
* **Answer:** "That is a later cohort scenario (`$750k` gross before fees and shells; `05-pricing.md`) for funding our larger creator graph once the product works. We are not opening a `$2,500` checkout today—our first paid test is 10 shells at `$45` + `$9/month`."
* **Real Gap to Admit:** "Zero people have paid `$2,500` or `$45` yet."

---

## 3. Post-Call Scorecard (Fill Out Within 10 Minutes of Hanging Up)

| Metric | Score (1–5) | Notes |
|---|---|---|
| **Did I show the shell and workspace in the first 5 minutes?** | `[ ] / 5` | |
| **Did I state "0 paid users today" honestly without apologizing?** | `[ ] / 5` | |
| **Did I keep every answer under 45 seconds?** | `[ ] / 5` | |
| **Did I get a clear next step (Yes / No / Specific Milestone Date)?** | `[ ] / 5` | |
| **What was the one question that made meramble?** | — | *Write the exact question here and tighten it in `13-talk-track.md`.* |
