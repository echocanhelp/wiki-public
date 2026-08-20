# Source continuity (live sites)

**SSOT registry:** `knowledge/operational/source-watch-registry.json`  
**Orchestrator:** `~/.hermes/profiles/pinto/scripts/echopedia-source-continuity.sh`  
**Schedule:** Sunday **06:00** local — job `echopedia-source-continuity` (`no_agent`)  
**Human surface:** morning-brief 07:55 (SOURCE CONTINUITY / NEXT INGEST sections)  
**Ship:** 2026-08-09 v3 — live-small (TC · GSTPC · ITPC · PCT). **2026-08-18:** `laijohn-com` added by owner (static HTTP; seeds=Who+TOC; no event stubs / no About AUTO).

## What it does

Weekly: poll enabled live sites → fingerprint URLs → append Tier2 on new/changed → narrow AUTO (`last_reviewed`, clean event stubs) → write summary + next-ingest tips.  
**Does not** push (ci-heal only). **Does not** watch dead/static/OCAC stub until owner watch-add. **`story-corpus`** is watchable after **ingest COMPLETE** (wiki + **P2** + Stories path; `class=story-corpus`, `work_stub`, no `event_stub`). Poll = seeds + recent REST. New A/B/C → AUTO work page. Never AUTO people. `archive only` is not COMPLETE.

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
$SC site add --id <id> --home <url> --hub content/sources/<slug>.md --primary content/organizations/<slug>.md [--class story-corpus]
$SC site baseline <id>
$SC site enable <id>
$SC site disable <id>    # pause
$SC site remove <id>     # soft-remove; keep corpus
$SC --dry-run --only <id>
$SC --self-check
```

### Add site

1. Gate A: `Echopedia website <domain>` until ingest COMPLETE (live + findable). `archive only` does not qualify.  
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
