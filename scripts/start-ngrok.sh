#!/bin/bash
# Start ngrok tunnel to LINE webhook port; update LINE_PUBLIC_URL and register webhook.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT/bridges/.env"
BIN="${NGROK_BIN:-/home/leedt/.local/bin/ngrok}"
if [[ ! -x "$BIN" ]]; then
  BIN="$ROOT/bridges/bin/ngrok"
fi
PIDFILE="$ROOT/bridges/pids/ngrok.pid"
LOG="$ROOT/bridges/logs/ngrok.log"
CONFIG="$ROOT/bridges/ngrok.yml"

_url_from_api() {
  local url=""
  for _ in $(seq 1 20); do
    url="$(curl -sf http://127.0.0.1:4040/api/tunnels 2>/dev/null | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    for t in d.get('tunnels',[]):
        u=t.get('public_url') or t.get('uri','')
        if u.startswith('https://'):
            print(u)
            break
except Exception:
    pass
" 2>/dev/null || true)"
    if [[ -n "$url" ]]; then
      break
    fi
    sleep 1
  done
  if [[ -z "$url" ]]; then
    echo "ERROR: ngrok started but no public URL yet — check $LOG"
    tail -5 "$LOG" 2>/dev/null || true
    return 1
  fi
  local base="${url%/}"
  if grep -qE '^LINE_PUBLIC_URL=' "$ENV_FILE"; then
    sed -i "s|^LINE_PUBLIC_URL=.*|LINE_PUBLIC_URL=${base}|" "$ENV_FILE"
  else
    echo "LINE_PUBLIC_URL=${base}" >>"$ENV_FILE"
  fi
  echo "  URL  $base"
  "$ROOT/scripts/set-line-webhook.sh"
}

if [[ ! -x "$BIN" ]]; then
  "$ROOT/scripts/install-ngrok.sh"
fi

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: $ENV_FILE missing"
  exit 1
fi

# shellcheck disable=SC1090
set -a
source "$ENV_FILE"
set +a

if [[ -z "${NGROK_AUTHTOKEN:-}" ]]; then
  echo "ERROR: NGROK_AUTHTOKEN missing in $ENV_FILE"
  echo ""
  echo "Add your ngrok authtoken (same account that owns the Echo domain):"
  echo "  1. https://dashboard.ngrok.com/get-started/your-authtoken"
  echo "  2. Edit $ENV_FILE and set NGROK_AUTHTOKEN=..."
  echo "  3. Re-run: $ROOT/scripts/start-ngrok.sh"
  exit 1
fi

PORT="${LINE_WEBHOOK_PORT:-8787}"
DOMAIN="${NGROK_DOMAIN:-}"

mkdir -p "$(dirname "$CONFIG")" "$(dirname "$LOG")"

if [[ -f "$PIDFILE" ]] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
  echo "  RUN  ngrok pid=$(cat "$PIDFILE")"
  _url_from_api || true
  exit 0
fi

"$BIN" authtoken "$NGROK_AUTHTOKEN" --config="$CONFIG" >/dev/null 2>&1 || \
  "$BIN" authtoken "$NGROK_AUTHTOKEN" >/dev/null

ARGS=(http "$PORT" --log=stdout --log-format=logfmt --config="$CONFIG" --pooling-enabled=true)
if [[ -n "$DOMAIN" ]]; then
  host="${DOMAIN#https://}"
  host="${host#http://}"
  host="${host%%/*}"
  ARGS+=(--url="https://${host}")
  echo "Starting ngrok → $host:$PORT (pooling enabled)"
else
  echo "Starting ngrok → auto URL on port $PORT"
fi

nohup "$BIN" "${ARGS[@]}" >>"$LOG" 2>&1 &
echo $! >"$PIDFILE"
echo "  START ngrok pid=$(cat "$PIDFILE") log=$LOG"

_url_from_api