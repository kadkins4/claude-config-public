# User — job-search context

Facts about the user that the job-search loop depends on. **This file is the canonical home for them.** Keeping them here (instead of as auto-memories) means they load with `/job-search` from any directory and cost zero context until then.

When one of these facts changes, **edit this file** — don't write a new memory for it.

**Fill this in before the first triage session.** Every `<...>` is a blank. Delete sections that don't apply; add sections when a new fact starts changing decisions. Each section should say what the fact is and **how to apply** it in a rundown — the second half is what makes it useful.

---

## Paths

- `JOB_SEARCH_DIR`: `<absolute path to the job-search folder, e.g. an Obsidian vault subfolder>`
- `RESUME_PATH`: `<absolute path to the markdown resume — the single source of truth for fit claims>`

---

## Employment status

_<One line: employed / laid off <date> / actively searching / search concluded <date>.>_

**How to apply:** <e.g. "Actively searching — treat every rejection as a live-pipeline event." or "Employed as of <date> — only closing out old applications; no urgency.">

---

## Location preference

_<Based in <city>. Remote / hybrid / onsite preference. Cities acceptable for hybrid. Cities they will NOT relocate to.>_

**Watch the application form, not just the JD:** location/relocation gates sometimes appear only in the apply form. Flag remote-status as an unknown to confirm whenever the JD omits it.

**How to apply:** score **Location** in every rundown: 🟢 matches preference · 🟡 hybrid in an acceptable city · 🔴 onsite or hybrid elsewhere. Weight it heavily in the recommendation.

---

## Comp floor

_<Number. Base salary floor for full-time. Optionally: how to price contract/hourly against it.>_

**How to apply:** anchor to the top of _their_ range; never reveal the floor. Flag under-floor comp. Score **Comp** in every rundown (⚪ if not posted — pull it in the screen).

---

## Domain no-gos

_<Industries or company types the user will not work in. Mark each HARD NO or LIKELY NO.>_

- **<domain> — HARD NO.** <why, when stated>
- **<domain> — LIKELY NO.** <why> (values flag — ask, don't auto-kill)

**How to apply:** for a hard-no, lead the analysis with it and recommend skip without a full work-up. For likely-no, name it up front with the dot and ask rather than assume.

---

## Stack — real vs. claimable

_<For each framework/language: how much real experience, whether it's on the resume, whether it can be claimed on an application or in a screen.>_

- **<Framework>** — <years, where, load-bearing or shallow>. Score roles naming it as **match / stretch / gap**.
- **<Language>** — <bootcamp-only / side projects>. **Never claim on an application.**

**General lesson:** the resume may omit real experience. **Do not infer an absence of experience from an absence of a resume bullet — ask.**

**How to apply:** never imply depth the user can't defend in an interview. If a listing names a gap skill first or second in its stack list, the req is weighted toward that skill and should be scored accordingly.

---

## Leadership / management experience

_<Pre-engineering management, tech-lead work, mentoring, on-call ownership. What clears an EM gate and what doesn't.>_

**How to apply:** <e.g. "Do not say 'no management experience.' Still does not clear 'X+ years managing engineering teams' gates.">

---

## Portfolio

_<URL. What it demonstrates and what it doesn't (e.g. no 3D/WebGL showpieces). Which pieces can carry which kind of role.>_

**How to apply:** when a listing screens on a portfolio bar the site doesn't clear, flag it as a portfolio gap, not just a skills question.

---

## Resume variants

_<If the user keeps more than one resume: letter each one and say which kind of role it targets. Note where the source lives and how the PDFs get regenerated.>_

- **A** — <focus>
- **B** — <focus>
- **C** — <focus>

**How to apply:** every rundown ends with **Resume: A / B / C** next to the 🟢/🟡/🔴 verdict.

---

## Career direction

_<Anything that reshapes fit reads: wants to move toward PM / EM / staff IC; framework-agnostic bet; domains they'd like to move into (e.g. game-adjacent web work but not in-engine game dev).>_

**How to apply:** <what to score higher or lower because of it>

---

## Cover letter and application-answer voice

_<Register: plain and composed / warm and informal. Benchmark letters, if any. Signature name.>_

**How to apply:** the `cover-letter` skill reads this. Note anything that overrides its defaults.

---

## Standing preferences

- **Rundown format:** one-line company blurb → scannable dot-list (`CATEGORY 🟢/🟡/🔴/⚪ → terse reason`) → red flags → recommendation + resume variant as the last line. Not prose.
- **No recruiter-questions section in the rundown.** Surface tailored questions only when a recruiter actually reaches out.
- **Research depth:** light pass by default. Deep-dive only when a listing is close and one unknown decides it.
- **Never write anything until the user says "apply" / "applied" / "skip".**
- <anything else: prose rules like "no em dashes", "flag anything untrue or contrived", etc.>

---

## PERM / labor-certification ads

Some listings are **PERM labor-certification ads**: legally required advertisements for a role that is _already filled_ by a foreign worker the employer is sponsoring for a green card. The ad exists to document a "labor market test" for the DOL, not to hire. Applying cannot get the user the job.

**User's position:** _<e.g. "Won't apply — a qualified applicant can derail someone's sponsorship; flag and skip on sight." or "Indifferent — score normally.">_

**Detection markers** (any 3+ together ≈ certain):

- **"(Multiple Positions)"** in the title.
- **`#LI-DNI` / `#LI-DNP`** — LinkedIn Do-Not-Index / Do-Not-Post. They must run the ad but are suppressing reach.
- **A State Workforce Agency application channel** (e.g. a `<state>works.gov` link). DOL requires a 30-day SWA job order (20 CFR 656.17).
- **"in the job offered or related occupation in which the required experience was gained"** — lifted verbatim from **ETA Form 9089**.
- **"In lieu of a Bachelor's... will also accept a Master's degree and three (3) years"** — the alternate-requirements clause.
- **Spelled-out numerals**: "five (5) years".
- **"Must reference Job Title & Job Code: NNNN"** + multiple apply channels incl. a bare email.
- **Absurdly broad degree list** ("Engineering (any), Analytics (any), Management (any)") — drafted around one person's diploma.
- Precise worksite street address; "Work Shift: Not Specified".

**Confirmed instances:** _<company, date, role — so they are never re-read>_

---

## Known ghost / fake listings

_<Company name, date confirmed, evidence (bounced apply email, unregistered domain, zero web footprint, no company name in the posting, equity-only comp). Never re-analyze or re-apply if it resurfaces.>_

**Tell:** a board serving one scraped/fake post is serving others — gut-check the source of any similar listing.

---

## Weekly cadence

_<If the user schedules search work: which mornings/blocks, the weekly review ritual (e.g. Sunday: run the "Oldest silent" view, chase or close).>_
