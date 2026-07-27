# Templates

Two documents: the **cheat sheet** (before) and the **debrief** (after).

The cheat sheet is read live, mid-call, under pressure. Optimize for retrieval, not completeness. Bold the sentence they actually have to say. Drop any section that does not apply — an empty section is worse than a missing one.

---

## Cheat Sheet

Filename: `<Company> R<n> — <Purpose>.md` (e.g. `Acme R1 — Recruiter Screen Cheat Sheet`).

```markdown
---
tags: [career, job-search-<year>, <company-slug>, <round-type>, cheat-sheet]
company: <Company>
round: <R1 recruiter screen | HM | panel | technical>
role: <title as posted>
interviewer: <name(s)>
when: <day, date, time + timezone, medium>
purpose: Phone-open cheat sheet for <round>
created: <YYYY-MM-DD>
---

# <Company> R<n> — <Purpose>

> [!info] Prep status
> BOOKED / PENDING SCHEDULING — <when, where, how long, who>. If the confirmation says otherwise, this doc changes.

> **The frame:** <What this round can and cannot decide, in two or three sentences.>
> **The objectives, numbered.** Usually: (1) do not lose it, (2) extract the one or two facts that gate further investment, (3) leave them one clean sentence they can repeat to the next person.
>
> **The unknowns that decide whether this is worth a loop:** <the specific ambiguities — level, band, format, location.>

# 🗺️ JUMP
[[#🏢 WHAT THEY DO]] · [[#👤 INTERVIEWER DNA]] · [[#🎙️ THE 90-SECOND STORY]] · [[#🎯 SKILLS TO HIGHLIGHT]] · [[#🔨 HAMMER THESE HOME]] · [[#❓ QUESTIONS FOR <NAME>]] · [[#💰 COMP + LEVEL]] · [[#🧗 IF STACK COMES UP]] · [[#⚠️ TRAPS]] · [[#🗓️ LOGISTICS]] · [[#🚩 PRIVATE READS]]

---

# 🏢 WHAT THEY DO, WHAT THE JOB IS
Plain-English product description first — the sentence they could say to a friend. Then: funding, scale, ARR/headcount, trajectory, notable customers, competitors. Then **the specific team or product surface** this req sits on, and what the job therefore actually is day to day. Close with one line: why this fits, in one breath.

> [!warning] Do not prep for the wrong interview
> Use this callout when public write-ups describe a different team's process at the same company.

# 👤 INTERVIEWER DNA
Per person: title, tenure, notable prior role, what they will likely ask, what they will not. Tag each. See `interviewer-research.md`.

# 🎙️ THE 90-SECOND STORY
*The "walk me through your background" answer. Say it out loud once before the call.*
1. **Now:** current status in one sentence — if there is a layoff, gap, or exit to explain, it goes here. Zero drama, move on.
2. **The lane:** the center of gravity, with the two strongest employer proof points.
3. **Why them:** map the lane onto their specific problem. Not flattery — shape-matching.
4. **The differentiator:** ownership, with the strongest hard number.

**One-liner for <them> to repeat to the hiring manager:**
> *"<One sentence, quotable, no hedging.>"*

# 🎯 SKILLS TO HIGHLIGHT
Ranked, numbered, most-relevant first. Each: the claim, then the concrete proof. Top three should be the ones that actually win this req.

**Do not volunteer:** <technologies not on the resume>. If asked → [[#🧗 IF STACK COMES UP]].

# 🔨 HAMMER THESE HOME
*If the call ends and none of these landed, it went badly.* Five or six, none long. Include the strongest hard number and spend it deliberately — do not scatter it.

# ❓ QUESTIONS FOR <NAME>
Ordered, with the scripted wording in blockquotes. At R1 the first two are level and band. Then process/format, then team, then timeline. For panels: per-person.

# 💰 COMP + LEVEL
Posted band (and which geo band applies). The anchor number with the sentence that delivers it. What changes if the level answer is different than assumed. The deflection line if they ask first. **Floor recorded here as a private number — never stated on the call.** Equity: ask for the mix, do not chase details.

# 🧗 IF STACK COMES UP
One honest line per gap. No bluffs — later rounds are technical and bluffs compound. Include the counterweight: they read the resume and reached out anyway.

# ⚠️ TRAPS
Facts not to misquote back to them (team size, funding history, their own phrasing for themselves). Claims not to make. Tone rules. Anything a previous round or debrief flagged.

# 🗓️ LOGISTICS / SCHEDULING
Where they will physically be, connection, backup, what time to be ready, who to email if running late, and any conflicts on the same day. Availability already sent — read from here, do not re-derive on the phone.

# 🚩 PRIVATE READS — not for the call
Glassdoor patterns, comp risk, leveling suspicions, domain/values check, and the honest assessment of this opportunity against the others in flight.
```

---

## Debrief

Write it the same day, while it is fresh. Short. Its job is to make the next doc better and to stop repeated mistakes.

Filename: `<Company> R<n> — Debrief.md`.

```markdown
---
tags: [career, job-search-<year>, <company-slug>, interview-debrief]
company: <Company>
round: <R1 recruiter screen (Name)>
date: <YYYY-MM-DD>
outcome: <honest one-line read + what happens next and by when>
---

# <Company> R<n> — Debrief

## Overall
Honest read in two or three sentences. Engagement signals, not just vibes.

## What I learned
Facts only — hours, comp mechanics, review cadence, next steps and their format, timeline. These feed the next cheat sheet and the [[#⚠️ TRAPS]] section.

## What to fix
Each item: what happened, then the concrete fix in their own words for next time. Not self-flagellation — a scripted replacement line.

## Action items
- [ ] Checkboxes with owners and dates. Anything that must start before the greenlight (drills, references, guides to read) goes here.
```

---

## Notes on Style

- **Confidence tags everywhere.** `[CERTAIN]` from a primary source, `[LIKELY]` inferred, `[GUESSING]` filling a gap. The user needs to know what is safe to say out loud.
- **Blockquote anything they say verbatim.** Scripted lines get quote formatting so they are findable at a glance.
- **✍️ marks answers only the user can supply.** Never improvise their personal history — flag it and let them fill it in before the call.
- **⚠️ marks a live risk** — a conflict, a deadline, a thing that will bite.
- Jump nav is worth its lines on anything over ~100 lines. Mid-call scrolling is the failure mode.
