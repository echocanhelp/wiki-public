#!/bin/bash
# Import LINE/Telegram tokens from legacy Hermes profile into bridges/.env
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEGACY_ENV="$ROOT/echopedia/ingest/legacy-jr2/root/.hermes/profiles/echohsu/.env"
BRIDGE_ENV="$ROOT/bridges/.env"
EXAMPLE="$ROOT/bridges/.env.example"

if [[ ! -f "$LEGACY_ENV" ]]; then
  echo "ERROR: legacy .env not found at $LEGACY_ENV"
  exit 1
fi

if [[ ! -f "$BRIDGE_ENV" ]]; then
  cp "$EXAMPLE" "$BRIDGE_ENV"
  echo "Created $BRIDGE_ENV from example"
fi

_import_var() {
  local key=$1
  local value
  value="$(grep -E "^${key}=" "$LEGACY_ENV" | tail -1 | cut -d= -f2- || true)"
  if [[ -z "$value" ]]; then
    return
  fi
  if grep -qE "^${key}=" "$BRIDGE_ENV"; then
    sed -i "s|^${key}=.*|${key}=${value}|" "$BRIDGE_ENV"
  else
    echo "${key}=${value}" >> "$BRIDGE_ENV"
  fi
}

for key in \
  TELEGRAM_BOT_TOKEN TELEGRAM_ALLOWED_USERS TELEGRAM_HOME_CHANNEL \
  LINE_CHANNEL_ID LINE_CHANNEL_SECRET LINE_CHANNEL_ACCESS_TOKEN \
  LINE_ALLOWED_GROUPS LINE_ALLOW_ALL_USERS LINE_ALLOWED_USERS LINE_PUBLIC_URL \
  API_SERVER_KEY NGROK_AUTHTOKEN NGROK_DOMAIN; do
  _import_var "$key"
done

if ! grep -qE '^NGROK_DOMAIN=.+' "$BRIDGE_ENV"; then
  echo "NGROK_DOMAIN=bucked-diabetes-shucking.ngrok-free.dev" >> "$BRIDGE_ENV"
fi

# Map legacy API key to bridge admin key
if grep -qE '^API_SERVER_KEY=.+' "$LEGACY_ENV"; then
  api_key="$(grep -E '^API_SERVER_KEY=' "$LEGACY_ENV" | tail -1 | cut -d= -f2-)"
  if grep -qE '^BRIDGE_ADMIN_KEY=' "$BRIDGE_ENV"; then
    sed -i "s|^BRIDGE_ADMIN_KEY=.*|BRIDGE_ADMIN_KEY=${api_key}|" "$BRIDGE_ENV"
  else
    echo "BRIDGE_ADMIN_KEY=${api_key}" >> "$BRIDGE_ENV"
  fi
fi

# LINE does not use X-Bridge-Key from LINE servers — keep empty
if grep -qE '^LINE_WEBHOOK_BRIDGE_KEY=' "$BRIDGE_ENV"; then
  sed -i 's|^LINE_WEBHOOK_BRIDGE_KEY=.*|LINE_WEBHOOK_BRIDGE_KEY=|' "$BRIDGE_ENV"
fi

chmod 600 "$BRIDGE_ENV"
echo "Imported messaging tokens into $BRIDGE_ENV (mode 600)"
echo "Review LINE_PUBLIC_URL — update for pinto (Tailscale Funnel or ngrok)."