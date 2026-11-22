---
title: "TAH Who's Who profile capture — Prof. Harrison Cheng (鄭學成教授)"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — Prof. Harrison Cheng (鄭學成教授)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 573
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-harrison-cheng|Prof. Harrison Cheng 鄭學成教授]] — TAH Who's Who profile
  (WordPress post id 74415, type `tah_person`)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-harrison-cheng.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-harrison-cheng/](https://taiwaneseamericanhistory.org/person/prof-harrison-cheng/)
- **Record id:** 74415 · **type:** `tah_person` · **profession taxonomy**
  (`person_profession` ids `[536, 2248, 2237, 1813]` → class list tags
  `person_profession-economist`, `-educator`, `-professor`, `-researcher`)
  — the `economist` and `researcher` tags are absent from the lean sidecar roles
  `professor, educator` (taxonomy richer than sidecar)
- **`modified` on source:** 2026-06-19T16:57:51 · page size 54,639 bytes
- **Verbatim fields (self-reported):** Birth Year `--` · Birth Place Pingtung, Taiwan ·
  First year/city/State in U.S. `-/-/-` · Address `CA`
- **Family:** `family: []`, `family_filled: false` — no family rows filled on the form
- **`content_html` and `excerpt` are empty** on the profile JSON — the site-rendered
  `page_text` is navigation chrome only; Capture 2 carries the narrative field set.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1912-harrison-cheng.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1912-harrison-cheng/](https://taiwaneseamericanhistory.org/whos-who-1912-harrison-cheng/)
- **Title:** `1912. Prof. Harrison Cheng 鄭學成教授` (TAH encyclopedia sequence #1912)
- **Verbatim fields (self-reported):** Birth Year `—` · Birth Place Pingtung, Taiwan ·
  First year/city/State in U.S. `-/-/-` · Address `CA` ·
  Family `1. Wife: —` `2. Daughter: —` `3. Son: —` (all blank)
- **Education:** National Taiwan Univ. — B.S., Mathematics (no year) ·
  Univ. of California, Berkeley — 1977 — Ph.D., Economics · UCSD — 2010 — MBA
- **Employment:** Alumni Scholars Alumni Association — 2008–2018 — Executive director ·
  UCSD — 2009–2010 — Teaching assistant · USC — 2010–2016 — Associate Professor, Dept. of Economics
- **Accomplishment / Publication / Hobby:** `—` in all three fields
  (label-inflation check: no withheld accomplishment, publication, or hobby content in the record)

## Twin check (2026-11-14)
Captures 1–2 are two serializations of **one self-report record family** on
taiwaneseamericanhistory.org. Containment run rather than naive md5: Capture 1's JSON
carries empty `content_html`/`excerpt` (narrative fields render only in Capture 2), so
Capture 2 is the **richer** narrative artifact (Education/Employment/blank roster rows),
while Capture 1 is richer only in metadata (`modified` stamp, profession taxonomy ids,
`page_bytes`). Agreement across two serializations of one editable self-report is
**not corroboration**: every biographical fact is labeled `self-reported`/`alleged` on
the subject page.

## Third-party records naming him (2026-11-14 whole-corpus sweep)
`grep -rlF '鄭學成' content knowledge` (non-index hits) plus case-insensitive
`grep -rliF 'Harrison Cheng'`:

1. **FAPA-OC 柑縣分會 2024 annual meeting** — `knowledge/web-archives/taiwandaily-net-42113-42113.md`
   (美洲台灣日報, published 2024-10-13, 記者林蓮華/柑縣報導, fetched 2026-10-23):
   「鄭學成會長開場，說明FAPA宗旨…」 — he is chairing/president of the FAPA Orange County
   (柑縣) chapter as of 2024-10-12. Third-party press byline, not self-report.
2. ** Irvine TPC 長青教室 2024 秋季班** — `knowledge/web-archives/itpc_senior_class.md`
   (Irvine Taiwanese Presbyterian Church Senior Class syllabus,
   https://www.irvinetpc.org/MinistriesPrograms/SeniorClass.html):
   「10/02 鄭學成教授, 中國經濟何去何從?」 with YouTube recording link.
3. **Irvine TPC 長青教室 2017 秋季班** — same syllabus file:
   「10/11 鄭學成教授 長青經濟學」 with Drive 記錄 + YouTube 錄影 links; mirrored as a
   roster row in `knowledge/web-archives/taiwaneseamericanhistory-org/posts/videos84.md`
   (TAH video item #84, 長青教室秋季班錄影 2017).

## Excluded hits (2026-11-14)
Machine indexes are not sources: `knowledge/research/taiwaneseamericanhistory-org/units.jsonl`,
`posts/index.jsonl`, `tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`,
`taiwaneseamericanhistory-org-family.json`, `ee-vault-index.v1–v5.json`. Own pages/hubs:
`people/prof-harrison-cheng.md`, `people/index.md`, `sources/taiwaneseamericanhistory-org.md`,
work page [[works/taiwaneseamericanhistory-org/whos-who-1912-harrison-cheng]].
Disambiguation HOLD (from the subject page): the 「鄭教授」 in
[[works/taiwaneseamericanhistory-org/ourjourneys277]] is 鄭良福 (Milwaukee, puppet troupe
donor) — different person, not merged. 「鄭文龍律師」 in the 2017 12/13 syllabus row is a
different speaker.
