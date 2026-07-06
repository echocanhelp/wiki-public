#!/usr/bin/env bash
# Full voice loop: TTS sample → Whisper STT → hybrid Tau → speak (TTS out).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AUDIO_DIR="$ROOT/sessions/audio"
mkdir -p "$AUDIO_DIR"
STAMP=$(date +%Y%m%d-%H%M%S)
IN_WAV="$AUDIO_DIR/voice-loop-in-$STAMP.wav"
OUT_WAV="$AUDIO_DIR/voice-loop-out-$STAMP.wav"
PROMPT_TEXT="Quick Echo status check. Reply in one short sentence, then speak it aloud."

echo "=== Voice loop test ($STAMP) ==="

for svc in "8002 Whisper" "8003 TTS" "8001 LLM"; do
  port=${svc%% *}
  name=${svc#* }
  curl -sf --max-time 5 "http://127.0.0.1:${port}/v1/models" >/dev/null 2>&1 \
    || curl -sf --max-time 5 "http://127.0.0.1:${port}/health" >/dev/null 2>&1 \
    || { echo "DOWN: $name (:$port)"; exit 1; }
  echo "OK: $name"
done

echo ""
echo "=== 1. Synthesize test utterance (TTS → WAV) ==="
UTTERANCE="Echo, what tier handles quick questions?"
HTTP=$(curl -s -o "$IN_WAV" -w "%{http_code}" http://127.0.0.1:8003/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"tts-1\",\"input\":\"$UTTERANCE\",\"voice\":\"alloy\",\"response_format\":\"wav\"}")
[[ "$HTTP" == "200" ]] || { echo "TTS failed HTTP $HTTP"; exit 1; }
ls -lh "$IN_WAV"
file "$IN_WAV"

echo ""
echo "=== 2. Whisper transcribe ==="
TRANSCRIPT=$(curl -sf http://127.0.0.1:8002/v1/audio/transcriptions \
  -F "file=@${IN_WAV}" \
  -F "model=whisper-1" \
  -F "language=en" | python3 -c "import json,sys; print(json.load(sys.stdin).get('text','').strip())")
echo "Heard: $TRANSCRIPT"
[[ -n "$TRANSCRIPT" ]] || { echo "Empty transcript"; exit 1; }

echo ""
echo "=== 3. Hybrid Tau (route from transcript) ==="
TAU_OUT=$(cd "$ROOT/tauergon" && python3 src/tau.py --llm hybrid --agent echo-concierge \
  "Voice message transcript: \"$TRANSCRIPT\". $PROMPT_TEXT Use the speak tool once (model tts-1, voice alloy)." 2>&1) || true
echo "$TAU_OUT" | grep -E 'Hybrid routing|llmg:|speak\(|ASSISTANT|Speech saved|audio' | head -15

echo ""
echo "=== 4. Direct speak fallback (if agent did not produce audio) ==="
REPLY=$(echo "$TAU_OUT" | grep -oP '\[ASSISTANT\]\s*\K.*' | tail -1 || true)
if [[ -z "$REPLY" ]]; then
  REPLY="Quick questions route to cpu-light, private work stays on gx10, hard reasoning uses SuperGrok."
fi
echo "Reply snippet: ${REPLY:0:120}..."
curl -sf http://127.0.0.1:8003/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d "$(python3 -c "import json; print(json.dumps({'model':'tts-1','input':'''${REPLY:0:300}''','voice':'alloy','response_format':'wav'}))")" \
  -o "$OUT_WAV"
ls -lh "$OUT_WAV"
echo ""
echo "Done."
echo "  Input : $IN_WAV"
echo "  Output: $OUT_WAV"
echo "  Play  : aplay $OUT_WAV"