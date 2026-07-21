---
name: monitor
description: Use when user asks to monitor, watch, or track a GitHub Actions run, PR merge, deploy, or any external process and get notified with sound when it completes.
---

# Monitor

Poll an external resource and play a sound when it reaches a target state.

## How to Use

1. **Identify the resource** — parse the user's URL or description to determine what to poll
2. **Check current state** — run the appropriate command to confirm the resource exists and get its status
3. **Set up CronCreate** — poll every 2 minutes (session-only, not durable)
4. **On completion** — play the notification sound and tell the user the result

## Polling Commands by Resource Type

| Resource        | Command                                                                     |
| --------------- | --------------------------------------------------------------------------- |
| GH Actions run  | `gh run view <id> -R <owner/repo> --json status,conclusion`                 |
| PR merge        | `gh api repos/<owner/repo>/pulls/<num> --jq '{state, merged}'`              |
| Deploy/workflow | `gh run list -R <owner/repo> -w '<workflow>' --json status,conclusion -L 1` |

Always use `dangerouslyDisableSandbox: true` for `gh` commands (SSH/network access).

## Completion Sound

Play **10 repetitions** of a system sound (default: Funk) unless the user specifies otherwise:

```bash
for i in $(seq 1 10); do afplay /System/Library/Sounds/Funk.aiff; done
```

Use `dangerouslyDisableSandbox: true` for `afplay` — the Bash sandbox blocks IPC to `coreaudiod` even though `afplay` is in the permission allow list, causing `AudioQueueStart failed (-66680)` and silent failure.

If the user requests a specific sound or duration, adapt accordingly. Available sounds are in `/System/Library/Sounds/`.

## Cron Prompt Template

The cron prompt should:

- Run the poll command
- If **completed/merged**: play the sound, tell the user the result, delete the cron job
- If **failed/closed without merge**: tell the user, delete the cron job
- If **still in progress**: do nothing (silent wait)

## Common Mistakes

- Forgetting `-R owner/repo` flag when not in the repo directory
- Not using `dangerouslyDisableSandbox: true` for `gh` network commands or `afplay` (sandbox blocks coreaudiod IPC, causing silent failure with error -66680)
- Making the cron durable — these are session-only monitors, not persistent jobs
