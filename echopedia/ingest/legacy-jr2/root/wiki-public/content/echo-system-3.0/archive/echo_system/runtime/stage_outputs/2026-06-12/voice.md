# Voice autonomous loop artifact

- Timestamp: 2026-06-12T06:15:36.860686-07:00
- Profile: voice
- Exit code: 1
- Issues seen: 1
- Cautions seen: 1

## Model Output

(no stdout)

## Runtime Cautions

- hermes-gateway has nonzero restart count

## Supporting Gateway Warnings

- 2026-06-12 07:02:53,077 WARNING gateway.platforms.telegram: [Telegram] Telegram network error, scheduling reconnect: httpx.ReadError: 
- 2026-06-12 07:02:53,078 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 1/10), reconnecting in 5s. Error: httpx.ReadError: 

## STDERR

hermes -z: agent failed: xAI OAuth state is missing access_token. Re-authenticate with `hermes model`.
