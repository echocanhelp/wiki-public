---
title: "README"
category: "operational"
source: "audiobook-albert-lai/README.md"
created: "2026-07-12"
---

# Albert Lai Audiobook Project

**Working title:** *Toward A Community of Hope — A Mission to Formosan Community in Los Angeles*  
**Author:** Dr. Albert S. Lai (賴信雄 / Lai Sin-hiong)  
**Producer:** TAHS / Echo System  
**Project root:** `~/echo-system/audiobook-albert-lai/`

## Canonical plan

→ **[MASTER_PLAN.md](./MASTER_PLAN.md)** — full end-to-end production & distribution plan  
→ **[STATUS.md](./STATUS.md)** — live checklist / decisions  
→ **[NEXT_ACTIONS.md](./NEXT_ACTIONS.md)** — what to do this week

## v1 product decision (locked for execution start)

| SKU | Language | Scope | Priority |
|-----|----------|-------|----------|
| A | English | Full unabridged audiobook | P0 |
| B | Taiwan Mandarin (華語) | Full unabridged | P0 |
| C | Taiwanese Hokkien (台語) | Companion EP / 選讀 first | P1 (does not block A/B) |
| D | Samples | Ch.1 EN+華語 free samples | P0 marketing |

**Narration default:** human professional for retail masters. AI only for scratch/timing unless legal + platform policy explicitly cleared.

**Distribution default:**
1. Audiobook aggregators (Findaway / Author’s Republic / ACX review) for true audiobook stores  
2. Music distributor path for YouTube Music + DSPs as chapter albums  
3. Echopedia free sample (shorter than retail exclusivity needs)

## Folder map

| Dir | Purpose |
|-----|---------|
| `00_legal/` | Licenses, rights memo |
| `01_AMT_scripts/` | Audio Master Text + language scripts (`en/`, `zh-TW/`, `nan-TW/`) |
| `02_pronunciation/` | Pronunciation bible + author name reel notes |
| `03_raw_sessions/` | Session WAVs (gitignored if large) |
| `04_edited_wav/` | Edited chapter WAVs |
| `05_masters_by_platform/` | Reference + platform encodes |
| `06_artwork/` | Cover 3000², thumbnails |
| `07_metadata_isrc/` | UPC/ISRC sheets, store metadata |
| `08_consents/` | Signed voice/text consents |
| `09_qc_reports/` | Loudness + proof-listen reports |
| `10_release_notes/` | Changelogs |
| `11_casting/` | Briefs, audition scorecards |
| `12_distribution/` | Distributor checklists, upload logs |

## Related Echopedia pages

- [Dr. Albert S. Lai](../content/people/albert-s-lai.md)
- [Ch.1 consent kit (legacy archival scope)](../content/people/albert-chapter1-audiobook-consent-and-recording-kit.md)
- [Ch.1 pilot audio page](../content/people/albert-chapter1-audiobook-taiwanese-female.md)

## Do not publish to gh-pages

Raw sessions, consents with personal contact data, and unreleased masters stay **off** the public wiki. Only approved samples + public marketing copy go live.
