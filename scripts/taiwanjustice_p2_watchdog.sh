#!/usr/bin/env bash
# Ensure taiwanjustice P2 bulk download is running. Resume-safe.
# Intended for no_agent cron every 15–30m. Silent when healthy & recent progress.
set -euo pipefail
ROOT=/home/leedt/echo-system
SCRIPT="$ROOT/scripts/taiwanjustice_wayback_bulk_download.py"
OUT="$ROOT/knowledge/web-archives/taiwanjustice-net"
PROG="$OUT/progress.json"
LOG="$OUT/watchdog.log"
mkdir -p "$OUT"

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }

alive=0
if pgrep -f "python3 $SCRIPT" >/dev/null 2>&1; then
  # confirm real python line
  while read -r line; do
    if [[ "$line" == *python3* && "$line" == *taiwanjustice_wayback_bulk_download.py* && "$line" != *pgrep* && "$line" != *watchdog* ]]; then
      alive=1
      break
    fi
  done < <(pgrep -af "taiwanjustice_wayback_bulk_download.py" 2>/dev/null || true)
fi

done_count=0
updated=""
if [[ -f "$PROG" ]]; then
  done_count=$(python3 -c "import json;print(json.load(open('$PROG')).get('done_count',0))" 2>/dev/null || echo 0)
  updated=$(python3 -c "import json;print(json.load(open('$PROG')).get('updated_at',''))" 2>/dev/null || echo "")
fi

# If alive, stay quiet unless progress very stale (>45m) while claiming alive (stuck)
if [[ "$alive" -eq 1 ]]; then
  stale_m=0
  if [[ -n "$updated" ]]; then
    stale_m=$(python3 - <<PY
from datetime import datetime, timezone
u=datetime.fromisoformat("${updated}".replace("Z","+00:00"))
print(int((datetime.now(timezone.utc)-u).total_seconds()/60))
PY
)
  fi
  if [[ "$stale_m" -lt 45 ]]; then
    exit 0  # healthy silent
  fi
  echo "$(ts) WATCHDOG: process alive but progress stale ${stale_m}m — killing and restarting (done=$done_count)" >>"$LOG"
  pkill -f "python3 $SCRIPT" 2>/dev/null || true
  sleep 2
fi

# finished?
if [[ "$done_count" -ge 59422 ]]; then
  exit 0
fi

# optional: rebuild state from manifest lightly if state missing
if [[ ! -f "$OUT/download-state.json" && -f "$OUT/DOWNLOAD_MANIFEST.jsonl" ]]; then
  python3 "$ROOT/scripts/taiwanjustice_wayback_bulk_download.py" --help >/dev/null 2>&1 || true
fi

echo "$(ts) WATCHDOG: starting downloader (done=$done_count)" >>"$LOG"
export TJ_SLEEP="${TJ_SLEEP:-0.85}" PYTHONUNBUFFERED=1
# detach fully so cron/watchdog exit doesn't kill child
nohup python3 "$SCRIPT" >>"$OUT/download.log" 2>&1 &
echo "$(ts) WATCHDOG: started pid=$!" >>"$LOG"
# notify only on restart
echo "TJ-P2 watchdog restarted downloader at $(ts) (prior done=$done_count). Log: $OUT/download.log"
