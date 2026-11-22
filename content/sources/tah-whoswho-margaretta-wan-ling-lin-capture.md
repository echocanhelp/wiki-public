---
title: "TAH Who's Who profile capture — 2291. Margaretta Wan-Ling Lin"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2291. Margaretta Wan-Ling Lin

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 770
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/margaretta-wan-ling-lin|Margaretta Wan-Ling Lin]] — TAH Who's Who record #2291

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/margaretta-wan-ling-lin.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/margaretta-wan-ling-lin/](https://taiwaneseamericanhistory.org/person/margaretta-wan-ling-lin/)
- **Record id:** 74783 · **type:** `tah_person` · page size 57,126 bytes
- **Profession taxonomy (`class_list`):** `activist` · `community leader` · `lawyer` · `public health` — note the sidecar `roles` field keeps only `lawyer`; the three other tags are site taxonomy absent from the roster dump.
- **`modified` on source:** 2026-06-02T17:25:14 · site-rendered banner on the same page reads `Last updated: June 2, 2026`
- **Verbatim fields (self-reported):** English Name `Margaretta Wan-Ling Lin` · Hanji Name `--` · Birth Year `--` · Birth Place `Taiwan`
- **First year / first city / state in U.S.:** `1968/-/-` — the only arrival-year record for this subject on this box (city/state blank)
- **Address:** `CA`
- **Family:** `1. Husband: --` · `2. Daughter: --` · `3. Son: --` — all three blank; JSON parses `family: []`, `family_filled: false`
- **Education:** 1. Univ. of Virginia — 1982–1986 — B.A., East Asian Studies and Religious Studies · 2. Beijing Normal Univ. — 1986–1987 — Mandarin · 3. Univ. of California, Berkeley — 1987–1991 — J.D.; 1988–1991 — M.A., East Asian Studies
- **Employment:** 1. East Bay Community Law Center — 2003–2009 — Director of Community Economic Justice · 2. City of Oakland — 2009–2010 — Senior Advisor to Mayor Ron Dellums; 2010–2011 — Deputy City Administrator; 2011–2015 — Director of Strategic Initiatives/Special Projects Director · 3. The Dellums Institute for Social Justice — 2015–2018 — Executive Director · 4. Just Cities — 2018–present — Executive Director
- **Accomplishment:** `1. Human rights lawyer & racial justice advocate` — restated verbatim in the page's `Notable Accomplishments` block; restatement inside one editable page is not corroboration
- **Publication / Hobby:** `--` — unfilled
- **`content_html` is empty** — the profile carries no free-text biography beyond the form fields.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…`), this record prints no upstream-source attribution, so no external article can be traced from it.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2291-margaretta-wan-ling-lin.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2291-margaretta-wan-ling-lin/](https://taiwaneseamericanhistory.org/whos-who-2291-margaretta-wan-ling-lin/)
- **Title:** `2291. Margaretta Wan-Ling Lin` · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2291-margaretta-wan-ling-lin|TAH #2291]], published 2020-11-04, `value_band: B`
- The dump reproduces the Capture 1 form fields (English Name through Hobby). It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14)
Frontmatter-stripped, `#`/whitespace-normalized: profile `page_text` 2,237 chars vs post dump 835 chars.
md5 `4533b5da150ea9d3e60df111b1a71d92` vs `8a5fa685863ffb36ce7b4d4482489816` — neither is a substring of the other
(difflib ratio 0.536): the post dump omits the site chrome and renders blank fields as `—`, while the profile
page adds the site navigation, the `Last updated: June 2, 2026` banner, and the footer summary block.
The biographical payload (education, employment, accomplishment, arrival year) is identical across the two
serializations of one editable self-report — agreement here is NOT corroboration.

## Harvest provenance
- Both captures come from the `wp-json` harvest of taiwaneseamericanhistory.org under
  `knowledge/web-archives/taiwaneseamericanhistory-org/` (`MANIFEST.json`).

## Twin & cross-check (2026-11-14)
Whole-vault sweeps this pass (`grep -rlF`, single pattern per form, over `content/` + `knowledge/`):
`Margaretta Wan-Ling Lin` hits only her own person page, own work page, own two captures, `people/index.md`,
the `sources/taiwaneseamericanhistory-org.md` hub listing, crawler/research indexes, and two disambiguation
notes ruling her out as a false hit — [[people/eric-ling|Eric Ling]] (surname-substring `Ling`, slices
10052045-19 / 10070714-18) and [[people/wan-lin-tsai|Wan-Lin Tsai]] (`Wan-Ling` vs `Wan-Lin`, slices
09160700-19 / 09170500-7). `Margaretta Lin`: zero hits. Chinese name forms 林萬玲 / 林婉鈴 / 林萬齡 / 萬玲:
only this page's own candidate-name list. Institution sweeps `Just Cities`, `Dellums Institute`,
`East Bay Community Law`: **zero files outside her own record**. No memoir (My Stories), taiwandaily, or
org page names her.

## What this capture does NOT establish
- No Chinese (Hanji) name — `--`; every Chinese form on the person page is an unverified guess.
- No birth year; birth place `Taiwan` is self-reported. The `1968` in the arrival field is the year of first
  arrival in the U.S. (city/state blank), not a birth year.
- No family names — husband/daughter/son rows present but blank.
- No accomplishments beyond the self-described `Human rights lawyer & racial justice advocate` label,
  no publications, no hobbies.
- Whether the Just Cities role (2018–present) is still current at capture time is unverified beyond the
  self-reported profile and its `modified` 2026-06-02 stamp.
