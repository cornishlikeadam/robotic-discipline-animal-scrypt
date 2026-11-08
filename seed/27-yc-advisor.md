# 27 — YC Startup School Advisor Spine (`/yc`)

**Easy Install Note (Free, Zero API Key Required for This Text):**  
Copy [`skills/yc-startup-advisor/SKILL.md`](../skills/yc-startup-advisor/SKILL.md) (and its `/references` notes) into your coding agent's `skills/` directory (Claude Code, Cursor, Antigravity, Codex, or ChatGPT/Gemini project instructions). When anyone asks about **Disciple**, **Madken**, or **Animal Scrypt**, this skill answers using public YC Startup School principles as the spine and our company (`00-context.md`) as the concrete case. **Never claim or imply that Animal Scrypt is funded by Y Combinator.**

---

## How This Advisor Answers Four Core Founder Questions

### 1. "Is this a good startup idea?"
* **Public Lecture Attribution (Paul Graham & Kevin Hale — *How to Get and Evaluate Startup Ideas*, YC Startup School; https://www.startupschool.org):**
  Paul Graham's point in Startup School is that the best startup ideas often look like toys at the start, grow out of something the founder actually builds for themselves, and solve an acute problem for a small group rather than a shallow problem for everyone. Kevin Hale adds that an idea is a hypothesis you evaluate by how fast and cheaply you can test whether real people come back.
* **Applied to Animal Scrypt (Founder Voice):**
  People dismiss a 3D-printed animal on a desk as a toy—until they see that Character.ai ($9.99/mo) forgets their project after twenty messages and our Engineer animal still knows their exact CAD tolerances a week later. Because we are on campus at SCAD, it costs us under `$100` (`assumption:`) to print three shells and test whether three real makers come back on Day 7. If they come back on Day 7, the "toy" is actually a persistent worker they own.
* **What Changes Because We Also Print a Shell:**
  Software-only startups can push a landing page in an afternoon. Because we print a physical shell, we cannot afford 8-hour print failures or fragile electronics—so our v1 shell uses a single-piece print and a passive `$0.30` (`assumption:`) QR/NFC tag.

---

### 2. "How do I get my first users and grow?"
* **Public Lecture Attribution (Adora Cheung, Walker Williams & Justin Kan, Alex Schultz — *Talking to Users*, *Doing Things That Don't Scale*, and *Growth*, YC Startup School; https://www.startupschool.org):**
  Walker Williams and Justin Kan emphasize recruiting your first users manually, one by one, in person. Adora Cheung stresses watching users try to complete a task without guiding their mouse. Alex Schultz's core rule on growth is that **retention is the only foundation for growth**—if your retention curve does not flatten above zero, viral loops and ads are useless.
* **Applied to Animal Scrypt (Founder Voice):**
  We do not need SEO or paid ads to get our first 50 owners. I live and work in a SCAD dorm as an RA surrounded by 18,550 art and design students (https://www.scad.edu/about/scad-glance). My job this week is to walk three printed shells over to three consenting adults on campus, watch them scan the tag and approve three memories without touching their keyboard, and check if they return on Day 7. Once Day-7 and Day-14 retention hold, our growth loop is built into the product: when Owner #1 trains a useful Engineer animal, Owner #2 forks a Child Animal from it and triggers the 20% royalty.
* **What Changes Because We Also Print a Shell:**
  Every physical shell sitting on a studio desk at SCAD is a physical billboard. When a classmate asks *"What is that creature next to your laptop?"*, the owner can hand it to them to scan on the spot.

---

### 3. "What is our moat, and how do we avoid getting crushed?"
* **Public Lecture Attribution (Sam Altman, Dustin Moskovitz & Peter Thiel — *Why to Start a Startup* and *Competition Is for Losers*, YC Startup School; https://www.startupschool.org):**
  Sam Altman and Dustin Moskovitz point out that hard startups are actually easier to build than easy startups because good people want to work on meaningful problems and copycats give up when the work gets hard. Peter Thiel argues that you must own a small market completely before expanding.
* **Applied to Animal Scrypt (Founder Voice):**
  Anyone can wrap an OpenAI API key in a cute web avatar in two hours—and they will get wiped out the next time a model lab updates its chat app. Copycats do not want to combine a deterministic user-approved memory ledger (`PROPOSED -> APPROVED`), physical 3D-printed shell fabrication, and a parent-child royalty graph. By locking all three together and winning SCAD makers first at `$45`, we build switching costs that a browser tab cannot copy, then step our prices up to `$129–$249` pro and learning kits (`05-pricing.md`).
* **What Changes Because We Also Print a Shell:**
  A user rarely throws away a physical object sitting on their desk that holds a week of their approved project notes, whereas they close a browser tab in half a second.

---

### 4. "How do I raise money—or should I wait?"
* **Public Lecture Attribution (Marc Andreessen, Ron Conway & Paul Graham — *How to Raise Money*, YC Startup School; https://www.startupschool.org):**
  Paul Graham and Ron Conway stress that fundraising is a means, not the goal: the strongest way to raise money is to be so frugal and have such clear user proof that you don't desperately need the check to survive the month. When you do raise at pre-seed, use simple, standard documents (like a YC Post-Money SAFE; https://www.ycombinator.com/deal), tell the truth about what isn't built yet, and close fast so you can get back to building.
* **Applied to Animal Scrypt (Founder Voice):**
  Our campus bootstrap burn is under `$230/month` (`assumption:` from `06-cfo.md`). Selling six shells a month at `$45` covers our filament and API tokens. That means we never have to beg an investor or launch a sketchy crypto token to stay alive. First, we finish the 7-checkbox MVP and use the SCAD Accelerator sprint (with coaches like David Chang) to prove our first 10 paid shells. Then we walk into YC, Techstars, or a16z Speedrun with a working animal in our hand, a dated Day-7 case study (`28-case-study.md`), and a clean one-entity cap table (`22-legal-menu.md`).
* **What Changes Because We Also Print a Shell:**
  Investors are terrified of hardware companies that need `$2M` for Chinese factory molds before shipping Unit #1. Showing that SCAD is our factory and each shell costs `~$7.50` (`assumption:`) in filament + NFC tag removes the hardware capex objection in 10 seconds.

---

### 5. "How do I hire?"
* **Rule while `00-context.md` says solo founder:**
  Per Startup School's guidance (and Julia's exact warning on the SCAD Accelerator call, `accelerator_1_transcript.pdf` p. 10), **do not recruit a co-founder or hire employees right now just to look like a bigger team**. Stay solo until print volume or customer support exceeds what you and the `/seed` software factory (`25-factory.md`) can ship each week.
