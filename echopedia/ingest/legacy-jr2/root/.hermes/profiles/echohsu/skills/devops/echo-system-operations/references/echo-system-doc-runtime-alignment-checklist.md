# Echo System doc runtime-alignment checklist

Use for `/root/echo_system/docs` cleanup tasks where runtime wording drift is common.

## Scope discipline
- Treat canonical docs as primary: `Echo_System_Master_Index.md`, `Echo_System_Operations_Guide.md`, `Echo_System_Agent_Prompts.md`, `Echo_System_Vision_Architecture.md`, plus canonical set rows.
- Do not bulk-normalize historical `exports/` snapshots unless explicitly requested.

## Runtime wording normalization
- Prefer: "native Hermes LINE adapter on `hermes-gateway-echohsu.service`".
- Remove active-state claims for standalone `hermes-line-bridge-echohsu.service` unless verified live.
- Replace active ToolGateway operator language with "Hermes core runtime/tooling"; keep historical/deprecation mentions in changelogs when needed.

## Master Index integrity checks
- Maintain exactly 6 living core document rows.
- Prevent duplicate rows (especially `operations_guide`).
- Keep status/version fields synchronized with edited canonical docs.
- If index table changes materially, add a changelog entry and bump master index version.

## Verification pass (before completion)
- Grep canonical docs for stale active runtime phrases: `ToolGateway`, `line-bridge`, `LINE-via-API-server bridge`, `API-server/bridge`.
- Confirm remaining hits are only historical/deprecation contexts, not active runtime assertions.
- Re-read canonical table + changelog blocks to catch accidental row replacement/duplication.
