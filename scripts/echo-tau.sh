#!/bin/bash
# Launch TauErgon with Echo System 3.0 config.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/tauergon"
exec python3 src/tau.py --llm gx10 "$@"