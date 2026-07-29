---
name: prototype-fidelity
description: Use when Kenny wants an approved prototype or design handoff turned into the real app, or wants to compare the current UI against a prototype surface by surface — "move it to the real deal", "go 1 for 1", "make it match the prototype", "why is this different from the mockup", "show me ours vs the prototype". Complements serve-prototype (which only serves); this covers faithful porting and drift auditing.
disable-model-invocation: true
---

# Prototype Fidelity

## Overview

When Kenny approves a prototype, "port it" means **1:1, not 'inspired by'.** His recurring frustration is drift — colors, spacing, node structure, and animation silently changing during the port ("why did the color change to brown? it should be the blue we were using"). The job isn't done when it renders; it's done when it matches the source.

Two modes: **compare** (decide what to build) and **port + audit** (build it faithfully, then prove it matches).

## Mode A — Surface-by-surface comparison

When deciding a redesign one screen at a time, render three live options per surface and let Kenny pick:

- **A = Ours** — the _current_ app UI, rebuilt from its real CSS/tokens (not a guess).
- **B = Prototype** — the design prototype as-is.
- **C = Hybrid** — your invented mix of the two.

Serve them together via a hub `index.html` (use `serve-prototype`), and track locked picks in the hub ("Your picks: ① C, ② C, …"). Go surface by surface; lock each before moving on.

## Mode B — Faithful port + fidelity audit

1. **Capture the source first.** Before porting, record the prototype's exact tokens: colors, spacing scale, fonts, border-radius, animation names + timing, and DOM/node structure. This is your acceptance checklist.
2. **Port exactly.** Made-up/placeholder data is fine first pass; wire real data after. The _visual_ must match now.
3. **Preserve URLs.** If the restructure moves or renames routes, **redirect old paths — no broken links.** Point legacy headers/links at the new pages.
4. **Run the fidelity audit before declaring done.** Walk the captured checklist against the live result: colors match? spacing? animation timing? node structure? Serve both side by side (`serve-prototype`) if drift is suspected. List any deltas and fix them.

## Quick Reference

| Kenny says                                                     | Mode                              |
| -------------------------------------------------------------- | --------------------------------- |
| "show me ours vs the prototype", "A/B/C", "surface by surface" | A — comparison                    |
| "move it to the real deal", "go 1 for 1", "make that the page" | B — port + audit                  |
| "why is this different / why did X change"                     | B — run the audit, find the drift |

## Red Flags — stop and fix

- You ported from memory/eyeballing instead of capturing the source tokens first.
- You declared the port done without running the fidelity audit.
- "Ours" in a comparison was a guess, not rebuilt from the real CSS.
- A route moved and an old link now 404s.
