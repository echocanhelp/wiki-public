# Echo / Hermes Hybrid Model Architecture (pinto)

**Status:** Active (updated 2026-07-06)  
**Host:** pinto (ASUS Ascent GX10, NVIDIA GB10, LAN `192.168.7.1`)  
**Agent runtime:** Hermes Agent (Echo System 3.0 deprecated)

## Goals

| Lane | When | Backend |
|------|------|---------|
| **Frontier** | Hard reasoning, multi-step design/build | **xai-oauth** (`grok-composer-2.5-fast`) via `/model`, delegation, or vision |
| **Private LAN** | PII, credentials, TAHS/community files, echopedia, local paths | **custom:pinto** — vLLM **35B NVFP4** @ `http://127.0.0.1:8001/v1` |
| **Modality uplift** | Vision when LAN model cannot see | **xai-oauth** (`auxiliary.vision`) |

**Deprecated (2026-07-06):** Emergency CPU tier @ :8004 (qwen3-8b-cpu llama.cpp) — removed to free RAM. No LAN inference fallback when GPU is down.

**Non-goals:** Sending private corpus to frontier by default; running GPU + heavy aux services concurrently on GB10 (`gpu-memory-utilization` **0.60**).

---

## Logical architecture

```
                    ┌─────────────────────────────────────┐
                    │         User / LINE / Telegram       │
                    └──────────────────┬──────────────────┘
                                       │
                    ┌──────────────────▼──────────────────┐
                    │   Hermes gateway + agent loop        │
                    │   (memory, soul, skills, sessions)   │
                    └──────────────────┬──────────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
     ┌────────▼────────┐    ┌─────────▼─────────┐   ┌────────▼────────┐
     │  Policy layer    │    │  Main LLM slot     │   │  Auxiliary slot  │
     │  (SOUL + skills) │───▶│  model.default     │   │  vision, compress│
     └─────────────────┘    │  + /model override │   │  delegation      │
                              └─────────┬─────────┘   └────────┬────────┘
                                        │                      │
                    ┌───────────────────┼──────────────────────┘
                    │                   │
         ┌──────────▼──────────┐ ┌──────▼──────┐
         │ Tier A: Frontier     │ │ Tier B: LAN │
         │ xai-oauth / Grok     │ │ 35B :8001   │
         └─────────────────────┘ └─────────────┘
```

---

## Tier definitions

### Tier A — Frontier (xai-oauth)

Architecture, trade-offs, large refactors, web research, vision analysis. User-directed via `/model`, `delegation.*`, or `auxiliary.vision`. **Public data only** unless user explicitly opts in.

### Tier B — Private LAN (35B NVFP4 @ :8001)

Default for TAHS/community ops, echopedia, credentials, LINE/Telegram. Hermes mapping: `custom_providers.pinto` → `http://127.0.0.1:8001/v1`.

---

## Outage behavior

| Component | Behavior |
|-----------|----------|
| `fallback_providers` | **Empty** — no CPU, no auto-cloud for main chat |
| `health-guard.sh` | Restarts `vllm-qwen36.service` when :8001 down |
| `auxiliary.compression.fallback_chain` | Grok when :8001 unreachable (64K+ only) |
| User action | `/model` xai-oauth for manual cloud switch |

---

## Hermes wiring (concrete)

```yaml
model:
  default: nvidia/Qwen3.6-35B-A3B-NVFP4
  provider: custom:pinto

custom_providers:
  - name: pinto
    base_url: http://127.0.0.1:8001/v1
    api_key: pinto
    model: nvidia/Qwen3.6-35B-A3B-NVFP4

auxiliary:
  compression:
    provider: custom:pinto
    model: nvidia/Qwen3.6-35B-A3B-NVFP4
    fallback_chain:
      - provider: xai-oauth
        model: grok-composer-2.5-fast
  vision:
    provider: xai-oauth

delegation:
  provider: xai-oauth
  model: grok-composer-2.5-fast
```

---

## Operational playbook (pinto / GB10)

1. **One heavy GPU consumer:** vLLM at `gpu-memory-utilization 0.60` (~72 GiB of 121 GiB unified).
2. **LINE/Telegram** via native Hermes gateway (:8646) for memory/soul.
3. **Health:** `health-guard.sh` pings :8001 + gateway :8646 every 10m.
4. **Secret handling:** `security.redact_secrets: true`; frontier gets sanitized briefs only.

---

## One-line summary

**Private text on 35B LAN, hard building on Grok (OAuth/delegation), broken GPU → health-guard restart + refuse (no auto-exfiltration), vision on Grok auxiliary.**