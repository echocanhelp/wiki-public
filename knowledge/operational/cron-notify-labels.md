# Cron Telegram labels (AUTO vs NEED YOU)

**SSOT for ownership tags on non-silent pinto cron deliveries.**  
**Updated:** 2026-08-09 · Helpers live under `~/.hermes/profiles/pinto/scripts/` (file copies, not symlinks).

## Contract

| Tag | Meaning | Owner reply? |
|-----|---------|--------------|
| ✅ **AUTO** | Already healed / machine will handle / silent-OK class | **No** |
| 🟡 **QUEUE** | Automated backlog on disk (intake, broken-link lists, link tips) | **No** unless you open a batch epic |
| 🔴 **NEED YOU** | Judgment only (identity, true FAIL, gateway down, irreversible approve) | **Yes** |
| ℹ️ **INFO** | Context / non-blocking polish (docs WARN, OPS orphan scripts) | **No** |

## Primary human surface

| When (local) | Job | What to read |
|--------------|-----|----------------|
| **07:55** | `vault-morning-brief` | **NEED YOU first** (≤5), then SOURCE CONTINUITY / NEXT INGEST / QUEUE |
| 07:20 | `echopedia-digest` | Health + AUTO/QUEUE strip |
| **Sun 06:00** | `echopedia-source-continuity` | Live-site watch (silent if clean) |
| else | silent watchdogs / clean audits | empty stdout = healthy |

Collectors **not** separate Telegram jobs: unfinished / connector / intelligence folded into morning-brief (disk).  
Live-site continuity: [source-continuity.md](source-continuity.md)


## Helpers

```bash
# Bash
source ~/.hermes/profiles/pinto/scripts/cron-notify-legend.sh
# Python
from cron_notify_legend import LEGEND_LINE, tag_auto, tag_queue, tag_need_you, tag_info
```

- `cron-notify-legend.sh`  
- `cron_notify_legend.py`  

Include legend near **top and footer** on multi-section briefs.  
**Silent success (empty stdout) stays silent** — no legend spam.

## Applied deliverers (2026-08-09)

morning-brief · digest · ci-heal wrapper · nightly-audit · janitor · weekly-improvement · docs-sync · deepeners · content-analysis · scout · **source-continuity** · watchdog alerts · skill `cron-job-management`

## Related

- [echopedia-first-path.md](echopedia-first-path.md) — first-answer → NEED YOU  
- [WHERE_WE_ARE.md](../../echopedia/WHERE_WE_ARE.md) — mission narrative  
- Cron schedule SSOT: `~/.hermes/profiles/pinto/cron/jobs.json`  
