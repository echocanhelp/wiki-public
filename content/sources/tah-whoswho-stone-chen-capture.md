---
type: source
title: "TAH Who's Who capture — Stone Chen 陳文石 (stone-chen)"
source_id: taiwaneseamericanhistory-org
source_url: https://taiwaneseamericanhistory.org/person/stone-chen/
tags:
  - source
  - tah-whoswho
  - capture
  - chen-wenshi
last_reviewed: 2026-11-14
---
# TAH Who's Who capture — Stone Chen 陳文石 (stone-chen)

Capture mirror for the TAH 台美史料中心 Who's Who profile at slug `stone-chen`, the
TAH-side slug behind the canonical Echopedia page [[people/chen-wenshi|Stone Chen (陳文石)]].
Minted by FLOOR-ANCHOR card t_eb6dc636 (2026-11-14) for the alias stub
[[people/stone-chen]], which is `verification_status: redirect` — every unique fact is
recorded on the canonical page; this page archives the crawl artifacts and the
sweep evidence so future passes do not re-open them.

## Raw artifacts (run twin/containment check before treating as two sources)

- Profile JSON: `knowledge/web-archives/taiwaneseamericanhistory-org/person/stone-chen.json`
  (WordPress `tah_person` id **73562**, `modified` **2026-06-19T16:42:17**, link
  https://taiwaneseamericanhistory.org/person/stone-chen/).
- Same-number post dumps checked (see ruling below): `posts/114-stone-chen.md`,
  `posts/collection-of-mr-stone-chen.md`,
  `posts/50-%e9%99%b3%e6%96%87%e7%9f%b3-stone-chen201505.md`, `posts/ourjourneys261.md`.

## Twin check (per `knowledge/web-archives/taiwaneseamericanhistory-org/person/stone-chen.json`, 2026-11-14)

Normalization: strip HTML tags, frontmatter, and all `#`/whitespace, then compare.

- Profile `content_html` normalized: **1,125 chars**.
- Containment tests run in-process: `content_html` is **not** a substring of, and does not
  contain, any of the four same-number post dumps (114: 267 chars, #50: 1,216,
  collection: 302, ourjourneys261: 801 normalized chars).
- Ruling: these are **four distinct records, not serializations of one editable record** —
  #114/#70/#50/#1002 are separate TAH encyclopedia entries with their own dates, and the
  Who's Who profile is the editable self-report. Per dossier doctrine, the self-report's
  unique fields (below) stay `alleged`/`self-reported` unless a second, non-TAH source
  corroborates them.

## Profile fields — `per knowledge/web-archives/taiwaneseamericanhistory-org/person/stone-chen.json`

- `title`: "Stone Chen 陳文石" *(self-reported)*
- `modified`: 2026-06-19T16:42:17 — last site-side edit of the record *(sourced: crawl metadata)*
- `person_profession` taxonomy (`class_list`): activist · artist · community-leader ·
  educator · oil-painter · painter · **publisher** · **sculptor** *(self-reported tags)*.
  Note: `publisher` and `sculptor` are tags that do **not** appear as roles on the
  canonical page's Identity Snapshot — they corroborate the 1995 望春風文化出版社
  co-founding row and the NTNU 1st-Place-in-Sculpture row already on canonical.
- `content_html` dated rows absent from the canonical TAH table *(absorb candidates, all
  self-reported via TAH submission, hence `alleged`)*:
  - 1989 — attended UCLA Art Extension *(alleged — one editable record)*
  - 1989–1990 — attended Art Center College of Design, Pasadena *(alleged)*
  - from 1960 — exhibited at the Tai Yang Fine Arts Show and the Province-Wide Fine Art Show over many years *(alleged)*
  - 1963 — prizes at the Taiwan Fine Art Youth Exhibition *(alleged)*
  - 1964 — First Place in Chinese Painting, Army Corps of Ilan exhibition *(alleged)*
  - 1974 (NTNU) — 1st Place Cubism designs, 1st Place Sculpture, 1st Place Artdeco designs, 2nd Place Water Color Painting *(alleged)*

## Same-number / collision rulings (do not re-open)

- `posts/114-stone-chen.md` — is TAH encyclopedia #114 「Stone Chen 陳文石」 (archived as
  [[works/taiwaneseamericanhistory-org/114-stone-chen]]); the number 114 is this record's
  own id, not a collision. *(sourced)*
- The whole-corpus grep for the literal slug `stone-chen` also hits
  `knowledge/research/*.json|jsonl`, `knowledge/operational/*` (deepen-x slices,
  ee-vault-index, linker state, floor findings) and `content-analysis` dumps — machine
  indexes that index this page's own text. Not sources; excluded. *(sourced: this pass's sweep)*
- The 2017-11-01 長青教室 lecturer 陳文石 stays **HOLD** (see canonical §Identity
  verification and [[people/bang-h-hwang]]) — not absorbed here.

## Sweep evidence (FLOOR-ANCHOR t_eb6dc636, 2026-11-14)

Probes, run from repo root `~/echo-system` (controls prove non-vacuity):

- `grep -rlF '陳文石' content knowledge` → hits in 6 work pages, 8+ article pages, the
  canonical dossier, this stub, the source hub `content/sources/taiwandaily-net.md`, and
  machine indexes. All dated community records are already absorbed on
  [[people/chen-wenshi]] (TAH #114/#70/#1002/#50, OurJourneys #261, 2025-06-26
  美洲台灣日報 board row, 2021-05-13 WHA roster, 2020-09-11 UN roster, Epoch Times
  corroboration chain, 2023-12-18 台江跨年展).
- `grep -rlF 'stone-chen' content` → 6 files: this stub, canonical page, the source hub,
  and 4 work pages — all accounted above.
- `grep -rl 'Stone Chen' content` — same set plus the 2023 TAHS publication source hub.
- Crawl-artifact harvest (`person/stone-chen.json`) opened this pass for the first time;
  its unique fields are archived above.
- Online arms (searched / HOLD, 2026-11-14): wikipedia `陳文石 画家` — searched, only the
  清代史學者 陳文石 hits (different person, canonical §Identity verification); wikidata —
  searched `Stone Chen painter`, no entry; 官網 (tah-society.org / taiwaneseamericanhistory.org)
  — absorb (the four TAH records above); 華文 press (大紀元/台灣日報) — absorb (美洲台灣日報
  byline lane + Epoch Times chain on canonical).

## GAPS / NEED YOU

- No non-self-reported third-party source for the 1989 UCLA Art Extension / 1989–90 Art
  Center College rows exists on this box beyond the TAH editable self-report — kept
  `alleged`. A UCLA/Art Center archival confirmation would upgrade them.
- 長青教室 2017 lecturer identity remains HOLD (see [[people/bang-h-hwang]]); no evidence
  either way on this box.
- 會館 tenure years (TAH 2007–08 vs 大紀元 2006–08) still unreconciled on canonical.
