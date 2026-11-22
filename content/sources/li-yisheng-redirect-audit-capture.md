---
type: source
title: "Redirect audit capture — li-yisheng → yi-sen-lee (李意盛)"
source_id: local-audit
tags:
  - source
  - audit
  - redirect
verification_status: verified
last_reviewed: 2026-11-13
---
# Redirect audit capture — li-yisheng → yi-sen-lee (李意盛)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 436
- wikilinks: 0


Audit capture minted by FLOOR-ANCHOR card t_39189af5 (2026-11-13). This page is a
harvest record, not a graded dossier page (`substance-lint.py` `iter_pages` walks only
`people/` + `organizations/`), so it carries the evidence the redirect stub
`content/people/li-yisheng.md` must not duplicate.

## Identity ruling

- `li-yisheng` was the provisional slug for **Yi Sen Lee (李意盛)**, canonical `people/yi-sen-lee`.
  Owner-confirmed merge: `knowledge/operational/tahs-priority-roster.md` line 153 —
  "Chart reconcile: Yi Sen Lee=李意盛 (merge li-yisheng→yi-sen-lee) … (2026-08-03)". *(sourced)*
- LINE identity link, same file line 151: "Yi Lee→Yi Sen Lee=李意盛 (2026-08-03)". *(sourced)*
- There is **no separate 李意盛/"Li Yi-sheng" subject** on this box: every corpus hit for
  李意盛 is scored to the canonical slug (see Evidence ledger below).

## Evidence ledger (dated, per source)

- **2025-09-03** — Installation of President 許景鴻 + first board meeting, at 台美人長輩會辦公室.
  Attendance list includes 李意盛. Recorded on the canonical page's "Board activity (2025)".
  Per `knowledge/web-archives/taiwanjustice-net/tier2/2025/20251107004331_台美人歷史協會新任會長許景鴻接椽-開啟世代傳承_11575c718bbd4c74.md`
  (`post_date: 2025-09-05T15:31:19-07:00`, `archive_ts: 20251107004331`). *(sourced)*
- **2025-09-05** — 台灣日報 (taiwandaily.net 南加社區/97560) report
  《台美人歷史協會 許景鴻接任會長》, same attendance sentence naming 李意盛 — an independent
  publication of the same event, mirrored at
  `knowledge/web-archives/taiwandaily-net-97560-97560.md` (frontmatter `fetched: 2026-10-17`,
  `Published Time: 2025-09-05`). *(sourced; second serialization of the same event fact,
  not independent corroboration of anything beyond attendance)*
- **2025-09-05 (scoring)** — `knowledge/research/taiwanjustice-net-priority-hits.jsonl`, record
  for `…_11575c718bbd4c74`: `l1:yi-sen-lee` alias 李意盛 body +40 AND `l2:li-yisheng` alias
  李意盛 body +20 — i.e. the retired alias is a scorer alias of the **same** person as the
  canonical `l1:yi-sen-lee` hit. *(sourced — machine index read this pass; index itself is not
  a source, the match aliases document the alias mapping)*
- **2026-08-03** — Slug rename `li-yisheng→yi-sen-lee` logged in
  `knowledge/operational/tahs-priority-roster.md` (roster rows 31/56/78 all carry
  "slug was li-yisheng"). *(sourced)*
- **2026-11-13** — Whole-corpus sweep for this slug (non-vacuous; see GAPS block on the stub):
  `grep -rlF 'li-yisheng' content knowledge` → 6 files: the two person pages themselves, the
  roster, and three scorer/index mirrors (`tdm-page-title-index.json`,
  `taiwanjustice-net-priority-lexicon.json`, `taiwanjustice-net-priority-hits.jsonl`).
  `grep -rlF '李意盛' knowledge/web-archives/` → 4 files: the TJJ raw html + tier2 capture (one
  article, two serializations), the 台灣日報 mirror above, and
  `knowledge/web-archives/latimes/leonard-hsu-monterey-park-trail.md` (a research digest whose
  §5 itself cites the taiwandaily 97560 mirror — same single event). *(sourced)*
- **2026-11-13** — False-provenance `## Works` counter check (sibling class of cai-shunyu,
  t_d9e94332): this stub carried **no** `N title hits, M body mentions` counter — clean. The
  class still fires on `people/cai-shunyu.md`, `people/shen-zizai.md`, `people/xu-shihuan.md`.
  No hardcoded name-map for `li-yisheng` exists in
  `scripts/echopedia-person-works-linker.py` / `scripts/enrich_columnist_pages.py` (grep clean). *(sourced)*
- **2026-11-16 (t_eb595a46 run 35511)** — Update to the class line above: the `cai-shunyu`
  emitter is **fixed** — the slug and its `蔡順宇` name-map pair are removed from
  `scripts/echopedia-person-works-linker.py` and `scripts/enrich_columnist_pages.py`
  (`removed t_eb595a46`), and the page's `## Works` block is fenced as STALE/false-provenance
  pending rebuild. The class now fires only on `people/shen-zizai.md`, `people/xu-shihuan.md`
  (and check `people/cai-yingwen.md`, `people/tsai-ingwen.md` before trusting). *(sourced)*

## Disambiguation note

`whoswho1092` / `musician25` in `content/works/taiwaneseamericanhistory-org/` matched a
grep only because of **Chin-Yi Lee (李琹怡)** — a different person (`people/chin-yi-lee`).
Not this subject. *(ruled 2026-11-13 so future passes do not re-open them)*
