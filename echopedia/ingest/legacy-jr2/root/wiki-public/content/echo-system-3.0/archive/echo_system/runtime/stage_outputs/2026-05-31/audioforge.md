# Audioforge autonomous loop artifact

- Timestamp: 2026-05-31T06:15:22.693440-07:00
- Profile: audioforge
- Exit code: 1
- Issues seen: 1
- Cautions seen: 1

## Model Output

(no stdout)

## Runtime Cautions

- hermes-gateway has nonzero restart count

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
  File "/usr/local/lib/hermes-agent/hermes_cli/oneshot.py", line 308, in _run_agent
    agent = AIAgent(
            ^^^^^^^^
  File "/usr/local/lib/hermes-agent/run_agent.py", line 419, in __init__
    init_agent(
  File "/usr/local/lib/hermes-agent/agent/agent_init.py", line 1464, in init_agent
    raise ValueError(
ValueError: Model grok-imagine-image-quality has a context window of 8,000 tokens, which is below the minimum 64,000 required by Hermes Agent.  Choose a model with at least 64K context, or set model.context_length in config.yaml to override.
