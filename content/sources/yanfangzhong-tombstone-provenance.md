---
type: source
title: "嚴防中 tombstone — measurement provenance (t_f3346433)"
tags:
  - source
  - qa-provenance
  - news-digest
verification_status: verified
last_reviewed: 2026-11-14
---
# 嚴防中 tombstone — measurement provenance

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 354
- wikilinks: 2


Captured 2026-11-14 by **FLOOR-ANCHOR t_f3346433** for [[people/嚴防中|嚴防中]].
This page exists so the tombstone's evidence measurements are re-runnable from disk:
archive paths, the instrument, the date of measurement, and the corpus records that
contain the string. No biography is asserted — the subject does not exist
(`verification_status: false_positive` on the person page).

## Instrument

- `echopedia-news-digest.py` (`~/.hermes/scripts/echopedia-news-digest.py`) — functions
  `surname_candidates()`, `archive_presence()`, `is_boilerplate_zh()`, `hanzi_index()`.
- Measured 2026-11-06 by t_ff066c81; quoted on the person page.

## Seeds and same-string records (per `knowledge/…` / `content/…` paths below)

- Wire seed: `knowledge/operational/news-wire.jsonl` — headline
  「嚴防中共對台跨國鎮壓 法務部擬修反滲透法增罪責 - Rti 中央廣播電臺」 delivered
  **twice on 2026-11-05** (04:30:28 UTC score 7.14, 05:20:29 UTC score 7.84).
  This is why the page is tombstoned rather than deleted — a delete would re-seed.
- Gate sibling page (same headline, live event record):
  `content/topics/t-嚴防中共對台跨國鎮壓-法務部擬修反滲透法增罪責.md`
  (`verification_status: pending`, created 2026-11-05 by the news-digest gate).
- Same-token article in the community corpus (verb usage, 嚴防＋中國):
  `content/articles/taiwanjustice-net/2022/20220306132638_2022_03_05_嚴防中國趁機犯台_專家指美對台政策漸趨清晰_ec7b32e301fd669f.md`
  (post_date 2022-03-05, Wayback snapshot 20220306132638). Linked from
  [[people/lai-ching-te|賴清德]] — which is one reason `links` can never be 0 here.
- Corpus-wide containment: `grep -rlF '嚴防中' content knowledge` = **73 files**,
  re-counted 2026-11-14 on this box. Every occurrence is 嚴防＋truncated object prose
  or a tombstone cross-reference; no line anywhere names a person called 嚴防中.
- Machine indexes (counted, NOT sources): `knowledge/operational/ee-vault-index.v5.json`,
  `content-analysis/*.jsonl`, `extracted/…`, `evaluated/…`, `generated/…`,
  `tdm-page-title-index.json`, `false-positive-history.json`.

## Twin / independence note

All three quoted lines on the person page come from ONE source family (news prose in
the taiwanjustice.net archive mirrors of Rti/VOA-lineage reporting). Restatement across
mirrors ≠ corroboration; there is nothing to corroborate because the referent is a verb.

## GAPS / NEED YOU

- No citable third-party source exists on this box for a **person** named 嚴防中 —
  checked 2026-11-14: whole-`content/` + whole-`knowledge/` `grep -rlF '嚴防中'`
  (73 files, all classified above), the 2026-11-05 wire seed in
  `knowledge/operational/news-wire.jsonl`, the gate topic sibling, the 2022 TJJ
  article, and the 嚴-adverb verb-bigram guard history in the digest script.
- Remaining need is the **script lane** (already open on the person page): add
  嚴防 and the 嚴-adverb family to `BOILERPLATE_ZH` in
  `~/.hermes/scripts/echopedia-news-digest.py` **and**
  `scripts/work-entity-linker.py` (declared mirrors — change both together).
