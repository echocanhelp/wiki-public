#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG="$ROOT/config/echo.json"

echo "=== Echo System 3.0 ==="
python3 -c "
import json
with open('$CONFIG') as f:
    c = json.load(f)
print(f\"  Version : {c['version']}\")
print(f\"  Host    : {c['host']['name']} ({c['host']['tailscale_ip']})\")
print(f\"  Migrate : {c['migration']['status']} from {c['migration']['source_host']}\")
"

check() {
  local name=$1 url=$2
  if curl -sf --max-time 3 "$url" >/dev/null 2>&1; then
    echo "  OK   $name — $url"
  else
    echo "  DOWN $name — $url"
  fi
}

echo ""
echo "=== Services ==="
LLM=$(python3 -c "import json; print(json.load(open('$CONFIG'))['services']['llm']['health'])")
WHISPER=$(python3 -c "import json; print(json.load(open('$CONFIG'))['services']['whisper']['health'])")
TTS=$(python3 -c "import json; print(json.load(open('$CONFIG'))['services']['tts']['health'])")
check "LLM (gx10)" "$LLM"
check "cpu-light" "http://localhost:8004/health"
check "Whisper" "$WHISPER"
check "TTS" "$TTS"
python3 -c "
import json, urllib.request
try:
    with open('$CONFIG') as f: c=json.load(f)
    r=c.get('services',{}).get('routing',{})
    print(f\"  Routing: {r.get('default','hybrid')} -> {r.get('local_group')}/{r.get('light_group','cpu-light')}/{r.get('cloud_group')}\")
except Exception: pass
" 2>/dev/null || true
python3 -c "
import json, urllib.request
try:
    with open('$CONFIG') as f: c=json.load(f)
    t=c['services']['tts']
    print(f\"  TTS model: {t.get('model_default','tts-1')} ({t.get('device','cpu')})\")
except Exception: pass
" 2>/dev/null || true

echo ""
echo "=== TauErgon ==="
if [[ -x "$ROOT/tauergon/src/tau.py" || -f "$ROOT/tauergon/src/tau.py" ]]; then
  echo "  OK   tau.py at $ROOT/tauergon/src/tau.py"
else
  echo "  MISS tau.py"
fi

echo ""
echo "=== Echopedia ==="
for f in Memory.md index.md; do
  if [[ -f "$ROOT/echopedia/$f" ]]; then
    echo "  OK   echopedia/$f"
  else
    echo "  MISS echopedia/$f"
  fi
done
wiki_count=$(find "$ROOT/echopedia/wiki" -name '*.md' 2>/dev/null | wc -l)
echo "  wiki pages: $wiki_count"

echo ""
echo "=== Agents ==="
ls -1 "$ROOT/agents"/*.json 2>/dev/null | xargs -I{} basename {} || echo "  none"

echo ""
echo "=== Messaging (Hermes gateway) ==="
for unit in hermes-gateway hermes-line-ngrok; do
  if systemctl --user is-active "${unit}.service" &>/dev/null; then
    echo "  RUN  ${unit}.service"
  else
    echo "  DOWN ${unit}.service ($(systemctl --user is-active "${unit}.service" 2>/dev/null || echo inactive))"
  fi
done
check "Hermes gateway" "http://127.0.0.1:8646/health"
BRIDGE_ENV="$ROOT/bridges/.env"
if [[ -f "$BRIDGE_ENV" ]] && command -v curl >/dev/null && grep -qE '^LINE_CHANNEL_ACCESS_TOKEN=' "$BRIDGE_ENV" 2>/dev/null; then
  line_token=$(grep -E '^LINE_CHANNEL_ACCESS_TOKEN=' "$BRIDGE_ENV" | tail -1 | cut -d= -f2-)
  registered=$(curl -sf --max-time 5 "https://api.line.me/v2/bot/channel/webhook/endpoint" \
    -H "Authorization: Bearer ${line_token}" 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('endpoint','?'))" 2>/dev/null || echo "unreachable")
  echo "  LINE registered webhook: $registered"
fi