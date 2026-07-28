#!/usr/bin/env bash
# Wrapper: run P2 bulk download under nohup-friendly logging.
set -euo pipefail
ROOT="/home/leedt/echo-system"
OUT="$ROOT/knowledge/web-archives/taiwanjustice-net"
mkdir -p "$OUT"
export TJ_SLEEP="${TJ_SLEEP:-0.85}"
export PYTHONUNBUFFERED=1
exec python3 "$ROOT/scripts/taiwanjustice_wayback_bulk_download.py" \
  >>"$OUT/download.log" 2>&1
