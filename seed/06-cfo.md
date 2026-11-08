# 06 — CFO Pressure Test (`/cfo`)

**Context read:** [`00-context.md`](./00-context.md), [`01-board.md`](./01-board.md), [`02-competitors.md`](./02-competitors.md), [`03-customers-100.md`](./03-customers-100.md), [`04-offer.md`](./04-offer.md), [`05-pricing.md`](./05-pricing.md)  
**Previous Verdict Acknowledged:** `05-pricing.md` scored **4.0 / 5.0 (PURSUE Option B: `$45` shell + `$9/mo` memory subscription, with a single-event 20% parent-to-child mint royalty)**.

---

## 1. What Kills Profit (The Four Margin Traps)

1. **Print time and failed shells (`assumption:`):** If a 3D-printed shell takes 9 hours on a printer, fails 30% of the time, and requires 2 hours of hand-sanding by the founder, a `$45` shell loses money on labor.
   * *Fix:* Design the v1 shell to print in **under 2.5 hours** in one or two snap-fit pieces with zero supports, keeping material + NFC tag cost under **`$6.00/unit`** (`assumption:`).
2. **Unbounded model token burn (`assumption:`):** If a user chats for 3 hours a day on a frontier reasoning model while paying `$9/month`, API costs will exceed `$15/month` and bankrupt the tier.
   * *Fix:* Use small/fast models (or local Ollama / Gemini Flash / GPT-4o-mini) with a strict 3-sentence zine response rule and cap active context injection to the top 15 `APPROVED` memory records (`assumption: ~$0.80–$1.80/user/month` in API tokens).
3. **High-touch troubleshooting (`assumption:`):** Living.AI gets crushed on Trustpilot because 2.4GHz Wi-Fi setup breaks in dorms (https://www.trustpilot.com/review/living.ai).
   * *Fix:* Zero Wi-Fi chips inside the shell. Use a passive QR code + NTAG215 NFC sticker (`$0.30` `assumption:`) that opens a regular browser URL in 2 seconds.
4. **Royalty stacking:** Paying royalties on subscriptions, secondary resales, and multi-generation children simultaneously eats 100% of software margin.
   * *Fix:* Enforce the `05-pricing.md` rule: pay a flat **20% creator royalty only on initial paid Child Animal mints**, never on the `$9/month` compute subscription.

---

## 2. Unit Economics of One Shipped Animal (Option B)

All cost numbers below are labeled **`assumption:`** until the first 10 shells are printed and timed at SCAD:

| Line Item | Per-Unit Amount (`assumption:`) | Notes |
|---|---|---|
| **Day-1 Retail Price (Shell + Month 1 Workspace)** | **`+$45.00`** | Paid by buyer at checkout |
| Stripe / payment processing (2.9% + $0.30) | `-$1.61` | Standard card fee |
| PLA / resin filament + NTAG215 NFC sticker + QR base | `-$5.50` | Printed using SCAD fabrication access |
| Cream/lime zine insert card + small box | `-$2.00` | Hand-packed in Savannah for campus pickup |
| Parent creator royalty (if forked from a parent animal; 20%) | `-$9.00` (`$0` if House/Founding animal) | Credited to parent maker |
| Month 1 LLM API + database cost | `-$1.50` | Bounded prompt + SQLite/Supabase row storage |
| **Day-1 Net Contribution Margin** | **`+$25.39` (Forked) to `+$34.39` (House)** | **56% to 76% gross margin** |
| **Month 2+ Recurring Subscription (`$9.00/mo`)** | **`+$6.90/mo` net** | `$9.00` minus `$0.56` Stripe fee and `$1.54` model/hosting cost (`77%` margin) |

---

## 3. Monthly Burn Categories (Once One Person Is Building Full-Time)

| Category | Student Bootstrap Mode (Now, on Campus) | Full-Time Solo Founder Mode (Post-Graduation / Funded) |
|---|---|---|
| **Founder Living / Stipend** | Covered by RA role / student budget (`$0` company draw) | `assumption: $3,500 – $4,500 / month` (Savannah, GA) |
| **Hosting & AI APIs (Supabase, Vercel, LLM tokens for <100 users)** | `assumption: $25 – $60 / month` | `assumption: $150 – $300 / month` |
| **3D Printing Filament, NFC Tags & Packaging (10–30 shells/mo)** | `assumption: $75 – $150 / month` | `assumption: $300 – $600 / month` |
| **Domain, Email & Dev Tools** | `assumption: $20 / month` | `assumption: $60 / month` |
| **Legal / State Filing / Accounting Reserve** | `assumption: $0 / month` (pre-incorporation) | `assumption: $200 / month` amortized |
| **Total Monthly Cash Burn** | **`assumption: ~$120 – $230 / month`** | **`assumption: ~$4,210 – $5,660 / month`** |

*At student bootstrap burn (`~$200/month`), selling just **6 shells per month at `$45`** makes the project cash-flow positive before raising a dime.*

---

## 4. The Cheapest Test That Can Fail

Before spending a dollar on lawyers, smart contracts, or ads, run this two-stage gate:

1. **Stage A — The 7-Day Functional Gate (Founder's MVP Done-Condition, Cost: `<$30`):**
   * Print **1 shell** (or 3 shells) with a QR/NFC tag.
   * Give it to **3 consenting adults** at SCAD.
   * Verify all 7 checkboxes in `00-context.md`: activation, conversation, recall of $\ge 3$ approved details after 7 days (including after an app restart), workspace controls, ownership view, and simulated royalty ledger entry.
2. **Stage B — The 10-Buyer, 14-Day Commercial Gate (Cost: `<$100` in filament/tags):**
   * Print **10 shells**, pair **10 animals**, and offer them to 10 young-adult makers/collectors (from the 10 Mom Test conversations in `03-customers-100.md`) at one price (**`$45`**).
   * Track how many still open their animal's workspace and approve a memory on **Day 14**.

---

## Final Phase 1 Verdict

* **CFO Score:** **4.0 / 5.0**
* **Verdict:** **Worth pursuing if** at least **2 of the first 3 consenting adult testers** complete the Day-7 recall test without founder hand-holding AND at least **3 of the first 10 prospects** pay `$45` (or put down a `$20` deposit) for a printed shell + 14 days of memory. **Kill or narrow if** users treat the shell as a one-time novelty on Day 1 and zero testers open the workspace on Day 7.
