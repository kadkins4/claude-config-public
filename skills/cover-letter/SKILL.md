---
name: cover-letter
description: Use when the user is writing a cover letter for a job application or posting — matches only their real strengths from their resume to the listing, never names gaps, and outputs a short letter in their genuine, plain-spoken voice.
disable-model-invocation: true
---

# Cover Letter

## Overview

Write a short cover letter that matches the user's real strengths to a job listing, in their **genuine, plain-spoken voice** (composed and direct, not chatty or bubbly — contractions and a real personal reason for wanting the role, but it reads like a measured professional, not a form letter and not a text message). **Highlight only what fits. Never name a gap.** A genuine reason is in; manufactured enthusiasm and filler are out. Just: here are my matching strengths, here's why this company specifically, said plainly in the user's own words.

**Voice calibration:** read the "Cover letter and application-answer voice" section of `~/.claude/skills/job-search/user-context.md` first — it may override the default register below, and it may point at a benchmark letter the user already edited. **Learn from the user's edits.** When they cut something from a draft, that cut is a standing rule, not a one-off. Record it in `user-context.md`.

**Three cuts most people make every single time** — apply them before showing a draft:

1. **Rhetorical lead-ins.** Cut the scene-setting first sentence that exists to make the real point land. "Most AI roles right now are thin wrappers around a chat box" → delete, open with the actual reason.
2. **Qualifiers and self-assessment.** Cut "genuinely hard," "which is rarer than it should be," "unusually," "truly," and any phrase rating the thing instead of stating it. "The graphics-heavy canvas is genuinely hard front-end work" → "Optimizing performance on a graphics-heavy canvas is the kind of problem I want to be working on."
3. **The clever closer.** Cut the aphorism at the end. A line that reads as written to be quoted gets deleted. State the thing and stop.

The test: every sentence should be a claim or a fact, not a frame around one. If a sentence's job is to set up the next sentence, delete it.

**This applies to short-answer application questions too**, not just letters — those want 3-5 plain sentences, and companies that say "not a cover letter" mean it.

## Inputs

1. **The job listing** — pasted by the user, or a URL/file. If missing, ask for it.
2. **The user's background** — read from the resume at `RESUME_PATH` in `user-context.md`. This is the single source of truth. Match against what's actually in it. If a claim isn't backed by the resume, don't make it.

## The Three Hard Rules

### 1. Positives only — never name a gap

Read the listing's requirements/wants. Cross-reference against the resume. **Write only about the matches.** A requirement the user doesn't meet does not appear in the letter at all — not hedged, not softened, not acknowledged.

If the listing wants 3 things and the resume covers 2, the letter is about those 2. The 3rd is invisible.

| Temptation                                              | Reality                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------- |
| "I should address the gap so it doesn't look ignored"   | Naming a gap creates the doubt. Silence on it is the goal. Omit it. |
| "I'll say they're 'eager to grow into' the missing skill" | That's flagging the gap with a bow on it. Cut it.                   |
| "I'll mention it but spin it positively"                | Still naming it. Omit entirely.                                     |
| "The role really centers on the thing they lack"        | Then lead harder on the matches. Never write the lack.              |

### 2. Defensibility — never claim what they can't defend out loud

Every sentence must survive an interviewer asking "tell me more about that." Don't overstate verifiable project facts or imply experience the user doesn't have — it unravels the moment it's probed.

| Temptation                                                          | Reality                                                                       |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| "real-time data" when the project only refreshes on load            | Say what it actually does. Soften any detail you can't defend.                |
| "I use your product" / "I'm in your world" when they've never used it | Reframe to what's true: "I value what you're optimizing for."                 |
| Inflating scale, users, or impact numbers                           | Use the real number or omit it. A challenged exaggeration sinks the letter.   |

If unsure whether a claim is defensible, ask the user or drop it.

### 3. Genuine, plain voice — but no fake enthusiasm or filler

Write it in the user's voice: composed and direct, contractions, a real reason this role fits them. It should read like a smart person talking plainly, not a form letter and not a chatty text. Not stiff and corporate, but not bubbly either — measured and honest is the target.

Genuine reason is not the same as performed excitement, and it is not the same as chattiness. The line: **a real reason this fits ("I care a lot about speed and polish," "the teams-and-agents direction is why I'm interested") stays; enthusiasm-theater ("I'm thrilled!", "dream job!") and winking asides ("which seems to be exactly how you operate") both go.** Keep the honest reason, cut the theater and the winks.

**Still banned** (fake enthusiasm and empty setup — different from personality):

- "I'm excited to apply…", "I'm thrilled…", "I was delighted to see…", "dream job / dream role"
- "As a passionate / lifelong…"
- "I believe I would be a great fit because…" (just show the fit)
- "I'd love the opportunity to…"
- Restating the job title back at them as a hook.
- Throat-clearing setup that says nothing ("There are many reasons I'm drawn to…").

**Voice rules:**

- **No em-dashes** (they read as an AI tell). Ellipses are fine.
- Lead with something concrete (a strength, a real hook), not a feeling.
- A genuine reason about the actual problem/mission is welcome, as long as it's true (see Rule 2: don't imply they use the product if they don't).
- Plainer beats warmer. When choosing between a chatty phrasing and a composed one, pick composed.

## Format Contract

- **Greeting:** `Dear [Company],` by default. Use `To Whom It May Concern,` only if the user says so or no company name is available. (`Hi [Company],` is acceptable for an obviously casual shop, but `Dear` is the default.)
- **Body:** **2 paragraphs maximum.**
  - Paragraph 1: strongest matching skills/experience, tied to the listing's needs.
  - Paragraph 2: why _this company_ / role specifically, plus how those skills help.
- **Closing line:** `Sincerely,`
- **Signature:** the user's full name as it appears on the resume.
- **Voice:** genuine and plain throughout (Rule 3). Composed not chatty. No em-dashes; ellipses ok.

## Process

1. Get the listing. Read `user-context.md`, then the resume.
2. List the listing's requirements/wants. Mark each met / not-met against the resume.
3. Draft using **only** the met items. Two paragraphs.
4. Draft in the user's genuine, plain voice. Strip fake-enthusiasm phrases, empty setup, and chatty winks (Rule 3) — but keep one honest reason this fits. Apply the three cuts. Kill any em-dashes.
5. Apply greeting + closing + signature.
6. Output in chat as paste-ready plain text (no file, no blockquote, no code fence — those come along on copy).

## Example shape

```
Dear Acme,

[Paragraph 1 — concrete matching strengths from the resume, mapped to what the listing asks for. Plain and composed. Real hook, not fake enthusiasm.]

[Paragraph 2 — why this company specifically, plus how those strengths help. One honest reason; keep it true and defensible.]

Sincerely,
[Full Name]
```

## Reference letter (target register)

Once the user has edited a draft into something they'd actually send, **save it in `user-context.md` as the benchmark** and match that register for every letter after. Until then, aim for: composed, plain, contractions, one genuine reason, no winks, no em-dashes, every sentence a claim or a fact.

## Red Flags — stop and rewrite

- The letter mentions a skill/requirement the user doesn't have (even to dismiss it).
- It opens with fake enthusiasm ("thrilled", "dream job") or a restated job title. (Genuine warmth/personality is fine — performed excitement is not.)
- It reads stiff and corporate instead of like the user talking.
- It contains an em-dash.
- It's longer than 2 paragraphs.
- A claim isn't supported by the resume.
- It states a project detail they couldn't defend if probed (overstated scope/scale, "real-time" when it isn't, implies they've used the product).
- A sentence exists only to set up the next one.
