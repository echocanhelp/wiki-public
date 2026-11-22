---
title: "TAH Who's Who profile capture — 2170. Yue-Juan (Joanne) Guo 郭玥娟"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2170. Yue-Juan (Joanne) Guo 郭玥娟

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 614
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/yue-juan-joanne-guo|Yue-Juan Joanne Guo 郭玥娟]] — TAH Who's Who record #2170

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/yue-juan-joanne-guo.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/yue-juan-joanne-guo/](https://taiwaneseamericanhistory.org/person/yue-juan-joanne-guo/)
- **Record id:** 74659 · **type:** `tah_person`
- **Profession taxonomy (site class_list):** `person_profession-artist` · `person_profession-sociologist`
  (`person_profession` term ids 2226 / 422). The crawl sidecar `roles` list carries only
  `artist` — the richer `sociologist` taxonomy is **only** in the site-rendered
  class_list and the rendered tag chips, a field no earlier pass of this page opened.
- **`modified` on source:** 2026-06-19T17:02:12 (page renders "Last updated: June 19, 2026") · page size 52,276 bytes
- **Verbatim fields (self-reported):** English Name Yue-Juan (Joanne) Guo · Hanji Name 郭玥娟 ·
  Birth Year `1949-2015` · Birth Place Tainan, Taiwan ·
  **First year / First city / State in U.S. `-/New York/NY`** (arrival year blank, first city New York/NY) · Address `--`
- **Family:** `1. Husband: Lung-Fong Chen` · `2. Daughter: --` · `3. Son: --` · `family_filled: true`
- **Education:** 1. Sophia Univ., Tokyo — `–` — B.S., History · 2. New York Univ. — `–` — M.S., Sociology (both `Year – Year` blank)
- **Employment:** 1. `-` — `-` — `-` (single blank row)
- **Accomplishment:** `1. Fellowship at New York Foundation of the Arts` ·
  **Publication:** `--` · **Hobby:** `--` — blank-field roster: evidence no
  withheld crown fact exists in the record
- **`content_html`:** empty in this capture (site renders from form fields); `page_text` carries the
  site-rendered profile block plus a second summary block (Hanzi/birth 1949/birthplace/Passed Away 2015/education)

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2170-yue-juan-guo.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2170-yue-juan-guo/](https://taiwaneseamericanhistory.org/whos-who-2170-yue-juan-guo/)
- **Title:** `2170.  Yue-Juan (Joanne) Guo 郭玥娟` · corpus index publish date 2018-11-06
  (`knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, id 50854)
- Field set identical to Capture 1.

## Twin check (2026-11-14)
The two artifacts are **two serializations of one editable self-report, not independent
corroboration**. Containment test run on the profile page's CONTENT BLOCK (from the
`Who's Who Taiwanese American Profile` marker to the footer line), not raw `page_text`,
per the theodore-ted-wing rule. Result: normalized dump 434 chars vs content block 711;
every dump field line is verbatim in the content block except the record-number title line
(`2170. …`, which the profile page renders without the number) and dash glyph variants
(`—` vs `--`/`-` — same blank fields). The JSON side is therefore a content superset, adding
the rendered profession chips (`artist`/`sociologist`), the `Notable Accomplishments` restatement,
and a second summary block (Hanzi / Birth Year 1949 / Birthplace / Passed Away 2015 / Education).
The dump side carries the record number 2170 and the 2018-11-06 publish stamp. Because both are
serializations of the same editable record, every fact from them stays `self-reported`/`alleged`
— restatement ≠ corroboration.

## Third-party attestation outside the subject's own record
- **Husband's own Who's Who record** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-58-lung-fong-chen.md`
  (`58. Dr. Lung-Fong Chen 陳隆豐博士`, Family field: `1. Wife: Yue-Juan Guo(郭玥娟)`) — a second
  editable self-report, authored by the spouse, not by the subject.
- **Husband's authored book dedication** — 台灣與國際組織/陳隆豐/2004/02/政治, archived at
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/308-…-陳隆豐-200402-政治.md`
  (corpus index publish date 2014-11-27, id 6587). Dedication text: 「寫本書時，受到作者的牽手陳郭玥娟
  百分之百不多不少的支持，不僅是鼓勵，更是鞭策」 and 「謹以此書，獻給我們兩人的偉大母親：母親大人陳黃來朱，
  與岳母大人郭孫雪娥。」 — names her married-name form 陳郭玥娟 and her mother 郭孫雪娥.

## Whole-corpus sweep (2026-11-14)
`grep -rlF '郭玥娟' content knowledge` and case-insensitive `yue-juan` sweeps: hits only the
subject's own person/work pages, the husband's page and records, the source hub, and machine
indexes (`units.jsonl`-class, `content-analysis/*.jsonl`, deepen-x slice state, scout/lexicon
files) — no third-party press, memoir, or organization coverage on this box.
