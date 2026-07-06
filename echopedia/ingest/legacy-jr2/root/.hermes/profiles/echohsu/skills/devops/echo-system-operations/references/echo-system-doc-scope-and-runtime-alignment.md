# Echo System doc scope + runtime alignment (2026-05-24)

## Durable lessons

- When asked to "review/update system docs" for Echo System operations, default authoritative path is `/root/echo_system/docs`.
- Treat `/root/wiki-public` and `/root/wiki-deploy` as wiki publishing surfaces, not substitutes for canonical Echo System runtime docs unless user explicitly asks for wiki work.
- Before editing runtime statements, verify live topology language:
  - Prefer "native LINE adapter on `hermes-gateway-echohsu.service`" when no separate line-bridge service is active.
  - Remove stale references to `hermes-line-bridge-echohsu.service` from baseline docs if runtime no longer uses it.
- Cleanup is part of update quality:
  - Remove duplicate section headings (e.g., duplicate `## Change Log`).
  - Replace deprecated ownership/enforcement wording (e.g., standalone ToolGateway references) with current architecture terms.

## Useful checklist

1. Confirm target doc set (`/root/echo_system/docs`).
2. Read master index + operations guide + deployment-reality export for comparison.
3. Search for stale strings (`ToolGateway`, `line-bridge`, legacy wording).
4. Patch canonical docs first, then align index rows/changelog metadata.
5. Re-read changed sections to verify consistency and no duplicate structure artifacts.
