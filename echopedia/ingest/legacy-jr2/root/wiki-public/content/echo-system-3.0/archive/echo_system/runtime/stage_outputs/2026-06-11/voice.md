# Voice autonomous loop artifact

- Timestamp: 2026-06-11T06:15:34.225913-07:00
- Profile: voice
- Exit code: 1
- Issues seen: 1
- Cautions seen: 1

## Model Output

(no stdout)

## Runtime Cautions

- hermes-gateway has nonzero restart count

## Supporting Gateway Warnings

- 2026-06-11 01:11:24,158 WARNING gateway.platforms.telegram: [Telegram] Telegram network error, scheduling reconnect: Bad Gateway
- 2026-06-11 01:11:24,158 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 1/10), reconnecting in 5s. Error: Bad Gateway
- 2026-06-11 01:12:09,880 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 2/10), reconnecting in 10s. Error: Timed out

## STDERR

hermes -z: agent failed: xAI OAuth state is missing access_token. Re-authenticate with `hermes model`.
