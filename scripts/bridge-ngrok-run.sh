#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT/bridges/.env"
BIN="${NGROK_BIN:-/home/leedt/.local/bin/ngrok}"
CONFIG="$ROOT/bridges/ngrok.yml"

# shellcheck disable=SC1090
set -a
source "$ENV_FILE"
set +a

PORT="${LINE_WEBHOOK_PORT:-8787}"
ARGS=(http "$PORT" --config="$CONFIG" --log=stdout --log-format=logfmt --pooling-enabled=true)

if [[ -n "${NGROK_DOMAIN:-}" ]]; then
  host="${NGROK_DOMAIN#https://}"
  host="${host#http://}"
  host="${host%%/*}"
  ARGS+=(--url="https://${host}")
fi

exec "$BIN" "${ARGS[@]}"