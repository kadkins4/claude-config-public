---
name: visual-plan
description: Render a plan as a visual, browser-served document — flow diagram, step cards (reuse-first), file map, annotated diff, data model, and open questions — instead of terminal text. Use after brainstorming/writing-plans whenever Kenny wants to see, review, or approve a plan visually before any code is written. Triggers include "visual plan", "show me the plan", "render the plan", or any plan he should review in the browser rather than the terminal.
---

# Visual Plan

Turn a plan into a single self-contained HTML document, served live in the browser. The planning _brains_ come from `superpowers:writing-plans` or `superpowers:brainstorming` — this skill only owns the **visual rendering and serving**.

## When to Use

- After producing a plan with `writing-plans` / `brainstorming` and Kenny needs to **see, review, or approve** it before code.
- Any non-trivial UI / state / workflow / backend change where a diagram, file map, or open-questions block makes the plan legible.
- **Skip it** for truly trivial work (typo, one-line fix, a single well-specified function) — just make the change. Never pad a plan with filler. Never render a single-step plan.

## Workflow

1. **Plan first, render second.** Get the plan content from `writing-plans` or `brainstorming` (research the real files, name actual symbols and data shapes — don't invent them). Planning is **read-only**: make no source edits while building the plan.
2. **Read `template.html`** in this skill folder — it holds the styling and one copy-paste example of every block.
3. **Compose the document.** Copy the template, fill in only the blocks that apply, and delete the rest. Block vocabulary below.
4. **Save** to `~/.claude/prototypes/<plan-slug>/index.html` (durable, not a job temp dir).
5. **Serve it live** via the `serve-prototype` skill:
   `bash ~/.claude/skills/serve-prototype/serve.sh ~/.claude/prototypes/<plan-slug>/index.html`
   Give Kenny the printed `http://127.0.0.1:<port>/...` URL.
6. **The plan is the approval gate.** Ask Kenny to review and approve, and name which files/areas the work touches. Don't ask a separate "does this look good?" — presenting the plan _is_ the sign-off request.
7. **On revisions**, overwrite the same file and tell him to refresh — the detached server survives. Keep the document standalone (a reader who never saw the chat should understand it); don't write it as a diff against an earlier draft.

## Block Vocabulary

Use only the blocks that earn their place. Order is flexible; this is a sensible default.

| Block              | When                               | Rule                                                                                                                                                                                                            |
| ------------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Header**         | always                             | Title, status pill, scope pills, one-line scope with explicit **out of scope**.                                                                                                                                 |
| **TL;DR**          | non-trivial plans                  | 2–3 sentences. Lead with what it _reuses_ before what it adds.                                                                                                                                                  |
| **Flow diagram**   | multi-step interaction / data flow | Hand-drawn CSS nodes + arrows. No mermaid / CDN — keep it self-contained.                                                                                                                                       |
| **Step cards**     | always                             | Each step names **Reuses** (existing actions/components/helpers) _before_ **Adds** (the genuinely new delta). This is the most important discipline — it stops the plan re-describing code that already exists. |
| **File map**       | any multi-file change              | Tree with `new` / `edit` tags, color-coded.                                                                                                                                                                     |
| **Annotated diff** | when there's a hard-to-reverse bet | Show the wire format / public id / data shape / auth boundary and call it out inline. Get these right in the plan even if the rest ships later.                                                                 |
| **Data model**     | new/changed records                | Table: field · type · notes; mark PUBLIC ids.                                                                                                                                                                   |
| **Open questions** | any unresolved decision            | One block at the **bottom**. Each question lists options with a **recommended** default pre-selected. Only include a question if the answer would change the design and you can't resolve it from the code.     |

## Notes

- **No hosted service, no auth, no lock-in** — plans are local HTML files, git-able if Kenny wants a source-controlled artifact.
- Match the target app's theme when relevant (pull real color tokens/fonts) so the mockup reads true.
- Honor Kenny's standing preferences inside plans: full player names (On The Clock), append larger changes to the in-app Change Log, include a card-themed variant for Ricochet Rogue UI, never propose slot-machine animations.
- This skill does **not** support inline reviewer comments (the one thing the hosted Builder.io version does). If Kenny needs stakeholder annotation on specific blocks, flag that gap.
