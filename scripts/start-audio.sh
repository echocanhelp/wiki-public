#!/bin/bash
# Start Echo voice I/O: Whisper :8002 (CPU) + XTTS :8003 (GPU, CPU fallback).
set -euo pipefail

AI_SERVICES="/home/leedt/ai-services"
cd "$AI_SERVICES"

set -a
[[ -f .env ]] && source .env
set +a

echo "=== Echo Audio Stack ==="

echo "Starting Faster Whisper (CPU, :8002)..."
docker compose up -d faster-whisper

echo "Waiting for Whisper..."
for i in $(seq 1 30); do
  if curl -sf http://localhost:8002/v1/models >/dev/null 2>&1; then
    echo "  OK Whisper ready on :8002"
    break
  fi
  sleep 2
done

start_xtts() {
  local mode=$1
  echo "Starting XTTS (:8003) mode=$mode ..."
  if [[ "$mode" == "gpu" ]]; then
    docker compose -f docker-compose.echo-tts-gpu.yml up -d
  else
    docker compose -f docker-compose.echo-tts.yml up -d
  fi
}

wait_xtts() {
  for i in $(seq 1 90); do
    if curl -sf http://localhost:8003/v1/models >/dev/null 2>&1; then
      echo "  OK XTTS ready on :8003"
      return 0
    fi
    sleep 3
  done
  return 1
}

# Try GPU first unless --cpu-only
if [[ "${1:-}" == "--cpu-only" ]]; then
  start_xtts cpu
else
  start_xtts gpu
  if ! wait_xtts; then
    echo "  GPU XTTS slow/failed — retrying CPU/piper mode..."
    docker compose -f docker-compose.echo-tts-gpu.yml down 2>/dev/null || true
    start_xtts cpu
  fi
fi

wait_xtts || echo "  WARN XTTS not responding yet — check: docker logs xtts-v2"

echo ""
echo "Done. Test TTS:"
echo "  curl -s http://localhost:8003/v1/audio/speech -H 'Content-Type: application/json' \\"
echo "    -d '{\"input\":\"Echo voice online.\",\"model\":\"tts-1-hd\",\"voice\":\"alloy\"}' -o /tmp/echo-test.wav"
echo "  aplay /tmp/echo-test.wav"
echo ""
echo "Status: $(dirname "$0")/status.sh"