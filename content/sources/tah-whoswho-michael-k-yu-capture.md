---
title: "TAH Who's Who profile capture — 1329. Michael K. Yu 游貴森"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1329. Michael K. Yu 游貴森

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two artifacts. Preserved because the biographical fields are
self-reported and the live site is editable. **No independent third-party record for
this person exists on this box** — see `## What this capture does NOT establish` and the
person page's `## Gaps / NEED YOU`.

## Subject
- [[people/michael-k-yu|Michael K. Yu 游貴森醫師]] — TAH Who's Who record #1329

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/michael-k-yu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/michael-k-yu/](https://taiwaneseamericanhistory.org/person/michael-k-yu/)
- **Record id:** 73870 · **type:** `tah_person` · **profession taxonomy:** `physician`, `surgeon` (`person_profession-physician` / `person_profession-surgeon` in `class_list`; numeric term ids `person_profession: [2234, 2280]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). Note the profile taxonomy carries **`surgeon`** where the person page's Identity Snapshot listed `physician` only — the class list is the fuller self-reported role set.
- **`modified` on source:** 2026-06-19T16:48:03 · `page_bytes`: 52,180 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `游貴森 醫師` / `Dr. Michael K. Yu` · Birth Year `-` · Birth Place `-/-/-`
- **U.S. arrival:** `-/-/-` (first year / first city / first state) — unfilled on the form
- **Address:** `Greenville/OH` — the footer block restates it as `Residence: Greenville, OH`
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — form rows present but unfilled; JSON parses `family: []`, `family_filled: false`. The subject self-reports a wife, a daughter, and a son exist, without names.
- **Education:** `1. Dartmouth College, Hanover, New Hampshire` `1991` `B.S.` · `2. New York University School` `1995` `M.D. Medicine` (the site footer block restates row 2 as `New York University School of Medicine / M.D. (1995)`)
- **Employment:** `-` `present` `urologist` (one row; start year unfilled)
- **Accomplishment:** `--` — unfilled.
- **Publication (Non-professional ones):** `--` — unfilled.
- **Hobby:** `--` — unfilled.
- **Website or Blog:** `--` — unfilled.
- **Provenance line (print submission source):** `Source from 北美洲台灣人醫師協會2016/10` — the record was submitted from the NATMA (北美人醫師協會/North American Taiwanese Medical Association) roster, 2016/10. One editable upstream print roster restated into an editable web form: held at `alleged`, not `documented`.
- **Footer block (restates the form, site-generated):** `Dr. Michael K. Yu` · Hanzi `游貴森醫師` · Residence `Greenville, OH` · Education `Dartmouth College B.S. (1991)` / `New York University School of Medicine M.D. (1995)` · Position `Urologist`. Restatement within one editable record is not corroboration; the footer's `School of Medicine` completion is site template normalization, not the subject's words.
- **Site motto line:** `Last updated: June 19, 2026` appears above the name in the rendered page — matches the JSON `modified` stamp.

## Capture 2 — form-field dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1329.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1329/](https://taiwaneseamericanhistory.org/whoswho1329/)
- **Title:** `1329. Michael K. Yu 游貴森 / 2016/10` · vault work record: [[works/taiwaneseamericanhistory-org/whoswho1329|TAH #1329]]
- The dump reproduces the Capture 1 form fields verbatim (Name, Birth Year `–`, Birth Place, arrival, Address, Family, Education, Employment, Accomplishment `–`, Publication `–`, Hobby, Website `–`, `Source from 北美洲台灣人醫師協會2016/10`). It is a second rendering of the same self-reported payload, not an independent source.
- **Twin check** (run 2026-11-14, in-process, frontmatter stripped + `#`/whitespace normalized): profile `page_text` = 1,264 normalized chars, md5 `a0f5ded8bde8934092a689afb368ac9d`; dump body = 396 normalized chars, md5 `05946bf08a8146e2a736e67fbda8037a`. Containment test run both ways: the dump body is **not** a substring of the profile text (the profile carries site chrome + the footer block; the dump keeps only form fields), and neither md5 matches — as expected for two serializations of **one** editable self-report. They do not corroborate each other; agreement across two renderings of one editable record keeps the record's own `Source from 北美洲台灣人醫師協會 2016/10` print citation at `alleged`.

## Number-collision ruling (do not treat as a second source)
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/publications1329.md` shares the number 1329 but is **`1329. 美西台灣人夏令會1987手冊 / 美西台灣人夏令會 / 07/1987`** — a Publications post (1987 USWest Taiwanese Summer Institute handbook, submitted by Mr. Frank Chou/CA, 01/2020) with zero biographical content about this subject. Read the H1 before counting same-number artifacts; recorded here so future passes do not re-open it.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`.
- This slug does **not** appear in that manifest's `weak.person` list, i.e. the harvest grader did not mark this profile's payload thin at fetch time (it is thin: Birth Year/Place, arrival, family names, and all four free-text fields are unfilled).

## What this capture does NOT establish
- Birth year or birthplace (form `-`).
- Year of first arrival in the U.S. (form `-`).
- Names of the wife, daughter, or son (rows present, values `-`, `family_filled: false`).
- The start date of the urologist post (row is `-` `present`).
- Any 北美洲台灣人醫師協會 (NATMA) membership detail beyond the submission-provenance footer: the NATMA yearbook work pages on this box (e.g. the 2005 南加州分會 yearbook) do not name him and no NATMA roster text is archived here.
- Whether `surgeon` in the taxonomy is a board-certified role or a self-tag alongside `urologist` — the only evidence is the site class list.

## Related
- [[people/michael-k-yu|Michael K. Yu 游貴森醫師]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whoswho1329|1329. Michael K. Yu 游貴森 / 2016/10]] — vault work record of the profile
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
