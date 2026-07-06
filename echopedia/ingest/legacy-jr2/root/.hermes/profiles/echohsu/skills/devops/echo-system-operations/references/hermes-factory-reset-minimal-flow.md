# Hermes Factory Reset — Minimal One-Pass Flow

Use this when user asks for a factory/default reset and signals confusion with complex branching.

## User-facing behavior
- Keep explanation to 3 parts only: what resets, what is preserved, what will be tested.
- Avoid layered option trees unless user asks.
- If user says "do it", execute immediately in one pass.

## Reset scope (safe default)
1. Backup profile config (`config.yaml`) with timestamp.
2. Reset target runtime code files to upstream defaults.
3. Restart gateway/service for affected profile.
4. Run canary prompt + log signature scan for known prior failures.
5. Report result as: done / healthy / next action only if broken.

## Preserve by default
- `.env` secrets
- `auth.json` OAuth tokens
- session/memory stores

## Verification checklist
- service active
- canary chat response successful
- no recurrence of previous crash signatures in recent logs

## Pitfalls
- Saying "reset done" before restart and canary verification.
- Over-explaining architecture when user asked for direct execution.
- Mixing config-reset and code-reset scopes without explicitly stating which one was executed.
