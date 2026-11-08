# 07 — Business Model Canvas (`/canvas`)

**Context read:** [`00-context.md`](./00-context.md) through [`06-cfo.md`](./06-cfo.md)  
**Company:** Animal Scrypt (operated by **Robotic Discipline**, also called **Disciple** and **Madken**)

---

## 1. Customer segments
*Questions: Who has the pain this month? Who can we reach without ads? Who is explicitly not the customer in v1?*

* **Who has the pain this month (V1 Beachhead):** Tech-curious young adults (ages 18–30, starting with SCAD students and makers in Savannah) who use AI tools for multi-week studio projects and collect desk figures, but hate how chatbots forget context across sessions.
* **Who we can reach without ads:** SCAD classmates, dorm residents (the founder is an RA), SCADpro collaborators, and local figure collectors.
* **Planned Phase 2–3 Expansion Segments (as prices grow):**
  * Adults and students with disabilities who want an accessible, low-friction memory and daily task companion.
  * Parents and older teens seeking self-directed AI project learning inspired by Alpha School's 2-hour learning model (https://alpha.school), without the `$40,000+/year` private tuition.
* **Who is explicitly NOT the customer in v1:** Children under 13 (no COPPA data collection in v1), enterprise IT departments, and crypto speculators looking to flip meme coins.

---

## 2. Value propositions
*Questions: What can they do after 10 minutes that they cannot do now? What do they hold in their hand? What would they tell a friend?*

* **After 10 minutes:** Scan your animal's tag, open its cream-and-lime zine workspace, talk through your project, and click **Approve** on three facts you want it to remember next week.
* **What you hold in your hand:** A numbered, 3D-printed animal shell with a QR/NFC tag linked to its digital identity.
* **What you tell a friend:** "I have a 3D-printed animal on my desk that actually remembers my project specs a week later, and if you copy the worker role I trained, I get a cut."

---

## 3. Channels
*Questions: Where do the first 50 come from (campus, a film of the print, a collector thread)? What do we refuse to do before we have a demo?*

* **First 3 (MVP Done-Condition):** Hand-picked consenting adult testers at SCAD in Savannah.
* **First 10 to 50:**
  * In-person demos at SCAD studio desks, dorm common rooms, and the SCAD Accelerator cohort.
  * Short raw video clips showing a shell coming off the 3D printer, scanning the tag, and passing the Day-7 memory check.
  * *The Book of Robotic Discipline* free chapters and worksheets, bringing solo builders into the funnel.
* **What we refuse to do before we have a working 7-day demo:** Paid social ads, influencer sponsorships, Discord token hype servers, or cold-emailing 500 VCs with no video.

---

## 4. Customer relationships
*Questions: Is this a cohort, a subscription, or support-by-founder? What does "the animal remembers me" require from us weekly?*

* **How it starts:** Direct founder onboarding in Savannah (20 minutes in person or on screen share), transitioning into a monthly memory subscription and later the `~300`-member founding cohort.
* **What "the animal remembers me" requires from us weekly:**
  * A database that never wipes approved memories on restart.
  * An explicit approval queue (`PROPOSED -> APPROVED`) so the animal never stores hallucinations as facts.
  * One weekly check-in prompt that pulls from the owner's approved memories so the animal proves it still knows them on Day 7, Day 14, and Day 30.

---

## 5. Revenue streams
*Questions: What is the first dollar for? Cohort, object, subscription, royalty — which one is v1? Which one is year two?*

* **First Dollar (V1 — Weeks 1–8):** **Object + Light Subscription (`assumption: $45` 3D-printed shell + `$9/month` memory workspace, Month 1 included).**
* **Growth Tier 2 (Months 3–6):** **Pro Worker Shells & Multi-Role Subscriptions (`assumption: $129–$199` shell/dock + `$19–$29/month`).**
* **Growth Tier 3 (Months 6–12):** **Guided Learning & Accessible Companion Kits (`assumption: $249` kit + `$39–$49/month`).**
* **Year Two / Post-Proof Scale:**
  * **Parent-Child Royalty (20% of paid child mint; `assumption:`):** When a user forks a trained parent animal, 20% goes to the parent maker and 80% stays with Animal Scrypt.
  * **Founding Cohort (`~300 × $2,500` scenario):** Opened only after the Day-7 and Day-14 proof gates pass.

---

## 6. Key resources
*Questions: Memory store, print pipeline, brand system, Litecoin record, the founder's time. Which one breaks first?*

* **Memory store:** SQLite/Supabase table of user-approved facts and personality state (`skeleton/schema.sql`).
* **Print pipeline:** SCAD 3D-printing lab access + founder's CAD shell files + passive QR/NFC tags.
* **Brand system:** Editorial zine look (`#EFE6D4` cream paper, `#D8FF3E` acid lime, hot blush unset).
* **Ownership & royalty ledger:** Simulated test ledger in v1 (`00-context.md` checkbox #6), moving to Litecoin rails after product proof.
* **The founder's time:** Full-time SCAD sophomore, RA, and builder.
* **Which one breaks first:** **The founder's time and print pipeline** if a shell takes 8 hours to print or if 10 users need manual bug fixes during midterms. Shells must print in under 2.5 hours (`assumption:`).

---

## 7. Key activities
*Questions: What do we do every week that is the product, not the pitch? Print, memory test, one user conversation, one public artifact.*

Every week has four non-negotiable jobs:
1. **Print:** Fabricate at least two physical shells and bind their QR/NFC tags.
2. **Memory test:** Run the Day-1 to Day-7 recall test across restarts and fix any memory drift.
3. **User conversation:** Sit down with at least two real people (Mom Test format from `03-customers-100.md`) and watch them use the workspace without touching their mouse.
4. **Public artifact:** Film a 30-second clip of what worked or broke and log the real numbers in `/seed`.

---

## 8. Key partners
*Questions: Who must say yes (print lab, chain tooling, a faculty reader, a lawyer later)? Who is a nice-to-have we will not wait on?*

* **Who must say yes right now:**
  * **Three consenting adult testers** at SCAD (`00-context.md` checkbox #7).
  * **SCAD fabrication / print shop access** (already available to the founder as a student).
* **Who we talk to next month:**
  * **SCAD Accelerator coaches** (e.g., David Chang, Adrian Gill) and a faculty reader for the methods note.
  * **A licensed startup lawyer** before taking outside money or issuing equity (`22-legal-menu.md`).
* **Nice-to-haves we will NOT wait on:** Litecoin Foundation grants, toy factory mass-production quotes, or school-district partnerships.

---

## 9. Cost structure
*Questions: Model tokens, hosting, filament and machine time, legal, travel to a program. What is the cost of one shipped animal?*

* **Cost of one shipped V1 animal (`assumption:` from `06-cfo.md`):** **`~$10.61`** (`$5.50` filament + NFC/QR tag, `$2.00` zine card/box, `$1.61` Stripe fee, `$1.50` Month-1 model tokens & database rows).
* **Monthly bootstrap burn on campus (`assumption:`):** **`~$120–$230/month`** (filament, tags, domain, and API credits for `<50` users).
* **Later costs (post-funding):** Full-time founder living draw (`assumption: $3,500–$4,500/mo` in Savannah), Delaware C-corp legal setup, and travel to accelerator interviews.

---

## The 6-Line Canvas (For a Tired Reader)

1. **Product:** We make collectible 3D-printed animals linked to browser workspaces that remember user-approved facts across weeks and take on worker jobs.
2. **Customer:** We start with 18–30 SCAD makers and collectors, then expand into accessible companions and parent/teen self-directed learning as prices grow.
3. **Wedge:** Chatbots forget your work next week (`https://www.reddit.com/r/CharacterAI/`), and `$5B` art toys (`https://www.popmart.com`) do nothing; our animal remembers on Day 7 and has a body you can hold.
4. **Money:** We start at `$45` per shell + `$9/mo` (`assumption: ~$10.61` unit cost), scale hardware/subscription tiers up to `$129–$249+`, and take an 80/20 split when a parent animal is forked into a paid child worker.
5. **Proof Gate:** Before pitching a `$2,500` founding cohort, we must check all 7 boxes of the 6–8 week MVP—ending with 3 consenting adults completing the 7-day memory test.
6. **Next Move:** Print 3 shells at SCAD, run 10 Mom Test chats, and log the Day-7 recall results in `28-case-study.md`.
