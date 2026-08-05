#!/usr/bin/env bash
# echopedia-backlink-auditor-all.sh — Run backlink auditor for all people with backlinks
# Runs daily at 04:10 after works linker
set -uo pipefail

SCRIPT_DIR="$HOME/echo-system/scripts"
PYTHON="python3"

echo "=== Backlink Auditor: All People ==="
$PYTHON "$SCRIPT_DIR/echopedia-backlink-auditor.py" --all 2>&1
echo "=== Done ==="
