---
title: "TAH Who's Who profile capture — 2010. Dr. Min-Yen Han 韓明元醫師"
type: source
tier: M
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-18
---
# TAH Who's Who profile capture — 2010. Dr. Min-Yen Han 韓明元醫師

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 1003
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/dr-min-yen-han|Dr. Min-Yen Han 韓明元醫師]] — TAH Who's Who record #2010

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-min-yen-han.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/dr-min-yen-han/](https://taiwaneseamericanhistory.org/person/dr-min-yen-han/)
- **Record id:** 74508 · **type:** `tah_person` · **profession taxonomy:** `physician` (`class_list` token `person_profession-physician`, numeric term id `person_profession: [2234]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form; the single taxonomy token and the crawl `sidecar` `roles: ["physician"]` agree)
- **`modified` on source:** 2026-06-19T16:59:30 · `page_bytes`: 53,104 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit in the raw HTML, not the extracted text)
- **Verbatim fields (self-reported):** English Name `Dr. Min-Yen Han` · Hanji Name `韓明元醫師` · Birth Year `--` · Birth Place `Taiwan`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank)
- **Address:** `NJ` — the single filled geography field besides birthplace; the footer block restates it as `Residence: NJ`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (1 row):** `1. National Taiwan Univ. College of Medicine` — `1969` — `M.D.`
- **Employment (2 rows, both year fields blank `-`):** `1. French Polyclinic Hospital` — `Residency` · `2. Vernon, NJ` — `Internist`
- **Accomplishment (1 row):** `1. Member of Tzu Chi International Medical Association, TIMA (國際慈濟人醫會成員)` — the single honor/community row; the footer Community block restates it as `Tzu Chi International Medical Association (TIMA) 國際慈濟人醫會 — Member`.
- **Publication / Hobby:** `--` — unfilled.
- **Upstream provenance line (this record carries one, unlike many siblings):** `Source from北美台大醫學院校友會 http://ntumcaa-na.org/Web_pages/programs%20at%20annual%20meeting_2009.htm` — the profile states that the biographical data was supplied by the North American Taiwan University Medical College Alumni Association (北美台大醫學院校友會) 2009 annual-meeting program. The upstream page itself is **not archived on this box** (the `ntumcaa-na.org` corpus has no local capture), so the alumni-association program is an unarchived upstream, not a second source here. Sibling TAH records cite the same feeder for other years (the 2009 / 2011 entries and a photo-album work record carry analogous `Source from北美台大醫學院校友會…programs at annual meeting_<year>.htm` lines), which shows the association was a standing biographical-data feeder to the TAH Who's Who, not a one-off mention of this subject.
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Footer summary block (same page, rendered below the form):** Hanzi `韓明元醫師` · Birthplace `Taiwan` · Residence `NJ` · Education `National Taiwan University College of Medicine, M.D. (1969)` · Position `French Polyclinic Hospital, Residency` / `Vernon, NJ, Internist` · Community `Tzu Chi International Medical Association (TIMA) 國際慈濟人醫會, Member`. The footer restates the form rows — restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2010-min-yen-han.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2010-min-yen-han/](https://taiwaneseamericanhistory.org/whos-who-2010-min-yen-han/)
- **Title:** `2010. Dr. Min-Yen Han 韓明元醫師` · **published:** 2018-02-06 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 46073) · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2010-min-yen-han|TAH #2010]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim, including the `Source from北美台大醫學院校友會…` provenance line. It is a second rendering of the same self-reported payload, not an independent source.

## Twin & cross-check (2026-11-12)
The two artifacts are **not byte-identical**: the post dump is the bare encyclopedia rendering (frontmatter + form fields, md5 `2060a3a06175dc53c0a51af9719a5f5b` raw / `d9f1294ed8e4c57bada844711c4be645` whitespace-stripped, 714 chars), while the JSON's `page_text` is the trafilatura extraction of the full site page including navigation chrome and the footer summary block (whitespace-normalized md5 `6f205731c80fb4e825e8bdd7fa86f240`, 1,577 chars). They are two renderings of one self-report; the footer block in Capture 1 is the only material the post dump lacks.

Whole-repo sweep this pass (`grep -rlE '韓明元|Min-?Yen ?Han|min-yen-han'` over `content/` + `knowledge/`, controls non-vacuous: `鄭仁澤` = 24 files, `北美台大醫學院校友會` = 25 files, `TIMA` = 9 files, `慈濟` = 483 files): hits are only his own two TAH captures, the [[works/taiwaneseamericanhistory-org/whos-who-2010-min-yen-han|TAH #2010 work page]], the `sources/taiwaneseamericanhistory-org.md` hub, crawler/analysis indexes (`units.jsonl`, `posts/index.jsonl`, `taiwaneseamericanhistory-org-family.json`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, `scout/*.jsonl`, `taiwanjustice-net-priority-lexicon.json` name list, `tahots-merge.jsonl`, `work-linker-state.jsonl`, deepen-x slice logs, floor findings), and one **negative** record in `knowledge/web-archives/tdm-202503-absorb-ledger.jsonl` — the 2026-11-05 taiwandaily 202503-s18 absorb explicitly ruled out a prep-tag hit here: 「candidate dr-min-yen-han 韓明元醫師 never named — prep-tag hit false」 (article 67286, a 慈濟 statement; 韓明元 never appears in it). No other person page, no taiwandaily/TJJ article, no memoir (《Our Journeys》/My Stories), and no org record names him. Institution sweeps: `French Polyclinic` matches his own capture files only; `Vernon` + `NJ` co-match only his own page in `content/`. The 9 `TIMA` hits in `content/` none name him.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`-filled form fields above.

## What this capture does NOT establish
- No birth year (Birth Year `--`); birthplace `Taiwan` is self-reported and unverified.
- No year, city, or state of U.S. arrival (`-/-/-`); `NJ` is the only residence datum, undated.
- No residency or practice years (both Employment year fields are `-`), so no ordering between the French Polyclinic residency and the Vernon practice is established.
- No wife/children names (fields present, blank), no family record.
- No publications (the internal-medicine literature an NTU-trained internist would have is **not archived on this box**), no hobbies.
- TIMA membership is undated on both captures — no year of joining is recorded anywhere on this box.
  *(Frontier pass 2026-11-18, t_df9fd7f1: third-party web records now date the TIMA
  membership — 慈濟 Indonesia names him 「anggota TIMA」 (2025) and the Tzu Chi USA Journal
  2024 portrait gives 2005 as the joining year; see
  [[sources/dr-min-yen-han-thirdparty-2026-11-18]]. The no-local-source verdict above holds
  for the box corpus only.)*
