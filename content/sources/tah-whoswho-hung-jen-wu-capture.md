---
title: "TAH Who's Who profile capture — 1578. Hung-Jen Wu 吳泓仁"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 1578. Hung-Jen Wu 吳泓仁

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, church, or community
record elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/hung-jen-wu|Hung-Jen Wu 吳泓仁]] — TAH Who's Who record #1578

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/hung-jen-wu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/hung-jen-wu/](https://taiwaneseamericanhistory.org/person/hung-jen-wu/)
- **Record id:** 74105 · **type:** `tah_person` · **profession taxonomy:** `chemical engineer`, `educator`, `engineer`, `professor`, `researcher` (from `class_list` `person_profession-*` slugs; numeric term ids `person_profession: [270, 2248, 2227, 2237, 1813]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form)
- **`modified` on source:** 2026-06-19T16:52:11 · `page_bytes`: 54,838 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** Name `吳泓仁教授` / `Prof. Hung-Jen Wu` · Birth Year `-` · Birth Place `台灣`
- **U.S. arrival:** first year `-` (unfilled), first city/state `College Station/TX` · **Address:** `College Station/ TX` — the footer block restates it as `Residence: College Station, TX`
- **Family:** `1. Wife: -` · `2.Daughter: -` · `3.Son: -` — all three fields present and blank; JSON parses to `family: []`, `family_filled: false`. No relative is named anywhere on the record.
- **Education (3 rows):** `1.成功大學 1998 B.S. Chemical Engineering` · `2. 成功大學 2000 M.S. Chemical Engineering` · `3. Texas A&M University 2006 Ph.D. Chemical engineering` (capitalization of `engineering` is as printed on rows 1–2 vs 3; quoted as-is)
- **Employment (2 rows):** `1. Texas A&M University 2013-present Assistant Professor` · `2. Synamen Corp., 2009-2010 consultant`
- **Accomplishment:** `Outstanding Performance Presentation of 2013 Annual Symposium-the Society of Chinese Bioscientists in America.` — restated once on the same page under `Notable Accomplishments`; restatement within one capture is not corroboration.
- **Publication (non-professional) / Hobby / Website or Blog:** `-` — unfilled. The three unfilled fields are themselves the record: no publication, hobby, or web-presence fact is being withheld elsewhere on this capture.
- **Provenance line:** `Source from 北美洲台灣人教授協會2013 annual meeting` — the record's own attribution of its content upstream to the 2013 annual meeting of the 北美洲台灣人教授協會 (Formosan Association of Professors in North America). No such meeting record, roster, or program is archived on this box, and no org page for the association is linked from this capture.
- **Footer summary block (same page, rendered below the form):** Hanzi `吳泓仁` · Birthplace `台灣` · Residence `College Station, TX` · Education (the same 3 rows) · Position `Texas A&M University — Assistant Professor (2013-)` and `Synamen Corp. — Consultant (2009-2010)`, plus a `Notable Accomplishments` restatement of the 2013 symposium row and a `Prof. Hung-Jen Wu` salutation.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/1578-hung-jen-wu-%e5%90%b3%e6%b3%93%e4%bb%81-201703.md`
- **Original:** [https://taiwaneseamericanhistory.org/1578-hung-jen-wu-%e5%90%b3%e6%b3%93%e4%bb%81-201703/](https://taiwaneseamericanhistory.org/1578-hung-jen-wu-%e5%90%b3%e6%b3%93%e4%bb%81-201703/)
- **Title:** `1578. Hung-Jen Wu 吳泓仁/ 2017/03` · **published:** 2017-03-23 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 39000) · vault work record: [[works/taiwaneseamericanhistory-org/1578-hung-jen-wu-e5-90-b3-e6-b3-93-e4-bb-81-201703|TAH #1578]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Name, blank Birth Year, Birth Place, Address, blank Family rows, Education, Employment, Accomplishment, blank Publication/Hobby/Website, the `Source from 北美洲台灣人教授協會2013 annual meeting` line). It is a second rendering of the same self-reported payload, not an independent source.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, 2,212 person / 339 org expected = counted).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `-`-filled Birth Year, Family, Publication, Hobby, and Website fields above.

## Twin & cross-check (2026-11-12)
Whole-corpus sweep this pass — single-pattern `grep -rlF` per name form, controls counted:
`吳泓仁` → 5 files in `content/`, 18 in `knowledge/`; `Hung-Jen Wu` → 5 / 18; `泓仁` → 5 / 18;
`Hungjen Wu` / `Hungjen` → 0 (romanization control — confirms no alternative-romanization record exists).
Every non-index hit is one of: his own two TAH captures, the [[works/taiwaneseamericanhistory-org/1578-hung-jen-wu-e5-90-b3-e6-b3-93-e4-bb-81-201703|TAH #1578]] work page,
`people/index.md`, the [[sources/taiwaneseamericanhistory-org|source hub]], the name-collision anchor on
[[people/hung-jen-liu|Rev. Hung-Jen Liu 劉弘仁]] (a different person — the page disambiguates him against
this subject and links this page as the disambiguation anchor), or crawler/analysis indexes
(`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5.json`, `tdm-page-title-index.json`,
`taiwaneseamericanhistory-org-family.json`, `taiwanjustice-net-priority-lexicon.json`,
`content-analysis/*.jsonl`) and deepen-x slice/incident logs, which are machine state, not sources.
**No memoir (《Our Journeys》 / My Stories), taiwandaily/TJJ article, church, org, or event record
names him.** The 2017-03-23 post date is the earliest dated record for him in the corpus.

**Twin check (the two artifacts are NOT byte-identical):** normalized body md5 after
stripping frontmatter and all whitespace — Capture 1 `page_text` =
`302beb17cda7b4943f59d87ba0f64eaa` (1,738 chars), Capture 2 dump =
`c397d92ecfe9bc920a8c61a083cf5d2b` (756 chars). They are not duplicates: Capture 1 is a
superset carrying the site chrome, the `Last updated: June 19, 2026` line, the profession
taxonomy class list, the `Prof.` honorific rendering, and the footer summary block. The form
fields they share are one payload, so shared fields are **not** corroboration of each other;
no third record with independent wording exists on this box.

## What this capture does NOT establish
- No birth year and no birth date of any kind (Birth Year `-`); birth place is `台灣` only.
- No year of U.S. arrival (`-`); only the first city/state `College Station/TX` is filled.
- No spouse or children names (Wife/Daughter/Son fields present, blank).
- Whether the `Texas A&M University — Assistant Professor (2013-present)` affiliation is
  still current is not independently verifiable — `present` is the subject's own form entry
  and `modified` 2026-06-19 is an edit timestamp, not a career date.
- No independent verification of the **Outstanding Performance Presentation of 2013 Annual
  Symposium — the Society of Chinese Bioscientists in America** award — no SCBA program,
  roster, or press record is archived on this box.
- The `Source from 北美洲台灣人教授協會2013 annual meeting` provenance line is untraceable on
  this box — the 2013 FAPNA annual-meeting record is not in the corpus, and neither the
  awarding body (SCBA) nor the association appears in any other record naming him.
- `Publication (non-professional)`, `Hobby`, and `Website or Blog` are blank, which proves
  only that this editable record withholds nothing in those fields — professional
  publications (his actual academic output) are outside the Who's Who schema and are not
  captured here at all.

## Related
- [[people/hung-jen-wu|Hung-Jen Wu 吳泓仁]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/1578-hung-jen-wu-e5-90-b3-e6-b3-93-e4-bb-81-201703|1578. Hung-Jen Wu 吳泓仁 / 2017-03]] — vault work record
- [[people/hung-jen-liu|Rev. Hung-Jen Liu 劉弘仁]] — name-collision disambiguation (different person)
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
