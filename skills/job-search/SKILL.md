---
name: job-search
description: Use at the start of a job-application triage session, or whenever the user pastes/links a job listing or forwards a rejection email during an active job search. Drives the whole loop — dup-check, fit rundown, wait-for-decision, log the application as its own note, process rejections, keep the counts right.
disable-model-invocation: true
---

# Job Search — Session Orchestrator

Single entry point for job-application triage. Run this and it drives the loop for every listing and rejection the user throws at you. Delegates fit-analysis internals to **job-posting-analysis** — it is `disable-model-invocation: true`, so `Read` `~/.claude/skills/job-posting-analysis/SKILL.md` and follow it inline rather than calling the Skill tool; this skill owns the _session flow_ and the _file mechanics_.

**First step, always:** `Read` `~/.claude/skills/job-search/user-context.md`. It holds the facts this loop depends on — employment status, location/domain constraints, real vs. claimed framework experience, tracker conventions, the display format, and the known ghost/PERM listings. It is the canonical home for those facts; when one changes, edit that file rather than writing a memory. **If it is still the unfilled template, stop and fill it in with the user before triaging anything** — every filter below reads from it.

## Structure (read this before writing anything)

Base folder: the `JOB_SEARCH_DIR` value in `user-context.md` (an Obsidian vault folder works well, but any markdown folder does). Referred to as `$BASE` below.

**One application = one note.** There is no big table to edit.

| Path                                                | What it is                                                                                                                                            |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Job Search Home.md`                                | Entrance. Counts, live pipeline, leads, weekly ritual. **No watchlist content** — that belongs in Board Watchlist.                                    |
| `Companies/<Company>/`                              | One folder per company. Holds its application note(s) **and** all its prep.                                                                           |
| `Companies/<Company>/<Company> — <Role> (<M-D>).md` | **The application.** Its frontmatter IS the table row.                                                                                                |
| `Applications.base`                                 | Obsidian **Bases** view that renders the table live from those frontmatters. Never hand-edit rows. (Optional — skip if not using Obsidian.)           |
| `Application Tracker.md`                            | Thin note: embeds the Bases view + status legend + the frontmatter schema.                                                                            |
| `Board Watchlist.md`                                | Companies to scan later (ATS sweep method, industry sweeps). Not applications.                                                                        |
| `Interview Prep.md`                                 | **Universal prep only.** No company list — the `Companies/` folder is the index. Never rebuild a name list here.                                      |
| `Companies Index.md`                                | **Generated** navigation index — all company folders grouped by status, leading with the ones that hold prep docs. Never hand-edit; re-run the script. |

**Resume (source of truth):** the `RESUME_PATH` in `user-context.md`. If the user keeps several variants (see `user-context.md` → Resume variants), every rundown ends with which one to send.

If the folder is cloud-synced markdown rather than a git repo, and the filesystem is **case-insensitive** (macOS default) — check for an existing folder before creating one that differs only by case.

> [!warning] Never put applications back into a table, and never put watchlist companies or prep into `Application Tracker.md`. A single monolith tracker file gets unusable past a couple hundred applications; that is why it is split this way.

**`Applications.base` views** (7): All applications · By status (grouped — the counts come from here) · Live pipeline · **Oldest silent (chase or close)** (Applied, oldest first — the weekly-review view) · Applied (awaiting reply) · Rejected · Passed. Point the user at a view rather than recomputing something the base already shows.

> [!danger] Editing `.base` files — one bad view kills the entire file
> A single malformed view makes Obsidian refuse to parse the whole base, and the error then appears **everywhere it is embedded**, so a bad guess takes the tracker down. **Never experiment in `Applications.base`** — put the experiment in a separate, un-embedded `.base` and open that directly.
>
> Verify syntax against the installed Obsidian's validator (`obsidian-<version>.asar` in `~/Library/Application Support/obsidian/`, grep for the key name — that is the ground truth, do not guess). Known as of Obsidian 1.12:
>
> - `groupBy` must be an object with **both** `property` and `direction`; `direction` must be exactly `ASC` or `DESC`. `groupBy: status` and a `property`-only object both throw.
> - Obsidian **rewrites the file on load**, normalizing `note.foo` → `foo` in `order:` and `sort:` while keeping the `note.` prefix in `filters:` and `properties:`. Match that convention; do not "fix" it back.

⚠️ **If a PreToolUse hook drops a `.bak` beside any file the Write tool fully rewrites**, prefer Edit for patches; if you do use Write, delete the `.bak` afterward or it accumulates as clutter.

## The loop (per listing)

```
paste/link → RULE 0 dup-check (blocking) → read the JD → (research ONLY if close + one unknown decides it) → rundown → WAIT → user says apply/skip → log or don't
```

1. **RULE 0 — dup-check FIRST, ALONE, AND BLOCKING.** Before any analysis, check **all three**:

   ```bash
   ls "$BASE/Companies" | grep -i "<company>"        # already applied? (folder = company)
   grep -ril "<company>" "$BASE/Companies" | head    # catches name variants inside notes
   grep -i "<company>" "$BASE/Board Watchlist.md"    # already scouted / already skipped, and why
   ```

   A hit in `Companies/` means they applied. A hit in `Board Watchlist.md` means we already scouted them and may have recorded a reason to skip. Report status + date + which file before continuing.

   ⚠️ **Do NOT parallelize the dup-check with anything else.** It is a _gate_. Fire it in its own tool block and wait. Failure mode seen in practice: dup-check and a company WebSearch fired in the same parallel block, and the search ran for a company the user had already applied to 8 days earlier. Speed is not worth breaking the gate.

2. **Read the JD and score it against the standing filters.** Level, stack, comp, location, domain. Most listings die here and need zero outside research. A light pass is the default (see Research depth below).

3. **Research only if the listing is genuinely close AND one specific unknown decides it** (unposted comp on a strong fit, ghost-listing doubt, "is remote actually remote," an ambiguous domain/values question). Scope it to that question. If a pass will run long, say so up front.

4. **Rundown** — the fit read (see Rundown format).

5. **WAIT.** Write nothing until the user says "apply" / "applied" / "skip". Hard gate.

6. **On "applied"** → create the application note, then bump counts in `Job Search Home.md`.
   **On "skip"** → usually **nothing**. Only create a note with `status: Passed` if asked to log the skip. If they're worth revisiting, that goes in `Board Watchlist.md`.

### Research depth

Default to a **light** research pass. Do not fire a deep-dive subagent on every posting — most listings end in a fast skip and the user is left waiting mid-triage.

- **Light pass is the default.** Read the JD, dup-check, apply the standing filters, give the rundown. If the listing fails a hard gate — wrong level, wrong stack, sub-floor comp, no-go domain, on-site — kill it from the JD alone.
- **Escalate only when the listing is genuinely close** and a specific unknown would change the decision.
- **Scope the escalation.** Research the one or two questions that matter, not a ten-section company brief.
- Durable findings go in the application note so they never need re-running.

## Logging (only after "applied")

### Step 1 — create the application note

Path: `Companies/<Company>/<Company> — <Role short> (<M-D>).md`

Company folder = the plain company name, no blurb, `/` replaced with `-`. Repeat applications = more files in the same folder. If the folder exists, use it.

```yaml
---
tags: [career, job-search, application]
company: "Acme"
company_full: "Acme (what they do; stage)"
role: "Senior Frontend Engineer"
role_detail: "full role line from the JD"
applied: 2026-07-26
status: "Applied"
status_detail: "Applied" # free text when the status carries nuance
resume: "A" # which variant was sent, if the user keeps several
fit: "🟢" # 🟢 clears · 🟡 stretch · 🔴 fail · ⚪ unknown
comp: "**$170K-$210K** (clears floor)"
link: "https://…"
---
```

Body: `## Fit read` (the same dot-list you showed them) · `## Comp` · `## Notes / next action` (what was actually submitted + `IF SCREEN:` reminders) · `## Link`.

The `tags` line must include `application` — that is what the Bases view and the index script filter on. Miss it and the row silently vanishes from the table.

### Status vocabulary — these ten values, nothing else

**Open:** `To-Apply` · `In progress` · `Applied` · `Interviewing` · `Offer` · `Waitlisted`
**Closed:** `Rejected` (**THEY** said no) · `Passed` (**I** said no, and recorded why)
**Bookkeeping:** `Superseded` (old note when a req is reposted/re-leveled) · `Lead` (never counted in Applied)

`Rejected` covers a silent close **only when there is affirmative evidence they moved on** (req reposted, role filled, "we hired someone") — put the evidence in `status_detail`. Mere silence is not a rejection.

⛔ Do not add a `Ghost` / `Ghosted` status — silence is not quantifiable and there is no honest moment to set it. A fake/non-existent req is `Passed`. Any value outside the ten is a bug: no filtered view catches it, so the row vanishes from everything except "All applications."

### Step 2 — re-derive the counts, then reconcile `Job Search Home.md` to them

**Never hand-tally, and never decrement the number sitting in the table.** Run the script — it walks every note's frontmatter and prints exactly what Home must say:

```bash
JOB_SEARCH_DIR="$BASE" python3 ~/.claude/skills/job-search/scripts/build_index.py 2026-08-01   # pass today's date
```

It regenerates `Companies Index.md` **and** prints a reconciliation block: total tracked, a line per status, the 🔥/🧊 split, plus a ✅/🛑 check that every status is inside the ten-value vocabulary and that no `Applied` note is missing its `applied:` date. Pass `--counts-only` to skip writing the index.

Then reconcile the `## 📊 At a glance` table to that output with **Read + Edit**, exact-string replace. Never awk it.

- `**N tracked**` → the script's number, and update the `(as of YYYY-MM-DD)` stamp.
- The matching row: `| 📮 Applied — submitted, no outcome | N |` → the script's number. **Match the full row label**, it is not just "Applied".
- **Both 🔥 and 🧊 come from the script, every time** — they decay daily with no edit event, so a new application is not simply "+1 to 🔥".
- If pipeline state moved, update the `## 🎉 Live pipeline` prose too — that is what the user actually reads.

> [!warning] `Applied` is a historical count, not a pipeline count
> It means "submitted, no outcome recorded." The two derived rows below it (🔥 fresh / 🧊 21+ days silent) are the real pipeline picture, and **they decay every day** — they are only true as of the stamped date. Dozens of applications can cross the 21-day line in a single quiet week with no event of any kind. **The script exists so this is never estimated.**

> [!info] The index counts companies; Home counts applications. They will not match.
> A company applied to twice is filed in the index under its **liveliest** status. Both are right; they answer different questions. The script's reconciliation block always prints **application** counts, which is what Home wants.

**One seat = one count.** If a company reposts a req the user already applied to, set the old note's status to `Superseded` rather than adding a second Applied.

### Step 3 — regenerate the index

Already done if you ran the script in Step 2. `Companies Index.md` is a **cache with a date stamp on it**, so a status flip that does not regenerate leaves it quietly wrong. Any session that changes a `status:` regenerates.

### Where other things go

- **Worth scanning later, not applying now** → `Board Watchlist.md`.
- **Prep for a company that responded** → `Companies/<Company>/<Company> — Interview Prep.md`, with round cheat sheets and debriefs alongside it (see the `interview-prep` skill).

## Rejections

1. Find the note: `ls "$BASE/Companies/<Company>/"`.
2. Edit its frontmatter: `status: "Rejected"`, and set `status_detail` to the stage it died at ("pre-screen, no human contact", "post-R1", "post-screen before HM round").
3. Prepend `REJECTED M/D` + cause to the top of `## Notes / next action`.
4. **Run the script** (Step 2 above) to re-derive the counts and regenerate `Companies Index.md`.
5. Reconcile `Job Search Home.md` to the script's output — **do not decrement by hand.** Also add a clause to **Recent rejections**, and remove it from `## 🎉 Live pipeline` if it was there.
6. Confirm the flip in one line.

⚠️ **A rejection out of the 🧊 bucket is normal and is not a late surprise.** Companies batch their rejections; letters at 3–5 weeks of silence are routine. **🧊 means "no letter yet," not "closed"** — which is the whole reason silence alone never sets `Rejected`.

**A silent close is not automatically a rejection.** Only set `Rejected` when there is affirmative evidence they moved on — req reposted, role filled, an explicit "we hired someone." Put that evidence in `status_detail`. If all you have is silence, the note stays `Applied` and its age carries the meaning.

## Rundown format

Delegate fit logic to **job-posting-analysis** (`Read` `~/.claude/skills/job-posting-analysis/SKILL.md`), present it this way:

1. **One-line company blurb** (what they do / stage).
2. **Scannable dot-list**, not prose: `CATEGORY 🟢/🟡/🔴/⚪ → terse reason`. 🟢 clears · 🟡 stretch · 🔴 fail · ⚪ unknown (pull it).
3. **Red-flags** section (terse; omit tells that don't apply).
4. **Close with the recommendation + which resume variant** (if the user keeps several). Last line they read.

**NO recruiter-questions section in the rundown.** Surface tailored questions ONLY when a recruiter actually reaches out.

## Standing filters (apply in every rundown)

All of these read from `user-context.md`. The shape:

- **Location:** score it every time. 🟢 matches the user's remote/hybrid/onsite preference · 🟡 hybrid in one of their acceptable cities · 🔴 elsewhere. Residency gates that exclude the user's state are a hard fail. Watch the **application form**, not just the JD — relocation gates sometimes appear only in the form.
- **Comp floor:** the number in `user-context.md`. Anchor to the top of _their_ range; never reveal the floor. Flag under-floor comp.
- **Contract / C2C / staffing-intermediary roles are NOT an auto-skip.** Score the listing normally on every other axis, then **flag the contract terms explicitly** — W2 vs C2C, duration, benefits (or their absence), whether comp is hourly, and whether an intermediary is taking a margin on an unnamed end client. Price it honestly against the FTE floor: no benefits/PTO/401k match means the effective rate has to run meaningfully above it.
- **Domain no-gos:** the user's hard-no and likely-no list. Hard-no → lead with it and recommend skip without a full work-up. Likely-no → name it up front and ask rather than assume.
- **Stack claims:** only what `user-context.md` and the resume back. Never imply depth the user can't defend.

## Red flags — stop

- You analyzed before dup-checking, or you dup-checked only one of the three places.
- You wrote anything before the user said "apply". The wait-gate is hard.
- You created an application note without the `application` tag (it vanishes from the Bases view and the index).
- You rebuilt a flat table anywhere, or hand-typed a list of company names into `Interview Prep.md`.
- You set a status outside the ten-value vocabulary, or introduced `Ghost`/`Ghosted`.
- You bumped a count in one place and left another stale.
- You hand-tallied or hand-decremented a count instead of running `scripts/build_index.py` and reconciling to it.
- You changed a `status:` and did not regenerate `Companies Index.md`, leaving a stamped file quietly wrong.
- You hand-edited `Companies Index.md` — it is generated output; fix the note's frontmatter and re-run.
- You put a recruiter-questions section in the rundown.
- You claimed a fit the resume doesn't back.
- You logged a skip without being asked.
- You ran triage against an unfilled `user-context.md`.
