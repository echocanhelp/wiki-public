# Echopedia-first reply path (operator note)

**Mission slice:** members/you ask → vault-backed answer or quiet capture → night/morning judgment only.

## Path

```text
question (LINE/TG/CLI)
    → echopedia-first-answer.py
         HIT  → short grounded reply (person/org page)
         MISS → capture message + gap-queue row
    → need-you-list.py (morning)
         open gaps + identity pending + top unfinished
         → ≤5 NEED YOU items in vault-morning-brief
```

## Commands

```bash
# Answer (LINE-friendly text)
python3 ~/.hermes/scripts/echopedia-first-answer.py --name "Phoenix Ko" --source line --plain

# Miss intentionally queues a gap
python3 ~/.hermes/scripts/echopedia-first-answer.py --text "who is X" --source telegram

# Gaps
python3 ~/.hermes/scripts/echopedia-first-answer.py --list-gaps --plain
python3 ~/.hermes/scripts/echopedia-first-answer.py --resolve gap_xxx --resolve-note "created page"

# Morning judgment list
python3 ~/.hermes/scripts/need-you-list.py --plain
```

## Files

| File | Role |
|------|------|
| `~/.hermes/scripts/echopedia-first-answer.py` | Lookup + gap enqueue |
| `~/.hermes/scripts/need-you-list.py` | Cap judgment list |
| `~/.hermes/scripts/vault-morning-brief.py` | Brief with NEED YOU first |
| `knowledge/operational/echopedia-gap-queue.jsonl` | Gap log |
| `knowledge/operational/intelligence/need-you.json` | Generated list |
| `knowledge/operational/intelligence/need-you.md` | Generated markdown |

Pinto copies (not symlinks): `~/.hermes/profiles/pinto/scripts/` same three scripts.

## Agent rule

For who/what person/org questions: **run CLI first**. Never invent. Miss = capture + gap.

## Not in scope (yet)

- Automatic LINE middleware hook (agent still calls CLI / skill)
- Auto thin-page creation from gaps (owner must approve identity)
