# START HERE — Robotic Discipline Operating Guide

Welcome to the unified knowledge base for **Robotic Discipline**, founded by **Kendren "KJ" Cornish**.

---

## 1. Golden Rule: One Company, One Evolving Vision

Before reading or editing any file in this workspace, understand this foundational rule:

> **Robotic Discipline, MADKEN (Mad Kin), Animal Scrypt, Disciple, and Space Fort are NOT separate startups or competing ventures.**  
> They are historical and functional expressions of **one unified business concept** developed by KJ Cornish.

* **Robotic Discipline** is the overarching company identity and practice ("discipline is the practice").
* **Disciple** has been used in *The Book of Robotic Discipline* and startup toolkit notes as the institutional/company name built from that practice.
* **MADKEN** (*Mad Kin*) describes the collectible physical figures, the 12 founding characters across 4 factions, the desk dock + removable cartridge system, the StarNetOS/Spaceport workspace, and the simulated civilization.
* **Animal Scrypt** describes the local-first AI companion layer, the inspectable memory ledger, the low-pressure social connection mechanics (shared ritual objects, parallel presence, bilateral memory-fragment exchange), and the community/homestead steward roles.
* **Space Fort** appears in earlier notes as an umbrella venture/IP studio framing (*The Artificial Civilization Project*, *ORBIT*, *Action Intelligence*).

**Never fragment these into separate cap tables, duplicate financial models, or competing pitches.** Preserve their distinct ideas as layers and staged milestones of one company.

---

## 2. Epistemic Hygiene: What Actually Exists Today vs. What Is Proposed

Every agent, collaborator, and document in this repository must distinguish between:

1. **Inspected & Runnable Today (`[IMPLEMENTED_SKELETON]`):**
   * [`skeleton/interfaces.py`](./skeleton/interfaces.py) & [`skeleton/schema.sql`](./skeleton/schema.sql): A working local Python + SQLite state kernel implementing companion registration, explicit `PROPOSED -> APPROVED -> DELETED` memory review, bilateral fragment exchange with dual sign-off and revocation, parallel-presence `ritual_objects` (`DORMANT -> RESONATING -> CRYSTALLIZED`), time-bounded `capability_leases`, JSON portable identity export, and a static HTML zine preview (`zine_demo_view.html`).
   * [`tests/test_kernel.py`](./tests/test_kernel.py): Automated unit tests verifying the state transitions and permission boundaries of the Stage-1 kernel.
2. **Founder-Confirmed Direction (`[FOUNDER_CONFIRMED]`):**
   * Unified company identity under **Robotic Discipline**.
   * Exclusion of unrelated housing documents from this product scope.
   * Priority on user-owned memory, explicit consent before storing or sharing facts, local-first/offline-capable architecture, and tangible character interfaces.
   * Active preparation for the **SCAD Accelerator** (application deadline noted in transcript as November 15; callback December 2; March Showcase; May Demo Day) and **SCAD Pro** entrepreneurial branding ecosystem.
3. **Historical Proposals & Roadmap Hypotheses (`[PROPOSED]`):**
   * 12 founding characters across 4 factions on a 6-month wave cadence over 6 years (~1,100 skills).
   * Custom hardware docks, removable hardware cartridges, 3D-printed shells, and robotic body transfers.
   * Litecoin / LitVM smart contracts, NFT provenance, and parent-child creator royalties.
   * Delaware PBC + Founder Trust + Wyoming DUNA / DAO legal hybrid.
   * *The Book of Robotic Discipline* (18 Laws field manual and 10 startup worksheets).
   * Shared neighborhood robotics, wet-lab cooperatives, sustainable data centers, and orbital/space biology extensions.

---

## 3. Reading Order by Role

* **If you are KJ (Founder):**
  1. Review [`DECISIONS.md`](./DECISIONS.md) to settle the **#1 Open Strategic Question** (selecting the primary Day-1 wedge for the SCAD Accelerator application and first 10 customer tests).
  2. Review [`accelerators/SCAD-ACCELERATOR-PREP.md`](./accelerators/SCAD-ACCELERATOR-PREP.md) for your written answers and two conversational video scripts.
* **If you are an Engineer or AI Coding Agent:**
  1. Read [`ARCHITECTURE.md`](./ARCHITECTURE.md), [`SECURITY.md`](./SECURITY.md), and [`PRIVACY.md`](./PRIVACY.md).
  2. Inspect [`skeleton/interfaces.py`](./skeleton/interfaces.py) and run `python3 -m unittest discover -s tests` before writing any code.
  3. Enforce strict TDD: **Failing test → Minimum implementation → Passing test → Refactor → Document.**
* **If you are an Accelerator Coach, Professor, or Investor:**
  1. Read [`COMPANY-IDENTITY.md`](./COMPANY-IDENTITY.md) and [`PRODUCT-VISION.md`](./PRODUCT-VISION.md).
  2. Read [`RESEARCH-QUESTIONS.md`](./RESEARCH-QUESTIONS.md) for the academic HCI and embodied-AI framing.
  3. Read [`BUSINESS-MODEL.md`](./BUSINESS-MODEL.md) and [`EVALUATION.md`](./EVALUATION.md) for transparent unit economics and risk scoring.
