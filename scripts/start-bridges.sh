#!/bin/bash
# DEPRECATED 2026-07-06 — TauErgon echo bridges replaced by Hermes gateway native plugins.
set -euo pipefail

cat <<'EOF'
Legacy Echo bridges are retired. Use Hermes gateway instead:

  systemctl --user status hermes-gateway.service
  systemctl --user status hermes-line-ngrok.service

Restart if needed (from host shell):
  hermes gateway restart
EOF
exit 1