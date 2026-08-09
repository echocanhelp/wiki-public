# Source continuity (live sites)

**SSOT registry:** `knowledge/operational/source-watch-registry.json`  
**Orchestrator:** `~/.hermes/profiles/pinto/scripts/echopedia-source-continuity.sh`  
**Schedule:** Sunday **06:00** local — job `echopedia-source-continuity` (`no_agent`)  
**Human surface:** morning-brief 07:55 (SOURCE CONTINUITY / NEXT INGEST sections)  
**Ship:** 2026-08-09 v3 — live-small only (TC · GSTPC · ITPC)

## What it does

Weekly: poll enabled live sites → fingerprint URLs → append Tier2 on new/changed → narrow AUTO (`last_reviewed`, clean event stubs) → write summary + next-ingest tips.  
**Does not** push (ci-heal only). **Does not** watch dead/static/OCAC stub.

## Labels

| Tag | Meaning |
|-----|---------|
| ✅ AUTO | Delta applied on disk |
| 🟡 QUEUE / NEXT INGEST | Advisory; not a gate |
| 🔴 NEED YOU | Parked/dead home or true fail |

Silent stdout when nothing to report.

## Site lifecycle (no redesign)

```bash
SC=~/.hermes/profiles/pinto/scripts/echopedia-source-continuity.sh

$SC site list
$SC site check <id>
$SC site add --id <id> --home <url> --hub content/sources/<slug>.md --primary content/organizations/<slug>.md
$SC site baseline <id>
$SC site enable <id>
$SC site disable <id>    # pause
$SC site remove <id>     # soft-remove; keep corpus
$SC --dry-run --only <id>
$SC --self-check
```

### Add site

1. Gate A: `Echopedia website <domain>` until COMPLETE + live 200  
2. `site add` → `site check` → `site baseline` → `site enable`  
3. **Do not** edit jobs.json  

### Remove / pause

- Pause: `site disable`  
- Soft-remove: `site remove` (Tier1/Tier2 retained)  
- Hard page delete: separate content playbook only  

## Freeze all

`SOURCE_CONTINUITY=0` on the job env, or disable every registry row.

## Related

- Plan: `~/.hermes/plans/2026-08-09_echopedia-source-continuity-and-next-ingest.md`  
- Labels: `cron-notify-labels.md`  
- WEBSITE_INGEST.md § delta refresh  
