#!/bin/bash
# Register LINE webhook URL (requires LINE_PUBLIC_URL in bridges/.env)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT/bridges/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: $ENV_FILE missing"
  exit 1
fi

# shellcheck disable=SC1090
source "$ENV_FILE"

if [[ -z "${LINE_CHANNEL_ACCESS_TOKEN:-}" ]]; then
  echo "ERROR: LINE_CHANNEL_ACCESS_TOKEN missing"
  exit 1
fi
if [[ -z "${LINE_PUBLIC_URL:-}" ]]; then
  echo "ERROR: LINE_PUBLIC_URL missing — set Tailscale Funnel or ngrok HTTPS URL"
  echo "  Example funnel: tailscale funnel --bg 8787"
  echo "  Then: LINE_PUBLIC_URL=https://pinto.tail31b2c.ts.net"
  exit 1
fi

PATH_PART="${LINE_WEBHOOK_PATH:-/line/webhook}"
WEBHOOK_URL="${LINE_PUBLIC_URL%/}${PATH_PART}"

echo "Setting LINE webhook → $WEBHOOK_URL"
curl -sf -X PUT "https://api.line.me/v2/bot/channel/webhook/endpoint" \
  -H "Authorization: Bearer ${LINE_CHANNEL_ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"endpoint\":\"${WEBHOOK_URL}\"}"

echo ""
curl -sf "https://api.line.me/v2/bot/channel/webhook/endpoint" \
  -H "Authorization: Bearer ${LINE_CHANNEL_ACCESS_TOKEN}" | python3 -m json.tool