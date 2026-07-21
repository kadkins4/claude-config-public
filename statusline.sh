#!/bin/bash
input=$(cat)

MODEL=$(echo "$input" | jq -r '.model.display_name')
DIR=$(echo "$input" | jq -r '.workspace.current_dir')
COST=$(echo "$input" | jq -r '.cost.total_cost_usd // 0')
PCT=$(echo "$input" | jq -r '.context_window.used_percentage // 0' | cut -d. -f1)
DURATION_MS=$(echo "$input" | jq -r '.cost.total_duration_ms // 0')
FIVE_H=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')
FIVE_H_RESET=$(echo "$input" | jq -r '.rate_limits.five_hour.resets_at // empty')
WEEK=$(echo "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty')
WORKTREE=$(echo "$input" | jq -r '.worktree.name // .workspace.git_worktree // empty')

CYAN='\033[36m'; GREEN='\033[32m'; YELLOW='\033[33m'; RED='\033[31m'; MAGENTA='\033[35m'; RESET='\033[0m'

# Pick bar color based on context usage
if [ "$PCT" -ge 90 ]; then BAR_COLOR="$RED"
elif [ "$PCT" -ge 70 ]; then BAR_COLOR="$YELLOW"
else BAR_COLOR="$GREEN"; fi

FILLED=$((PCT / 10)); EMPTY=$((10 - FILLED))
BAR=$(printf "%${FILLED}s" | tr ' ' '█')$(printf "%${EMPTY}s" | tr ' ' '░')

MINS=$((DURATION_MS / 60000)); SECS=$(((DURATION_MS % 60000) / 1000))

BRANCH=""
if git -C "$DIR" rev-parse --git-dir > /dev/null 2>&1; then
  BR=$(git -C "$DIR" branch --show-current 2>/dev/null)
  [ -z "$BR" ] && BR=$(git -C "$DIR" rev-parse --short HEAD 2>/dev/null)
  DIRTY=""
  git -C "$DIR" status --porcelain 2>/dev/null | grep -q . && DIRTY="*"
  AB=""
  read -r BEHIND AHEAD <<< "$(git -C "$DIR" rev-list --left-right --count '@{upstream}...HEAD' 2>/dev/null)"
  [ "${AHEAD:-0}" -gt 0 ] && AB="${AB}↑${AHEAD}"
  [ "${BEHIND:-0}" -gt 0 ] && AB="${AB}↓${BEHIND}"
  BRANCH=" | 🌿 ${BR}${DIRTY}${AB}"
fi

WT=""
[ -n "$WORKTREE" ] && WT=" | ${MAGENTA}🌲 ${WORKTREE}${RESET}"

# Color a usage percentage green/yellow/red
pct_color() {
  local p=${1%%.*}
  if [ "$p" -ge 90 ]; then printf '%b' "$RED"
  elif [ "$p" -ge 70 ]; then printf '%b' "$YELLOW"
  else printf '%b' "$GREEN"; fi
}

LIMITS=""
if [ -n "$FIVE_H" ]; then
  R5=""
  [ -n "$FIVE_H_RESET" ] && R5=" (→$(date -r "${FIVE_H_RESET%%.*}" +%-I:%M%p | tr 'APM' 'apm'))"
  LIMITS=" | 5h: $(pct_color "$FIVE_H")$(printf '%.0f' "$FIVE_H")%${RESET}${R5}"
fi
if [ -n "$WEEK" ]; then
  LIMITS="${LIMITS} | wk: $(pct_color "$WEEK")$(printf '%.0f' "$WEEK")%${RESET}"
fi

echo -e "${CYAN}[$MODEL]${RESET} 📁 ${DIR##*/}$BRANCH$WT"
COST_FMT=$(printf '$%.2f' "$COST")
echo -e "${BAR_COLOR}${BAR}${RESET} ${PCT}% | ${YELLOW}${COST_FMT}${RESET} | ⏱️ ${MINS}m ${SECS}s${LIMITS}"
