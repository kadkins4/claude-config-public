---
name: visual-recap
description: Render a code change as a visual, browser-served recap — Before/After headline, outcome narrative, data-model/API summary, file map, and tabbed key-change diffs — instead of terminal text. Use after finishing work or when Kenny wants to see, review, or summarize a PR, branch, or diff visually. Triggers include "visual recap", "recap this", "recap PR <n>", "show me what changed", or any change he should review in the browser rather than the terminal.
disable-model-invocation: true
---

# Visual Recap

Turn a code change into a single self-contained HTML document, served live in the browser. The inverse of [[visual-plan]]: a plan looks forward, a recap looks back. The _reading-the-diff brains_ come from `gh` / `git` plus skills like `write-summary` and `code-review` — this skill only owns the **visual rendering and serving**.

## When to Use

- After finishing a feature/fix and Kenny wants to **see, review, or summarize** what changed before pushing or merging.
- Recapping a specific PR (his or a teammate's), or self-reviewing his own branch.
- **Skip it** for trivial diffs (typo, one-line fix) — just describe the change in a sentence. A recap must be substantial enough to earn the surface.

## Resolve the Input (auto-detect)

Recap **whatever changes are actually there**. Resolve in this order:

1. **PR number or URL given** → `gh pr diff <N>` (and `gh pr view <N>` for title/status/stats).
2. **No arg** → recap the pending delta on the current checkout, first non-empty wins:
   - Uncommitted working changes present → `git diff HEAD` (staged + unstaged).
   - On a feature branch → `git diff <base>...HEAD` (base = `main`/`master`/repo default).
   - On `main`/default with unpushed commits → `git diff @{upstream}..HEAD` (fallback `git diff origin/<default>..HEAD`).
3. Get stats with `git diff --stat` (or `gh pr view`). If the resolved diff is empty, say so — don't fabricate a recap.

## Workflow

1. **Resolve and read the diff** (above). Read the actual hunks and changed files — ground every claim in the real diff; never invent files, symbols, or behavior.
2. **Read `template.html`** in this skill folder — it holds the styling and one example of every block, including the clickable tabs.
3. **Compose the recap.** Copy the template, fill the blocks that apply, delete the rest. Block vocabulary + budgets below.
4. **Save** to `~/.claude/prototypes/recap-<slug>/index.html` (durable, not a job temp dir).
5. **Serve it live** via the `serve-prototype` skill:
   `bash ~/.claude/skills/serve-prototype/serve.sh ~/.claude/prototypes/recap-<slug>/index.html`
   Give Kenny the printed `http://127.0.0.1:<port>/...` URL.
6. **Report briefly in chat** what the recap covers (files, +/−, headline change) so it's useful even before he clicks.
7. **On revisions**, overwrite the same file and tell him to refresh — the detached server survives.

## Block Vocabulary & Budgets

Use only blocks that earn their place. Default order, top to bottom:

| Block                | When                       | Rule                                                                                                                                                                                                                                              |
| -------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Header**           | always                     | Title (≤70 chars), status pill (Merged / Open PR / Local branch), file count, `+adds / −dels`, project.                                                                                                                                           |
| **Before / After**   | the headline               | The recap's center of gravity. UI change → before/after wireframe frames. Schema/contract change → two labeled columns (old shape vs new). Show exact placement; for a flow, show entry → opened surface → result, not just the first affordance. |
| **Narrative**        | always                     | 1–3 short paragraphs: what changed, why, and any hard-to-reverse decision that got locked in.                                                                                                                                                     |
| **Data model / API** | schema or contract changes | Table or before/after columns. Mark PUBLIC ids.                                                                                                                                                                                                   |
| **File map**         | multi-file change          | Tree with `new`/`edit` tags and per-file `+/−` stats.                                                                                                                                                                                             |
| **Key changes**      | always                     | Horizontal **tabs** of focused `diff` blocks. **3–8 tabs.** Each gets a one-line summary + annotations on the load-bearing hunks. Keep each excerpt **under ~150 lines** — summarize/link the rest, never dump a whole file.                      |

**Substantial, not sparse, not a dump.** Fewer than 3 key-change tabs on a large change under-serves the reviewer; a single unsegmented diff dump is worse. Segment and annotate.

## Notes

- **No hosted service, no auth, no lock-in** — recaps are local HTML files, git-able if Kenny wants a checked-in artifact.
- Matches the [[visual-plan]] visual language so a feature's plan and recap read as a set.
- Honor Kenny's standing prefs (full player names on On The Clock, card motif for Ricochet Rogue UI, no slot-machine animations).
- **Gap:** no inline reviewer comments (the one thing the hosted Builder.io version does). Flag it if stakeholder annotation on specific hunks is needed.
- **Security:** never paste secrets/tokens/keys from the diff into the recap; redact them.
