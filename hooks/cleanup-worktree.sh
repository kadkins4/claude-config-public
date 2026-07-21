#!/usr/bin/env bash
# SessionEnd hook: if cwd is inside a .claude/worktrees/ path and the
# worktree is clean, remove it so the branch can be checked out in the
# main repo. Skips removal (preserves work) if there are uncommitted changes.

input=$(cat 2>/dev/null || echo '{}')
cwd=$(printf '%s' "$input" | jq -r '.cwd // empty' 2>/dev/null)
[ -z "$cwd" ] && cwd="$PWD"

case "$cwd" in
  */.claude/worktrees/*) ;;
  *) exit 0 ;;
esac

main_repo="${cwd%%/.claude/worktrees/*}"

if [ -n "$(git -C "$cwd" status --porcelain 2>/dev/null)" ]; then
  printf '{"systemMessage": "Worktree %s has uncommitted changes — left intact."}\n' "$cwd"
  exit 0
fi

if git -C "$main_repo" worktree remove "$cwd" >/dev/null 2>&1; then
  printf '{"systemMessage": "Removed worktree %s — branch released to %s."}\n' "$cwd" "$main_repo"
fi
