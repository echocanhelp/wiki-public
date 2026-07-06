# Echo / Hermes Hybrid Model Architecture (pinto)

**Status:** Design (2026-07-05)  
**Host:** pinto (ASUS Ascent GX10, NVIDIA GB10, LAN `192.168.7.1`)  
**Agent runtime:** Hermes Agent (Echo System 3.0 deprecated)

## Goals

| Lane | When | Backend |
|------|------|---------|
| **Frontier** | Hard reasoning, multi-step design/build, weak local model | **xai-oauth** (`grok-composer-2.5-fast` or successor) |
| **Private LAN** | PII, credentials, TAHS/community files, echopedia, local paths | **custom:pinto** — vLLM **qwen36** @ `http://192.168.7.1:8001/v1` |
| **Emergency CPU** | GPU vLLM down, OOM, 96% GPU, or LAN unreachable | **custom:pinto-cpu** — gemma2 (or equivalent) @ `http://192.168.7.1:8004/v1` |
| **Modality uplift** | Vision / native multimodal turn when LAN model cannot see/hear | **xai-oauth** (main turn or `auxiliary.vision`) |

**Non-goals:** Sending private corpus to frontier by default; running GPU + heavy aux services concurrently on GB10 (keep `gpu-memory-utilization` ≤ 0.80).

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
     │  (see below)     │───▶│  model.default     │   │  vision, STT→   │
     └─────────────────┘    │  + /model override │   │  text, compress  │
                              └─────────┬─────────┘   └────────┬────────┘
                                        │                      │
                    ┌───────────────────┼──────────────────────┘
                    │                   │
         ┌──────────▼──────────┐ ┌──────▼──────┐ ┌──────────────▼────────────┐
         │ Tier A: Frontier     │ │ Tier B: LAN │ │ Tier C: Emergency CPU      │
         │ xai-oauth / Grok     │ │ qwen36 :8001│ │ CPU model :8004           │
         └─────────────────────┘ └─────────────┘ └───────────────────────────┘
```

**Policy layer** is the piece Echo had in `config/routing.json` (keyword/path scoring). Hermes does **not** ship that router today; you implement it as **convention + ops** (phases below), optionally a small router skill or gateway hook later.

---

## Tier definitions

### Tier A — Frontier (xai-oauth)

**Use for:**

- Architecture and trade-off analysis (“design hybrid…”, “compare approaches”)
- Large refactors, greenfield builds, debugging subtle cross-service bugs
- Tasks where tool-heavy loops need strong instruction following
- **Multimodal** when the turn requires the **main** model to reason over images/video the LAN stack cannot attach to qwen36

**Avoid sending (keep on Tier B):**

- Raw `.env`, bridge secrets, member PII, full echopedia dumps
- Long pasted transcripts that include credentials (compress or redact first)

**Hermes mapping:** `model.provider: xai-oauth`, `model.default: grok-composer-2.5-fast`

---

### Tier B — Private LAN (qwen36 @ :8001)

**Use for:**

- Day-to-day TAHS / community ops, LINE/Telegram replies with **memory + soul** already in Hermes
- Reading/writing under `/home/leedt/echo-system`, echopedia, local bridges archive
- Anything the user marks “stay local”, “private”, “on pinto”
- Long context that should not leave the LAN (subject to model context window)

**Hermes mapping:** `custom_providers` entry `pinto` → `http://192.168.7.1:8001/v1`, model `qwen36`  
Switch for a session: `/model` → custom pinto / qwen36

**Echo `routing.json` alignment:** `local_signals.keywords` + `path_patterns` are the authoritative list of “force local” intents.

---

### Tier C — Emergency CPU (:8004)

**Use when:**

- `curl http://192.168.7.1:8001/v1/models` fails or hangs
- GPU saturated (vLLM OOM / zombie process) and you need **degraded but up** replies
- Scheduled watchdog cron reports LAN unhealthy

**Hermes mapping:** second `custom_providers` entry (name e.g. `pinto-cpu`), base URL **`http://192.168.7.1:8004/v1`** (no extra `:` in path)  
**Availability chain:** first entry in `fallback_providers` should be **LAN**, second **CPU**, not frontier — frontier is a policy choice, not an outage fallback (see below).

---

## Modality (vision / voice / audio / video)

| Capability | Local qwen36 | Hermes today | Recommended |
|------------|--------------|--------------|-------------|
| Text chat | ✓ | Main model | Tier B default for private threads |
| STT (voice → text) | N/A (Whisper service) | `stt` local/groq | Prefer **local Whisper** when GPU allows; text then Tier B |
| Vision analyze | ✗ on main | `vision_analyze` + `auxiliary.vision` | Pin `auxiliary.vision` to **xai-oauth** + Grok vision-capable model **or** use frontier as main for that session |
| Image gen | N/A | FAL / etc. | Non-private prompts OK on cloud; private prompts → describe locally, generate only if user approves |
| LINE audio reply | TTS pipeline | `tts` + platform | Keep media on LAN; don’t route audio bytes to Grok |

**Rule:** *Transcribe locally when possible → reason on text locally if private → only attach pixels/audio to frontier when user intent is non-sensitive or user explicitly opts into cloud vision.*

---

## Hermes wiring (concrete)

### 1. Custom providers (`~/.hermes/config.yaml`)

```yaml
custom_providers:
  - name: pinto
    base_url: http://192.168.7.1:8001/v1
    api_key: pinto
    model: qwen36
  - name: pinto-cpu
    base_url: http://192.168.7.1:8004/v1
    api_key: pinto
    model: gemma2   # match whatever :8004 actually serves
```

Fix any typo like `8004:/v1` → `8004/v1`.

### 2. Default vs fallback (important distinction)

| Mechanism | Triggers on | Good for |
|-----------|-------------|----------|
| `model.*` | Every turn (until `/model`) | **Policy default** |
| `fallback_providers` | 429, 503, connection errors | **Outage ladder** |

**Recommended outage ladder (availability only):**

```yaml
model:
  default: qwen36          # or grok — pick your daily driver
  provider: custom         # use custom:pinto when default is LAN
  base_url: http://192.168.7.1:8001/v1
  api_key: pinto

fallback_providers:
  - provider: custom
    model: qwen36
    base_url: http://192.168.7.1:8001/v1
  - provider: custom
    model: gemma2
    base_url: http://192.168.7.1:8004/v1
  # Optional last resort — only if you accept cloud during total LAN failure:
  # - provider: xai-oauth
  #   model: grok-composer-2.5-fast
```

If **frontier is default**, fallbacks should still be **LAN → CPU** before cloud, so a GPU stall doesn’t automatically exfiltrate context to xAI unless you add that explicitly.

### 3. Auxiliary vision (multimodal without making Grok the main model)

```yaml
auxiliary:
  vision:
    provider: xai-oauth
    model: grok-2-vision-1212   # or current Grok vision slug from `hermes model`
    timeout: 120
```

Main session stays on qwen36; `vision_analyze` uses Grok for pixels only.

### 4. Delegation (frontier subagent for “build” tasks)

```yaml
delegation:
  provider: xai-oauth
  model: grok-composer-2.5-fast
  max_iterations: 50
```

Parent on LAN runs `delegate_task` for “design + implement” with **sanitized** `context` (paths and requirements, not secrets).

### 5. Cron / watchdog

- **no_agent** script on schedule: ping `:8001` and `:8004`, GPU `nvidia-smi` utilization → Telegram alert
- LLM cron jobs that touch member data: `model: { provider: custom, model: qwen36 }` + `deliver: telegram`

---

## Policy router (Echo `routing.json` → Hermes)

Legacy scoring (already in `echo-system/config/routing.json`):

| Signal group | Effect in Echo | Hermes equivalent (today) |
|--------------|----------------|---------------------------|
| `local_signals` | Route gx10 | User says “stay local” + `/model` pinto; AGENTS.md instructs agent to switch |
| `cloud_signals` | Route supergrok | User says “use frontier” or `/model` xai-oauth |
| `light_signals` | cpu-light | Short replies on CPU via `/model` or fallback when GPU busy |
| `fallback.gx10_unhealthy_to` | cpu-light | `fallback_providers` order |

**Phase 1 (no code):** Add to `~/.hermes/SOUL.md` or project `AGENTS.md`:

- Default: **LAN** for TAHS, echopedia, bridges, memory flush content
- **Frontier** when user asks for architecture, deep reasoning, or multimodal
- **CPU** when user reports “GPU pegged” or health cron says vLLM down

**Phase 2:** Skill `echo-hybrid-routing` with checklist: classify message → recommend `/model` + whether to delegate.

**Phase 3:** Thin pre-hook (plugin or `execute_code` cron is insufficient) — only if you need automatic per-message routing like TauErgon; evaluate upstream Hermes feature request vs local plugin.

---

## Operational playbook (pinto / GB10)

1. **One heavy GPU consumer:** vLLM OR XTTS+Whisper, not both at 96%.
2. **LINE/Telegram** should use **native Hermes gateway** (not raw vLLM bridge) so Tier B gets memory/soul.
3. **Health order:** `:8001` → `:8004` → optional xai-oauth.
4. **Secret handling:** `security.redact_secrets: true`; frontier prompts get **summaries** of private state, not raw `.env`.

---

## Suggested defaults for Leonard (mission-first)

| Surface | Default tier | Notes |
|---------|--------------|-------|
| Telegram DM (orchestration) | Frontier **or** LAN | You’re on Grok now — good for building; switch `/model` pinto for TAHS member content |
| LINE (community) | **LAN** | Lower latency, private; frontier via explicit user ask |
| `delegate_task` (build) | Frontier | Sanitized context |
| `vision_analyze` | Frontier aux | LAN main unchanged |
| Outage | CPU | Then user decides on cloud |

---

## Implementation checklist

- [ ] Fix `pinto-cpu` base_url (`8004/v1`)
- [ ] Reorder `fallback_providers`: LAN → CPU → (optional) xai-oauth
- [ ] Set `auxiliary.vision` to xai-oauth
- [ ] Set `delegation` to xai-oauth for build tasks
- [ ] Document in SOUL.md: when to `/model` pinto vs grok
- [ ] GPU/vLLM watchdog cron (`no_agent` script)
- [ ] Retire custom LINE→vLLM bridge; native LINE on gateway :8646

---

## One-line summary

**Private text on qwen36 (LAN), hard building on Grok (OAuth), broken GPU on :8004 (CPU), pixels/audio understanding on Grok auxiliary or frontier session — with Hermes fallbacks for outages, not for philosophy.**