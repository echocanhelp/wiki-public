#!/usr/bin/env bash
# Quick LLM throughput benchmark (qwen36, gemma2-2b, or any OpenAI-compatible endpoint)
# Usage: benchmark-llm.sh [model] [base_url]
#   benchmark-llm.sh all   — benchmark gx10 + cpu-light if reachable
set -euo pipefail
MODEL="${1:-qwen36}"
URL="${2:-http://localhost:8001/v1}"

if [[ "$MODEL" == "all" ]]; then
  echo "=== gx10 (qwen36) ==="
  "$0" qwen36 http://localhost:8001/v1 || echo "gx10: unreachable"
  echo ""
  echo "=== cpu-light (gemma2-2b) ==="
  "$0" gemma2-2b http://localhost:8004/v1 || echo "cpu-light: unreachable"
  exit 0
fi
python3 - "$MODEL" "$URL" << 'PY'
import json, sys, time, urllib.request

model, base = sys.argv[1], sys.argv[2].rstrip("/")

def bench(label, prompt, max_tokens=128):
    data = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "stream": False,
        "chat_template_kwargs": {"enable_thinking": False},
    }).encode()
    req = urllib.request.Request(
        f"{base}/chat/completions",
        data=data,
        headers={"Content-Type": "application/json", "Authorization": "Bearer local"},
        method="POST",
    )
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=600) as r:
        body = json.loads(r.read())
    elapsed = time.perf_counter() - t0
    usage = body.get("usage", {})
    out_toks = usage.get("completion_tokens", 0)
    in_toks = usage.get("prompt_tokens", 0)
    tps = out_toks / elapsed if elapsed > 0 else 0
    print(f"{label}: {in_toks} in / {out_toks} out in {elapsed:.2f}s => {tps:.1f} tok/s gen")

print(f"Benchmark {model} @ {base}")
bench("short", "Count from 1 to 30, one number per line.")
bench("reasoning", "Solve step by step: What is 17*23? Show work then answer.")
PY