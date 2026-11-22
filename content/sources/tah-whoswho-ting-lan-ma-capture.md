---
title: "TAH Who's Who profile capture — 2210. Ting-Lan Ma 馬鼎嵐"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2210. Ting-Lan Ma 馬鼎嵐

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 765
- wikilinks: 2


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/ting-lan-ma|Ting-Lan Ma 馬鼎嵐]] — TAH Who's Who record #2210

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ting-lan-ma.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ting-lan-ma/](https://taiwaneseamericanhistory.org/person/ting-lan-ma/)
- **Record id:** 74703 · **type:** `tah_person` · **profession taxonomy (`class_list`):** `educator`, `professor`, `psychologist`, `researcher` (term ids `[2248, 2237, 465, 1813]`) — the `psychologist` and `researcher` tags are **absent from the sidecar roles** (`roles: ["professor","educator"]`), i.e. the site taxonomy is richer than the person-page frontmatter
- **`modified` on source:** 2026-06-19T17:02:57 · page size 55,755 bytes · the rendered profile also prints `Last updated: June 19, 2026` — same date, so the crawl is current to the source's own stamp
- **Verbatim fields (self-reported):** English Name Ting-Lan Ma · Hanji Name 馬鼎嵐 · Birth Year `--` · Birth Place Taiwan · First year / First city / State in U.S. `-/-/-` · Address `WI`
- **Family:** `1. Husband: --` · `2. Daughter: --` · `3. Son: --` · `4. Father/Mother: -/-` — all blank; capture JSON `family: []`, `family_filled: false`
- **Education:** 1. National Chunhua Univ. — 2006 — B.S. Counseling Psychology · 2. Univ. of Wisconsin — 2009 — M.S., Educational Psychology; 2013 — Ph.D., Human Development, Educational Psychology
- **Employment:** 1. Edgewood College in Madison, Wisconsin — 2015-present — Assistant Professor · 2. Univ. of Irvine — 2017-2019 — Assistant Project Researcher
- **Accomplishment (full list, self-reported):** 1. O'Shea Fellowship, Univ. of Wisconsin, 2011-2012 · 2. Vilas Dissertator Award, Univ. of Wisconsin, 2012-2014 · 3. Dissertator Fellow, European Society for Research on Adolescence / Society for Research on Adolescence, 2013 · 4. Graduate Travel Award, Univ. of Wisconsin, 2010-2014 · 5. Faculty Mini-Grant, Edgewood College, 2015-2018
- **Publication / Hobby:** `--` (blank) — label-inflation proof that no crown fact is withheld from this record; the `Notable Accomplishments` block restates the same five awards verbatim

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2210-ting-lan-ma.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2210-ting-lan-ma/](https://taiwaneseamericanhistory.org/whos-who-2210-ting-lan-ma/)
- **Title:** `2210. Ting-Lan Ma 馬鼎嵐` · works record [[works/taiwaneseamericanhistory-org/whos-who-2210-ting-lan-ma|2210. Ting-Lan Ma 馬鼎嵐]] dated 2019-07-04, value band B (bibliographic)
- Field set identical to Capture 1 (English Name / Hanji Name / Birth Year / Birth Place / arrival / Address / Family / Education / Employment / Accomplishment / Publication / Hobby), rendered as the 2019 encyclopedia entry.

## Twin check (2026-11-14)
Re-measured with frontmatter excluded and whitespace + `#` stripped:
- crawled profile content block (from `Who's Who Taiwanese American Profile` to the site footer line `Travel the roads paved…`): **1,573 norm chars**, md5 `45d09f910c437f9091b3d444451293bf`
- encyclopedia-entry dump body: **842 norm chars**, md5 `d45144370b25cdf847f64808d3b4bf2b`
- Containment test: neither is a substring of the other (`post in profile: False`, `profile in post: False`), but a field-level diff shows the dump carries **no field the profile lacks** — the profile block alone carries the extra `Last updated: June 19, 2026` stamp, the `educator/professor/psychologist/researcher` taxonomy, and the `Hanzi Name` / `Birthplace` / `Residence` / `Position` re-render labels plus the duplicated `Notable Accomplishments` restatement.

The two artifacts are therefore **two serializations of one editable self-report, not independent
corroboration**: agreement across them keeps every field at `self-reported` / `alleged`, and is why the
2019 encyclopedia date and the 2026 profile stamp are treated as publication/refresh dates of the same
record rather than two sources.

## Gaps / NEED YOU
Sources checked 2026-11-14 on this box (whole `content/` + `knowledge/`, case-insensitive `grep -rilF`, machine indexes excluded):
- `馬鼎嵐` → own works record, own person page, sources page, machine research JSONs (`taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`), own post dump, own person JSON. No third-party hit.
- `Ting-Lan Ma` / `Ting-Lan` / `ting-lan` → same hit set plus deepen-x slice logs and operational incident files (machine artifacts, not sources).
- `Tinglan` → only her own person page.
- `Edgewood` → her own artifacts plus `posts/38-ming-franz.md`, `posts/artist2-chaomin-liu.md`, `person/ming-franz.json` — spot-check 2026-11-14: those mention Edgewood's own gallery/campus events and do not name 馬鼎嵐 (0 hits for her name in them).
- `Dissertator` → only her own artifacts.
- Wikipedia / Wikidata / 華文 press / 官網 arms: no local capture of any of the four exists for this subject on this box (see `## Online arms` on the person page).

No further citable source exists on this box beyond the subject's own editable self-report and its
bibliographic mirror. What remains externally: a university/faculty-page confirmation of the Edgewood
appointment and the dissertation title, and any 華文 press coverage.
