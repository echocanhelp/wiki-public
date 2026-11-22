---
title: "TAH Who's Who profile capture — 1441. Yuan-Shuh Lii 李元恕"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1441. Yuan-Shuh Lii 李元恕

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 504
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/yuan-shuh-lii|Yuan-Shuh Lii 李元恕]] — TAH Who's Who record #1441

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/yuan-shuh-lii.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/yuan-shuh-lii/](https://taiwaneseamericanhistory.org/person/yuan-shuh-lii/)
- **Record id:** 73975 · **type:** `tah_person` · **profession taxonomy:** `person_profession-educator`, `person_profession-professor`, `person_profession-researcher`, `person_profession-scholar`
- **`modified` on source:** 2026-06-19T16:49:45 · page size 53,921 bytes
- **Verbatim fields (self-reported):** Name 李元恕 教授 / Prof. Yuan-Shuh Lii · Birth Year `-/-/-` · Birth Place 台灣 · Address 台灣
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; `family_filled: false`
- **Education:** 1. 東海大學 — `-` — B.S.國際貿易 · 2. Portland State University — `-` — M.S.企業管理 · 3. Portland State University — `-` — Ph.D.行銷
- **Employment:** 1. Portland State University — 1995–2009 — 研究肋理 (rendered 研究助理 in the site's own summary block) · 2. 逢甲大學 — present — 行銷系教授,主任
- **Accomplishment / Publication (Non-professional) / Hobby / Website or Blog:** all `-`
- **Cited upstream source (self-declared):** 「Source from http://www.taiwancenter.com/sdtca/articles/2-04/7.html(美國加州聖地牙哥台灣同鄉會)」

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1441.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1441/](https://taiwaneseamericanhistory.org/whoswho1441/)
- **Title:** `1441. Yuan-Shuh Lii 李元恕 / 2016/12` · **published:** 2016-12-26 (per `knowledge/research/taiwaneseamericanhistory-org/units.jsonl` unit 36202)
- Field set identical to Capture 1, including the same upstream SDTCA source line.

## Twin check (2026-11-14)
The two artifacts are **distinct records, not archive twins**: Capture 1 is the crawled profile
page (site chrome + the 2026-06-19 `modified` stamp + the duplicate summary block), Capture 2 is
the encyclopedia-entry dump (`###`-headed field render). Every biographical value present in one
appears verbatim in the other, so value repetition across them is **not** independent
corroboration — both descend from one self-report.

## Upstream SDTCA article — checked, yields nothing on this subject
- The self-declared upstream source is archived locally at
  `knowledge/web-archives/sdtca-taiwancenter-com/2-04-7-20081012.html` (crawl stamp 2008-10-12).
- A 2026-11-14 grep for 李元恕 / Yuan-Shuh / Yuan Shuh over that HTML returns **no hit**; the
  page is a Big5-encoded article about 張德良 (Andre Chang) and the San Diego Taiwanese Cultural
  Association / 台美雜誌 history. The TAH profile cites it as provenance for the *article layout*,
  not as a record naming this subject.

## What this capture does NOT establish
- No birth year, no birth date, no spouse/children names — those fields are blank in both artifacts.
- No `Accomplishment`, publication, hobby, or website value is recorded.
- The 1995–2009 Portland State University role is recorded as a self-report; its title string is
  inconsistent within the single record (研究肋理 in the Employment field, 研究助理 in the summary
  block), so neither variant is asserted as authoritative.
- Whole-corpus sweep 2026-11-14 (`grep -rl '李元恕|Yuan-Shuh Lii'` over `content/` + `knowledge/`):
  hits only this page, `works/taiwaneseamericanhistory-org/whoswho1441.md`, the two archive
  artifacts above, the source hub listing, and index/analysis ledgers — no memoir, directory, or
  third-party press record naming the subject.
