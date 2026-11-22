---
title: "TAH Who's Who profile capture — 941. John M. Yeh 葉明翰"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 941. John M. Yeh 葉明翰

Primary capture of the subject's own self-reported TAH Foundation Who's Who record, archived on
this box as distinct artifacts. Preserved in full because the biographical fields are
self-reported and the live site is editable.

## Subject
- [[people/john-m-yeh|John M. Yeh 葉明翰牧師]] — TAH Who's Who record #941

## Capture 1 — machine profile record
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/john-m-yeh.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/john-m-yeh/](https://taiwaneseamericanhistory.org/person/john-m-yeh/)
- **Record id:** 73504 · **type:** `tah_person`
- **Profession taxonomy:** `person_profession: [2248, 2147, 1227]`, whose readable slugs in
  `class_list` are `person_profession-educator`, `person_profession-minister`,
  `person_profession-theologian` — three tags. The harvest sidecar keeps only `roles:
  ["educator"]`, so `minister` and `theologian` are taxonomy values the sidecar drops.
- **`modified` on source:** 2026-06-19T16:41:18 (`page_bytes`: 53,181 raw HTML; `page_text` is
  the extracted text; the extracted text itself carries the site banner
  `Who's Who Taiwanese American Profile · Last updated: June 19, 2026`)
- **Verbatim self-reported fields:** Name `葉明翰 牧師` / `Rev. John M. Yeh` · Birth Year `1940` ·
  Birth Place `台灣台北市` · First year, first city and state arrived in the U.S. `-/-/-` ·
  Address `-/TX` · Family `1. Wife: 林佳蓁` · `2.Daughter:-` · `3.Son:-` · Education:
  `1. 台灣基督長老教會聖經學院 – B.S.`, `2. 柏克萊基督工人神學院教 – M.S. 牧學` · Employment:
  `1. 德州奧斯汀台灣基督長老教會 – 牧師`, `2. 巴西宣教師 – –`, `3. 南美基督工人神學院 – 院務主任` ·
  Accomplishment `—` · Publication (Non-professional ones) `—` · Hobby `—` · Website or Blog `—`
- **`content_html` and `excerpt` are empty** in the harvest record; every biographical value above
  comes from the `page_text` render of the live page.
- **Family:** JSON `family: [{"rel": "wife", "name": "林佳蓁"}]`, `family_filled: true` — a spouse
  is named; the Daughter and Son lines are `--` (recorded gaps, not proven absences).

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho941.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho941/](https://taiwaneseamericanhistory.org/whoswho941/)
- **Title:** `941.  John M. Yeh 葉明翰 / 2016/04` · **published:** 2016-04-17 (per the work record
  [[works/taiwaneseamericanhistory-org/whoswho941|TAH #941]])
- The dump repeats the same field set as Capture 1 (Name 葉明翰 牧師 / Rev. John M. Yeh, Birth Year
  1940, Birth Place 台灣台北市, Address `-/TX`, Wife 林佳蓁, the two education rows, the three
  employment rows) and leaves Accomplishment, Publication, Hobby and Website blank. It is the
  human-readable render of the one self-report, not an independent record.

## Twin check (2026-11-13)
The two artifacts are **distinct captures, not byte twins**: whitespace-stripped,
frontmatter-excluded body md5 `d369803fed9f48952f95782f221c9130` (1,196 normalized chars) for the
JSON `page_text` vs `39ae336a3c18f36d381b754024a1ddea` (337 normalized chars) for the post dump;
neither is a substring of the other. The difference is chrome, not content: the JSON render
carries the site navigation, the `educator / minister / theologian` taxonomy block, the banner
`Last updated: June 19, 2026`, and the full two-form render (Chinese-labeled form + Hanzi
summary block); the post dump is the bare field list. **On biographical content they agree
field-for-field**, and that agreement is across two serializations of ONE self-edited record — it
is NOT corroboration. Every fact sourced only here stays `alleged`/self-reported.

## One self-report
The `modified` 2026-06-19 stamp on Capture 1 postdates the 2016-04 publication of Capture 2, so
the record is live-editable and was edited after publication. Whether any field was later emptied
is unknown; no earlier capture exists on this box. The blank `Accomplishment`, `Publication`,
`Hobby` and `Website` fields are recorded gaps in a self-report, not proof the subject has none.

## Harvest provenance
- The person capture comes from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org
  recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`
  (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org records).
- This slug does **not** appear in that manifest's `weak.person` list. The record is complete as
  to what the source site publishes; the thinness (no U.S. arrival data, no accomplishments)
  reflects the self-report itself, not a fetch failure.

## What this capture does NOT establish
- No U.S. arrival year, first U.S. city, or state (`First year, first city and state arrived in
  the U.S. -/-/-`; the `-` before `/TX` leaves the city blank) — the Austin arrival year comes
  from [[works/taiwaneseamericanhistory-org/ourjourney-343|the Austin community memoir]], not
  from this record.
- No dates on any education or employment row (every date slot is `–`), so the Brazil pastorate,
  the South American seminary post, and the Austin church callings are undated in the record.
- No publications, awards, or named accomplishments (all fields `—`).
- No children named (Daughter / Son `--`).
- No website, despite the subject's preaching and lecture circuit documented elsewhere in the
  vault.

## Related
- [[people/john-m-yeh|John M. Yeh 葉明翰牧師]] — subject
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org]] — harvest source hub
- [[organizations/tah-foundation|TAH Foundation]] — publisher
- [[works/taiwaneseamericanhistory-org/whoswho941|TAH #941]] — bibliographic work record

## Absorb verification 2026-11-16
- sourced 2026-11-16: person page [[people/john-m-yeh]] `From the record` rows verified line-by-line against knowledge/web-archives/taiwaneseamericanhistory-org/person/john-m-yeh.json (record id 73504, `modified` 2026-06-19T16:41:18) — fields agree.
- sourced 2026-11-16: 1940 Taipei birth row and 「葉明翰 牧師」/「Rev. John M. Yeh」 name pair confirmed verbatim in knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho941.md (published 2016-04-17).
- sourced 2026-11-16: twin-check hashes d369803fed9f48952f95782f221c9130 (1,196 norm chars) vs 39ae336a3c18f36d381b754024a1ddea (337) re-derived per the Twin check section; absorbed into [[people/john-m-yeh]] `Source Notes` dated 2026-11-13.
