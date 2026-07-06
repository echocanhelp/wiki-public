#!/usr/bin/env bash
set -euo pipefail

LOG="/root/.hermes/profiles/echohsu/logs/agent.log"
STATE_DIR="/root/.hermes/profiles/echohsu/cron/state"
STATE_FILE="$STATE_DIR/codex_hardfail_watchdog.state"
mkdir -p "$STATE_DIR"

if [[ ! -f "$LOG" ]]; then
  exit 0
fi

total_lines=$(wc -l < "$LOG" || echo 0)
last_line=0
if [[ -f "$STATE_FILE" ]]; then
  last_line=$(cat "$STATE_FILE" 2>/dev/null || echo 0)
fi

if ! [[ "$last_line" =~ ^[0-9]+$ ]]; then
  last_line=0
fi

if (( last_line > total_lines )); then
  last_line=0
fi

start=$((last_line + 1))
new_chunk=$(sed -n "${start},${total_lines}p" "$LOG" || true)

echo "$total_lines" > "$STATE_FILE"

if [[ -z "$new_chunk" ]]; then
  exit 0
fi

hits=$(printf '%s\n' "$new_chunk" | grep -E "Invalid API response after 3 retries|Codex response remained incomplete after 3 continuation attempts|Non-retryable client error: 'NoneType' object is not iterable" || true)

if [[ -z "$hits" ]]; then
  exit 0
fi

printf 'ALERT: codex hard-failure signatures detected in echohsu agent.log\n\n'
printf '%s\n' "$hits" | tail -n 40
