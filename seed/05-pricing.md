replaced 2026-11-08 because founder confirmed v1 customer focus and directed that prices must grow after v1 proof.

# 05 — Pricing (`/pricing`)

**Context read:** [`00-context.md`](./00-context.md), [`04-offer.md`](./04-offer.md)  
**Previous Verdict Acknowledged:** `04-offer.md` scored **3.8 / 5.0 (PURSUE under the narrowed 18–30 adult maker wedge)** — delivering one 3D-printed shell, one browser workspace, and 7-day recall of at least three approved facts.

---

## 1. Three Starting Options & The Price Growth Ladder

| Option | What it is | Price (`assumption:`) | Risk |
|---|---|---|---|
| **A** | Subscription only (software animal, no physical shell included) | `$9.99/month` | Easy to copy. Looks just like Character.ai (`$9.99/mo`; https://www.reddit.com/r/CharacterAI/) and loses the physical twin moat. |
| **B** | **V1 Entry Wedge: Buy the animal + light subscription for memory** | **`$45` one-time shell + `$9/month` memory & workspace (first month included)** | **Needs a real physical object.** Requires printing shells cleanly at SCAD and keeping filament/time costs under `$10` (`assumption:`). |
| **C** | **Founding Cohort / Patron Tier (`$2,500` + parent-child royalty)** | **`$2,500` one-time founding pass (~300 spots planned)** | **Too big if the demo is weak.** Opens only after the 7-day memory proof and first 10 Option B shells ship. |

### The Price Growth Ladder (Founder Rule: Prices Grow as Proof and Roles Expand)
We do not stay at student entry pricing forever. As soon as the 7-day recall test and first 10 shells work, prices step up across four tiers (`assumption:`):

1. **Tier 1 — V1 Campus Proof (Weeks 1–8):** **`$45` shell + `$9/month`** (18–30 SCAD makers & collectors; proves 7-day memory + 1 shell + 1 worker role).
2. **Tier 2 — Pro Worker & Collector Drop (Months 3–6):** **`$129–$199` numbered multi-part shell / dock + `$19–$29/month`** (adds multi-role switching, local/cloud sync, and higher memory capacity; Undercuts Living.AI EMO at `$279–$369`; https://living.ai).
3. **Tier 3 — Family Learning & Accessible Companion Edition (Months 6–12):** **`$249` hardware kit + `$39–$49/month`** (guided learning and accessibility features for parents and assistive users—priced at a fraction of Alpha School's `$10,000/yr` home software or `$40,000+/yr` tuition; https://alpha.school).
4. **Tier 4 — Founding Cohort & Studio Master Pass (Post-Case Study):** **`$2,500` founding cohort pass (~300 planned)** (includes custom-sculpted founding parent animal, priority print lineage, and Genesis parent-child royalty rights).

---

## 2. Founding Cohort Scenario Math (`~300 × $2,500`)

This is a **scenario** from `00-context.md`, **not a forecast or closed round**:

* **Gross Scenario Receipts:** `300 founders × $2,500 = $750,000` gross.
* **Deductions (`assumption:` until measured):**
  * `assumption:` Payment processing / on-ramp fees (3.5%): `-$26,250`
  * `assumption:` 10% refund / cancellation reserve (30 units): `-$75,000`
  * `assumption:` Custom 3D-printed shell, NFC tag, zine box, and shipping (`$35/unit × 270 net units`): `-$9,450`
  * `assumption:` 12 months of cloud model inference & Supabase hosting reserved per founding animal (`$3/mo × 12 mos × 270 units`): `-$9,720`
  * `assumption:` Legal, accounting, and tax reserve (Delaware C-corp conversion + CPA): `-$25,000`
* **Net Scenario Operating Runway (if 300 sold):** `~$604,580` before founder salary and taxes.
* **Reality Gate:** Open the `$2,500` cohort only after the 7-checkbox MVP in `00-context.md` passes with 3 real users and 10 Tier 1 (`$45`) buyers keep their animal past Day 14.

---

## 3. The V1 Royalty Rule (One Event Only)

To avoid a tangled pyramid of micropayments, we lock v1 to **one clear definitions table and one triggering event**:

* **Parent Animal:** An original animal whose owner has trained it with approved domain memories and prompt skills (with private personal memories stripped out).
* **Child Animal:** A new animal instance forked from that Parent Animal's public worker template by a second user.
* **The Single V1 Triggering Event:** **Paid Child Mint / Purchase.**
  * When User B pays to mint a Child Animal from User A's Parent Animal template, **20% of net hardware/mint price (`$9.00` on a `$45` Tier 1 child, `$30.00` on a `$150` Tier 2 child; `assumption:`)** is credited to the Parent Animal's maker in the royalty ledger. As shell prices grow, the creator's dollar payout per child grows automatically.
* **What We Refuse to Pay On in V1:**
  * Zero royalties on free test forks (prevents wash-minting).
  * Zero multi-hop grandchildren royalties (`Gen 1 -> Gen 2` only in v1).
  * Zero split on the monthly compute subscription (which covers our database and model token costs).

---

## Verdict
* **Pricing Score:** **4.2 / 5.0**
* **Verdict:** **PURSUE the 4-Tier Price Growth Ladder** — Start at `$45 + $9/mo` (Tier 1) to prove the 10-shell test fast, then step up to `$129–$249 + $19–$49/mo` (Tiers 2–3) and the `$2,500` Founding Cohort (Tier 4) once 7-day retention is measured.
