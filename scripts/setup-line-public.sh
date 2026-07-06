#!/bin/bash
# Expose LINE webhook via ngrok and register with LINE API.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "$ROOT/scripts/start-ngrok.sh"