---
name: serve-prototype
description: Use whenever building or showing Kenny a visual/web prototype, mockup, design comparison, or any standalone HTML — always serve it over a local HTTP server and open it in the browser instead of sending a static file. Kenny wants prototypes live, not as file attachments.
---

# Serve Prototype

Kenny's standing preference: **prototypes are always served live**, never handed over as a static file to double-click. Live serving means real CSS (`oklch()`, custom props, fonts), working relative paths, and instant refresh when iterating.

## When to Use

- Any standalone HTML mockup or design comparison (e.g. "show me option A vs B").
- Visual exploration of a component/screen before wiring it into the app.
- Anything where Kenny needs to _see_ a rendered page.
- **Physical / print artifacts too** — a nameplate, plaque, sign, printed page. When the target is a real-world object, size the canvas to the actual dimensions (e.g. an `@page` size or a fixed-px box matching the plaque) instead of a screen layout, and offer a print-friendly variant.

**Do NOT use for:** a real app prototype that already has its own dev server (Vite, Next, etc.) — run that project's `npm run dev` instead. This skill is for standalone/static prototypes.

## Workflow

1. **Save the prototype to a durable location**, not a job temp dir (those get cleaned up).
   Default: `~/.claude/prototypes/<topic>/index.html` (or a descriptive `.html` name).
   Create the dir if needed: `mkdir -p ~/.claude/prototypes/<topic>`.

2. **Serve and open it** with the helper:

   ```bash
   bash ~/.claude/skills/serve-prototype/serve.sh ~/.claude/prototypes/<topic>/<file>.html
   ```

   It picks a free port (8137–8166), starts a detached `python3 -m http.server`,
   reuses an existing server if one is already serving that directory, opens the
   browser, and prints the URL.

3. **Health-check, then give Kenny the URL.** Before handing over
   `http://127.0.0.1:<port>/<file>.html`, `curl -sf` it once and confirm it
   responds — don't hand over a dead URL. The server is detached and _should_
   survive across turns, but in long brainstorm/iterate sessions it does die.
   So: when iterating, overwrite the file, **re-check the URL before telling him
   to refresh, and re-run `serve.sh` to restart if it's dead** (the script reuses
   the existing server or spins a fresh one). Don't make Kenny be the one who
   notices it died.

## Notes

- One server per directory (tracked by a pidfile), so re-running the script is cheap and won't spawn duplicates.
- Put multiple variants in one HTML file (side-by-side panels) so a single page shows the whole comparison.
- Match the target app's theme: pull real color tokens / fonts from its CSS so the mockup reads true.
- To stop a server: `lsof -ti tcp:<port> | xargs kill`.
