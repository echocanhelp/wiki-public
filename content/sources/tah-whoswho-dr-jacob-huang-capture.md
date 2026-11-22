---
title: "TAH Who's Who profile capture — 1681. Dr. Jacob Huang 黃正雅醫師"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1681. Dr. Jacob Huang 黃正雅醫師

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/dr-jacob-huang|Dr. Jacob Huang 黃正雅醫師]] — TAH Who's Who record #1681

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-jacob-huang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/dr-jacob-huang/](https://taiwaneseamericanhistory.org/person/dr-jacob-huang/)
- **Record id:** 74196 · **type:** `tah_person` · **profession taxonomy:** `community leader`,
  `educator`, `physician`, `professor`, `public health`, `researcher`
  (`person_profession-*` classes in `class_list`; numeric `person_profession: [2242, 2248, 2234, 2237, 348, 1813]`)
- **`modified` on source:** 2026-06-19T16:53:49 (`page_bytes`: 54,175 raw HTML; `page_text` is the
  trafilatura-extracted text)
- **Site-rendered header:** `Who's Who Taiwanese American Profile · Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** Name `Dr. Jacob Huang` / `黃正雅醫師` · Birth Year `--` ·
  Birth Place `Taiwan` · First year / First city / State in U.S. `-/-/-` · Address `NY`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three rows present and empty;
  structured `family: []`, `family_filled: false`
- **Education:** 1. Columbia Univ. — year field empty — Ph.D., Public Health
- **Employment:** 1. New York Univ. — Professor of Preventive Medicine · 2. New York City Dept. of
  Health — Director (both rows year-empty)
- **Publication / Hobby:** empty (`--`)
- **Accomplishment:** `1. President of Taiwanese American Association of New York (紐約台灣同鄉會會長)` ·
  `2. Awarded the Gold Medal by Congress (獲國會頒發金牌獎章)` — the latter is repeated in the
  site-rendered `Notable Accomplishments` block below the form
- **Provenance line on the profile:** `Source from 美東台灣人夏令會07/1988` — the record was harvested
  from the 美東台灣人夏令會 (TACEC) of July 1988
- **Site-rendered second block (below the form fields):** `Dr. Jacob Huang` · `Hanzi Name 黃正雅醫師` ·
  `Birthplace Taiwan` · `Residence NY` · then the same degree and positions rendered as
  `Education / Columbia University / Ph.D., Public Health` and `Position / New York University /
  Professor of Preventive Medicine` + `New York City Department of Health / Director`, plus
  `Community / Taiwanese American Association of New York / President`
- **Closing line rendered on the profile:** `Travel the roads paved by those who came before us.` —
  site chrome shared by these profiles; see *What this capture does NOT establish*.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1681-jacob-huang.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1681-jacob-huang/](https://taiwaneseamericanhistory.org/whos-who-1681-jacob-huang/)
- **Title:** `1681. Dr. Jacob Huang 黃正雅醫師` · the vault works record
  [[works/taiwaneseamericanhistory-org/whos-who-1681-jacob-huang|TAH #1681]] dates it 2017-05-25
- Field set identical to Capture 1: name pair, `--` birth year, `Taiwan` birthplace, `-/-/-` U.S.
  arrival, `NY` address, the three empty Family rows, the one degree, the two employment rows,
  both `Accomplishment` items (同鄉會會長 + 國會金牌獎章), empty Publication / Hobby, and the same
  `Source from 美東台灣人夏令會07/1988` provenance line.

## Sidecar
`knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-jacob-huang.json` carries a structured
`sidecar`: `hanzi: 黃正雅醫師` · `birth_year: "--"` · `birthplace: Taiwan` ·
`roles: ["physician", "professor", "educator"]`. The sidecar carries three roles where the
`class_list` taxonomy above carries six — it drops `community leader`, `public health`, and
`researcher`, i.e. exactly the three roles the community record (同鄉會會長、夏令會公衛演講) corroborates.

## Twin check (2026-11-12)
The two artifacts are **distinct records, not archive twins**: whitespace-stripped,
frontmatter-excluded body md5 `33c783b8f789` (1,658 chars — the crawled profile page, incl. site
chrome, the six-tag profession taxonomy, the site-rendered Notable Accomplishments / Position
block, and the 2026-06-19 `modified` stamp) vs `3ba7d2a3d5c5` (526 chars — the encyclopedia-entry
dump). The education/employment/accomplishment field set therefore occurs twice within Capture 1
and once in Capture 2. Repetition of one field set within the same self-report is **not**
independent corroboration.

## What this capture does NOT establish
- No birth year (`--` in both artifacts), no city of birth (only `Taiwan`), no U.S. arrival
  year/city (`-/-/-`), no graduation year for the Columbia Ph.D., no start/end years for either
  employment row.
- No spouse, daughter, or son named — the three Family rows are present and empty, and the
  structured `family` array is `[]` with `family_filled: false`. This is an absence of record,
  not evidence of an absence of family.
- `Awarded the Gold Medal by Congress (獲國會頒發金牌獎章)` is recorded exactly as self-reported.
  No congressional record, press item, or organizer document naming 黃正雅 / Jacob Huang as a
  gold-medal recipient exists on this box — whole-corpus grep `國會頒發金牌|Gold Medal by Congress`
  outside these two self-report artifacts returns zero files. The claim is `sourced`
  (self-report) but carries **no third-party corroboration**.
- The `Travel the roads paved by those who came before us.` line cannot be attributed to the
  subject as his own words — it is site chrome shared by these profiles.
- The works page [[works/taiwaneseamericanhistory-org/whos-who-1681-jacob-huang|TAH #1681]] is a
  bibliographic-only record (`value_band: B`, "Bibliographic record only. Full text stays in the
  vault") and carries none of the biographical fields above.
- zh.wikipedia / Wikidata: not probed on this card (WEB-PASS lane owns that lookup).

## Related
- [[people/dr-jacob-huang|Dr. Jacob Huang 黃正雅醫師]] — the subject
- [[works/taiwaneseamericanhistory-org/whos-who-1681-jacob-huang|1681. Dr. Jacob Huang 黃正雅醫師]] —
  the vault's bibliographic record for the same entry
- [[organizations/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org]] — the publishing body
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org source hub]]
