---
name: take-home-strategist
description: Use when the user has a real take-home assignment or system-design assessment from a company and wants help scoping and planning it — "I have a take-home", "what are they actually testing?", "lay of the land then a plan, don't code yet", or prepping to defend it (Loom/walkthrough). Not for practice rigs (use interview-rig-builder) or algorithm drilling (use leetcode-coach).
disable-model-invocation: true
---

# Take-Home Strategist

## Overview

A take-home is graded on one or two axes that the prompt rarely states outright. The user's first ask is almost always **"what are they actually testing?"** — answer that before anything else. The build is downstream of the diagnosis.

This skill does the analysis AND the implementation planning (unlike `leetcode-coach`, which withholds answers).

## The Spine

1. **Find the graded axis.** Read the prompt for what they reward, not what they list. Tells:
   - Tight time box + vague requirements → they're grading **scoping and judgment**, not completeness.
   - "Walk us through your reasoning" / Loom / live review → they're grading **how you defend it on camera**, so the README and commit story matter as much as the code.
   - Cost/scale language in a system-design prompt → they're grading **cost discipline and tradeoff reasoning**.
   - A deliberately under-specified spec → they're grading whether you **ask the right questions / state assumptions**.
     State the axis with a confidence tag. This is the highest-value output.

2. **Cut to the graded axis.** Drop anything that doesn't move the grade. Name what you're cutting and why, so it's a defensible choice, not an omission.

3. **Scope the deliverable.** Smallest thing that demonstrates the graded axis convincingly. Tiered if time allows (must-have → if-time).

4. **Plan in isolation — do NOT start coding.** Set up a worktree + branch, write the plan, and stop at the plan. The user says "go" before implementation. (If other agents share the repo, diff their branches first to avoid colliding on the same files.)

5. **Prep the defense.** If there's a walkthrough/Loom, draft the 3–4 talking points: the graded axis, the key tradeoff, what you cut and why, what you'd do with more time.

## When NOT to use

- It's a LeetCode-style algorithm screen → `leetcode-coach`.
- It's a fake practice repo the user wants built for drilling → `interview-rig-builder`.

## Red Flags — stop and fix

- You started scaffolding code before stating the graded axis and getting "go".
- You aimed for feature-completeness when the prompt was grading judgment.
- You planned in the shared working tree instead of an isolated branch.
