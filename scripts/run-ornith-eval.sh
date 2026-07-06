#!/bin/bash
# TauErgon evaluation harness for Ornith on Echo 3.0
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TAU="$ROOT/tauergon/src/tau.py"
LOG="$ROOT/logs/ornith-eval-$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$ROOT/logs"

run_test() {
  local id=$1 prompt=$2
  echo "========== TEST $id ==========" | tee -a "$LOG"
  echo "PROMPT: $prompt" | tee -a "$LOG"
  cd "$ROOT/tauergon"
  timeout 300 python3 "$TAU" --llm gx10 "$prompt" 2>&1 | tee -a "$LOG" || echo "TEST $id: TIMEOUT or ERROR" | tee -a "$LOG"
  echo "" | tee -a "$LOG"
}

echo "Ornith eval started $(date -Is)" | tee "$LOG"

run_test 1 "You are Echo concierge. In 2-3 sentences, explain what Echo System 3.0 is and which LLM powers it today. Be concise."

run_test 2 "You are the Echo researcher agent. Read /home/leedt/echo-system/echopedia/Memory.md and /home/leedt/echo-system/echopedia/wiki/System.md using file_read. Summarize: (a) current inference backend, (b) GB10 constraints, (c) migration status. Output a bullet list only."

run_test 3 "Create a new Echopedia wiki page at /home/leedt/echo-system/echopedia/wiki/Ornith-Eval.md with: title Ornith Evaluation, date $(date +%Y-%m-%d), sections Purpose, Model, and Status noting Ornith 35B NVFP4 is primary on port 8001. Use file_write. Then file_read the file to confirm."

run_test 4 "Solve step by step: A GX10 has 121 GiB unified memory. vLLM uses 0.80 gpu-memory-utilization. Ornith weights are ~24 GB. Roughly how much headroom remains for KV cache and OS if weights+overhead consume ~30 GB? Show arithmetic, then one-sentence conclusion."

run_test 5 "Use bash to run: echo ornith-tool-ok && ls -1 /home/leedt/echo-system/agents/*.json | wc -l. Report the exact command output. Use the bash tool once only."

echo "Eval complete. Log: $LOG"