# Echo System 3.0 — Architecture (GX10 Skeleton)

## Components

| Layer | Component | Location / Endpoint |
|-------|-----------|---------------------|
| Inference | vLLM + proxy (qwen36 AEON NVFP4 + DFlash) | `http://localhost:8001/v1` — model `qwen36` |
| Agents | TauErgon | `echo-system/tauergon/src/tau.py` |
| Knowledge | Echopedia | `echo-system/echopedia/` |
| Speech-in | Faster Whisper | `http://localhost:8002/v1` (optional) |
| Speech-out | openedai-speech (piper/XTTS) | `http://localhost:8003/v1` — `tts-1` CPU on GB10 |
| Embeddings | bge-m3 via vLLM | `http://localhost:8009/v1` (disabled until tested) |
| Monitoring | Prometheus/Loki | `:9090`, `:3100` (ai-services) |

## Network

| Interface | Address |
|-----------|---------|
| LAN | `192.168.7.1` |
| Tailscale | `100.104.120.42` |
| Legacy (migration source) | `100.125.172.124` |

## GB10 constraints

- Unified memory — avoid running multiple large GPU services simultaneously.
- Current production LLM uses 0.80 GPU util cap and CUTLASS kernel disables.
- Start Whisper (CPU) before adding embeddings or XTTS on GPU.