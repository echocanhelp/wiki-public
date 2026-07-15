# Echopedia Knowledge Base (Tier 2)

Part of the **single vault** at `~/echo-system` (see root `SCHEMA.md` and `log.md`).

## Structure

```
~/echo-system/knowledge/
├── README.md                 ← This file
├── interactions/             ← LINE community auto-capture (private, gitignored)
│   └── line/YYYY-MM-DD.jsonl
├── web-archives/             ← Scraped web content
├── research/                 ← Research notes
├── operational/              ← Community projects (incl. audiobook ops)
└── staging/                  ← Draft wiki pages not yet published
```

## Tiers

| Tier | Location | Purpose | Public? |
|------|----------|---------|---------|
| **1 Wiki** | `content/` | Curated person/org/media | Publishable |
| **2 Knowledge** | `knowledge/` | Raw / work product | Private by default |

## Channels

| Channel | Intake |
|---------|--------|
| **LINE** | Auto → `interactions/line/` via `scripts/line_tier2_append.py` |
| **Telegram** | Admin only — **not** community Tier 2 intake |

## Audiobook

Community knowledge (Albert Lai audiobook ops) lives under `knowledge/operational/` and `audiobook-albert-lai/` (vault-visible; not for public Pages by default).

## Search

```bash
python3 ~/echo-system/scripts/knowledge_qa.py "search query"
python3 ~/echo-system/scripts/knowledge_qa.py --list
python3 ~/echo-system/scripts/knowledge_qa.py --stats
```

## LINE append example

```bash
python3 ~/echo-system/scripts/line_tier2_append.py \
  --chat-id Cxxx --user-id Uxxx --text "message" --display-name "Name"
```
