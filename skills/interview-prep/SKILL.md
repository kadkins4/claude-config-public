---
name: interview-prep
description: Use when an interview is booked or invited and the user wants a prep doc, cheat sheet, or research on the company and the person interviewing them — "I have an interview with X", "prep me for this call", "who is this interviewer", "build the cheat sheet", "recruiter screen tomorrow". Also covers the post-interview debrief. Not for working a take-home assignment or drilling algorithm problems.
disable-model-invocation: true
---

# Interview Prep

## Overview

Produce **one phone-open document** the user can read live during the call, plus a debrief after it.

The document is not a research dump. It is an operating manual for thirty to sixty minutes under pressure. Every section earns its place by being something they would otherwise have to recall while talking.

**Core principle: match the doc to what the round can actually decide.** A recruiter screen cannot be won — it can only be lost, and it is the cheapest place to extract level, band, and format. A hiring-manager or founder round is most of the decision. Prep for the round in front of them, not for "the interview."

## The Spine

Work these in order. Do not skip to writing the doc.

1. **Pin the round.** Who, when, how long, what medium, which round of how many, and what that round decides. If the invite doesn't say, say so and mark it an assumption. Wrong-format prep is worse than thin prep.
2. **Research the company.** Product in plain English, scale/funding/trajectory, the specific team or product surface, competitors. Use WebSearch — never write company facts from memory. Tag every claim `[CERTAIN]` / `[LIKELY]` / `[GUESSING]`.
3. **Research the interviewer.** The part most preps skip, and the part that changes the doc the most. See `interviewer-research.md`.
4. **Map them onto the req.** Rank the strengths that actually win this job. Name the gaps and write the honest one-liner for each. Never invent experience; never bluff a stack — bluffs compound in later rounds.
5. **Write the doc.** See `templates.md`. Use the section set that matches the round; drop sections that do not apply rather than padding them. Mark every answer only the user can supply with ✍️ — do not fill it with a plausible guess.
6. **Fill the ✍️ blanks by grilling — never by guessing.** See "Filling the Blanks" below. This is a required step, not an optional one.
7. **Debrief after.** See `templates.md`. Facts learned, what to fix, action items. This is what makes the _next_ round's doc good.

## Filling the Blanks

Once the doc is drafted, the ✍️ items are the whole remaining job. **Do not write them from inference.** Invoke the **`grill-me`** skill (which loads `grilling`) and work the list.

Why this and not a questionnaire: answering one sharp question at a time makes the user _think_ about the answer they will actually give out loud. A wall of questions gets skimmed, and skimmed answers collapse under a follow-up. The grilling loop is also what surfaces the facts that change the doc — the details that matter are usually volunteered in the third sentence of a reply, not the first.

How to run it:

- **One question at a time.** Wait for the answer. Never batch.
- **Order by dependency, not by document order.** Ask the thing that changes other answers first — the comp decision usually gates posture for the whole call.
- **Always carry a recommendation.** Say which answer you would give and why, so they can push back on something concrete rather than face a blank page.
- **Use `AskUserQuestion` with candidate answers as options to jog recall.** Offering three plausible shapes of a memory works far better than "tell me about a time when…". Always leave the escape hatch for "it's something else."
- **Look up facts; ask only for decisions and memories.** Dates, headcounts, posted comp, prior employers — go find those. Never spend a question on something the filesystem, the vault, or the web can answer.
- **Mine the answer, don't just transcribe it.** The strongest card is usually a detail the user threw away — a peer asking their advice, a contractor's warning, a rule they set. Name why it is the strongest card when you write it in.
- **Push back once when the answer would hurt them.** Blunt raw material is not the script. Reframe it, show the reframe, and say plainly what the unreframed version would cost.
- **Write each answer into the doc as you go**, tick its checkbox, and re-point any section that referenced it as unfilled.

## Non-Negotiables

These come from real calls that went sideways. Violating one costs money or a loop.

- **Never write the floor into the doc as something to say.** Record it privately; the doc scripts the anchor, not the floor.
- **At R1, level and band are the same question, and they come first.** A wide posted band usually means it spans levels. Ask early, warmly, once.
- **Confirm the format before building a deep-technical section.** Public interview write-ups often describe a _different team_ at the same company. Prepping database internals for a product-UI role burns days.
- **Every gap gets a scripted honest sentence** — one line, no hedging, no apologizing, then redirect to real depth. The "do not volunteer" list matters as much as the "hammer these home" list.
- **Private reads live in their own section, clearly labeled not-for-the-call.** Skepticism about the company belongs in the doc; it does not belong in their mouth.
- **Do not re-litigate the gaps on their behalf.** They read the resume and booked the call anyway. Put that sentence in the doc as a counterweight.
- **Never badmouth a past employer.** Some formats (Topgrading) exist specifically to catch it. If there is a layoff, gap, or messy exit to explain, it gets one breath — factual, warm, then move on.
- **Never invent the user's own history.** Their exits, what they enjoyed, what they'd decide about an offer — these are not inferable, and a confident guess in the doc gets read back as fact under pressure. Mark it ✍️ and go ask.
- **Verify names and dates of anything they will say out loud.** Former employers, interviewers, products. A misremembered employer name or a spelling said wrong is a free own-goal in a chronological interview, and it is always cheap to check.
- **Check the resume timeline for gaps before writing the chronology.** A job the user omitted from their resume is usually the honest answer to a gap the interviewer is about to walk straight into — an asset, not a liability. Find the gap first.

## Depth Dial

| Signal                      | Doc                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Applied, no interview yet   | 3–6 lines in the company's prep note. Do not build a cheat sheet on spec.                                           |
| R1 recruiter screen booked  | Full cheat sheet, comp/level/format-forward, light technical.                                                       |
| HM / founder / panel booked | Full cheat sheet + interviewer DNA + per-person questions + format-specific script (e.g. chronological/Topgrading). |
| Technical round booked      | Cheat sheet + a named ramp list in priority order, saying plainly which items are real gaps.                        |

## Where It Goes

Default: the company's folder in an Obsidian vault, alongside the application note — `Companies/<Company>/<Company> R<n> — <Purpose>.md`. One folder per company, every artifact for that company inside it: application, prep, cheat sheets, debriefs.

**If no vault is configured, ask once where prep notes should live and use that.** Nothing here requires Obsidian — it requires a folder per company. Wikilinks degrade to plain text in any other editor.

## Red Flags — stop and fix

- You wrote company facts from memory instead of searching.
- No interviewer section because "it's just a recruiter" — recruiter background predicts the entire call.
- Untagged claims. If it is not tagged, the user cannot tell what is safe to say out loud.
- You built a technical deep-dive before confirming the round is technical.
- The doc is long but unnavigable mid-call — no jump nav, no ordering, no bolding of the line they actually have to say.
- You changed an application's status or tracker counts. This skill writes prep and debrief notes only.
- You filled a ✍️ blank with a guess instead of grilling for it.
- You batched the blank-filling questions into one message. One at a time, or the answers get skimmed.
- You transcribed the user's raw phrasing straight into the doc. Blunt raw material is not a script — reframe it, and say what the unreframed version would have cost.
