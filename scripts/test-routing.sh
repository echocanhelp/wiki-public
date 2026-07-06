#!/usr/bin/env bash
# Dry-run hybrid routing classifier (no LLM calls).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/tauergon/src"

python3 - <<'PY'
from agent_llm_router import route_prompt

cases = [
    ("private", "Read my private notes in echopedia/Memory.md. Reply LOCAL only.", "hybrid", None),
    ("reasoning", "Prove step by step that sum of first n odd numbers is n squared.", "hybrid", None),
    ("quick", "Quick: what is 2+2? One line.", "hybrid", None),
    ("short", "Hello", "hybrid", None),
    ("long_private", "x" * 7000 + " summarize this private doc", "hybrid", None),
    ("orchestrator", "Plan a multi-step migration", "hybrid", "orchestrator"),
    ("explicit_cpu", "anything", "cpu-light", None),
    ("explicit_gx10", "anything", "gx10", None),
]

print("Hybrid routing dry-run")
print("-" * 60)
for name, prompt, group, agent in cases:
    resolved, reason = route_prompt(prompt, agent_id=agent, explicit_group=group)
    print(f"{name:16} -> {resolved:12} | {reason}")
PY