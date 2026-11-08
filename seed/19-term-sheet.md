NOT LEGAL ADVICE. Do not file this. A lawyer licensed in the right state has to review it.

# 19 — Term Sheet & SAFE Reading Guide (`/terms`)

**Context read:** [`00-context.md`](./00-context.md), [`10-investor-match.md`](./10-investor-match.md)  
**Purpose:** Plain-English guide so KJ can read a pre-seed SAFE, convertible note, or accelerator agreement without getting trapped.

---

## 1. The Five Terms That Actually Matter on a SAFE or Note

At pre-seed, you will almost certainly be handed a **YC Post-Money SAFE** (Simple Agreement for Future Equity; https://www.ycombinator.com/documents) or a convertible note—not a 60-page Series A stock purchase agreement. Here is what the five numbers mean:

### 1. Valuation Cap (Post-Money vs. Pre-Money)
* **What it is:** The maximum company valuation at which the investor's money converts into shares later.
* **Why "Post-Money" matters:** On a standard YC **Post-Money SAFE**, the ownership percentage is locked immediately:
  $$\text{Investor Ownership \%} = \frac{\text{Check Size}}{\text{Post-Money Valuation Cap}}$$
  * *Example:* If an angel invests **`$100,000`** on a **`$2,000,000` Post-Money Valuation Cap**, you just sold **exact 5.0%** of the company (`$100k / $2M`), and any additional SAFEs you raise in the same round dilute **you (the founder)**, not that SAFE holder.

### 2. Discount Rate
* **What it is:** A percentage discount (usually **15% to 20%**) off the share price of the next priced round if the company raises at a valuation lower than the cap.
* **Watch out for:** A SAFE with *both* a very low Valuation Cap *and* a massive Discount (e.g., 30%+). Most standard YC SAFEs use **either** a Valuation Cap **or** an uncapped MFN—not a predatory stack of both.

### 3. MFN (Most Favored Nation)
* **What it is:** If you raise money on an **Uncapped MFN SAFE** (like YC's `$375k` second tranche or Techstars' `$200k` SAFE; https://www.ycombinator.com/deal), that investor gets no cap today—but if you later give *another* investor a SAFE with a Valuation Cap (say, `$4M`), the MFN holder automatically gets to upgrade their SAFE to match that `$4M` cap.
* **Rule for KJ:** Never sign a "friend discount" SAFE at a tiny `$500k` cap after taking an Uncapped MFN SAFE, or you will accidentally re-price the entire `$200k–$375k` MFN tranche down to `$500k`!

### 4. Pro Rata Rights
* **What it is:** The right (not the obligation) for the investor to buy more shares in your *next* round (e.g., Seed or Series A) so their ownership percentage doesn't shrink.
* **Rule for KJ:** On post-money SAFEs, pro rata rights are usually granted in a separate **Pro Rata Side Letter**. Give pro rata side letters only to real lead checks (`$50k+`) or top accelerators—not to a `$2,500` check.

### 5. Who Pays Legal Fees
* **What it is:** A clause saying whether each side pays its own lawyer, or whether **your startup has to pay the investor's lawyer** out of the check they just wired you.
* **Rule for KJ:** On a standard SAFE, legal fees should be **$0 / each side pays their own**. Never sign a pre-seed term sheet that makes you reimburse `$15,000–$25,000` of an investor's legal bill out of a `$50,000` check.

---

## 2. Red Flags This Founder Must Never Sign Without a Lawyer

1. **Issuing a YC Corporate SAFE from an LLC:** A standard YC SAFE is written for a **Delaware C-Corporation** (`Common Stock` / `Preferred Stock`). Do not sign and take money on a C-Corp SAFE while Robotic Discipline is still an unincorporated project or a Georgia/Wyoming LLC without a lawyer converting the entity first (`22-legal-menu.md`).
2. **Full-Ratchet Anti-Dilution or Guaranteed Board Control at Pre-Seed:** No pre-seed angel writing a `$25k–$100k` check should get a veto over company operations, a majority board seat, or the right to fire the founder.
3. **IP Assignment Traps in University or "Venture Studio" Contracts:** Before signing any studio, incubator, or contractor agreement that provides "in-kind dev or branding work," have a lawyer check the **Intellectual Property (IP)** clause to ensure **Robotic Discipline** retains 100% ownership of the Animal Scrypt / Madken / Disciple names, character designs, and code.
4. **"Token Warrant" Side Letters That Promise a Launch Date:** Never sign a side letter promising to issue and list a liquid Litecoin/crypto token by a fixed calendar date, which can create severe U.S. SEC securities liability.

---

## Next Step
When any investor or accelerator sends an agreement, drop the text into `/seed/` (locked under `nda-status.md`) and take the flagged clauses above to a licensed startup attorney before signing.
