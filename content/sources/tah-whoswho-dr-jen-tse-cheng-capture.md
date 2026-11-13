---
title: "TAH Who's Who profile capture — 2009. Dr. Jen-Tse Cheng 鄭仁澤醫師"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-12
---
# TAH Who's Who profile capture — 2009. Dr. Jen-Tse Cheng 鄭仁澤醫師

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1099
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/dr-jen-tse-cheng|Dr. Jen-Tse Cheng 鄭仁澤醫師]] — TAH Who's Who record #2009

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-jen-tse-cheng.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/dr-jen-tse-cheng/](https://taiwaneseamericanhistory.org/person/dr-jen-tse-cheng/)
- **Record id:** 74507 · **type:** `tah_person` · **profession taxonomy:** `physician` (`class_list` token `person_profession-physician`, numeric term id `person_profession: [2234]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form; here the single taxonomy token and the crawl `sidecar` `roles: ["physician"]` agree)
- **`modified` on source:** 2026-06-19T16:59:29 · `page_bytes`: 54,360 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** English Name `Dr. Jen-Tse Cheng` · Hanji Name `鄭仁澤醫師` · Birth Year `--` · Birth Place `Taiwan`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank)
- **Address:** `NY` — the single filled geography field besides birthplace; the footer block restates it as `Residence: NY`
- **Family:** `1. Wife: —` · `2. Daughter: —` · `3. Son: —` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (1 row, no year range):** `1. National Taiwan Univ. College of Medicine` — `1961` — `M.D.`
- **Employment (3 rows):** `1. Bronx-Lebanon Hospital Center` — `1978` — `Residency` · `2. Bronx Va Medical Center` — `1980` — `Residency` · `3. Bronx, NY` — `present` — `Nephrologist` (the third row's year field literally reads `present`)
- **Accomplishment:** `1. Fellowship, The Johns Hopkins Hospital, 1971` · `2. Fellowship, Duke Univ. Hospital, 1978` — the only two honor rows, both dated.
- **Publication / Hobby:** `--` — unfilled.
- **Upstream provenance line (this record carries one, unlike many siblings):** `Source from北美台大醫學院校友會 http://ntumcaa-na.org/Web_pages/programs%20at%20annual%20meeting_2009.htm` — the profile states that the biographical data was supplied by the North American Taiwan University Medical College Alumni Association (北美台大醫學院校友會) 2009 annual-meeting program. The upstream page itself is **not archived on this box** (the `ntumcaa-na.org` corpus has no local capture), so the alumni-association program is an unarchived upstream, not a second source here. Sibling TAH records cite the same feeder for other years (2006, 2007, 2010, 2011, 2015 entries carry analogous `Source from北美台大醫學院校友會…programs at annual meeting_<year>.htm` lines), which shows the association was a standing biographical-data feeder to the TAH Who's Who, not a one-off mention of this subject.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Footer summary block (same page, rendered below the form):** Hanzi `鄭仁澤醫師` · Birthplace `Taiwan` · Residence `NY` · Education `National Taiwan University College of Medicine, M.D. (1961)` / `The Johns Hopkins Hospital, Fellowship (1971)` / `Duke University Hospital, Fellowship (1978)` · Position `Bronx-Lebanon Hospital Center, Residency (1978-)` / `Bronx VA Medical Center, Residency (1980-)` / `Bronx, NY, Nephrologist`. The footer restates the form rows with the residency years normalized to open-ended ranges (`1978-`, `1980-`) — restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2009-jen-tse-cheng.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2009-jen-tse-cheng/](https://taiwaneseamericanhistory.org/whos-who-2009-jen-tse-cheng/)
- **Title:** `2009. Dr. Jen-Tse Cheng 鄭仁澤醫師` · **published:** 2018-02-06 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 46070) · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2009-jen-tse-cheng|TAH #2009]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim, including the `Source from北美台大醫學院校友會…` provenance line. It is a second rendering of the same self-reported payload, not an independent source.

## Twin & cross-check (2026-11-12)
The two artifacts are **not byte-identical**: the post dump is the bare encyclopedia rendering (frontmatter + form fields, md5 `c708f01cd6d4cd39bb430a7bddb576f9`), while the JSON's `page_text` is the trafilatura extraction of the full site page including navigation chrome and the footer summary block (whitespace-normalized md5 `fa4b86c56e55dc54ab73dbeb09fef820`). They are two renderings of one self-report; the footer block in Capture 1 is the only material the post dump lacks.

Whole-vault sweep this pass (`grep -rlE '鄭仁澤|Jen-?Tse Cheng|仁澤'` over `content/` + `knowledge/`, controls non-vacuous: `教授` = 3,088 files, `台大醫學院` = 56 files, `Johns Hopkins` = 218 files): hits are only his own two TAH captures, the [[works/taiwaneseamericanhistory-org/whos-who-2009-jen-tse-cheng|TAH #2009 work page]], `people/index.md`, the `sources/taiwaneseamericanhistory-org.md` hub, crawler/analysis indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`), and the `taiwanjustice-net-priority-lexicon.json` name list — all machine indexes carrying only his name forms from the harvest, no biographical content. No other person page names him.
Institution sweeps: `Bronx-Lebanon` matches 6 files and `Bronx VA` 3 — every one of them either this subject's own captures or a different subject's page (e.g. the TAHS `faces-of-taiwan-series-opens-in-the-bronx` work record, a 紐約醫院 pandemic article, a jazz review — none name 鄭仁澤). `腎臟科` matches 2 files, `nephrolog` 5, none naming this subject outside his own record. No taiwandaily/TJJ article, memoir (《Our Journeys》/My Stories), or org record names him.
`ntumcaa` (the alumni association) matches 20 files — sibling TAH Who's Who profiles citing other annual-meeting program years — **none of which name this subject**; the association is the data feeder for his record, not an independent community mention of him.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`-filled form fields above.

## What this capture does NOT establish
- No birth year (Birth Year `--`); birthplace `Taiwan` is self-reported and unverified.
- No year, city, or state of U.S. arrival (`-/-/-`).
- No wife/children names (fields present, blank), no family record.
- No publications (the nephrology literature a Hopkins/Duke-trained nephrologist would have is **not archived on this box**), no hobbies.
- The M.D. (1961), residencies (1978, 1980) and fellowships (1971, 1978) are self-reported dates with no institutional corroboration on this box. Note the 1971 fellowship preceding the 1978 residency row — the record's own ordering of training vs. residency years is unexplained and unverified.
- Whether `Bronx, NY — Nephrologist` is still current is only what the form's `present` marker says at data-entry time; the upstream NTUMCAA 2009 program page (not archived here) is the dated anchor for that claim.
- The Chinese name `鄭仁澤` is self-reported and unverified against any second source.
