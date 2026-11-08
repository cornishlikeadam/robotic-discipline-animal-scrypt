---
name: software-factory
description: Garry Tan gstack-inspired software factory (/plan-ceo-review, /plan-design, /plan-eng-review, /qa, /ship) with strict Red-Green-Refactor TDD for Animal Scrypt (Robotic Discipline).
---

# Animal Scrypt Software Factory (`/factory`)

Read [`/seed/00-context.md`](../../seed/00-context.md), [`/seed/nda-status.md`](../../seed/nda-status.md), and [`/seed/25-factory.md`](../../seed/25-factory.md) before writing or editing any code.

## Pre-Code Gate (Never Skip)
1. **Brainstorm (`/plan-ceo-review`):** Clarify with the founder until the user story is one paragraph. Cut anything outside the 7-checkbox MVP (`00-context.md`). You are allowed to say "do not build this."
2. **Spec (`/plan-design` + `/plan-eng-review`):** Write the spec (cream `#EFE6D4`, lime `#D8FF3E`, ink `#101419`, database schema, NDA lock, and small tasks with test names). **Stop and wait for founder approval.**
3. **Strict TDD:**
   - Write a failing test first.
   - Write the minimum code to make it pass.
   - Refactor only while tests stay green.
4. **QA & Ship (`/qa` + `/ship`):** Test in a real execution environment or browser, log reproduction steps for any bug, and list what was NOT tested in the release note.
