#!/usr/bin/env bash
# serve-prototype: serve a file or directory over a local static HTTP server
# and open it in the browser. Reuses one server per directory so repeated
# calls don't pile up orphaned ports.
#
# Usage: serve.sh <file-or-dir>
# Prints the URL on success.
set -euo pipefail

target="${1:?usage: serve.sh <file-or-dir>}"
if [ -d "$target" ]; then
  dir="$target"; file=""
else
  dir="$(dirname "$target")"; file="$(basename "$target")"
fi
dir="$(cd "$dir" && pwd)"

# One server per directory, tracked by a pidfile keyed on the dir path.
key="$(printf '%s' "$dir" | cksum | cut -d' ' -f1)"
portfile="${TMPDIR:-/tmp}/proto-server-$key.port"

port=""
if [ -f "$portfile" ]; then
  existing="$(cat "$portfile")"
  if curl -s -o /dev/null "http://127.0.0.1:$existing/"; then
    port="$existing"   # still alive and serving this dir — reuse it
  fi
fi

if [ -z "$port" ]; then
  for cand in $(seq 8137 8166); do
    if ! lsof -iTCP:"$cand" -sTCP:LISTEN >/dev/null 2>&1; then
      port="$cand"; break
    fi
  done
  [ -n "$port" ] || { echo "no free port in 8137-8166" >&2; exit 1; }
  ( python3 -m http.server "$port" --bind 127.0.0.1 --directory "$dir" \
      >/dev/null 2>&1 & )
  printf '%s' "$port" > "$portfile"
  sleep 1
fi

url="http://127.0.0.1:$port/${file}"
command -v open >/dev/null 2>&1 && open "$url" || true
echo "$url"
