#!/bin/bash
# Audit-convention hits-hash sweep (deterministic, 0-LLM).
# Usage: depth_sweep.sh <slice>   e.g. depth_sweep.sh 09300848-29
# For each page listed in knowledge/operational/deepen-x-slice-<slice>.txt,
# grep works/ + articles/ for 'NAME_ZH\NAME_EN', build sorted relative hit-path
# list, sha1 -> first 12 hex = hits-hash. Prints "<slug> hits-hash=<12hex>"
# lines AND writes them to knowledge/operational/deepen-x-slice-<slice>.hashes.txt
cd "$(dirname "$0")/../.." || exit 1   # -> content/
SLICE="${1:?usage: depth_sweep.sh <slice>}"
OUT="knowledge/operational/deepen-x-slice-$SLICE.hashes.txt"
: > "$OUT"
while read -r rel; do
  case "$rel" in people/*|organizations/*) ;; *) continue;; esac
  [ -f "$rel" ] || { echo "$rel MISSING" >> "$OUT"; continue; }
  nz=$(grep -m1 '^name_zh:' "$rel" | sed 's/^name_zh:[[:space:]]*//' | tr -d '"')
  ne=$(grep -m1 '^name_en:' "$rel" | sed 's/^name_en:[[:space:]]*//' | tr -d '"')
  hits=$(grep -rl "$ne\\|$nz" works articles 2>/dev/null | sort)
  h=$(printf '%s' "$hits" | sha1sum | cut -c1-12)
  echo "$(basename "$rel" .md) hits-hash=$h" | tee -a "$OUT"
done < "knowledge/operational/deepen-x-slice-$SLICE.txt"
