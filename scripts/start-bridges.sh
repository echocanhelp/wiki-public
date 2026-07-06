#!/bin/bash
# Start Echo LINE (webhook) and Telegram (polling) bridges
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if systemctl --user list-unit-files echo-bridges.target &>/dev/null && \
   systemctl --user list-unit-files echo-bridges.target 2>/dev/null | grep -q echo-bridges.target; then
  echo "=== Echo Bridges (systemd) ==="
  systemctl --user start echo-bridges.target
  systemctl --user --no-pager status echo-bridge-telegram.service echo-bridge-line.service echo-bridge-ngrok.service || true
  exit 0
fi
BRIDGES="$ROOT/bridges"
VENV="$BRIDGES/.venv"
LOGS="$BRIDGES/logs"
PIDS="$BRIDGES/pids"
ENV_FILE="$BRIDGES/.env"

mkdir -p "$LOGS" "$PIDS"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing $ENV_FILE — run: $ROOT/scripts/import-bridge-env.sh"
  exit 1
fi

if [[ ! -d "$VENV" ]]; then
  echo "Creating bridge venv..."
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q -r "$BRIDGES/requirements.txt"
fi

# shellcheck disable=SC1091
source "$VENV/bin/activate"

_start() {
  local name=$1 script=$2
  local pidfile="$PIDS/${name}.pid"
  local logfile="$LOGS/${name}.log"
  if [[ -f "$pidfile" ]] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo "  RUN  $name (pid $(cat "$pidfile"))"
    return
  fi
  nohup python3 "$script" >>"$logfile" 2>&1 &
  echo $! >"$pidfile"
  echo "  START $name pid=$(cat "$pidfile") log=$logfile"
}

echo "=== Echo Bridges ==="

TELEGRAM_ENABLED=$(grep -E '^TELEGRAM_ENABLED=' "$ENV_FILE" | tail -1 | cut -d= -f2- || echo true)
LINE_ENABLED=$(grep -E '^LINE_ENABLED=' "$ENV_FILE" | tail -1 | cut -d= -f2- || echo true)

if [[ "${TELEGRAM_ENABLED,,}" != "false" ]]; then
  _start telegram "$BRIDGES/telegram/bridge.py"
else
  echo "  SKIP telegram (TELEGRAM_ENABLED=false)"
fi

if [[ "${LINE_ENABLED,,}" != "false" ]]; then
  _start line "$BRIDGES/line/bridge.py"
  if grep -qE '^NGROK_AUTHTOKEN=.+' "$ENV_FILE" 2>/dev/null; then
    "$ROOT/scripts/start-ngrok.sh" || echo "  WARN ngrok failed — set NGROK_AUTHTOKEN in bridges/.env"
  else
    echo "  SKIP ngrok (NGROK_AUTHTOKEN not set — LINE webhook needs public URL)"
    echo "        Run: $ROOT/scripts/start-ngrok.sh after adding token"
  fi
else
  echo "  SKIP line (LINE_ENABLED=false)"
fi

echo ""
echo "Status: $ROOT/scripts/status.sh"
echo "Logs:   tail -f $LOGS/telegram.log $LOGS/line.log"
echo "Stop:   $ROOT/scripts/stop-bridges.sh"