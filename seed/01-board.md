# 01 — Board Review (`/board`)

**Context read:** [`00-context.md`](./00-context.md)  
**Mode:** Write (with Review pushback on customer scope)

---

## Seat 1: Offer
**Question:** Would a specific person pay, and for what result? What is the promise in one sentence, and what proof comes before the pitch?

* **Pushback:** In `00-context.md`, the founder named three totally different buyers at once: 18–30 tech-curious young adults, people with disabilities, and parents looking for Alpha School-style child learning (https://alpha.school). Those three groups do not buy in the same room, at the same price, or under the same laws. Selling to children triggers COPPA rules. Selling disability assistance invites medical and ADA scrutiny. Meanwhile, your MVP done-condition #7 explicitly tests **three consenting adults**.
* **One-sentence promise (for v1):** You get a 3D-printed animal on your desk that opens a browser workspace and remembers the project or study facts you approve across seven days.
* **Proof required before the pitch:** Hand three consenting SCAD students or young adults (18–30) a printed shell with a QR/NFC tag, let them approve three facts on Day 1, restart the app, and film them coming back on Day 7 to see the animal use those three facts.
* **Score:** **2 / 5** — We have a clear 7-checkbox MVP checklist in `00-context.md`, but zero paying users and three conflicting customer targets (`metrics_we_have: none yet`).

---

## Seat 2: Monopoly
**Question:** What is the secret, and what 0-to-1 thing is actually new? Is "AI pet" the company, or is the royalty-plus-body the company?

* **Pushback:** "AI pet" is a crowded graveyard. Character.ai has millions of users at $9.99/mo (https://www.reddit.com/r/CharacterAI/), and Living.AI sells $279 desktop robots (https://living.ai). On the other side, NFT creature projects like CryptoZoo and Pixelmon burned buyers so badly that leading with "Litecoin NFTs" will get you rejected by accelerators on sight (https://en.wikipedia.org/wiki/CryptoZoo).
* **What is actually new:** The secret is **continuity that belongs to the user, anchored to a physical object, with a creator royalty when a trained worker animal is forked.** Pop Mart made RMB 37.12 billion (~$5.1B+ USD) in 2025 selling plastic characters that do nothing (https://www.popmart.com). Tonies made EUR 630 million in 2025 selling NFC figurines that only play static audio (https://ir.tonies.com). Nobody has bound an inspectable, user-approved worker memory to a physical shell where training the animal creates a reusable asset that pays the parent maker.
* **Verdict on identity:** The company is **the memory-plus-body-plus-royalty graph**, not a cute chatbot skin.
* **Score:** **3 / 5** — The three-part hook (user-approved memory + 3D-printed shell + parent-child royalty ledger) already exists in local code (`skeleton/interfaces.py`), but no real creator has earned a cent from a child animal yet.

---

## Seat 3: Product
**Question:** What do we cut so the first version is one animal, one memory, one shell? What is the demo that takes 60 seconds?

* **Pushback:** Do not stand up four new services (Next.js + Supabase + Dify + Open WebUI + live Litecoin mainnet contracts) before testing with three people. You already have a working Python + SQLite + zine HTML kernel in `skeleton/interfaces.py` that handles companion bios, user-approved memory (`PROPOSED -> APPROVED`), ownership records, and simulated ledger records. Put a thin web route and a QR/NFC link on top of that, connect one model, and print one shell at SCAD.
* **What we cut for the next 6 weeks:**
  1. Cut live Litecoin wallet signing (keep the simulated test ledger in checkbox #6).
  2. Cut child/parent COPPA accounts and clinical disability claims (test with 18–30 consenting adults at SCAD first).
  3. Cut the 300 × $2,500 checkout until the 7-day memory test works on 3 people.
* **The 60-second demo:**
  * **0–15s:** Hold the 3D-printed shell in your hand. Scan its NFC/QR tag with a phone or laptop.
  * **15–35s:** The cream-and-lime zine workspace opens. Tell the animal three facts about your week. Click **Approve** on the memory cards. Restart the server on camera.
  * **35–50s:** Re-open the workspace (or show the Day 7 log). The animal recalls all three facts accurately without hallucinating.
  * **50–60s:** Click **Fork Child Worker** in the dashboard. Show the test ledger credit a royalty to the parent animal's maker.
* **Score:** **4 / 5** — The founder's 7-checkbox MVP definition in `00-context.md` is tight, testable, and maps directly to code we can finish and hand to three adults at SCAD this month.

---

## What Kills the Company This Year
Trying to build for three different customer groups (young adults, disabled users, and K–12 parents) on four software stacks while pitching a $2,500 crypto cohort before a single adult has used one animal for seven days.

---

## Board Verdict
* **Overall Board Score:** **3.0 / 5.0**
* **Verdict:** **NARROW** (then pursue).
* **Mandatory Narrowing Rule for `02`–`06`:** Lock v1 on **Customer Group 1: tech-curious young adults (18–30, starting with SCAD students and makers)**. Keep parents/learning and accessibility as documented Phase 2 expansion tracks after the 3-adult, 7-day MVP test passes.
