#!/bin/bash
# Install ngrok agent for LINE public webhook (linux arm64).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN="$ROOT/bridges/bin/ngrok"

mkdir -p "$ROOT/bridges/bin"

if [[ -x "$BIN" ]]; then
  echo "ngrok already installed: $($BIN version)"
  exit 0
fi

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

echo "Downloading ngrok (linux arm64) ..."
if ! curl -fsSL -o "$tmp" "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip"; then
  echo "ERROR: download failed"
  exit 1
fi
unzip -o "$tmp" -d "$ROOT/bridges/bin" ngrok
chmod +x "$BIN"
echo "Installed: $($BIN version)"