#!/bin/bash
# Install systemd user units for Echo bridges (boot + crash recovery).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
USER_UNIT_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user"
SRC="$ROOT/systemd"

mkdir -p "$USER_UNIT_DIR" "$ROOT/bridges/logs" "$ROOT/bridges/pids"
chmod +x "$ROOT/scripts/bridge-ngrok-post.sh"

for unit in echo-bridges.target echo-bridge-telegram.service echo-bridge-line.service echo-bridge-ngrok.service; do
  install -m 0644 "$SRC/$unit" "$USER_UNIT_DIR/$unit"
  echo "  installed $unit"
done

# Stop legacy nohup processes if any
"$ROOT/scripts/stop-bridges.sh" 2>/dev/null || true

systemctl --user daemon-reload
systemctl --user enable echo-bridges.target
systemctl --user enable echo-bridge-telegram.service echo-bridge-line.service echo-bridge-ngrok.service

if [[ "${1:-}" == "--no-start" ]]; then
  echo "Enabled (not started). Run: systemctl --user start echo-bridges.target"
  exit 0
fi

systemctl --user start echo-bridges.target
sleep 3
systemctl --user --no-pager status echo-bridge-telegram.service echo-bridge-line.service echo-bridge-ngrok.service || true

echo ""
echo "=== Boot persistence (linger) ==="
linger=$(loginctl show-user "$USER" -p Linger --value 2>/dev/null || echo no)
if [[ "$linger" == "yes" ]]; then
  echo "  OK   linger enabled — bridges start at boot without login"
else
  if loginctl enable-linger "$USER" 2>/dev/null; then
    echo "  OK   linger enabled"
  elif sudo -n loginctl enable-linger "$USER" 2>/dev/null; then
    echo "  OK   linger enabled (sudo)"
  else
    echo "  WARN linger not enabled — bridges only start after you log in"
    echo "  Run: loginctl enable-linger $USER"
    echo "    or: sudo loginctl enable-linger $USER"
  fi
fi

echo ""
echo "Status: $ROOT/scripts/status.sh"