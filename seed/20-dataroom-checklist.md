# 20 — Data Room Checklist (`/dataroom` Checklist)

**Context read:** [`00-context.md`](./00-context.md), [`nda-status.md`](./nda-status.md)  
**Lock Status:** Checked against [`nda-status.md`](./nda-status.md) (`nda: none`, `stage2_unlock: false`). Sensitive Stage 2 documents remain locked until an investor's NDA is approved.

---

## 1. Stage 1 Rooms (Public / No NDA Required)

Any accelerator reviewer or Stage 1 investor can view these rooms today:

| Folder / Room | Document | Status (`Exists` vs. `Missing`) | File Path / Notes |
|---|---|---|---|
| **01 — Overview** | Executive Context & Stat Block | **Exists** | [`seed/00-context.md`](./00-context.md) |
| **01 — Overview** | Business Model Canvas & Plan | **Exists** | [`seed/07-canvas.md`](./07-canvas.md), [`seed/08-business-plan.md`](./08-business-plan.md) |
| **01 — Overview** | Investor Deck & Stage Deck | **Exists** | [`seed/11-deck-investor.md`](./11-deck-investor.md), [`seed/12-deck-stage.md`](./12-deck-stage.md) |
| **02 — Team** | Founder Bio & SCAD Context | **Exists** | [`FOUNDER-CONTEXT.md`](../FOUNDER-CONTEXT.md) (KJ Cornish — solo founder; no fake co-founders) |
| **03 — Product** | Stage-1 Zine Workspace HTML Preview | **Exists (Synthetic Demo)** | [`skeleton/zine_demo_view.html`](../skeleton/zine_demo_view.html) |
| **03 — Product** | 60-Second Demo Video & Shell Photo | **Missing (`not yet`)** | Scripts ready in [`seed/16-videos.md`](./16-videos.md); needs physical shell print + recording |
| **04 — Milestones** | 7-Checkbox MVP Checklist & 8-Week Plan | **Exists** | [`seed/00-context.md`](./00-context.md), [`seed/08-business-plan.md`](./08-business-plan.md) |
| **04 — Milestones** | Dated Build & 7-Day Memory Case Study | **In Progress (Build Case)** | [`seed/28-case-study.md`](./28-case-study.md) (0 of 3 adult user tests completed) |

---

## 2. Stage 2 Rooms (Sensitive — Locked Behind `stage2_unlock: true` After NDA Approval)

Per [`nda-status.md`](./nda-status.md), these rooms and their underlying files must **never** be exposed to public viewers or un-NDA'd AI chat sessions:

| Folder / Room | Document | Status (`Exists` vs. `Missing`) | Lock & Action Needed |
|---|---|---|---|
| **05 — Financials** | Unit Economics, Burn & Cohort Scenario Math | **Exists (Draft Scenario)** | [`seed/05-pricing.md`](./05-pricing.md), [`seed/06-cfo.md`](./06-cfo.md) — **LOCKED (Stage 2)** |
| **05 — Financials** | Historical Bank Statements & Stripe Ledger | **Missing (`none yet`)** | Pre-revenue (`$0`); open business bank account after entity filing — **LOCKED (Stage 2)** |
| **06 — Cap Table** | Founder Equity Ledger (`100%` KJ Cornish) | **Missing (Pre-Incorporation)** | Draft only after choosing LLC vs. Delaware C-Corp (`22-legal-menu.md`) — **LOCKED (Stage 2)** |
| **07 — Legal** | Certificate of Formation / Incorporation | **Missing (`not filed yet`)** | Entity name selected (`Robotic Discipline`); await counsel review — **LOCKED (Stage 2)** |
| **07 — Legal** | Signed Customer / Tester Consent Forms | **Missing (`0 of 3 signed`)** | Needed for the 3 consenting adult MVP testers — **LOCKED (Stage 2)** |
| **08 — Tax** | EIN Confirmation Letter & State Tax Filings | **Missing (`not filed yet`)** | Obtain IRS EIN (`$0` at `irs.gov`) after forming entity — **LOCKED (Stage 2)** |
| **09 — IP** | Founder IP Assignment & SCAD Policy Clearance | **Missing (`needs review`)** | Verify SCAD student IP rules (`22-legal-menu.md`); lock prompts/royalty code — **LOCKED (Stage 2)** |

---

## Next Step
Do not fake missing Stage 2 files. Show Stage 1 openly, mark unfiled legal/tax docs as `"Pre-incorporation — scheduled upon accelerator entry"`, and see [`seed/23-dataroom-product-spec.md`](./23-dataroom-product-spec.md) for the self-hosted data room software spec.
