# Echo System Deployment Reality Audit

- Generated at: 2026-06-23T13:45:18.243493+00:00
- Status: DRIFT DETECTED
- Drift count: 15

## Architecture contract

- Hybrid model topology: primary=xai-oauth/grok-4.3, local vLLM for specialist roles (updated 2026-05-18)
- Provider: openai-codex
- Base URL: None

## Observed profiles

- archivist: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- audioforge: provider=xai-oauth model=grok-imagine-image-quality base_url=https://api.x.ai/v1
- content: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- default: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- echohsu: provider=openai-codex model=gpt-5.5 base_url=https://chatgpt.com/backend-api/codex
- echohsu-staging: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- echonomics: provider=custom model=RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic base_url=http://192.168.7.1:8001/v1
- evolver: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- healer: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- historian: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- orchestrator: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- profiler: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- sentinel: provider=openai-codex model=gpt-5.3-codex base_url=https://chatgpt.com/backend-api/codex
- videoforge: provider=xai-oauth model=grok-imagine-video base_url=https://api.x.ai/v1
- vision: provider=xai-oauth model=grok-2-vision-latest base_url=https://api.x.ai/v1
- voice: provider=xai-oauth model=grok-tts-1 base_url=https://api.x.ai/v1

## Observed local models

- gpt-5.3-codex: 10 profile(s)
- RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic: 1 profile(s)
- gpt-5.5: 1 profile(s)
- grok-2-vision-latest: 1 profile(s)
- grok-imagine-image-quality: 1 profile(s)
- grok-imagine-video: 1 profile(s)
- grok-tts-1: 1 profile(s)

## Drift details

- archivist: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- default: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- echohsu-staging: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- echonomics: provider_mismatch (expected=openai-codex observed=custom)
- echonomics: base_url_mismatch (expected=None observed=http://192.168.7.1:8001/v1)
- evolver: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- healer: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- historian: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- orchestrator: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- profiler: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- sentinel: base_url_mismatch (expected=None observed=https://chatgpt.com/backend-api/codex)
- vision: provider_mismatch (expected=openai-codex observed=xai-oauth)
- vision: base_url_mismatch (expected=None observed=https://api.x.ai/v1)
- voice: provider_mismatch (expected=openai-codex observed=xai-oauth)
- voice: base_url_mismatch (expected=None observed=https://api.x.ai/v1)

## Operational guidance

- Treat profile config files as the source of truth for deployment reality.
- Treat this generated audit as the read-back artifact that narrative docs should match.
- If the local vLLM model changes, update human-facing docs only where they claim the current observed local model.
