# Echopedia-first reply path (operator note)

**Mission slice:** members/you ask → vault-backed answer or quiet capture → morning **🔴 NEED YOU** only.

**Updated:** 2026-08-09

## Path

```text
question (LINE/TG/CLI)
    → echopedia-first-answer.py
         HIT  → short grounded reply (person/org page)
         MISS → capture message + gap-queue row
    → need-you-list.py (morning)
         open gaps + identity pending + top unfinished
         → ≤5 🔴 NEED YOU items in vault-morning-brief (07:55 local)
```

Telegram labels: [cron-notify-labels.md](cron-notify-labels.md)  
Only **🔴 NEED YOU** requires owner reply. Gaps without identity stay 🟡 QUEUE (no auto page create).

## Commands

Prefer **pinto** scripts (profile cron copies):

```bash
# Answer (LINE-friendly text)
python3 ~/.hermes/profiles/pinto/scripts/echopedia-first-answer.py --name "Phoenix Ko" --source line --plain

# Miss intentionally queues a gap
python3 ~/.hermes/profiles/pinto/scripts/echopedia-first-answer.py --text "who is X" --source telegram

# Gaps
python3 ~/.hermes/profiles/pinto/scripts/echopedia-first-answer.py --list-gaps --plain
python3 ~/.hermes/profiles/pinto/scripts/echopedia-first-answer.py --resolve gap_xxx --resolve-note "created page"

# Morning judgment list
python3 ~/.hermes/profiles/pinto/scripts/need-you-list.py --plain

# Full brief (no_agent stdout)
python3 ~/.hermes/profiles/pinto/scripts/vault-morning-brief.py
```

Global `~/.hermes/scripts/` copies may exist; pinto path is cron SSOT.

## Files

| File | Role |
|------|------|
| `…/pinto/scripts/echopedia-first-answer.py` | Lookup + gap enqueue |
| `…/pinto/scripts/need-you-list.py` | Cap judgment list |
| `…/pinto/scripts/vault-morning-brief.py` | Brief: NEED YOU first + labels |
| `knowledge/operational/echopedia-gap-queue.jsonl` | Gap log |
| `knowledge/operational/intelligence/need-you.json` | Generated list |
| `knowledge/operational/intelligence/morning-brief.md` | Last brief |

## Agent rule

For who/what person/org questions: **run CLI first**. Never invent. Miss = capture + gap.

## Not in scope (by design)

- Auto thin-page creation from gaps (owner must approve identity)  
- Separate Telegram spam for unfinished/connector/intelligence collectors  
