#!/bin/bash
# DEPRECATED 2026-07-06 — TauErgon echo bridges replaced by Hermes gateway native plugins.
set -euo pipefail

cat <<'EOF'
echo-bridge-* systemd units are REMOVED (2026-07-06).

Messaging is handled by:
  hermes-gateway.service     — LINE + Telegram native plugins (:8646)
  hermes-line-ngrok.service  — ngrok tunnel → :8646

Do not reinstall legacy echo-bridge-line/telegram/ngrok units.
EOF
exit 1