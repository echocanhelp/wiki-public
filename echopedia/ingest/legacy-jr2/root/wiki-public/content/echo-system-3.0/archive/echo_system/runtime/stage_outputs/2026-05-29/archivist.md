# Archivist autonomous loop artifact

- Timestamp: 2026-05-29T05:30:19.611095-07:00
- Profile: archivist
- Exit code: 1
- Issues seen: 1
- Cautions seen: 1

## Model Output

(no stdout)

## Runtime Cautions

- hermes-gateway has nonzero restart count

## Supporting Gateway Warnings

- 2026-05-29 01:11:19,701 WARNING gateway.platforms.telegram: [Telegram] Telegram network error, scheduling reconnect: Bad Gateway
- 2026-05-29 01:11:19,702 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 1/10), reconnecting in 5s. Error: Bad Gateway
- 2026-05-29 01:11:28,934 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 2/10), reconnecting in 10s. Error: Bad Gateway
- 2026-05-29 01:11:59,283 WARNING gateway.platforms.telegram: [Telegram] Telegram network error (attempt 3/10), reconnecting in 20s. Error: Timed out

## STDERR

Traceback (most recent call last):
  File "/usr/local/lib/hermes-agent/venv/bin/hermes", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/hermes-agent/hermes_cli/main.py", line 14068, in main
    run_oneshot(
  File "/usr/local/lib/hermes-agent/hermes_cli/oneshot.py", line 181, in run_oneshot
    response = _run_agent(
               ^^^^^^^^^^^
  File "/usr/local/lib/hermes-agent/hermes_cli/oneshot.py", line 290, in _run_agent
    runtime = resolve_runtime_provider(
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/hermes-agent/hermes_cli/runtime_provider.py", line 1363, in resolve_runtime_provider
    creds = resolve_codex_runtime_credentials()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/hermes-agent/hermes_cli/auth.py", line 3415, in resolve_codex_runtime_credentials
    data = _read_codex_tokens()
           ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/hermes-agent/hermes_cli/auth.py", line 3199, in _read_codex_tokens
    raise AuthError(
hermes_cli.auth.AuthError: No Codex credentials stored. Run `hermes auth` to authenticate.
