---
title: "TAH Who's Who profile capture — 1375. Theodore (Ted) Wing 溫庭宇"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1375. Theodore (Ted) Wing 溫庭宇

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 767
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/theodore-ted-wing|Theodore (Ted) Wing 溫庭宇]] — TAH Who's Who record #1375

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/theodore-ted-wing.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/theodore-ted-wing/](https://taiwaneseamericanhistory.org/person/theodore-ted-wing/)
- **Record id:** 73913 · **type:** `tah_person` · **profession taxonomy:** `entrepreneur` (`class_list` token `person_profession-entrepreneur`, term id `[2241]`)
- **`modified` on source:** 2026-06-19T16:48:41 · page size 51,459 bytes · the rendered profile also prints `Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** Name 溫庭宇 / Theodore(Ted) Wing · Birth Year `-` · Birth Place `-/-/-` · First year, first city and state arrived in the U.S. `-/-/-` · Address `-/TX`
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; capture JSON `family: []`, `family_filled: false`
- **Education:** 1. Texas A&M University — 2013 — M.S.
- **Employment:** Gradalis Inc. — present — Surgical Training Specialist
- **Accomplishment / Publication (Non-professional) / Hobby / Website or Blog:** all `-`
- **Provenance line (self-cited):** `Source from http://www.symposium2016. ttbatw.org/` — the profile records that it was recruited from the 2016 symposium site of the [[organizations/texas-taiwanese-biotechnology-association|Texas Taiwanese Biotechnology Association]] (德州台灣生物科技協會)

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1375.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1375/](https://taiwaneseamericanhistory.org/whoswho1375/)
- **Title:** `1375.  Theodore (Ted) Wing 溫庭宇 / 2016/11` · works record dated 2016-11-05
- Field set identical to Capture 1 (Name / Birth Year / Birth Place / arrival / Address `-/TX` / Family / Education / Employment / Accomplishment / Publication / Hobby / Website), including the `Source from http://www.symposium2016. ttbatw.org/` provenance line.

## Twin check (2026-11-14)
Re-measured with the frontmatter excluded and whitespace + `#` stripped:
- crawled profile content block (from `Who's Who Taiwanese American Profile` to the site footer): **553 norm chars**, md5 `021c4c8b6954`
- encyclopedia-entry dump body: **381 norm chars**, md5 `0d6781c75416`
- Containment test: neither is a substring of the other (`post in profile: False`, `profile in post: False`), but a field-level diff shows the dump is a **serialization subset** of the profile page — every dump line occurs in the profile block; the profile block alone carries 10 extra lines (`Last updated: June 19, 2026`, the `entrepreneur` taxonomy, `Theodore Wing` / `Hanzi Name` / `Residence` / `Position` render labels, `(2013)`).

The two artifacts are therefore **two serializations of one editable self-report, not independent
corroboration**: agreement across them keeps every field at `self-reported`, and it is what keeps the
record's own `Source from…` line at provenance rather than fact.

## Cohort note (why the provenance line is not corroboration of the bio)
The `symposium2016.ttbatw.org` provenance string appears in **20 captures** under
`knowledge/web-archives/taiwaneseamericanhistory-org/` — 10 `tah_person` JSON records (Chou-Long Huang
黃朝龍, Diane D-S. Tang-Liu 湯丹霞, Haofan (Eric) Peng 彭浩帆, Henry C. Liu, Joshua C. Chang 張嘉熙,
Theodore (Ted) Wing 溫庭宇 #73913, Tiencheng Arthur Chang, Wei-Chiang Chen, Yi-Cheng Liu, Yu-Chieh (Jack)
Wang), 10 matching `whoswho` post dumps, plus the TTBATW org directory capture — re-verified 2026-11-14
(`grep -rlF 'symposium2016'` + `grep -rlF 'ttbatw'` over `content knowledge`). A sibling who's-who
subject's capture page (`sources/tah-whoswho-diane-d-s-tang-liu-capture.md`, measured 2026-11-12) found
the same 20-file cohort. The string records where the profiles were collected, not an independent
statement about any one subject. The TTBATW works records
([[works/taiwaneseamericanhistory-org/texas-taiwanese-biotechnology-association|19. Texas Taiwanese
Biotechnology Association]], published 2016-09-14) do **not** name this subject (`溫庭宇 / Wing` = 0 hits
in the sibling captures' sweep and in this pass), so the recruitment link is provenance, not a second
biography.

## Number-collision ruling (2026-11-14)
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/publications-1375.md` shares the number 1375
but is **not** this subject: its H1 is `1375. 南加州台南一中&台南女中校友會2022年刊 | 09/2023/Magazine` — a
Publications post (the Tainan alumni yearbook) with zero biographical fields for Theodore Wing. Do not
count it as a second source.

## What this capture does NOT establish
- No birth year, no birth date, no arrival year/city/state, no spouse/children names — those fields are blank in both artifacts (`family_filled: false`).
- No degree dates beyond the single `2013` M.S. year, no accomplishments, publications, hobbies, or personal website — all `-`.
- The employment row gives no start date — `present` is the only temporal token, undated as a range.
- The symposium-site URL (`symposium2016.ttbatw.org`) is itself gone from the vault — only the TAH profile's citation of it and the TTBATW org captures survive on this box.
- The works page [[works/taiwaneseamericanhistory-org/whoswho1375|TAH #1375]] is a bibliographic-only record (`value_band: B`, "Bibliographic record only. Full text stays in the vault") and carries none of the biographical fields above.
