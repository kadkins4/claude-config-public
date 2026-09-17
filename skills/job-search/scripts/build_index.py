#!/usr/bin/env python3
"""Regenerate `Companies Index.md` from note frontmatter + the Companies/ tree.

The index is a CACHE, never a source of truth. Re-run it any time a status flips.
    JOB_SEARCH_DIR="/path/to/Job Search" python3 ~/.claude/skills/job-search/scripts/build_index.py 2026-08-01

Config (env vars):
    JOB_SEARCH_DIR   absolute path to the job-search folder (required). Holds Companies/.
    JOB_SEARCH_VAULT_REL   optional. If the folder lives inside an Obsidian vault, the
                     vault-relative path to Companies/ (e.g. "Work/Career/Job Search/Companies")
                     so generated wikilinks resolve. Defaults to "Companies".
"""
import os, re, sys, datetime

BASE = os.environ.get("JOB_SEARCH_DIR")
if not BASE:
    sys.exit("set JOB_SEARCH_DIR to the absolute path of your job-search folder")
VAULT_REL = os.environ.get("JOB_SEARCH_VAULT_REL", "Companies")
COMPANIES = os.path.join(BASE, "Companies")

today = (datetime.date(*map(int, sys.argv[1].split("-"))) if len(sys.argv) > 1
         else datetime.date.today())

# most-live-first; a company folder is filed under the liveliest status it holds
ORDER = ["Offer", "Interviewing", "In progress", "Waitlisted", "Applied",
         "To-Apply", "Lead", "Rejected", "Passed", "Superseded"]
RANK = {s: i for i, s in enumerate(ORDER)}
LABEL = {"Offer": "🏆 Offer", "Interviewing": "🎉 Interviewing", "In progress": "🧪 In progress",
         "Waitlisted": "⏸️ Waitlisted", "Applied": "📮 Applied", "To-Apply": "🔖 To-Apply",
         "Lead": "🌱 Lead", "Rejected": "❌ Rejected", "Passed": "🚫 Passed",
         "Superseded": "♻️ Superseded"}


def field(fm, key):
    m = re.search(r'^%s:\s*"?([^"\n]*)' % key, fm, re.M)
    return m.group(1).strip().rstrip('"') if m else ""


def scan():
    out = {}
    for entry in os.scandir(COMPANIES):
        if not entry.is_dir():
            continue
        apps, prep = [], []
        for f in sorted(os.listdir(entry.path)):
            if not f.endswith(".md"):
                continue
            text = open(os.path.join(entry.path, f), encoding="utf-8", errors="replace").read(4000)
            m = re.match(r"---\n(.*?)\n---", text, re.S)
            fm = m.group(1) if m else ""
            tags = re.search(r"^tags:.*$", fm, re.M)
            if tags and "application" in tags.group(0):
                apps.append({"file": f[:-3], "status": field(fm, "status"),
                             "applied": field(fm, "applied"), "role": field(fm, "role"),
                             "detail": field(fm, "status_detail")})
            else:
                prep.append(f[:-3])
        out[entry.name] = {"apps": apps, "prep": prep}
    return out


def link(folder, note, alias):
    return f"[[{VAULT_REL}/{folder}/{note}|{alias}]]"


def age(app):
    if app["status"] != "Applied" or not app["applied"]:
        return None
    try:
        d = datetime.date(*map(int, app["applied"].split("-")))
    except ValueError:
        return None
    return (today - d).days


def build():
    data = scan()
    companies = []
    for name, v in sorted(data.items(), key=lambda kv: kv[0].lower()):
        if not v["apps"]:
            continue
        live = min(v["apps"], key=lambda a: RANK.get(a["status"], 99))
        companies.append({"name": name, "status": live["status"], "live": live,
                          "apps": v["apps"], "prep": v["prep"]})

    L = []
    A = L.append
    A("---")
    A("tags: [career, job-search, index]")
    A(f"updated: {today}")
    A("---")
    A("")
    A("# Companies — Index")
    A("")
    A(f"Every company folder, grouped by status. **Generated {today} from note frontmatter.**")
    A("")
    A("> [!warning] This file is a cache, not the source of truth")
    A("> Statuses live in each application note's frontmatter. This index is rebuilt from them, so"
      " **it is only accurate as of the date above** — a rejection logged after that date will not"
      " show here until it is regenerated. Never edit a status here; edit the note and re-run:")
    A("> ```")
    A("> JOB_SEARCH_DIR=<folder> python3 ~/.claude/skills/job-search/scripts/build_index.py")
    A("> ```")
    A("")
    A("[[Job Search Home]] · [[Application Tracker]] · [[Board Watchlist]] · [[Interview Prep]]")
    A("")

    # ---- the section that actually solves the scroll ----
    with_prep = [c for c in companies if c["prep"]]
    n_prep_docs = sum(len(c["prep"]) for c in with_prep)
    A("## 📁 Companies with prep docs")
    A("")
    A(f"**{len(with_prep)} of {len(companies)} folders** hold anything beyond the application note "
      f"({n_prep_docs} docs total). Everything else is an application note and nothing more, so this "
      "is the only section worth browsing when you are looking for prep, a cheat sheet, or a debrief.")
    A("")
    A("**The status beside each one tells you whether the prep is still worth reading.** "
      "That is the thing a flat list could never show, and the reason the old name-list in "
      "[[Interview Prep]] was deleted rather than maintained.")
    A("")
    open_prep = [c for c in with_prep if c["status"] not in ("Rejected", "Passed", "Superseded")]
    closed_prep = [c for c in with_prep if c["status"] in ("Rejected", "Passed", "Superseded")]

    for heading, group, note in (
        ("### ▶️ Live / open — prep is current", open_prep, ""),
        ("### 🗄️ Closed — archive, kept for reuse", closed_prep,
         "Dead processes. Worth raiding for question banks and debrief lessons, not for prepping "
         "these companies again unless a re-apply opens."),
    ):
        if not group:
            continue
        A(heading)
        A("")
        if note:
            A(note)
            A("")
        for c in group:
            A(f"- **{c['name']}** — {LABEL.get(c['status'], c['status'])}")
            for p in c["prep"]:
                A(f"    - {link(c['name'], p, p)}")
        A("")

    # ---- everything, by status ----
    total_apps = sum(len(c["apps"]) for c in companies)
    A("## 🗂️ All companies by status")
    A("")
    A(f"{len(companies)} folders. 📁 marks one that has prep docs.")
    A("")
    A("> [!info] These counts are **companies**, not applications — they will not match "
      "[[Job Search Home]], and that is correct")
    A(f"> {len(companies)} company folders hold **{total_apps} applications**. Where a company was "
      "applied to more than once, its folder is filed under the **liveliest** status it holds, so a "
      "company with one rejection and one open application appears under `Applied` only. Home counts "
      "every application separately. **Neither is wrong; they answer different questions.** Use Home "
      "for pipeline numbers and this file for finding a company.")
    A("")
    for status in ORDER:
        group = [c for c in companies if c["status"] == status]
        if not group:
            continue
        if status == "Applied":
            fresh = [c for c in group if (age(c["live"]) or 99) < 21]
            cold = [c for c in group if (age(c["live"]) or 99) >= 21]
            for sub, label, blurb in (
                (fresh, f"### 🔥 Applied — under 21 days ({len(fresh)})",
                 "The plausibly-live subset."),
                (cold, f"### 🧊 Applied — 21+ days silent ({len(cold)})",
                 "No evidence they closed, so they stay `Applied`. **Silence is not a rejection** "
                 "— rejection letters at 3-5 weeks of silence are routine, and they come out of this bucket."),
            ):
                if not sub:
                    continue
                A(label)
                A("")
                A(blurb)
                A("")
                A(" · ".join(
                    ("📁 " if c["prep"] else "") + link(c["name"], c["live"]["file"], c["name"])
                    for c in sub))
                A("")
            continue
        A(f"### {LABEL.get(status, status)} ({len(group)})")
        A("")
        if status in ("Rejected", "Passed", "Superseded"):
            A(" · ".join(
                ("📁 " if c["prep"] else "") + link(c["name"], c["live"]["file"], c["name"])
                for c in group))
            A("")
        else:
            for c in group:
                extra = f" — {c['live']['detail']}" if c["live"]["detail"] else ""
                A(f"- {'📁 ' if c['prep'] else ''}"
                  f"{link(c['name'], c['live']['file'], c['name'])}{extra}")
                for other in c["apps"]:
                    if other is not c["live"]:
                        A(f"    - also: {link(c['name'], other['file'], other['file'])} "
                          f"(`{other['status']}`)")
            A("")

    multi = [c for c in companies if len(c["apps"]) > 1]
    if multi:
        A("## 🔁 Companies with more than one application")
        A("")
        A("One seat is never counted twice — a repost of a req already applied to sets the older "
          "note to `Superseded`. These are genuinely separate applications.")
        A("")
        for c in multi:
            A(f"- **{c['name']}** ({len(c['apps'])})")
            for a in c["apps"]:
                A(f"    - {link(c['name'], a['file'], a['file'])} — `{a['status']}`"
                  f"{', applied ' + a['applied'] if a['applied'] else ''}")
        A("")

    return "\n".join(L) + "\n", companies, with_prep


def report(companies):
    """Print the numbers `Job Search Home.md` must be reconciled to.

    These are APPLICATION counts (what Home tracks), not company counts.
    """
    apps = [a for c in companies for a in c["apps"]]
    counts = {}
    for a in apps:
        counts[a["status"]] = counts.get(a["status"], 0) + 1
    bad = [(c["name"], a["status"]) for c in companies for a in c["apps"]
           if a["status"] not in RANK]
    applied = [a for a in apps if a["status"] == "Applied"]
    fresh, cold, undated = 0, 0, []
    for a in applied:
        d = age(a)
        if d is None:
            undated.append(a["file"])
        elif d < 21:
            fresh += 1
        else:
            cold += 1

    print(f"\n=== reconcile `Job Search Home.md` to these ({today}) ===")
    print(f"  **{len(apps)} tracked**   ({len(companies)} company folders)")
    for s in ORDER:
        if counts.get(s):
            print(f"  {LABEL[s]:<18} {counts[s]}")
    total = fresh + cold
    pct = (cold / total * 100) if total else 0
    print(f"  🔥 applied <21d      {fresh}")
    print(f"  🧊 applied 21+d      {cold}   ({pct:.1f}% cold)")
    if undated:
        print(f"  ⚠️  Applied with no `applied:` date: {undated}")
    if bad:
        print(f"  🛑 STATUS OUTSIDE THE TEN-VALUE VOCABULARY: {bad}")
    else:
        print("  ✅ all statuses valid")
    print("  ⚠️  these are APPLICATION counts; the index groups by COMPANY, so they differ\n")


if __name__ == "__main__":
    text, companies, with_prep = build()
    if "--counts-only" not in sys.argv:
        path = os.path.join(BASE, "Companies Index.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {path}")
        print(f"  {len(companies)} companies · {len(with_prep)} with prep docs · {len(text)} bytes")
    report(companies)
