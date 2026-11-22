---
title: "TAH Who's Who profile capture — 2130. Dr. Kopin Liu 劉國平博士"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 2130. Dr. Kopin Liu 劉國平博士

Primary capture of the subject's own self-reported TAH Foundation Who's Who record, archived on
this box as two distinct artifacts. Preserved in full because the biographical fields are
self-reported and the live site is editable, and because every directory fact on
[[people/dr-kopin-liu|Dr. Kopin Liu 劉國平博士]] traces to these two files.

## Subject
- [[people/dr-kopin-liu|Dr. Kopin Liu 劉國平博士]] — TAH Who's Who record #2130, published 2018-06-13

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-kopin-liu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/dr-kopin-liu/](https://taiwaneseamericanhistory.org/person/dr-kopin-liu/)
- **Record id:** 74619 · **type:** `tah_person` · **profession taxonomy:** `chemist`, `physicist`,
  `researcher`, `scientist` (`person_profession-chemist`, `person_profession-physicist`,
  `person_profession-researcher`, `person_profession-scientist` in `class_list`; numeric
  `person_profession: [2239, 2230, 1813, 2235]`)
- **`modified` on source:** 2026-06-19T17:01:33 (`page_bytes`: 56,602 raw HTML; `page_text` is the
  trafilatura-extracted text)
- **Site-rendered header:** `Who's Who Taiwanese American Profile · Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** `English Name Dr. Kopin Liu` · `Hanji Name 劉國平博士` ·
  Birth Year `1949` · Birth Place `Hsinchu, Taiwan` ·
  `First year / First city / State in U.S.` `-/Athens/OH` · Address `Taiwan`
- **Family (verbatim):** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three rows present
  and empty; structured `family: []`, `family_filled: false`. This is an absence of record, not
  evidence of an absence of family.
- **Education:** 1. National Tsing Hua Univ. — `1971` — B.S., Chemistry · 2. Ohio Univ. — `1977` —
  Ph.D., Chemistry
- **Employment:** 1. Argonne National Laboratory — `1982-1993` — Researcher ·
  2. Institute of Atomic and Molecular Sciences, Academia Sinica — `1993-2001` Researcher /
  `2001-2004` Director / `2002-present` Distinguished Researcher ·
  3. National Taiwan Univ. — `2110-present` — Distinguished Research Lecturer of the Dept. of Physics
- **Accomplishment (verbatim, all five rows):** `1. A Chaired Professor of the Lin Rong-shan
  Foundation 1993-1996` · `2. Elected as a fellow of the American Physics Society, 1998` ·
  `3. An Awardee of the Foundation for the Advancement of Outstanding Scholarship 1996-2001 &
  2001-2006` · `4. Presidential Science Prize, 2001` ·
  `5. A member of Academia Sinica in 2004 and a fellow of TWAS in 2005.`
- **Publication / Hobby:** both `--` (empty), so no bibliography and no personal detail is being
  withheld from the person page by this artifact
- **Sidecar vs taxonomy delta:** the crawl `sidecar` carries `hanzi: 劉國平博士` ·
  `birth_year: "1949"` · `birthplace: "Hsinchu, Taiwan"` · `roles: ["scientist", "professor"]`. The
  sidecar's two roles **drop** `chemist` and `physicist` from the four-token `class_list`
  taxonomy — and `professor` appears in no taxonomy token at all, only in the sidecar. The
  chemistry/physics identity is the taxonomy's, not the sidecar's.
- **Internal typo pair (same artifact):** the form field reads
  `Elected as a fellow of the American Physics Society, 1998`; the site-rendered
  `Notable Accomplishments` block below the form reads
  `Elected as a Fellow of the American Physical Society, 1998`. Same honor, two spellings of the
  awarding body inside one capture — `American Physical Society` (APS) is the real body; the
  transcription carries both forms and neither is silently corrected.
- **Year typo:** the NTU lectureship year field reads `2110-present` in both artifacts — a
  three-decade forward typo for `2010-present`. Recorded as-found, not corrected.
- **Site-rendered second block (below the form fields):** `Dr. Kopin Liu` ·
  `Hanzi Name 劉國平博士` · `Birth Year 1949` · `Birthplace Hsinchu, Taiwan` · `Residence Taiwan` ·
  then the same Education / Position entries re-rendered with the degree years in parentheses
  (`B.S., Chemistry (1971)`, `Ph.D., Chemistry (1977)`, `Researcher (1982-1993)`,
  `Director (2001-2004)`, `Distinguished Researcher (2002-)`). This block repeats the form fields
  and adds no fact; note it silently drops the `First year / First city / State in U.S.` arrival
  datum that the form carries.
- **Closing line rendered on the profile:** `Travel the roads paved by those who came before us.`
  — sits in the site chrome directly above the TAH Foundation mission paragraph; not his words.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2130-kopin-liu.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2130-kopin-liu/](https://taiwaneseamericanhistory.org/whos-who-2130-kopin-liu/)
- **Title:** `2130. Dr. Kopin Liu 劉國平博士` · the vault works record
  [[works/taiwaneseamericanhistory-org/whos-who-2130-kopin-liu|TAH #2130]] dates it 2018-06-13
  (`value_band: B`)
- Field set identical to Capture 1 — name pair, Birth Year `1949`, Birth Place `Hsinchu, Taiwan`,
  `-/Athens/OH` first-year-in-U.S. field, Address `Taiwan`, the three empty Family rows, both
  education rows, all employment rows including `2110-present`, the full five-row `Accomplishment`
  block (single `American Physics Society` spelling), empty Publication / Hobby. No `Accomplishment`
  field is withheld anywhere on the directory record.

## Twin check (2026-11-12)
The two artifacts are **distinct records, not archive twins**: whitespace-stripped,
frontmatter-excluded body md5 `4ab5c0461435` (3,019 chars — the crawled profile page, incl. site
chrome, the four-token profession taxonomy, the `Notable Accomplishments` block with the
`American Physical Society` spelling, the site-rendered Education/Position block, and the
2026-06-19 `modified` stamp) vs `5747134078b3` (1,208 chars — the encyclopedia-entry dump). The
education/employment/accomplishment field set therefore occurs twice inside Capture 1 and once in
Capture 2. Repetition of one field set within the same self-report is **not** independent
corroboration.

## What this capture does NOT establish
- The Athens/OH first-U.S. field carries **no year** (`-`), so no arrival date is recorded.
- No spouse, daughter, or son named — three Family rows present and empty, `family: []`,
  `family_filled: false`.
- Every honor is **self-reported**. No press item, academy announcement, or association record
  naming 劉國平 / Kopin Liu exists on this box (see the corpus sweep on the person page). Each is
  `sourced` (self-report) with **no third-party corroboration**: the Lin Rong-shan Foundation
  named professorship, the 1998 APS fellowship, the FAOS awards, the 2001 Presidential Science
  Prize, the 2004 Academia Sinica membership, and the 2005 TWAS fellowship. The Academia Sinica
  affiliation is at least *institutionally consistent* — the same record places him at that
  institution's Institute of Atomic and Molecular Sciences as Researcher (1993-2001), Director
  (2001-2004), Distinguished Researcher (2002-).
- The `Travel the roads paved by those who came before us.` line is site chrome shared by these
  profiles and is not quoted as the subject's own words.
- zh.wikipedia / Wikidata: not probed on this card (WEB-PASS lane owns that lookup).

## Related
- [[people/dr-kopin-liu|Dr. Kopin Liu 劉國平博士]] — the subject
- [[works/taiwaneseamericanhistory-org/whos-who-2130-kopin-liu|2130. Dr. Kopin Liu 劉國平博士]] — the
  vault's bibliographic record for the same entry
- [[organizations/tah-foundation||TAH Foundation]] — publisher
- [[sources/taiwaneseamericanhistory-org||taiwaneseamericanhistory.org]] — source corpus
