---
title: "TAH Who's Who profile capture — 70. Ya-hui Chiu 邱雅惠"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 70. Ya-hui Chiu 邱雅惠

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 782
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record
(#70, published 2014-10-23), archived on this box as two distinct artifacts plus one
third-party community record. Preserved because the biographical fields are
self-reported and the live site is editable.

## Subject
- [[people/ya-hui-chiu|Ya-hui Chiu 邱雅惠]] — TAH Who's Who record #70

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ya-hui-chiu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ya-hui-chiu/](https://taiwaneseamericanhistory.org/person/ya-hui-chiu/)
- **Record id:** 72660 · **type:** `tah_person`
- **Profession taxonomy (`class_list`):** `person_profession-engineer`, `person_profession-entrepreneur`, `person_profession-physicist`, `person_profession-researcher`, `person_profession-scientist` (numeric ids `person_profession: [2227, 2241, 2230, 1813, 2235]`). Note: **`physicist` and `researcher` appear only in the taxonomy** — the `sidecar` roles list keeps only `engineer / entrepreneur / scientist`, so the sidecar is role-truncating, not the full taxonomy.
- **`modified` on source:** 2026-06-19T16:26:35 · `page_bytes`: 55,340 (raw HTML; `page_text` is the trafilatura-extracted text)
- **Verbatim fields (self-reported):** English Name `Dr. Ya-Hui Chiu` · 漢文名 `邱雅惠 博士` · Birth Year `1949-2016` · Birth Place `台灣台南` · First arrival in U.S. `-/-/-` (never filled) · Address `Ridgewood, NJ`
- **Family:** `1. Wife: 方美玲` · `2.Daughter: Robin邱如敏` · `3.Daughter: Candice邱如珍` — JSON parses as `family_filled: true`
- **Education (3 rows):** `1.台灣大學 — B.S. Physics` · `2.Yale University — M.S. Physics` · `3.Yale University — Ph.D. Physics`
- **Employment (4 rows):** `1.Yale University 1979-1981 post-doctor fellow` · `2.Bell Laboratory 1981-1983 Member of technical staff` · `3.Western Union 1983-1989 Senior Engineer` · `4.Asia Satellite Telecomunications 1989-2011 CEO` (typo `Telecomunications` as printed on the form)
- **Accomplishment / Publication (non-professional) / Hobby / Website or Blog:** `-` — all four unfilled. The unfilled fields are themselves the record: no self-published web arm or non-professional publication is withheld elsewhere on this capture.
- **Footer restatement block (second serialization in the same `page_text`):** restates `Residence: Ridgewood, NJ`, splits `Birth Year: 1949` from `Passed Away: 2016` (the form field prints the single string `1949-2016`), and reprints all education/employment rows with the typo corrected to `Asia Satellite Telecommunications`. The `Travel the roads paved by those who came before us…` line is site footer chrome, not subject data.

## Capture 2 — whoswho #70 post dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho71.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho71/](https://taiwaneseamericanhistory.org/whoswho71/)
- **Work page:** [[works/taiwaneseamericanhistory-org/whoswho71|70. Ya-hui Chiu 邱雅惠]] (published 2014-10-23, bibliographic record)
- Carries the same form fields (English Name through Website or Blog); does not carry the footer restatement block.

## Twin check
Ran per policy: profile slice taken from the `Who's Who Taiwanese American Profile` marker to the `Travel the roads paved…` footer line; both sides normalized by stripping `#`/whitespace; md5 + both containment directions.

- `md5(profile)` = `0a35401df001601a977800cc8018cb14` (981 norm chars)
- `md5(post)` = `90fdbd9cd07f0f97ee0eeef6ce1a6f54` (612 norm chars)
- Containment: `post ⊂ profile` → False · `profile ⊂ post` → False (the profile slice carries the `Last updated: June 19, 2026` line, the taxonomy tag list, and the footer restatement block, none of which appear in the post dump; the post dump carries its own `# 70. …` heading and `–` en-dash glyph variants)

Ruling: this is **one editable self-report rendered twice**, not two independent
records. Field-level diff shows the post dump's content-block fields are a subset of
the profile's content-block fields; the non-containment is serialization noise
(restatement block, updated-stamp line, dash glyph), not corroborating content.
Agreement across the two is therefore **not corroboration** — which is what keeps the
record's own fields at `self-reported/alleged` rather than `documented`.

## Third-party community record (corroboration)
- **Death notice, TAC-GNY via TAANJ members list, 2016-11-09** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/newsletter-of-taanj.md` (work page [[works/taiwaneseamericanhistory-org/newsletter-of-taanj|TAA/New Jersey Chapter newsletter]], forwarded item):
  > Subject: [TAANJmembers] Fwd: [TAC-GNY] 11/12 3pm 邱雅惠會長告別式
  > 「Our dear friend 邱雅惠先生於11月4日 驟然過往. 告別式訂於本週六在紐澤西舉行。時間：11月12日星期六下午3時 地點：Vander Plaat Funeral Home, 257 Godwin Avenue, Wyckoff, New Jersey」
  Sent Wednesday, November 9, 2016 (Mark Kao, TAA-NJ President forwarding TAC-GNY). Third-party, dated, and independent of the editable self-report: it fixes **death 2016-11-04** and funeral **2016-11-12 at Vander Plaat Funeral Home, Wyckoff, NJ**, and it titles him **會長** (president — organization not named in the notice itself; TAC-GNY is the forwarding list, see GAPS).
- **Wife's own community role, TAA/NNJ 2018 annual meeting roster, 2018-02** — `knowledge/web-archives/taiwaneseamericanhistory-org/posts/activities-of-taannj.md` (work page [[works/taiwaneseamericanhistory-org/activities-of-taanj|TAA/NJ 紐澤西台灣同鄉會的活動]], dated 2019-01-14): the 2018 理事名單 lists 「十一位理事:呂佩璜,陳企勻, 張惠珍, 陳桂芳,張國卿, 廖淑怜, 陳振庭,洪月玲,黃安玲, 李鎧宇,方美玲」 — i.e. **方美玲, the wife named in his self-report, seated as a TAA/NNJ chapter 理事**. This is a same-name match against the self-reported spouse; treated as corroborating context, labeled `alleged` pending an identity confirmation.

## Disambiguation
Same-given-name hits checked and excluded (per existing notes on sibling pages):
詹雅惠/Nancy Jan, 王雅惠, 黃雅惠 (TAH #76), 張雅惠 (Our Journeys #305 roster) are different
people — see `content/people/ya-hui-wang.md` disambiguation note and
`content/people/ming-liang-lee.md` wife note.

## Machine indexes excluded as non-sources
`knowledge/research/taiwaneseamericanhistory-org/units.jsonl`,
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`,
`knowledge/operational/ee-vault-index.v*.json`,
`knowledge/operational/content-analysis/*.jsonl` — machine indexes, not citable records.
