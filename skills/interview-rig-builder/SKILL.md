---
name: interview-rig-builder
description: Use when the user wants a practice take-home scaffolded so they can drill AI-assisted coding interviews — "build me a practice take-home", "set up an interview-practice repo", "spin up a repo to practice my AI interviewing", "make me an assessment drill". This builds a FAKE assignment to practice on; for a REAL company take-home use take-home-strategist.
disable-model-invocation: true
---

# Interview Rig Builder

## Overview

The user practices AI-assisted coding interviews by working real-feeling take-homes under time pressure. This skill scaffolds the **simulator**: a production-realistic repo with PM-style tickets and deliberate traps, that builds green cold but is missing the features the tickets ask for.

The point is to make them practice the skills a real take-home tests — deriving scope, spotting hidden requirements, sequencing work — so the rig must NOT do those things for them.

## Build Contract

**Tickets:**

- PM format: each ticket has **context/problem + acceptance criteria**. Describe the outcome, not the implementation.
- **NO "depends on" / dependency field.** Working out the dependency graph is part of the drill — never hand it to them.
- Tag **complexity** (S/M/L or 1–5), **never time estimates**.
- ~6–8 tickets is a good batch.

**Planted traps** (the part that makes it real — don't skip):

- A hidden requirement buried in prose, not in the acceptance criteria.
- Dependency-blindness bait: two tickets that look independent but collide.
- A README/answer-key detail that's subtly wrong or a red herring.
- Keep them small — "force you to pay attention," not "impossible."

**Baseline repo:**

- Deliberately **missing the features the tickets ask for** — that's their job to add.
- But **green cold**: build, lint, types, and tests all pass on a fresh clone with nothing implemented yet.
- A monorepo with realistic structure if the practice domain warrants it.
- Land it as a **single atomic commit**.

## Verify Before Handing Over

Clone/checkout fresh and confirm it's **green cold** — build, lint, typecheck, test all pass with zero feature work done. If anything's red on a clean checkout, the rig is broken; fix before handing it over. Do not leak the trap list to the user.

## Red Flags — stop and fix

- You added a "depends on" field or otherwise pre-solved the sequencing.
- You used time estimates instead of complexity tags.
- The baseline already implements what the tickets ask for.
- The repo isn't green on a cold clone.
- No traps planted (then it's not practicing anything).
