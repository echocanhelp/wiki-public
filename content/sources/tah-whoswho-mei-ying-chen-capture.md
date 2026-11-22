---
title: "TAH Who's Who profile capture — 1285. Mei-Ying Chen 陳美瑩"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1285. Mei-Ying Chen 陳美瑩

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 670
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as three distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable.

## Subject
- [[people/mei-ying-chen|Mei-Ying Chen 陳美瑩]] — TAH Who's Who record #1285 (WordPress post id 73827, type `tah_person`)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/mei-ying-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/mei-ying-chen/](https://taiwaneseamericanhistory.org/person/mei-ying-chen/)
- **Record id:** 73827 · **type:** `tah_person` · **profession taxonomy:** `educator` + `professor` + `scholar` (`person_profession-educator`, `person_profession-professor`, `person_profession-scholar` in `class_list`; numeric term ids `person_profession: [2248, 2237, 2245]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form)
- **`modified` on source:** 2026-06-19T16:47:13 · `page_bytes`: 52,515 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Page title on source:** `Mei-Ying Chen 陳美瑩`
- **Verbatim fields (self-reported):** Name `陳美瑩 教授` / `Prof. Mei-Ying Chen` · Birth Year `-` · Birth Place `台灣`
- **First year, first city and state arrived in the U.S.:** `-/-/-` — unfilled
- **Address:** `台灣`
- **Family:** `1. Husband:-` · `2.Daughter:-` · `3.Son:-` — all three fields present and blank; JSON parses this as `family: []`, `family_filled: false`. A separate `## Family` block on the person page restates `_No filled family fields on the TAH profile._`
- **Education (2 rows, no year ranges):** `1.華盛頓州立大學` — `M.S.` · `2. 華盛頓州立大學` — `Ph.D.` (printed forms quoted as-is)
- **Employment (1 block, 2 institutions, no year range):** `1.科羅拉多大學Boulder分校` — `東亞語文學系講師` · `國立嘉義教育大學` — `副教授`
- **Accomplishment / Publication (non-professional) / Hobby / Website or Blog:** `-` — unfilled. The blank fields are themselves the record: no accomplishment, publication, hobby, or website fact is being withheld elsewhere on this capture.
- **Provenance line:** `Source from Source from台美心聲 04/2007` — the doubled `Source from` is the publisher's own text. Upstream source is 台美心聲 04/2007; **no 台美心聲 archive exists on this box** (whole-vault `grep -rlF '台美心聲'` hits only this record's artifacts, whoswho1283/Irene Lin, and irene-lin's capture — no magazine corpus), so the 2007 upstream article cannot be checked against our holdings.
- **Footer summary block (same page, rendered below the form):** Hanzi `陳美瑩` · Birthplace `台灣` · Residence `台灣` · Education `華盛頓州立大學 — M.S.` / `華盛頓州立大學 — Ph.D.` · Position `科羅拉多大學Boulder分校 — 東亞語文學系講師` / `國立嘉義教育大學 — 副教授`. Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1285.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1285/](https://taiwaneseamericanhistory.org/whoswho1285/)
- **Title:** `1285. Mei-Ying Chen 陳美瑩` · **published:** 2016-09-22 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 33644) · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1285|TAH #1285]], `value_band: B`, bibliographic record only
- The dump reproduces the Capture 1 form fields verbatim (Name, blank Birth Year, Birth Place `台灣`, Address `台灣`, blank Family ×3, 華盛頓州立大學 M.S./Ph.D., 科羅拉多大學Boulder分校 東亞語文學系講師 / 國立嘉義教育大學 副教授, blank Accomplishment/Publication/Hobby/Website, the `Source from Source from台美心聲 04/2007` line). It is a second rendering of the same self-reported payload, not an independent source.

## Capture 3 — harvest manifest
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `-`-filled form fields above.

## Name-collision note (2026-11-14 sweep)
Whole-vault sweep this pass (`grep -rIl` per name form, controls counted). Beyond her own
page/index/source-hub artifacts and crawler indexes, the only other hits are **吳美瑩 (Wu Mei-Ying)**,
a *different person*: NTPW 2025 西南區代表 in `content/organizations/national-taiwanese-presbyterian-council.md`,
`knowledge/research/ntpc-usa-org-entities.md`, and `knowledge/web-archives/ntpc-usa-org-ntpw.md`
(crawled 2026-08-18). No record on this box links the two name forms; recorded here so a future
pass does not sweep the NTPW roster line into this subject. The only other mention of her name
forms outside her own artifacts is the false-positive note on [[people/ying-chen-kao|Ying-Chen Kao]]
(deepen-x 2026-09-15), which already rules out TAH #1285 as a "Ying … Chen" name collision.
