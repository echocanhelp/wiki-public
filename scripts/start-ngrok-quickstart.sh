#!/bin/bash
# ngrok Agent CLI quickstart: OAuth-protected HTTP server on :8080
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PATH="/home/leedt/.local/bin:$PATH"

echo "=== ngrok quickstart ==="

if ! command -v ngrok >/dev/null; then
  echo "Installing ngrok v3 ..."
  curl -fsSL -o /tmp/ngrok.deb "https://ngrok-agent.s3.amazonaws.com/pool/main/n/ngrok/ngrok_3.39.9-0_arm64.deb"
  dpkg-deb -x /tmp/ngrok.deb /tmp/ngrok-deb-extract
  install -m 755 /tmp/ngrok-deb-extract/usr/local/bin/ngrok /home/leedt/.local/bin/ngrok
fi

# HTTP server on 8080
if ! curl -sf --max-time 2 http://127.0.0.1:8080/ >/dev/null 2>&1; then
  nohup python3 "$ROOT/bridges/quickstart/service.py" >>"$ROOT/bridges/logs/quickstart-8080.log" 2>&1 &
  echo $! >"$ROOT/bridges/pids/quickstart-8080.pid"
  sleep 1
fi
echo "  OK   HTTP server :8080"

PIDFILE="$ROOT/bridges/pids/ngrok-quickstart.pid"
if [[ -f "$PIDFILE" ]] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
  echo "  RUN  ngrok cli-quickstart pid=$(cat "$PIDFILE")"
  exit 0
fi

echo "Starting ngrok start cli-quickstart ..."
nohup ngrok start cli-quickstart --log=stdout --log-format=logfmt \
  >>"$ROOT/bridges/logs/ngrok-quickstart.log" 2>&1 &
echo $! >"$PIDFILE"
sleep 3

if ! kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
  echo "  FAIL ngrok exited — likely jr2 still holds reserved domain"
  tail -6 "$ROOT/bridges/logs/ngrok-quickstart.log" 2>/dev/null || true
  echo ""
  echo "Stop ngrok on jr2, then re-run this script."
  exit 1
fi

URL=$(curl -sf http://127.0.0.1:4040/api/tunnels 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)
for t in d.get('tunnels',[]):
    u=t.get('public_url','')
    if u.startswith('https://'):
        print(u); break
" 2>/dev/null || echo "https://bucked-diabetes-shucking.ngrok-free.dev")

echo "  OK   ngrok pid=$(cat "$PIDFILE")"
echo "  URL  $URL (expect Google OAuth login in browser)"