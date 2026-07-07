#!/bin/bash
# Stop legacy nohup bridge processes (if any). Systemd echo-bridge units removed 2026-07-06.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PIDS="$ROOT/bridges/pids"

_stop() {
  local name=$1
  local pidfile="$PIDS/${name}.pid"
  if [[ ! -f "$pidfile" ]]; then
    echo "  --   $name (not running)"
    return
  fi
  local pid
  pid="$(cat "$pidfile")"
  if kill -0 "$pid" 2>/dev/null; then
    kill "$pid" 2>/dev/null || true
    for _ in $(seq 1 30); do
      kill -0 "$pid" 2>/dev/null || break
      sleep 1
    done
    if kill -0 "$pid" 2>/dev/null; then
      kill -9 "$pid" 2>/dev/null || true
      echo "  KILL $name pid=$pid"
    else
      echo "  STOP $name pid=$pid"
    fi
  else
    echo "  --   $name stale pid=$pid"
  fi
  rm -f "$pidfile"
}

_stop_ngrok() {
  local pidfile="$PIDS/ngrok.pid"
  if [[ ! -f "$pidfile" ]]; then
    echo "  --   ngrok (not running)"
    return
  fi
  local pid
  pid="$(cat "$pidfile")"
  if kill -0 "$pid" 2>/dev/null; then
    kill "$pid" 2>/dev/null || true
    echo "  STOP ngrok pid=$pid"
  else
    echo "  --   ngrok stale pid=$pid"
  fi
  rm -f "$pidfile"
}

echo "=== Stopping legacy Echo bridge processes (nohup only) ==="
_stop telegram
_stop line
_stop_ngrok