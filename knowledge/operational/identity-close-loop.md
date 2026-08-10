# Identity close-loop (EVO-3)

**SSOT registry:** `echopedia/identity/identity_registry.json`  
**Audit:** `echopedia/identity/identity_audit.jsonl`  
**CLI:** `~/.hermes/profiles/pinto/scripts/identity-decide.py`  
**NEED YOU builder:** `need-you-list.py` (soft pending ≠ NEED YOU)

## Problem solved
`owner_verified` people with sticky `pending[]` (e.g. capture LINE id, chinese_name) were permanent 🔴 NEED YOU.  
Those are **soft** tasks — not owner judgment.

## Soft vs hard

| Soft pending (queue only) | Hard (NEED YOU) |
|---------------------------|-----------------|
| `capture_line_user_id_on_first_sender_message` | `state=proposed` |
| `chinese_name` | `state=pending_page` |
| `profile_photo` | `state=pending_line_user_id` (no page confirm) |
| `optional_bio` | hard custom pending tags |

## Operator commands

```bash
# list
python3 ~/.hermes/profiles/pinto/scripts/identity-decide.py list
# or: go identity list

# confirm link
python3 .../identity-decide.py link <slug>

# clear soft pending
python3 .../identity-decide.py clear-pending <slug> all

# defer 30d → QUEUE not NEED YOU
python3 .../identity-decide.py defer <slug> --days 30 --reason waiting

# not a member
python3 .../identity-decide.py not-member <slug> --reason visitor

# age soft pending into queue (also run from weekly)
python3 .../identity-decide.py expire --days 30

# reply cheat-sheet
python3 .../identity-decide.py templates
```

Telegram plain language (go-router):
- `go identity link yang-jia-you`
- `go identity clear-pending becky-yang chinese_name`
- `go identity defer rex-chen --days 14`
- `go identity not-member visitor-slug`

## Morning brief
- 🔴 NEED YOU — hard identity only  
- 🟡 QUEUE / identity — soft_queue + deferred (no reply required)

## Charles / Becky (2026-08-10)
Already `owner_verified`. Soft pending moved to **identity-queue** (`soft_queue`).  
NEED YOU cleared. Runtime may still capture Charles LINE id on first sender message.
