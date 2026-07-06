#!/usr/bin/env bash
# Fresh xAI OAuth PKCE login for SuperGrok subscription (no API key).
# Uses Grok CLI OAuth flow, then syncs tokens into echo-system config.
set -euo pipefail

ROOT="/home/leedt/echo-system"
GROK="${GROK_BIN:-/home/leedt/.local/bin/grok}"

echo "=== xAI OAuth login (SuperGrok) ==="
echo "This opens a browser PKCE flow via Grok CLI, then syncs to echo-system."

if [[ ! -x "$GROK" ]]; then
  echo "ERROR: grok CLI not found at $GROK"
  exit 1
fi

"$GROK" login --oauth

python3 << 'PY'
import sys
sys.path.insert(0, "/home/leedt/echo-system/tauergon/src")
from agent_xai_oauth import import_from_grok_cli, ECHO_OAUTH_PATH

data = import_from_grok_cli()
if not data:
    print("ERROR: failed to import OAuth tokens from ~/.grok/auth.json")
    sys.exit(1)
email = data.get("email", "(unknown)")
print(f"OK: synced xAI OAuth to {ECHO_OAUTH_PATH} for {email}")
PY

echo "Test token refresh:"
python3 << 'PY'
import sys
sys.path.insert(0, "/home/leedt/echo-system/tauergon/src")
from agent_xai_oauth import get_access_token
tok = get_access_token()
print(f"access_token length: {len(tok)} (valid)")
PY