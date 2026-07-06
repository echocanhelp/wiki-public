#!/bin/bash
# Test Echo voice: direct TTS + TauErgon speak tool (migration summary).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AUDIO_DIR="$ROOT/sessions/audio"
mkdir -p "$AUDIO_DIR"

MIGRATION_TEXT="Echo System 3.0 migrated to pinto on July second, twenty twenty-six. Legacy knowledge imported. Ornith thirty-five B powers inference on port eight thousand one."

echo "=== 1. Direct TTS API (:8003) ==="
OUT="/tmp/echo-migration-summary.wav"
MODEL="${TTS_MODEL:-tts-1-hd}"

if ! curl -sf http://localhost:8003/v1/models >/dev/null 2>&1; then
  echo "XTTS not ready on :8003"
  exit 1
fi

HTTP_CODE=$(curl -s -o "$OUT" -w "%{http_code}" http://localhost:8003/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$MODEL\",\"input\":\"$MIGRATION_TEXT\",\"voice\":\"alloy\",\"response_format\":\"wav\"}")

if [[ "$HTTP_CODE" != "200" ]]; then
  echo "tts-1-hd failed (HTTP $HTTP_CODE), trying tts-1 CPU fallback..."
  MODEL=tts-1
  curl -sf http://localhost:8003/v1/audio/speech \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$MODEL\",\"input\":\"$MIGRATION_TEXT\",\"voice\":\"alloy\",\"response_format\":\"wav\"}" \
    -o "$OUT"
fi

ls -lh "$OUT"
file "$OUT"
echo "Play: aplay $OUT"

echo ""
echo "=== 2. TauErgon speak tool ==="
cd "$ROOT/tauergon"
python3 src/tau.py --llm gx10 \
  "You are Echo concierge. Read wiki/GX10-Migration.md from echopedia, then use speak to say a one-sentence spoken summary of the migration. Use speak once only."

echo ""
echo "=== 3. Latest session audio ==="
ls -lt "$AUDIO_DIR" 2>/dev/null | head -5 || echo "No session audio yet"