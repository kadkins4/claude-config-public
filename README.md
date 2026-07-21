# claude-config-public

A shareable snapshot of my [Claude Code](https://code.claude.com/docs) setup — the config, custom skills, and slash commands I actually use day to day. Published for friends who are learning to code and want to see how an AI-assisted workflow is wired together.

Everything here lives in `~/.claude/` on my machine. Claude Code picks it up automatically.

## What's in here

| Path | What it is |
| --- | --- |
| `CLAUDE.md` | My global instructions — loaded into every Claude session. Sets communication style and standing rules. |
| `settings.json` | Harness config: permissions, hooks (auto-format on edit, run tests after changes, sound notifications), plugins. |
| `skills/` | Custom skills — reusable workflows Claude loads when a task matches. Each is a folder with a `SKILL.md`. |
| `commands/` | Slash commands (`/eli5`, `/grill-me`, …) — mostly short reference docs Claude reads on demand. |
| `hooks/` | Shell scripts wired into `settings.json` (cleanup, notifications). |
| `statusline.sh` | Custom terminal status line: model, cost, context-window usage bar, git branch. |

## If you're learning — start here

**Skills worth reading first:**

- **`skills/teach/`** — the most relevant one for you. A full tutoring workflow: Claude builds a workspace per topic, runs missions, tracks what you've retained across sessions. Shows how a multi-file skill is structured.
- **`skills/leetcode-coach/`** — Socratic coach for algorithm practice. Deliberately never gives the answer; a good example of constraining an LLM's default behavior with instructions.
- **`skills/grill-with-docs/`** — makes Claude challenge your plan instead of agreeing with it, and write down decisions as you make them.
- **`skills/visual-plan/` + `skills/visual-recap/`** — render plans and code changes as visual pages in the browser instead of terminal text.

**Commands worth reading:** `commands/tests.md`, `commands/mocking.md`, `commands/deep-modules.md`, `commands/interface-design.md`, `commands/refactoring.md` — these are condensed software-design references (largely from *A Philosophy of Software Design* and testing best practices). Useful reading even without Claude.

**Config worth reading:** `settings.json` shows hooks — shell commands that run automatically on events (after every file edit: prettier + eslint + related tests; on task finish: a notification sound). This is how you make the AI's environment enforce quality instead of trusting the model to remember.

## Ideas worth stealing

1. **Instructions beat prompting.** `CLAUDE.md` rules ("rate your confidence", "no filler praise", "disagree with structure") apply to every session automatically — you don't re-type them.
2. **Skills are just markdown.** A skill is a folder with a `SKILL.md` describing when to use it and the steps to follow. No code required to start.
3. **Hooks make behavior deterministic.** Formatting, linting, and test runs happen in `settings.json` hooks, not by asking nicely.
4. **Make the AI push back.** Several skills here exist purely to stop the model from being agreeable (`grill-with-docs`, `leetcode-coach`). Default LLM behavior is to please you; that's not always what helps you.

## Docs

- Claude Code: <https://code.claude.com/docs>
- Skills: <https://code.claude.com/docs/en/skills>
- Hooks: <https://code.claude.com/docs/en/hooks>
- Anthropic's model docs: <https://docs.anthropic.com>
