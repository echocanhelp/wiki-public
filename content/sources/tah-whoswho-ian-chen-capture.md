---
title: "TAH Who's Who profile capture — 2232. Ian Chen 陳彥竹"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 2232. Ian Chen 陳彥竹

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/ian-chen|Ian Chen 陳彥竹]] — TAH Who's Who record #2232

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ian-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ian-chen/](https://taiwaneseamericanhistory.org/person/ian-chen/)
- **Record id:** 74726 · **type:** `tah_person` · **profession taxonomy:** `composer`, `conductor`, `musician`
  (`person_profession-composer`, `person_profession-conductor`, `person_profession-musician`;
  term ids `person_profession: [2264, 2266, 2250]`)
- **`modified` on source:** 2026-06-19T17:03:21 · page size 54,704 bytes
- **Site-rendered line:** `Who's Who Taiwanese American Profile — Last updated: June 19, 2026` ·
  name line `Ian Chen 陳彥竹`
- **Verbatim fields (self-reported):** Name 陳彥竹 / Ian Chen · Birth Year `--` ·
  Birth Place `Kaohsiung, Taiwan` · First year, first city and state arrived in the U.S. `-/-/-` ·
  Address `CA`
- **Family:** `1. Wife: —` · `2. Daughter: —` · `3. Son: –` · `4. Father/Mother: -/-` — all blank;
  structured `family: []`, `family_filled: false`
- **Education:** 1. Cornell Univ. — 2007-2011 — B.A., Music, Biology · 2. NYU — 2011-2012 — M.S., Music
- **Employment:** 1. `-` — 2010-present — Composer for Film and Multimedia ·
  2. Alkaloide Music Productions, LLC — 2012-2015 — Orchestrator, Arranger ·
  3. NJ Buddha's Light Youth Chinese Orchestra — 2012 — Guest Conductor
- **Accomplishment (verbatim, both items):**
  1. `This Land won him nominations at several film and music festivals across the globe`
  2. `Soul prisoner Simon's soundtrack shortlisted for the Golden Bell Award for Best Sound (魂囚西門配樂入圍最佳音效金鐘獎)`
- **Publication (Non-professional) / Hobby:** `—` (blank — no crown fact withheld)
- **Embedded press line (verbatim):** `- 用音樂幫電影畫面提味，台灣作曲家陳彥竹好萊塢築夢` followed by
  `Source from www.taiwanjustice.net.` — the profile itself names a taiwanjustice.net article as an
  earlier source for this record
- **`content_html` / `excerpt`:** both empty — the page's data lives in the taxonomy terms and the
  rendered field table, not in a post body.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2232-ian-chen.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2232-ian-chen/](https://taiwaneseamericanhistory.org/whos-who-2232-ian-chen/)
- **Title:** `2232. Ian Chen 陳彥竹` · work record published 2019-12-10
  ([[works/taiwaneseamericanhistory-org/whos-who-2232-ian-chen|TAH #2232]])
- Field set identical to Capture 1, including both `Accomplishment` items, the
  `用音樂幫電影畫面提味…好萊塢築夢` press line, and the trailing `Source from www.taiwanjustice.net.`

## Twin check (2026-11-12)
The two artifacts are **distinct records, not archive twins**: whitespace-stripped,
frontmatter-excluded body md5 `ed5790117360` (2,973 chars — the crawled profile page incl. site
chrome, the profession taxonomy, the `Last updated: June 19, 2026` line and the `modified` stamp) vs
`359fb19e61e0` (742 chars — the encyclopedia-entry dump). Every biographical string they share is the
subject's single self-report restated in two serializations of one editable record, so field agreement
across the two captures is **not** independent corroboration.

## What this capture does NOT establish
- No birth year — the field is `--` in both captures; only `Birth Place: Kaohsiung, Taiwan` is filled.
- No year/city/state of first arrival in the U.S.; the address is only the state `CA`.
- No spouse, children, or parents — all family fields blank, `family_filled: false`.
- The 1. Employment row names no company (`-`); `Alkaloide Music Productions, LLC` appears only on
  row 2, so the page does not state which company employs the 2010-present composer role.
- The named works `This Land` and the `Soul prisoner Simon` soundtrack, and the Golden Bell
  shortlisting, are the subject's own accomplishment claims — the press article they cite
  (`用音樂幫電影畫面提味，台灣作曲家陳彥竹好萊塢築夢`, `Source from www.taiwanjustice.net.`)
  is **not archived on this box**: whole-corpus greps for the exact title, for `魂囚` and for
  `好萊塢築夢` return only these two captures, and the single other `提味` hit
  (`knowledge/web-archives/taiwanjustice-net/raw-html/2025/20250417211943_…深澳小卷名店….html`)
  is a same-site unrelated YouTube-embed title about a squid restaurant — false positive, not the
  cited article. Nothing from that article is asserted here.
- The works page [[works/taiwaneseamericanhistory-org/whos-who-2232-ian-chen|TAH #2232]] is a
  bibliographic-only record (`value_band: B`, "Bibliographic record only. Full text stays in the vault")
  and carries none of the biographical fields above.

## Related
- [[people/ian-chen|Ian Chen 陳彥竹]] — the subject
- [[works/taiwaneseamericanhistory-org/whos-who-2232-ian-chen|TAH #2232 work record]]
- [[sources/taiwaneseamericanhistory-org||taiwaneseamericanhistory.org source hub]]

## Absorb verification 2026-11-16
- sourced 2026-11-16 — person-page absorb re-graded against this capture: page 陳彥竹 in knowledge/web-archives/taiwaneseamericanhistory-org/person/ian-chen.json carries Education 「Cornell Univ. 2007-2011 B.A., Music, Biology」 and 「NYU 2011-2012 M.S., Music」, both rows rendered verbatim on [[people/ian-chen]] — twin-check md5 ed5790117360 (2,973 chars).
- sourced 2026-11-16 — Employment rows 2010-present composer, 2012-2015 Alkaloide Music Productions, LLC orchestrator/arranger, and 2012 NJ Buddha's Light Youth Chinese Orchestra guest conductor in knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2232-ian-chen.md match the page table line-for-line (md5 359fb19e61e0, 742 chars).
- sourced 2026-11-16 — both 「」 Accomplishment claims (`This Land` festival nominations; `魂囚西門配樂入圍最佳音效金鐘獎` Golden Bell sound shortlisting) are reproduced on [[people/ian-chen]] labeled as the subject's own self-report; the cited taiwanjustice.net article stays unarchived per the GAPS roster above.
