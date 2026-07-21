---
name: write-summary
description: Use when a bug fix, refactor, or code change is complete and the user asks for a summary, explanation doc, or .md writeup of what was done and why.
---

# Write Summary

Generate a concise .md doc explaining a completed code change. Be terse — sacrifice grammar for concision.

## Structure

Three sections, no more:

### Problem

What was broken. Include symptoms, affected platforms/browsers, and when it manifests. 1-3 sentences max.

### Root Cause

Why it was broken. Include the specific code/pattern that caused it. Show the offending code snippet if short. Keep technical but brief.

### Fix

What changed and why this approach. Bullet the behavioral outcomes (e.g. "no event selected → list full width"). Mention what was considered and rejected only if it adds clarity.

## Rules

- **Concise over grammatical.** Fragments ok. Drop articles, filler, transitions.
- **No preamble.** Jump straight into the problem.
- **Code snippets only when they clarify.** Don't paste entire files.
- **Place the doc next to the changed code.** Name it after the component/module (e.g. `EventsGrid.md`).
- **No headings beyond the three sections** unless the fix is multi-part.
- **Target: <200 words total.** If you need more, you're over-explaining.
