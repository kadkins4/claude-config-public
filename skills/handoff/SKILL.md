---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: What will the next session be used for?
disable-model-invocation: true
---

# Handoff

Write a handoff document summarising the current conversation so a fresh agent can continue the work with no prior context.

## Where to save

Save to the OS temp directory — **not** the current workspace.

- Resolve the temp dir at runtime: `echo "${TMPDIR:-/tmp}"` (macOS uses `$TMPDIR`, Linux falls back to `/tmp`).
- Name it discoverably: `handoff-<topic>-<YYYYMMDD-HHMM>.md`.
- Print the absolute path when done so the next session can find it.

## What to include

1. **Goal** — what the work is trying to achieve. If arguments were passed, treat them as the focus of the next session and tailor the whole doc toward that.
2. **Current state** — what's done, what's in progress, what's verified vs. assumed.
3. **Next steps** — the concrete first actions the next agent should take.
4. **Key context** — decisions made, constraints, dead-ends already ruled out, gotchas not obvious from the code.
5. **Suggested skills** — skills the next agent should invoke, by name, with when to use each.
6. **References** — paths/URLs to related artifacts.

## Also emit a kickoff prompt (always)

After writing the doc, **output a short, ready-to-paste prompt** for launching the next agent — Kenny asks for this every time, so produce it by default without being asked. It should:

- point the next agent at the handoff doc by absolute path,
- name the **first concrete action** to take,
- list the skills to invoke (mirror the Suggested skills section),
- include the workspace path and tell the agent to **verify it before working** (stale duplicate clones exist — confirm the right one).

Put it in a copy-paste code block so Kenny can grab it directly.

## Sibling-session sync

Handoff isn't only fresh-agent pickup — Kenny also uses it to **pass status back to an existing long-lived session** ("create a handoff so I can pass it back to my other session to update"). When that's the intent, lead with the _deltas_ (what changed since they last knew) rather than full from-scratch context.

## Suggested skills section

List skills by name with a one-line reason/trigger. Pick ones relevant to the work in progress and the stated focus of the next session. Example:

```markdown
## Suggested skills

- `superpowers:test-driven-development` — before writing any implementation code
- `code-review` — review the diff before merging
```

## Do not

- **Don't duplicate** content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.
- **Don't leak secrets.** Redact API keys, passwords, tokens, and PII before writing the file.
