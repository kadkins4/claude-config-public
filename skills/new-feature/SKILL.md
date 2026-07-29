---
name: new-feature
description: Use when Kenny wants to build a new feature for an existing codebase end-to-end — "I need this new feature", "start the feature pipeline", or any feature big enough to deserve a spec before code.
disable-model-invocation: true
---

# New Feature Pipeline

Run these phases in order. Each phase invokes an existing skill — this skill only sequences them. Don't skip a phase without Kenny's explicit ok.

**Invoking the sub-skills:** several are marked `disable-model-invocation: true`, so the Skill tool refuses them. For those, `Read` `~/.claude/skills/<name>/SKILL.md` and follow it inline. Marked ⟨read⟩ below.

1. **Grill** — ⟨read⟩ `grill-with-docs` (repos with domain docs or that deserve them) or `/grill-me` (throwaway/small repos). Hard stop-gate: do not proceed until Kenny confirms shared understanding.

2. **Spec** — ⟨read⟩ `to-spec` → `.scratch/<feature-slug>/spec.md`. Pure synthesis; no re-interviewing.

3. **Tickets** — ⟨read⟩ `to-tickets` → `.scratch/<feature-slug>/issues/`. Iterate the breakdown with Kenny until approved.

4. **Approval gate** — `/visual-plan`: render the spec + ticket graph in the browser. Kenny approves here before any code.

5. **Handoff** — after approval, ⟨read⟩ `handoff` and write it to `.scratch/<feature-slug>/handoff.md`. Capture what the spec does NOT hold: rejected alternatives, constraints discussed in grilling, Kenny's stated preferences. The kickoff prompt must point at `spec.md`, `issues/`, and `handoff.md`.

6. **Implement** — work the ticket frontier (any ticket whose blockers are done):
   - Continuing in this session → superpowers:subagent-driven-development, one ticket = one unit of work.
   - Fresh session later → start from the kickoff prompt, then superpowers:executing-plans over the tickets.
   - Either way: superpowers:test-driven-development per ticket; isolate in a worktree; ff-merge each verified ticket to local main; never push (Kenny merges manually).

7. **Wrap** — superpowers:verification-before-completion (evidence before "done"), then `/code-review`, then ⟨read⟩ `visual-recap`.

**Escalation valve:** if grilling reveals the effort is too big for one session to plan, switch to ⟨read⟩ `wayfinder`. Each region of the map it resolves re-enters this pipeline at phase 2.
