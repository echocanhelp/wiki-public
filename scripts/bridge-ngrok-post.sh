#!/bin/bash
# After ngrok starts: capture public URL, update .env, register LINE webhook.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT/bridges/.env"

for _ in $(seq 1 30); do
  url="$(curl -sf http://127.0.0.1:4040/api/tunnels 2>/dev/null | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    for t in d.get('tunnels', []):
        u = t.get('public_url', '')
        if u.startswith('https://'):
            print(u)
            break
except Exception:
    pass
" 2>/dev/null || true)"
  if [[ -n "$url" ]]; then
    base="${url%/}"
    if grep -qE '^LINE_PUBLIC_URL=' "$ENV_FILE"; then
      sed -i "s|^LINE_PUBLIC_URL=.*|LINE_PUBLIC_URL=${base}|" "$ENV_FILE"
    else
      echo "LINE_PUBLIC_URL=${base}" >>"$ENV_FILE"
    fi
    "$ROOT/scripts/set-line-webhook.sh" || true
    exit 0
  fi
  sleep 1
done

echo "WARN: ngrok tunnel URL not ready after 30s" >&2
exit 0