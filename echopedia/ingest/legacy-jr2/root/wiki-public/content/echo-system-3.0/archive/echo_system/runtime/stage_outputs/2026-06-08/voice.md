# Voice autonomous loop artifact

- Timestamp: 2026-06-08T06:15:36.476692-07:00
- Profile: voice
- Exit code: 1
- Issues seen: 1
- Cautions seen: 1

## Model Output

(no stdout)

## Runtime Cautions

- hermes-gateway has nonzero restart count

## Supporting Gateway Warnings

- 2026-06-08 01:11:11,543 WARNING gateway.platforms.telegram: [Telegram] Telegram network error, scheduling reconnect: Bad Gateway
- 2026-06-08 01:11:11,544 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 1/10), reconnecting in 5s. Error: Bad Gateway
- 2026-06-08 01:11:57,302 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 2/10), reconnecting in 10s. Error: Timed out

## STDERR

hermes -z: agent failed: xAI OAuth state is missing access_token. Re-authenticate with `hermes model`.
