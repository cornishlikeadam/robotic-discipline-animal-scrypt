# 08 — Business Plan (`/plan`)

**Context read:** [`00-context.md`](./00-context.md) through [`07-canvas.md`](./07-canvas.md)  
**Company:** Animal Scrypt (legal entity name: **Robotic Discipline**, also called **Disciple** and **Madken**)  
**Founder:** Kendren "KJ" Cornish

---

## 1. What we are building

We build collectible AI animals that remember you, change over time, and can do a job. Each animal has two halves that stay linked: a 3D-printed physical shell you hold in your hand (paired via a QR code or NFC tag) and a persistent digital workspace in your browser.

Unlike a fresh chat tab that forgets you tomorrow, an Animal Scrypt creature keeps an inspectable memory ledger of facts you approve and takes on a worker role—starting with engineer, artist, musician, or researcher. When an owner trains an animal to be good at a job and another person forks a child animal from it, the ledger credits a royalty to the parent animal's maker.

---

## 2. Who it is for first

Our v1 customer is a **tech-curious young adult (ages 18–30), starting with SCAD students, makers, and figure collectors in Savannah, Georgia**. They already spend hours every week building studio projects with AI tools and buying desk figures, and we can reach them in person on campus today.

Once the 7-day memory loop and physical shell are proven with young adults, our roadmap expands into two higher-price segments identified by the founder:
1. **People with disabilities** seeking an accessible, low-friction AI companion that remembers daily routines and assistive preferences without repeating instructions.
2. **Parents and older teens** looking for self-directed, adaptive AI project tools inspired by Alpha School's 2-hour learning approach (https://alpha.school), at a consumer price rather than `$40,000+/year` private tuition.

---

## 3. Why now

1. **Paid chat companions still fail at memory:** Users paying `$9.99/month` for Character.ai (`c.ai+`) and `$19.99/month` for Replika Pro complain constantly on Reddit that bots forget plot details, persona traits, and ongoing projects after a few dozen messages (https://www.reddit.com/r/CharacterAI/, https://replika.com).
2. **Adults are spending billions on physical characters that do nothing:** Pop Mart grew 184.7% in 2025 to RMB 37.12 billion (`~$5.1B+ USD`) selling vinyl collectibles (https://www.popmart.com), while Tonies grew 31% in FY 2025 to EUR 630 million selling 173M+ NFC figurines that only play static audio (https://ir.tonies.com).
3. **Small-batch fabrication and model costs crossed the solo-builder threshold:** A SCAD student with campus 3D printers, `$0.30` (`assumption:`) NFC/QR tags, and bounded API/local models can manufacture and run a persistent physical-digital creature for under `$11` (`assumption:`) without factory injection molds.

---

## 4. Product, v1, in one week of work chunks

Our 6–8 week MVP is locked to the founder's 7 done-conditions in `00-context.md`:

* **Week 1 — Identity & Database Kernel:** Finalize the browser-accessible SQLite/Supabase schema (`companions`, `memory_records`, `ownership`, `royalty_ledger`) based on our existing `skeleton/interfaces.py` kernel. Verify that approved memories survive server restarts.
* **Week 2 — Personality & Conversational Workspace:** Build the cream (`#EFE6D4`) and acid lime (`#D8FF3E`) editorial zine dashboard displaying the creature's name, biography, worker role, chat box, and explicit memory approval buttons (`Approve` / `Edit` / `Delete`).
* **Week 3 — Physical Shell & QR/NFC Pairing:** Print the first 3D shell at SCAD, embed the QR/NFC tag, and link the scan URL directly to the owner's verification and pairing page.
* **Week 4 — Simulated Royalty Ledger:** Add the "Fork Child Worker" button that transfers a template from creator to new owner and records the 20% royalty allocation in the test ledger without processing real money (`00-context.md` checkbox #6).
* **Week 5 — Internal 7-Day Memory Dry Run:** Run one creature across 7 days internally, feeding it 5 project facts on Day 1, restarting the app mid-week, and verifying recall of at least 3 facts on Day 7.
* **Week 6 — Three Consenting Adult User Tests:** Hand 3 printed shells to 3 consenting adults at SCAD. Observe independent activation, Day-1 conversation/approval, and Day-7 return recall.
* **Weeks 7–8 — Fixes & Case Study Packaging:** Fix every UI friction point recorded during Week 6 and publish the dated build-and-user record in `28-case-study.md`.

---

## 5. How we get the first 50

1. **Users 1–3 (Week 6):** Three consenting adult SCAD students recruited in person from the 10 Mom Test interviews (`03-customers-100.md`).
2. **Users 4–15 (Weeks 7–10):** Table demos in SCAD studio buildings, dorm common rooms, and the SCAD Accelerator cohort—selling the first 10 paid Tier 1 shells at `$45` (`assumption:`).
3. **Users 16–50 (Months 3–4):**
   * Every owner who trains a worker animal can invite a classmate to fork a Child Animal (triggering the royalty ledger).
   * Short, unedited build videos showing the 3D print + Day-7 recall test posted to builder/collector channels.
   * Readers of *The Book of Robotic Discipline* free chapters and startup worksheets who opt in to test the companion tools.

---

## 6. Money in and money out (scenario, not forecast)

All numbers below are **scenarios and labeled assumptions (`assumption:`)** from `05-pricing.md` and `06-cfo.md`, not existing revenue:

### Scenario A: First 50 Customers (Months 1–4, Bootstrap Proof)
* **Money In (`assumption:`):**
  * 3 free MVP test units: `$0`
  * 27 Tier 1 Starter Shells at `$45`: `+$1,215`
  * 20 Tier 2 Pro Worker Shells at `$129` (as prices grow in Months 3–4): `+$2,580`
  * 30 active monthly memory subscriptions at `$9–$19/mo` over 2 months: `+$840`
  * **Total 4-Month Scenario Cash In:** **`+$4,635`**
* **Money Out (`assumption:`):**
  * 50 printed shells, NFC/QR tags, and zine boxes (`~$7.50/unit`): `-$375`
  * 4 months of LLM tokens, Supabase/Vercel, and domain (`~$150/mo`): `-$600`
  * Stripe fees & 20% creator royalty payouts on forked units: `-$480`
  * **Total 4-Month Scenario Cash Out:** **`-$1,455`**
* **Net Bootstrap Scenario Margin:** **`+$3,180`** (proves unit profitability before institutional capital).

### Scenario B: Post-Proof Price Growth & Founding Cohort (Year 1–2 Target)
* Stepping hardware kits to **`$129–$249`**, subscriptions to **`$19–$49/mo`**, and opening the planned **`~300 × $2,500` Founding Cohort (`$750,000` gross / `~$604,580` net scenario)** only after Scenario A retention is measured.

---

## 7. Team as it is, not as a fantasy org chart

* **Kendren "KJ" Cornish — Founder (Solo):** Rising sophomore at SCAD in Savannah, Georgia. U.S. military veteran (~8 months served, diver path). Resident assistant on campus. Helps run a family nonprofit and church conference. Experienced in research transfer, 3D fabrication at SCAD, and AI agent workflows (including an adjacent SCADpro research thread on equine telehealth, gait, and vocalization).
* **Open Gaps (No Pretend VPs):** We do not have a full-time hardware electrical engineer, a smart-contract auditor, or a legal counsel on retainer yet. We use SCAD fabrication labs and coaches during the accelerator sprint.

---

## 8. What we are not building this year

1. We are **not** building motorized walking robots with batteries and Wi-Fi chips inside the shell (which killed Living.AI reviews; https://www.trustpilot.com/review/living.ai).
2. We are **not** launching a tradable meme coin, speculative NFT egg auction, or multi-level royalty pyramid.
3. We are **not** merging the SCADpro equine telehealth project into the consumer toy.
4. We are **not** collecting data from children under 13 or making medical/clinical treatment claims.
5. We are **not** forming a multi-entity Delaware PBC + Trust + Wyoming DUNA conglomerate before we have paying customers (`22-legal-menu.md`).

---

## 9. Risks that can kill it

1. **Day-7 novelty drop-off:** Users scan the shell once on Day 1, think it is cute, and never open the workspace again on Day 7. *(Mitigation: Anchor the animal to a real weekly studio/project job and test 7-day retention on 3 adults before scaling).*
2. **Memory pollution or hallucination:** The AI saves wrong facts and annoys the user. *(Mitigation: Enforce the explicit `Approve / Edit / Delete` memory gate so zero facts are stored silently).*
3. **Crypto stigma:** Investors or art-school buyers hear "Litecoin" and assume it is a scam like CryptoZoo (https://en.wikipedia.org/wiki/CryptoZoo). *(Mitigation: Keep the v1 royalty ledger simulated in SQLite/Supabase per checkbox #6 and lead 100% with the animal, the shell, and the memory).*
4. **SCAD IP or campus policy ambiguity:** Using university printers for commercial shells without checking school IP rules. *(Mitigation: Verify SCAD student entrepreneurship IP policy inside the SCAD Accelerator before commercial sales).*

---

## 10. The ask, if any

1. **Immediate Ask (SCAD Accelerator):** Admission into the 10-team SCAD Accelerator winter sprint, pairing with a product/angel coach (such as David Chang or Adrian Gill) to pressure-test the first 10 paid shells between January and May Demo Day.
2. **Next Ask (YC / Techstars / a16z Speedrun — Post-MVP Proof):** Pre-seed accelerator investment (`$125k–$500k` standard program terms) once all 7 MVP checkboxes and the Day-7 case study (`28-case-study.md`) are complete.
