#!/bin/bash
MSG="${1//\"/}"
terminal-notifier -message "$MSG" -title "Claude Code" -activate com.apple.Terminal
afplay "${2:-/System/Library/Sounds/Glass.aiff}"
