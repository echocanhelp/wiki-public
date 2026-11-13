---
title: "TAH Who's Who profile capture — 1370. Ian Y. Lian / 2016/11"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1370. Ian Y. Lian / 2016/11

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1121
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record, archived on this
box as two distinct artifacts. Preserved because the biographical fields are self-reported and the
live site is editable, and because this is the **only** source on this box for this person — no
memoir, article, church, org, or event record elsewhere in the corpus names him (see Twin &
cross-check below).

## Subject
- [[people/ian-y-lian|Ian Y. Lian]] — TAH Who's Who record #1370

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ian-y-lian.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ian-y-lian/](https://taiwaneseamericanhistory.org/person/ian-y-lian/)
- **Record id:** 73908 · **type:** `tah_person`
- **Profession taxonomy:** `person_profession: [2248, 2227, 2237, 1813, 2235]` with
  `class_list`: `person_profession-educator`, `person_profession-engineer`,
  `person_profession-professor`, `person_profession-researcher`, `person_profession-scientist` —
  **five** taxonomy terms, and the rendered page prints all five tags
  (`educator / engineer / professor / researcher / scientist`). The harvest `sidecar.roles`, by
  contrast, records only `[engineer, scientist, professor, educator]` — **`researcher` is dropped
  by the sidecar and recovered only from the class_list and the page text**. No taxonomy name→id map
  is archived on this box, so the class-list slugs are the readable form.
- **`modified` on source:** 2026-06-02T17:21:58 · `page_bytes`: 53,609 (raw HTML; `page_text` in the
  JSON is the trafilatura-extracted text — the site chrome, the five profession tags and the
  `Last updated: June 2, 2026` line sit in the raw HTML, not in the extracted summary)
- **Verbatim fields (self-reported):** Name `Dr. Ian Y. Lian` · Birth Year `-` ·
  Birth Place `-/-/-` · Address `Beaumont /TX` (the footer block restates it as
  `Residence: Beaumont, TX`)
- **U.S. arrival:** the field is present and unfilled — it prints the form placeholder
  `year, City/State`, not data. No arrival year, city, or state exists on this record.
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; the JSON parses
  `family: []`, `family_filled: false`. A recorded gap, not an absence of family.
- **Education (3 rows, all UCSD):** `1. UCSD — 1999 — B.S. Bioengineering` ·
  `2. UCSD — 2004 — M.S. Bioengineering` · `3. UCSD — 2007 — Ph.D. Bioengineering`
- **Employment (1 row):** `1. Department of Biology, Lamar University — 2013-present — Assistant Professor`
- **Accomplishment:** `-` · **Publication (non-professional):** `-` · **Hobby:** `-` ·
  **Website or Blog:** `-` — all four unfilled. The unfilled fields are themselves the record: no
  publication, honor, or self-reported external link is being withheld elsewhere on this capture.
- **Hanzi:** `sidecar.hanzi: null` — no Chinese name exists in either artifact.
- **Motto line rendered on the page (same editable self-report):** `Travel the roads paved by
  those who came before us.` Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1370.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1370/](https://taiwaneseamericanhistory.org/whoswho1370/)
- **Title:** `1370. Ian Y. Lian / 2016/11`
- The dump reproduces the Capture 1 form fields verbatim (empty Name heading row, `Dr. Ian Y. Lian`,
  Birth Year `–`, Birth Place `-/-/-`, the unfilled U.S.-arrival placeholder, Address
  `Beaumont /TX`, the three blank Family rows, the three UCSD education rows, the single Lamar
  University employment row, and blank Accomplishment / Publication / Hobby / Website). It is a
  second rendering of the same self-reported payload, not an independent source. Unlike sibling
  records (e.g. abby-hong's `Source from 美洲台灣日報…`), this record carries **no upstream-source
  attribution line**, so no external article can be traced from it.

## Third vault record — the bibliographic work page
- **File:** `content/works/taiwaneseamericanhistory-org/whoswho1370.md`
- **Title:** `1370. Ian Y. Lian / 2016/11` · `value_band: B` · `license: all-rights` ·
  `Date: 2016-11-05` · `Byline: —`
- It is a **bibliographic-only** record (`Bibliographic record only. Full text stays in the vault`)
  and carries none of the biographical fields above — the web-archive captures, not the work page,
  are the provenance for every dated row on the person page. Its `## Subjects` lists this subject as
  `mentioned in this record` and still reads `(named subjects pending absorb)`.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded
  in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`,
  `method: wp-json`, expected 2,212 person / 339 organization).
- This slug **is** in that manifest's `weak.person` list (1,857 of the 2,212 person records), i.e.
  the harvest grader marked this profile's payload thin at fetch time — consistent with the
  `-`-filled fields above.

## Twin & cross-check (2026-11-12)
Normalized body md5 (frontmatter excluded, `#`/whitespace stripped), computed this pass:

| artifact | md5 (12) | normalized chars |
|---|---|---|
| Capture 1 — crawled profile page (JSON `page_text`) | `483b3d29bce4` | 2,430 |
| Capture 2 — encyclopedia-entry dump (`posts/whoswho1370.md`) | `5633cccf5bd3` | 412 |
| Work page #1370 (`content/works/.../whoswho1370.md`) | `2690d005f0a9` | 931 |

The two captures are **distinct serializations of one editable self-report, not two independent
sources**. Their field sets agree because Capture 2 is a dump of the same WordPress payload Capture 1
crawled; agreement across two serializations of one form establishes only that the form was not
edited between the fetches. That is why self-reported honors stay `alleged` and never rise to
corroboration — and here there is no honor to grade, since `Accomplishment` is `-`.

Whole-corpus sweep this pass — single-pattern `grep -rlF` per name form, controls counted:
`Ian Y. Lian` → content 6 / knowledge 5 (own page, `people/index.md` at two lines, the work page, the
source hub, plus crawler/research indexes); `Ian Lian` → content 1 (own page only); `ian-y-lian` →
the same set plus 8 `knowledge/operational/deepen-x-slice-*.txt` builder artifacts and the
floor/scout/incident indexes. No CJK name exists to sweep (both artifacts record `hanzi: null`).
`Lamar University` returned no file naming this subject. Every non-index hit is his own capture, the
work page, `people/index.md`, the source hub, or a machine index (`units.jsonl`,
`posts/index.jsonl`, `ee-vault-index.v*.json`, `tdm-page-title-index.json`,
`taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`,
`content-analysis/*.jsonl`) — indexes are not sources.

Same-name / near-name false positives excluded before the sweep was called clean: `whos-who-2232-ian-chen`
(Ian Chen), `whos-who-1727-ian-cheng` (Ian Cheng), `865-i-y-lin-林一洋`, `i-yang-lin-m-d-memorial-lectureship`
(I-Yang Lin), and the `ourjourneys262` "Ian" already excluded by the 2026-10-08 pass as the Ding
sons' son (丁博生夫婦之公子). None is this subject; none was merged.

**No memoir (`mystories*`), Our Journeys issue, taiwandaily/TJJ article, church, org, or event record
on this box names him.**

## What this capture does NOT establish
- No Chinese name, no birth year, no birthplace, no U.S. arrival year/city/state, no spouse or
  children names — those fields are blank or placeholder in both artifacts.
- No publication list, no honor, no award, no grant, no lab name, no research specialty, and no
  service to any Taiwanese American association — the corresponding form fields are `-`.
- The `Lamar University` affiliation is self-reported with a `2013-present` range; no Lamar faculty
  roster, course listing, or publication record is archived on this box, so current status is
  unverified as of this pass.
