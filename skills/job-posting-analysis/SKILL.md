---
name: job-posting-analysis
description: Use when the user pastes or links a job listing and wants a read on it — "anything weird?", "thoughts on this listing?", "is this a fit?", "should I apply?". Produces a red-flag scan and a fit verdict. Not for writing the cover letter (use cover-letter), strategizing a take-home (use take-home-strategist), or running a full triage session incl. logging (use job-search, which calls this).
disable-model-invocation: true
---

# Job Posting Analysis

## Overview

The user is job-hunting and triages a lot of postings. For each one they want the fit read fast and scannable: **a one-line company blurb, whether it fits them, and what's off about the posting.** Be blunt — a posting that wastes their time should get called out as one. (This skill is the fit-analysis engine; **job-search** orchestrates the full session around it — dup-check, wait-gate, logging.)

**Read `~/.claude/skills/job-search/user-context.md` first.** It holds the resume path, the stack the user can actually claim, the location preference, the comp floor, and the domain no-gos. Source of truth for "fit" = the resume at `RESUME_PATH`. Don't claim a fit the resume doesn't back.

## Output Contract

Lead with a **one-line company blurb** (what they do / stage). Then two sections. Close with the recommendation + which resume variant (if the user keeps several) — that's the last line they read.

### 1. Fit — scannable dot-list

**Not prose.** Each line: `CATEGORY 🟢/🟡/🔴/⚪ → terse reason`. Dots: 🟢 clears · 🟡 stretch · 🔴 fail · ⚪ unknown (pull it). Always score **Location** and **Comp**. Say which requirements they clear, which are a stretch, and which they miss — **this is internal triage, naming gaps here is correct** (the opposite of the cover-letter rule). Never imply depth the user can't defend; score against what `user-context.md` says is real.

Example:

- **Stack** 🟢 core TS/React match
- **Location** 🟢 remote, no residency gate
- **Level** 🟡 Staff scope at Senior title
- **Comp** ⚪ not posted — pull it

### 2. Red flags

**Hard gates first — these kill a listing outright, score them before anything else:**

- **Domain no-gos:** the HARD NO list in `user-context.md`. LIKELY NO entries are a values flag, not an auto-kill — name it and ask.
- **Location:** the preference in `user-context.md`. A residency gate that excludes the user's state is a hard fail.
- **Comp floor:** the number in `user-context.md`. Anchor to the top of _their_ range; never reveal the floor.
- **PERM / labor-cert ads** (fake openings with someone already in the seat) — detection markers and the user's stance are in `user-context.md`.

Then scan for these tells (omit ones that don't apply — don't pad):

| Signal                                                                | What it usually means                                                   |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Staff/Lead duties at a Senior title or pay band                       | Scope/level mismatch — they want more than they're leveling for         |
| No salary range                                                       | **Pull the number in the recruiter screen before investing more time.** |
| Title says IC, body says manage/mentor a team (or vice versa)         | They haven't decided what the role is                                   |
| "Nice to have" duplicates "Qualifications", grammar breaks mid-bullet | Copy-paste / pasted from an internal leveling rubric — read what leaked |
| Stale stack naming ("AngularJS" not "Angular", "Redux" not "RTK")     | Codebase age / tech debt — grill on versions                            |
| Health/fintech app with no mention of HIPAA/SOC2/compliance           | Either early or careless — ask                                          |
| "U.S. citizenship required / ITAR / export control"                   | ≈ defense/gov contractor                                                |
| Private company touting equity                                        | Treat equity as illiquid / maybe-someday; value the cash                |
| No company name, equity-only comp, bare-email apply channel           | Possible ghost/scraped listing — check the domain resolves and the email doesn't bounce |

**NO recruiter-questions section in the rundown.** The rundown is blurb + fit + red flags + recommendation only. Surface tailored questions ONLY when a recruiter actually reaches out for a screen/interview, then flag them for the user to raise.

## Logging

**Don't log here.** The **job-search** skill owns the wait-gate and all file mechanics: never write anything until the user says "apply" / "applied", and a "skip" gets nothing unless they ask to log it.

There is **no markdown table**. Each application is its own note at `$JOB_SEARCH_DIR/Companies/<Company>/<Company> — <Role> (<M-D>).md`, and its frontmatter is the row; an Obsidian **Bases** view (`Applications.base`) renders the table live. Counts live in `Job Search Home.md`. If you're running this skill standalone, hand off to job-search for logging — don't improvise a file.

**Status vocabulary is fixed at ten values** — `To-Apply` · `In progress` · `Applied` · `Interviewing` · `Offer` · `Waitlisted` · `Rejected` (**they** said no) · `Passed` (**I** said no) · `Superseded` · `Lead`. There is no `Ghost` status; a fake or non-existent req is `Passed`. Anything outside the ten silently drops out of every filtered view.

⚠️ **RULE 0 still applies even standalone:** dup-check before analyzing. Check `Companies/` folder names, grep recursively inside `Companies/`, and grep `Board Watchlist.md` (already-scouted companies with recorded skip reasons never appear in the applications set).

## Red Flags — stop and fix

- You softened a real red flag to be nice. Don't — the point is to save their time.
- You claimed a fit not in the resume, or implied depth `user-context.md` says they can't defend.
- You wrote the fit read as prose instead of the scannable dot-list.
- You added a recruiter-questions section to the rundown.
- You skipped reading `user-context.md` and guessed at the filters.
