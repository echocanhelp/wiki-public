# Echo System Deployment Reality Audit

- Generated at: 2026-07-01T13:45:08.623803+00:00
- Status: DRIFT DETECTED
- Drift count: 10

## Architecture contract

- Hybrid model topology: primary=xai-oauth/grok-4.3, local vLLM for specialist roles (updated 2026-05-18)
- Provider: openai-codex
- Base URL: None

## Observed profiles

- archivist: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1
- content: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1
- default: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1
- echohsu: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1
- echonomics: provider=custom model=RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic base_url=http://192.168.7.1:8001/v1
- historian: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1
- orchestrator: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1
- videoforge: provider=xai-oauth model=grok-4.3 base_url=https://api.x.ai/v1

## Observed local models

- grok-4.3: 7 profile(s)
- RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic: 1 profile(s)

## Drift details

- archivist: provider_mismatch (expected=openai-codex observed=xai-oauth)
- archivist: base_url_mismatch (expected=None observed=https://api.x.ai/v1)
- default: provider_mismatch (expected=openai-codex observed=xai-oauth)
- default: base_url_mismatch (expected=None observed=https://api.x.ai/v1)
- echonomics: provider_mismatch (expected=openai-codex observed=custom)
- echonomics: base_url_mismatch (expected=None observed=http://192.168.7.1:8001/v1)
- historian: provider_mismatch (expected=openai-codex observed=xai-oauth)
- historian: base_url_mismatch (expected=None observed=https://api.x.ai/v1)
- orchestrator: provider_mismatch (expected=openai-codex observed=xai-oauth)
- orchestrator: base_url_mismatch (expected=None observed=https://api.x.ai/v1)

## Operational guidance

- Treat profile config files as the source of truth for deployment reality.
- Treat this generated audit as the read-back artifact that narrative docs should match.
- If the local vLLM model changes, update human-facing docs only where they claim the current observed local model.
