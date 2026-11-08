# 26 — Fifteen Book Skills & Router (`/books`)

**Context read:** [`00-context.md`](./00-context.md), [`nda-status.md`](./nda-status.md)  
**NDA Lock Rule:** When running on the portfolio front page chat or inside an agent, this router may read Stage 1 docs and `00-context.md`. It **must never** read or quote Stage 2 rooms (`cap table`, `bank and tax`, `signed contracts`, `private customer names`, `unreleased prompts/royalty code`) unless `nda-status.md` shows `stage2_unlock: true` for the current viewer. If a question asks for a locked number, teach the method and state: *"That specific number sits behind the Stage 2 NDA."*

---

## 1. The Start-Here Diagnostic Router

When a user asks a plain question, route it automatically:

* **"What's wrong with my startup?" / "I don't know where to start"** $\to$ Run **Diagnose First**:
  1. *Do you have 3 people outside your family using the animal on Day 7?* **No** $\to$ Go to **Book #1 (The Mom Test)** & **Book #3 (The Lean Startup)**.
  2. *Do people get confused about whether you are a toy, a chatbot, or a crypto app?* **Yes** $\to$ Go to **Book #4 (Obviously Awesome)**.
  3. *Are you adding features instead of charging money?* **Yes** $\to$ Go to **Book #9 ($100M Offers)** & **Book #10 (Monetizing Innovation)**.
* **"How do I talk to customers?"** $\to$ Route to **Book #1 (The Mom Test)** + **Book #2 (The Four Steps to the Epiphany)**.
* **"How do I price or monetize?"** $\to$ Route to **Book #10 (Monetizing Innovation)** + **Book #9 ($100M Offers)**.
* **"How do I improve from where we are today?"** $\to$ Route to **Book #3 (The Lean Startup)** + **Book #11 (The Lean Product Playbook)** against `00-context.md`.

---

## 2. The Fifteen Reusable Book Guides

### Book 1: *The Mom Test* (Rob Fitzpatrick)
1. **Framework:** Never ask someone if your startup idea is good—even your mom will lie to protect your feelings. Ask only about their past behavior, the tools they already pay for, and the last time they hit the problem. Compliments and "I would definitely buy that" are worth `$0`. Only time given, reputation risked, or money paid counts as a real signal.
2. **Use This Week on Animal Scrypt:** Ask 10 SCAD students to show you their desk figures and their last ChatGPT thread from this week (`03-customers-100.md`). Do not mention Animal Scrypt until the last 60 seconds.
3. **Decision Tree:**
   * *Did the person talk about their own past week?* **No** $\to$ Stop pitching and ask *"When did an AI chat forget something you needed this week?"*
   * *Did they say "cool idea"?* **Yes** $\to$ Ignore it and ask to schedule a 7-day shell test on their desk starting today.
4. **Examples:**
   * *Public History:* Dropbox tested real action (joining a beta waitlist after watching a 3-minute demo video) instead of asking survey questions (https://techcrunch.com/2011/10/19/dropbox-minimal-viable-product/).
   * *Animal Scrypt:* Asking a SCAD Industrial Design student *"Show me where you wrote down your 3D-printer tolerances last Tuesday"* instead of *"Would you buy an AI animal?"*
5. **Outdated or not for you if:** You already have 50 paying customers and can measure churn directly in Stripe.

---

### Book 2: *The Four Steps to the Epiphany* (Steve Blank)
1. **Framework:** Startups are not smaller versions of big companies; they are temporary searches for a repeatable business model. Work in four steps: Customer Discovery, Customer Validation, Customer Creation, and Company Building. Never scale sales or marketing (Step 3) until strangers buy your v1 offer repeatability (Step 2).
2. **Use This Week on Animal Scrypt:** Stay in Step 1 (Discovery) and Step 2 (Validation) with one beachhead—18–30 SCAD makers—until 3 consenting adults finish the Day-7 recall test and 10 buyers pay `$45` (`06-cfo.md`).
3. **Decision Tree:**
   * *Have 3 consenting adults completed the Day-7 recall test?* **No** $\to$ You are in Step 1 (Customer Discovery). Do not hire or run ads.
   * *Have 10 people paid `$45` for a shell?* **Yes** $\to$ Move to Step 2 repeatable pricing tests (`$129` Tier 2).
4. **Examples:**
   * *Public History:* Webvan built warehouses and fleets (Step 4) before validating customer unit economics (Step 2) and went bankrupt (https://steveblank.com).
   * *Animal Scrypt:* Testing 3 printed shells in Savannah before ordering 1,000 injection-molded bodies or launching a `$2,500` cohort.
5. **Outdated or not for you if:** Never—jumping to Step 3 before Step 2 still kills hardware-software startups today.

---

### Book 3: *The Lean Startup* (Eric Ries)
1. **Framework:** Turn every assumption into a Build-Measure-Learn loop around a Minimum Viable Product (MVP). Measure **actionable cohorts** (what percentage of Week 1 users come back on Day 7), never **vanity metrics** (social views or unpaid signups). Pivot or persevere based on whether the test moves that one metric.
2. **Use This Week on Animal Scrypt:** Our single metric for the 6–8 week MVP (`00-context.md`) is **Day-7 recall completion across 3 consenting adults** (`3 approved details recalled after restart`).
3. **Decision Tree:**
   * *Does the feature help 3 adults recall 3 approved facts on Day 7?* **No** $\to$ Cut it from the 6-week build.
   * *Did at least 2 of 3 testers come back on Day 7?* **Yes** $\to$ Persevere to the 10-shell paid test. **No** $\to$ Fix the onboarding/memory prompt before printing more shells.
4. **Examples:**
   * *Public History:* Zappos photographed shoes at local stores to test if people would buy shoes online before holding inventory (https://theleanstartup.com).
   * *Animal Scrypt:* Using a simulated royalty ledger (`00-context.md` checkbox #6) to test if users fork worker animals before deploying live Litecoin smart contracts.
5. **Outdated or not for you if:** You treat "Lean" as an excuse to ship broken plastic shells that embarrass your craft at SCAD.

---

### Book 4: *Obviously Awesome* (April Dunford)
1. **Framework:** Customers judge your product by the **market category** you put in their head in the first 5 seconds. List what your customer would use if you didn't exist, isolate what you have that those alternatives lack, map that to concrete value, and pick the category frame where your weirdness is an unfair advantage.
2. **Use This Week on Animal Scrypt:** Never introduce Animal Scrypt as "an NFT project" or "a chatbot." Frame it as **a collectible 3D-printed worker animal that remembers your projects across weeks**.
3. **Decision Tree:**
   * *Does your opening line make the listener compare you to CryptoZoo?* **Yes** $\to$ Rewrite it around memory and the physical shell.
   * *Does the buyer immediately understand why it sits on their studio desk?* **Yes** $\to$ Keep that category frame.
4. **Examples:**
   * *Public History:* Tonies positioned the Toniebox as a screen-free story toy rather than an MP3 player, growing to EUR 630M in FY25 revenue (https://ir.tonies.com).
   * *Animal Scrypt:* Positioning ourEngineer animal against forgetful `$9.99/mo` chat tabs and silent `$30` Pop Mart figures.
5. **Outdated or not for you if:** You change your positioning sentence every day before testing one frame on 10 real buyers.

---

### Book 5: *Zero to One* (Peter Thiel)
1. **Framework:** Competition is for losers; build a small monopoly by knowing a **secret** that conventional wisdom misses. Start by dominating a tiny, specific niche you can win outright (like PayPal on eBay power-sellers), then expand into concentric circles.
2. **Use This Week on Animal Scrypt:** Our secret (`01-board.md`) is that **model weights are a commodity, while user-approved memory + a physical twin + a creator royalty graph is the durable asset**. Our tiny niche is SCAD makers in Savannah.
3. **Decision Tree:**
   * *Can a user get the exact same result by typing one prompt into free ChatGPT?* **Yes** $\to$ You have no secret; enforce the multi-week approved memory ledger + physical tag.
   * *Can we win 50 makers on one campus before chasing the whole internet?* **Yes** $\to$ Lock the Savannah beachhead.
4. **Examples:**
   * *Public History:* Facebook won Harvard undergrads completely before opening to other colleges (https://en.wikipedia.org/wiki/History_of_Facebook).
   * *Animal Scrypt:* Winning SCAD studio desks in Savannah before selling to every consumer in America.
5. **Outdated or not for you if:** You use "monopoly" talk to justify building a 6-year conglomerate before selling Shell #1.

---

### Book 6: *The Hard Thing About Hard Things* (Ben Horowitz)
1. **Framework:** There is no silver bullet for a startup crisis—only lead bullets (doing the unglamorous, specific work). Tell the truth about bad news early, manage your own psychology as a founder, and focus on the one thing that keeps the company alive this week.
2. **Use This Week on Animal Scrypt:** State our real gaps out loud on Slide 8 (`0 paid users today`) and in every monthly update lowlight (`21-investor-update.md`).
3. **Decision Tree:**
   * *Are you hiding a broken feature or zero users behind big words?* **Yes** $\to$ Put the gap in the first paragraph and name the fix date.
   * *Are you overwhelmed by 20 tasks as a solo student founder?* **Yes** $\to$ Drop everything except the 1 shell, 1 memory test, and 3 adult testers.
4. **Examples:**
   * *Public History:* Loudcloud survived the 2000 dot-com crash by disclosing its exact runway and cutting non-core lines (https://a16z.com/books/the-hard-thing-about-hard-things/).
   * *Animal Scrypt:* Cutting four extra software stacks and multi-entity legal filings so KJ can ship the 7-checkbox MVP between SCAD classes.
5. **Outdated or not for you if:** You read the chapters on firing VPs when you are still a solo founder.

---

### Book 7: *Crossing the Chasm* (Geoffrey Moore)
1. **Framework:** There is a dangerous gap ("the chasm") between early tech enthusiasts (innovators) and pragmatic mainstream buyers (the early majority). To cross it, you must win one "bowling pin" niche completely with a "whole product" before jumping to adjacent segments.
2. **Use This Week on Animal Scrypt:** **Do NOT use this book yet.** You are pre-chasm (`0` users). Your job today is winning your very first 10 early adopters at SCAD, not selling to the mainstream majority.
3. **Decision Tree:**
   * *Do you have at least 100 early adopters using the animal weekly?* **No** $\to$ Close this book and go back to Book #1 (*The Mom Test*).
   * *Are you ready to expand from SCAD makers (Pin 1) to parents/learning (Pin 2)?* **Yes** $\to$ Use the bowling-pin map here.
4. **Examples:**
   * *Public History:* Documentum won pharmaceutical FDA filings completely before expanding to other regulated industries (https://en.wikipedia.org/wiki/Crossing_the_Chasm).
   * *Animal Scrypt:* Sequence our segments as Bowling Pin 1 (SCAD makers, `$45`), Pin 2 (Pro/Collectible studios, `$129–$199`), Pin 3 (Accessible & Alpha School-style learning kits, `$249`).
5. **Outdated or not for you if:** **Not for you right now** at `0` users—save for Month 6+.

---

### Book 8: *Traction* (Gabriel Weinberg & Justin Mares)
1. **Framework:** Most startups fail from lack of distribution, not lack of code. Spend 50% of your time on product and 50% on testing one traction channel at a time using the Bullseye Framework (brainstorm 19 channels, test the top 1–3 cheaply, double down on the single channel that works).
2. **Use This Week on Animal Scrypt:** Our #1 inner-ring channel costs `$0`: **offline campus studio demos at SCAD + filming the 3D print**.
3. **Decision Tree:**
   * *Are you spending 100% of your week editing code/docs and 0% talking to buyers?* **Yes** $\to$ Block Tuesday and Thursday afternoons for campus table demos.
   * *Did campus demos get 3 testers faster than cold posts?* **Yes** $\to$ Put 100% of distribution effort on campus until you hit 50 users.
4. **Examples:**
   * *Public History:* Tinkercad and MakerBot grew their first user bases by bringing working 3D printers to local maker faires and design schools (https://www.wired.com).
   * *Animal Scrypt:* Putting 3 printed shells on a table in a SCAD studio building and letting students scan the NFC tag live.
5. **Outdated or not for you if:** You try to run 5 marketing channels at once as a solo student.

---

### Book 9: *$100M Offers* (Alex Hormozi)
1. **Framework:** Ignore the loud internet-marketer tone and keep the **Value Equation**:
   $$\text{Value} = \frac{\text{Dream Outcome} \times \text{Perceived Likelihood of Achievement}}{\text{Time Delay} \times \text{Effort \& Sacrifice}}$$
   To charge higher prices as you grow (`$45 -> $149 -> $249 -> $2,500`), shrink the **Time Delay** (how fast the animal works after unboxing) and shrink the **Effort** (pre-loaded worker skills instead of blank prompts).
2. **Use This Week on Animal Scrypt:** Make the first scan-to-memory-approval take **under 3 minutes** with zero terminal commands required by the buyer.
3. **Decision Tree:**
   * *Does the buyer have to install Python or configure API keys to talk to their animal?* **Yes** $\to$ Effort is too high; host the workspace URL behind the QR/NFC tag.
   * *Does the animal come pre-loaded with an Engineer or Artist starter kit?* **Yes** $\to$ You can raise the price from Tier 1 (`$45`) to Tier 2 (`$129+`).
4. **Examples:**
   * *Public History:* Apple's iPod succeeded against cheaper MP3 players by making "1,000 songs in your pocket" sync in one plug-in (https://www.apple.com).
   * *Animal Scrypt:* Shipping a Tier 2 Pro Animal pre-trained on 30 CAD/print rules so the buyer gets help in 60 seconds.
5. **Outdated or not for you if:** You copy the "get rich quick" income claims—never promise buyers they will get rich from royalties (`The Book of Robotic Discipline` FTC rule).

---

### Book 10: *Monetizing Innovation* (Madhavan Ramanujam & Georg Tacke)
1. **Framework:** Design the product around the price, not the price around the product after it's built. Test willingness to pay early, avoid "feature shock" (stuffing 20 features into v1 that buyers don't value), and build a **Good / Better / Best** tier ladder so entry buyers and power buyers self-select.
2. **Use This Week on Animal Scrypt:** Use our 4-Tier Price Growth Ladder (`05-pricing.md`) and ask in our 10 campus conversations what price feels like a no-brainer vs. too expensive.
3. **Decision Tree:**
   * *Are you adding a feature that does not raise willingness to pay or Day-7 retention?* **Yes** $\to$ Cut it or move it to Tier 2 (`$129`).
   * *Did 3 of 10 people pay `$45` without blinking?* **Yes** $\to$ Test `$69` and `$129` on the next batch of 10 shells.
4. **Examples:**
   * *Public History:* Porsche surveyed willingness to pay across every feature of the Cayenne before finalizing the engineering bill of materials (https://www.simon-kucher.com).
   * *Animal Scrypt:* Starting at `$45 + $9/mo` for a 1-role campus shell, then charging `$129–$249` for multi-role docks and guided learning editions.
5. **Outdated or not for you if:** You run 50-page conjoint pricing surveys instead of simply asking 10 people on campus for `$45`.

---

### Book 11: *The Lean Product Playbook* (Dan Olsen)
1. **Framework:** Keep the **Problem Space** (who the user is and what underserved need they have) separate from the **Solution Space** (your specific UI, shell, and code). Build a thin vertical slice that delivers "must-have" value + one "delighter," and watch real users click through it while speaking out loud.
2. **Use This Week on Animal Scrypt:** Watch your 3 consenting adult testers (`00-context.md` checkbox #7) scan the QR/NFC tag and approve 3 memories without touching their keyboard for them.
3. **Decision Tree:**
   * *Did the tester hesitate for more than 10 seconds on the memory approval button?* **Yes** $\to$ Rewrite the button label tonight.
   * *Did they smile when the physical tag opened their named creature?* **Yes** $\to$ Keep that exact physical-to-digital transition as the core delighter.
4. **Examples:**
   * *Public History:* Intuit watched small business owners struggle with accounting jargon and stripped QuickBooks down to a checkbook screen (https://dan-olsen.com).
   * *Animal Scrypt:* Replacing raw database JSON with three clean `[Approve]` / `[Edit]` / `[Delete]` cards in the zine dashboard.
5. **Outdated or not for you if:** You test only on yourself and assume other people know what "bilateral fragment" means.

---

### Book 12: *Inspired* (Marty Cagan)
1. **Framework:** Great product work tackles **four risks before scaling engineering**: (1) Value risk (will they choose to use it?), (2) Usability risk (can they figure out how?), (3) Feasibility risk (can we build and print it with our time/tools?), and (4) Viability risk (does it work for our costs and legal rules?).
2. **Use This Week on Animal Scrypt:** As a solo founder, you are the PM. Your 7-checkbox MVP in `00-context.md` tests all four risks in 6 weeks for under `$100`.
3. **Decision Tree:**
   * *Which of the 4 risks is highest for Animal Scrypt today?* **Value risk (Day-7 return use).**
   * *Have we proven Value risk yet?* **No** $\to$ Do not spend 4 weeks building complex backend scaling before the 3-adult test finishes.
4. **Examples:**
   * *Public History:* Humane AI Pin spent ratusan of millions on hardware manufacturing before proving Value risk, resulting in returns outpacing sales (https://www.theverge.com).
   * *Animal Scrypt:* Proving 3 adults come back on Day 7 using a `$7.50` 3D-printed shell before spending money on injection molds.
5. **Outdated or not for you if:** You read the chapters on managing 50 product managers at a giant tech company—skip those.

---

### Book 13: *Venture Deals* (Brad Feld & Jason Mendelson)
1. **Framework:** Investors care about only two buckets in a financing deal: **Economics** (valuation cap, discount, option pool, liquidation preference) and **Control** (board seats, protective vetoes, drag-along rights). Never give up control terms on a small pre-seed check, and always know your exact dilution math before signing (`19-term-sheet.md`).
2. **Use This Week on Animal Scrypt:** Keep our financing target simple: standard accelerator SAFEs (YC `$500k` deal or Techstars `$220k` deal) or a clean Post-Money SAFE after the MVP proof.
3. **Decision Tree:**
   * *Does the document ask for a board veto, full-ratchet anti-dilution, or founder IP assignment to an external studio?* **Yes** $\to$ Do not sign; take it to a lawyer (`19-term-sheet.md`).
   * *Is it a standard unmodified YC Post-Money SAFE?* **Yes** $\to$ Calculate `Check / Post-Money Cap = Ownership %` and have counsel confirm your entity is a Delaware C-Corp.
4. **Examples:**
   * *Public History:* Standardizing the YC Post-Money SAFE eliminated months of seed-stage legal negotiation for early founders (https://www.ycombinator.com/documents).
   * *Animal Scrypt:* Refusing to sign complex token warrants or multi-entity agreements before pre-seed product proof.
5. **Outdated or not for you if:** You are reading Series B preferred-stock participating liquidation clauses when you are raising a first pre-seed check.

---

### Book 14: *High Growth Handbook* (Elad Gil)
1. **Framework:** A tactical manual for scaling from 10 to 1,000 employees (board management, late-stage M&A, executive hiring). **90% of this book is N/A while you are a solo pre-seed founder.** The only two sections that apply today are: (1) guarding founder time ruthlessly, and (2) keeping your cap table and IP clean from Day 1.
2. **Use This Week on Animal Scrypt:** Audit your calendar: every hour this week should go to SCAD classes, RA duties, printing the shell, or testing the 7-day memory workspace.
3. **Decision Tree:**
   * *Does the chapter talk about hiring a VP of Sales or running a 7-person board?* **Yes** $\to$ **Mark N/A** until you have `$1M+` ARR.
   * *Does it talk about clean IP assignment and founder calendar blocks?* **Yes** $\to$ Apply it today (`22-legal-menu.md`).
4. **Examples:**
   * *Public History:* Stripe kept its early team tiny and obsessed over developer onboarding before building an enterprise sales org (https://stripe.com).
   * *Animal Scrypt:* Keeping KJ as a solo founder assisted by the `/seed` software factory (`25-factory.md`) instead of handing out 50% equity to an uncommitted classmate (`accelerator_1_transcript.pdf` p. 10).
5. **Outdated or not for you if:** **Mostly not for you today**—do not play "big company CEO" at zero users.

---

### Book 15: *The Cold Start Problem* (Andrew Chen)
1. **Framework:** Every network product starts with an empty room ("the cold start problem"). You solve it in two steps: (1) **"Come for the tool, stay for the network"**—make the product useful for **one single player** with zero other users online, and (2) build an **atomic network** of 10–50 people in one physical place (like one college dorm or studio) before expanding.
2. **Use This Week on Animal Scrypt:** Animal Scrypt's single-player tool is **one animal that remembers your own studio project for 7 days**. The network layer is **forking a trained worker animal (with the 20% parent-child royalty)** inside our atomic network at SCAD.
3. **Decision Tree:**
   * *Is Animal Scrypt useful if only 1 person on Earth uses it?* **Yes** — if the 7-day memory workspace and shell help them finish their project.
   * *How does Player 1 bring in Player 2?* Player 1 trains an Engineer animal on SCAD printer settings and lets Player 2 fork a Child Animal from it.
4. **Examples:**
   * *Public History:* Instagram won its first users as a single-player photo filter tool before the social feed network took off (https://andrewchen.com).
   * *Animal Scrypt:* Proving single-player 7-day memory recall with 3 SCAD students (Checkboxes #1–#5), then activating the parent-child royalty graph (Checkbox #6) inside the SCAD studio building.
5. **Outdated or not for you if:** You launch an empty "agent marketplace" with 0 trained animals and expect strangers to browse it.
