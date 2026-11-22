---
title: "Taiwan Center group-members captures — 慶瑛文教基金會 Ching Ying Cultural and Educational Foundation"
type: source
tags:
  - source
  - taiwan-center
  - taiwan-center-group-member
  - primary-source
verification_status: pending
last_reviewed: 2026-11-14
---
# Taiwan Center group-members captures — 慶瑛文教基金會

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 612
- wikilinks: 2


Primary captures of every occurrence of 慶瑛文教基金會 / Ching Ying Cultural and
Educational Foundation in the local archive, preserved because the live page is an
editable Webflow site and the organization has no first-party site of its own on this box.

## Subject
- [[organizations/ching-ying-cultural-and-educational-foundation|Ching Ying Cultural and Educational Foundation]] (慶瑛文教基金會) — group member of [[organizations/taiwan-center|Taiwan Center Foundation of the Greater Los Angeles]]

## Capture 1 — 團體會員 (ZH group-members) page
- **File:** `knowledge/web-archives/taiwancenter-org-group-members.md`
- **Original:** [https://www.taiwancenter.org/group-members](https://www.taiwancenter.org/group-members)
- **Fetched:** 2026-07-16T01:12:07 · **method:** jina · 314 lines / 5,937 bytes (MANIFEST `results[32]`, status ok)
- **Verbatim block (lines 204–208, bilingual pair):**

  ```
  慶瑛文教基金會

  Ching Ying Cultural and Educational Foundation
  ```

- **Positional context:** between 「快樂排舞班 Happy Dancers Club」 and 「柑縣台灣同鄉會 / OCTA Orange County Taiwanese Association」 in the single continuous official roster.

## Capture 2 — Group Members (EN) page
- **File:** `knowledge/web-archives/taiwancenter-org-en-group-members.md`
- **Original:** [https://www.taiwancenter.org/en/group-members](https://www.taiwancenter.org/en/group-members)
- **Fetched:** 2026-07-16T01:12:07 · **method:** jina · 3,768 bytes (MANIFEST `results[12]`, status ok)
- **Verbatim line (line 108):** `Ching Ying Cultural and Educational Foundation`
- The English render drops the Chinese name; it is the same roster serialized in English, same fetch batch.

## Continuity deltas (dated re-captures)
- `knowledge/web-archives/taiwancenter-org-delta-2026-10-04-en-group-members.md` — fetched 2026-10-05T06:45:52Z, method `source-continuity-delta`, 12,350 bytes, MANIFEST `entries[68]`. Raw-HTML capture; **grep `Ching Ying` / `慶瑛` = 0** — the extracted text is truncated site chrome before the roster renders. The roster is *absent* here, not stated absent; this delta is the dated fact that the capture method changed, and it constrains any "delisted" reading.
- `knowledge/web-archives/taiwancenter-org-delta-2026-10-11-group-members.md` — fetched 2026-10-12T06:45:06Z, same method, 13,267 bytes, MANIFEST `entries[70]`. Same: grep zero, raw-HTML chrome only (`<h1>團體會員</h1>` present, roster not rendered).
- Manifest: `knowledge/web-archives/taiwancenter-org-MANIFEST.json` (domain-scoped crawl, 38 URLs).

## Twin / containment check (2026-11-14)
Capture 2's English line is a **serialization of Capture 1's bilingual pair**, same site, same 2026-07-16 fetch batch — agreement across the ZH and EN renderings is **not** independent corroboration. Both are one editable Webflow roster maintained by Taiwan Center, so every row on the org page stays `alleged`.

## Whole-corpus sweep (2026-11-14, this card)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rlF '慶瑛' content knowledge` → **3 files**: the org page itself, `content/organizations/taiwan-center.md` (its own Subjects-list backlink, line 199), and Capture 1 above. No narrative record anywhere.
- `grep -rli 'ching ying' content knowledge` → adds only `content/.wiki-index.md`, `content/organizations/index.md`, the org page, Capture 1/2, machine indexes (`knowledge/operational/ee-vault-index.v1–v5.json`, `knowledge/operational/content-analysis/*.jsonl`) and the L4 lexicon entry `knowledge/research/taiwanjustice-net-priority-lexicon.json` → `entries[2437]` `l4:ching-ying-cultural-and-educational-foundation`, `name_zh: ""` (index, not a source).
- `grep -rl '慶瑛' knowledge/web-archives/taiwanjustice-net/{raw-html,tier2}` (29,103 md files) → **0 hits**.
- Prior deepen-x stamps (2026-09-18 → 2026-10-06) grepped only `works/`+`articles/`; this sweep re-ran over all of `content/` + `knowledge/` per name form, as required.

## Web pass (2026-11-14, searches recorded)
- Searched `"慶瑛文教基金會"`, 2026-11-14 — returns the live taiwancenter.org group-members pages (already archived as Captures 1–2), Echopedia's own pages, and one new third-party hit (below).
- Searched `"Ching Ying Cultural and Educational Foundation"`, 2026-11-14 — same set, no additional record.
- **One third-party hit found:** 國立中興大學第十四屆傑出校友 PDF `https://archive.nchu.edu.tw/data/pdf/1405.pdf` lists 徐新宏 (Hsu Hsin-hung, JH Biotech founder) with 現任 「…大洛杉磯台灣會館基金會董事長」「慶瑛文教基金會董事長」, and his 得獎感言 names 「先妻張慶瑛女士」 — i.e. the foundation appears to be named for his late wife. **Downloaded and archived on this box 2026-11-14 (FLOOR-ANCHOR t_b893f1d6):** `knowledge/web-archives/nchu-edu-tw/1405.pdf`, 3,926,180 bytes, md5 `14ae76c079dce149173bfef30cb2c58d`, fetched via curl from `https://archive.nchu.edu.tw/data/pdf/1405.pdf`. Extracted text confirms verbatim: 現任 list items 「7、大洛杉磯台灣會館基金會董事長」「8、慶瑛文教基金會董事長」 for 徐新宏 (土壤系60級), and 得獎感言 「先妻張慶瑛女士在背後的全力支持」. The org↔chairman link is recorded as `alleged` on the org page — single tertiary source (alumni-nomination record, not a foundation filing).

## Ruling
The citable harvest is the two dated 2026-07-16 roster captures, the two dated 2026-10 continuity deltas with their grep-zero (rendering) result, the MANIFEST byte/URL facts, and the NCHU outstanding-almumni PDF pointer. Nothing else on this box names this foundation.
