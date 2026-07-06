---
name: mlops-model-workflows
description: "Umbrella for model hub operations, local/served inference, evaluation, experiment tracking, model surgery, and multimodal model tools."
version: 1.0.0
author: Hermes Agent Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [mlops, huggingface, inference, evaluation, wandb, vllm, llama-cpp, gguf, audiocraft, sam]
---

# MLOps Model Workflows

Use this class-level skill for practical ML/model operations: finding models/datasets, downloading/uploading on Hugging Face, running local or served inference, benchmarking LLMs, tracking experiments, model surgery, and multimodal model utilities.

## Route by job class

- **Hub operations**: Hugging Face search/download/upload, auth, dataset/model repos, Spaces.
- **Local inference**: llama.cpp/GGUF for CPU/edge/Apple Silicon/local quantized runs.
- **Served inference**: vLLM for OpenAI-compatible, high-throughput, GPU-backed endpoints.
- **Structured generation**: Outlines-style regex/JSON/Pydantic constrained decoding when exact output shape matters.
- **Evaluation**: lm-evaluation-harness for benchmarks; define model, tasks, few-shot, batch size, and output path explicitly.
- **Experiment tracking**: W&B for metrics, artifacts, sweeps, dashboards, and model registry.
- **Model surgery/abliteration**: treat as research/experimental; keep originals, record configs, and evaluate behavior before/after.
- **Multimodal models**: AudioCraft for MusicGen/AudioGen; SAM for zero-shot segmentation.

## Operating pattern

1. Confirm hardware, Python environment, and credentials before installing heavy packages.
2. Prefer isolated virtual environments (`uv venv` / `uv pip`) for ML dependencies.
3. Start with the smallest model/sample/batch that validates the path.
4. Save commands, configs, and output paths so runs are reproducible.
5. Verify with an actual inference/eval/artifact output before reporting success.

## Pitfalls

- Model names, quantization formats, and GPU support drift quickly; check current docs or CLI help when exact flags matter.
- Do not conflate local model runtime with hosted API behavior.
- Large ML installs can be slow and platform-specific; surface blockers early and offer smaller alternatives.

## Consolidated model/tool families

### Local and served LLM inference
- **llama.cpp / GGUF**: use for local quantized inference, CPU/edge/Apple Silicon testing, model conversion/quantization, and lightweight OpenAI-compatible local servers. Verify with a short prompt and record model path, quantization, context size, and server flags.
- **vLLM**: use for GPU-backed OpenAI-compatible serving, batching, tensor parallelism, and production-ish throughput checks. Confirm CUDA/GPU availability, model access, port readiness, and a real `/v1/chat/completions` or equivalent request.

### Evaluation and experiment tracking
- **lm-evaluation-harness**: define tasks, model adapter, few-shot count, batch size, output path, and exact command. Start with one small task/sample before a full benchmark.
- **Weights & Biases**: use for experiment metrics, artifacts, sweeps, dashboards, and model registry. Check `WANDB_API_KEY`/login state and log a minimal run or artifact before claiming setup works.

### Model surgery and behavior modification
- **OBLITERATUS / abliteration**: treat as experimental model-surgery work. Keep immutable originals, save config and vectors, evaluate before/after behavior, and document refusal/utility trade-offs.

### Multimodal model utilities
- **AudioCraft / MusicGen / AudioGen**: isolate dependencies, select music vs sound-effect path, generate a short sample first, and return the actual media path.
- **Segment Anything (SAM)**: use for zero-shot masks from points/boxes/textual region plans; verify image path, coordinate space, and output masks/overlays.