# 24 — Open-Source VC & Startup Tools Directory Spec (`/directory` Spec)

**Context read:** [`00-context.md`](./00-context.md), Section 13 & Section 20 of Master Prompt  
**Factory Gate:** **STOP FOR APPROVAL BEFORE CODE.** Do not build the Next.js/HTML UI until the founder approves this spec.

---

## 1. Purpose & Reader
A fast, single-page searchable directory on desktop and mobile where a founder or investor can find open-source startup, fundraising, and VC tools in under 10 seconds.
* **Tone:** Directory, not a marketing landing page. Maximum 40-word header. Search box + Category filter chips + Stage filter chips + Responsive Card Grid.
* **Palette:** Cream paper (`#EFE6D4`), dark ink (`#101419`), acid lime active chips (`#D8FF3E`).

---

## 2. Single Source of Truth (Markdown Content Rule)

We do **not** maintain a separate SQL database for the directory. Every card is rendered directly from markdown files stored in `/content/tools/*.md` (or a single `tools-directory.md` collection) with this exact YAML frontmatter shape:

```yaml
---
name: "Pitch Deck Playbook"
url: "https://github.com/startupmark/pitch-deck-playbook"
description: "Live-room pitch deck structure, typography rules, talk tracks, and zero-traction slide guidance."
category: "fundraising"
stage: "pre-seed"
language: "Markdown"
stars: "fetched at build or labeled as of 2026-11-08"
---
```

* **Adding or updating a tool:** Drop a markdown block into the folder and refresh. Zero migrations.

---

## 3. Required Categories & Stage Badges

* **11 Filter Categories:**
  `deal sourcing` · `due diligence` · `valuation` · `legal docs` · `cap table management` · `portfolio tracking` · `fund ops` · `startup metrics` · `fundraising` · `market research` · `AI tools`
* **4 Required Stage Badges (Every card must show one primary badge):**
  * `Pre-seed`
  * `Seed`
  * `Series A+`
  * `All stages` *(use when a tool serves multiple stages, and note details in the description)*

---

## 4. Initial Seed Catalog (15 Founder-Provided Repositories)

All 15 repositories from Section 20 of the Master Prompt are seeded below with honest descriptions, category mappings, and stage badges. Star counts must be fetched live via the GitHub API at build time or labeled `n/a (unfetched as of 2026-11-08)`—never invented:

| # | Name | Repository URL | Category | Primary Stage Badge | Language | One-Sentence Description |
|---|---|---|---|---|---|---|
| 1 | **pitch-deck-playbook** | https://github.com/startupmark/pitch-deck-playbook | `fundraising` | `Pre-seed` | Markdown | Story flow, stage-friendly typography, talk tracks, and honest slides for pre-traction founders. |
| 2 | **awesome-pitch-decks** | https://github.com/midovislam/awesome-pitch-decks | `fundraising` | `All stages` | Markdown | Curated reference collection of real startup pitch decks across pre-seed, seed, and Series A+. |
| 3 | **pitchsync** | https://github.com/avase33/pitchsync | `fundraising` | `Pre-seed` | TypeScript | Draft-to-critique workflow tool for iterating startup pitch narratives and slide alignment. |
| 4 | **startup-application-coach** | https://github.com/betahope/startup-application-coach | `fundraising` | `Pre-seed` | Markdown | Three-mode AI prompt coach (Review, Write, Coach) for accelerator application answers. |
| 5 | **Y-Combinator-application-and-interviews-guide** | https://github.com/rohitdotmittal/Y-Combinator-application-and-interviews-guide | `fundraising` | `Pre-seed` | Markdown | Practical checklist and interview preparation guide for Y Combinator applicants. |
| 6 | **business-model-canvas-md-template** | https://github.com/duxor/business-model-canvas-md-template | `market research` | `Pre-seed` | Markdown | Clean Markdown template for editing a 9-block Business Model Canvas inside Git or Notion. |
| 7 | **business-plan-skill** | https://github.com/huaxialucaicaizi/business-plan-skill | `market research` | `Pre-seed` | Markdown | Structured agent skill for turning founder notes into a 10-section startup business plan. |
| 8 | **Startup-Starter-Pack** | https://github.com/Ro5s/Startup-Starter-Pack | `startup metrics` | `All stages` | Markdown | Operational checklist covering legal, finance, product, and growth chores for new startups. |
| 9 | **startup-dataroom** | https://github.com/CreativateLabs/startup-dataroom | `due diligence` | `Seed` | TypeScript | Investor data room room-structure reference and permissioned document-sharing template. |
| 10 | **awesome-vc-opensource** | https://github.com/isanthoshgandhi/awesome-vc-opensource | `deal sourcing` | `All stages` | Markdown | Open-source index of tools for venture capital deal sourcing, fund ops, cap tables, and valuation. |
| 11 | **gstack** | https://github.com/garrytan/gstack | `AI tools` | `All stages` | Markdown | Garry Tan's slash-command software factory workflow (`CEO -> Design -> Eng -> QA -> Ship`). |
| 12 | **founder-skill** | https://github.com/Jakeschincariol/founder-skill | `market research` | `Pre-seed` | Markdown | Virtual board, 100-customer simulation, offer design, pricing, and CFO pressure-test skills. |
| 13 | **seed-skill** | https://github.com/Jakeschincariol/seed-skill | `fundraising` | `Seed` | Markdown | Shared `/seed` folder handoff workflow chaining market sizing, investor matching, decks, and outreach. |
| 14 | **solo-founder-playbook** | https://github.com/yayashuxue/solo-founder-playbook | `startup metrics` | `Pre-seed` | Markdown | Operating patterns, failure modes, and weekly cadences for one-person companies. |
| 15 | **solopreneur** | https://github.com/Solo-Entrepreneur/solopreneur | `AI tools` | `Pre-seed` | Markdown | YC Startup School lecture advisor spine adapted for solo technical and creative founders. |

---

## 5. Build Plan (Once Approved)
1. Write a Markdown parser (`lib/tools-loader.ts` or Python generator) that reads `/content/tools/*.md` and validates required frontmatter fields (`name`, `url`, `description`, `category`, `stage`, `language`, `stars`).
2. Write unit tests verifying that filtering by any of the 11 categories + 4 stage badges + text search returns the exact matching cards.
3. Build the responsive directory page with zero hero fluff (under 40 words at the top) and mobile-friendly cards.
