---
title: "TAH Who's Who profile capture — 1922. Prof. Oliver Chyan 錢明仁教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1922. Prof. Oliver Chyan 錢明仁教授

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): ~520
- wikilinks: 5

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable.

## Subject
- [[people/prof-oliver-chyan|Prof. Oliver Chyan 錢明仁教授]] — TAH Who's Who record #1922

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-oliver-chyan.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-oliver-chyan/](https://taiwaneseamericanhistory.org/person/prof-oliver-chyan/)
- **Record id:** 74424 · **type:** `tah_person` · **profession taxonomy (5 terms):** `chemist`, `educator`, `professor`, `researcher`, `scientist` (`person_profession-*` tokens in `class_list`; numeric term ids `person_profession: [2239, 2248, 2237, 1813, 2235]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). The crawl `sidecar` role list is thinner — only `scientist`, `professor`, `educator` — so **`chemist` and `researcher` exist only in the site class list** (role-dropping sidecar).
- **`modified` on source:** 2026-06-19T16:58:02; the rendered page banner reads `Who's Who Taiwanese American Profile · Last updated: June 19, 2026`; `page_bytes` 56,635
- **Verbatim fields (self-reported):** English Name `Prof. Oliver Chyan` · Hanji Name `錢明仁教授` · Birth Year `--` · Birth Place `Taiwan` · Address `TX`
- **U.S. arrival (self-reported):** `First year / First city / State in U.S. = -/-/-` — all three parts blank
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three blank; `family_filled: false`, `family: []`
- **Education:** 1. National Chung-Hsing Univ. — 1980 — B.S., Chemistry · 2. National Taiwan Univ. — 1982 — M.S., Analytical Chemistry · 3. Univ. of Texas at Arlington — 1984 — M.S., Analytical Chemistry · 4. Massachusetts Institute of Technology — 1989 — Ph.D., Chemistry
- **Employment:** 1. Univ. of Cincinnati, OH — 1990-1992 — Research Associate · 2. Univ. of North Texas — 1992-Present — Professor · 3. Institute of Atomic and Molecular Sciences, Taiwan Academia Sinica — 2003-2004 — Visiting Associate
- **Accomplishment (2 entries):** `1. Certificate of Honor Teach (Siemens Westinghouse Science & Technology Competition), 1994, 1997, 2000, 2001, 2004` · `2. Univ. of North Texas Developing Scholar Award, 1997-98` — item 2 is present in both captures but was **not** carried onto the person page before this card; absorbed there 2026-11-14.
- **Publication:** `--` · **Hobby:** `--` (blank — label-inflation proof that no crown fact is withheld on the form)
- **C.V. attachment (self-reported filename):** `C.V. :錢明仁-VITA-1` — the attachment itself is not archived on this box.
- **`content_html` is empty** — no free-text biography beyond the form fields; the form fields are the whole payload. The site-rendered footer block restates Hanzi/Birthplace/Residence/Education/Position — restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1922-oliver-chyan.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1922-oliver-chyan/](https://taiwaneseamericanhistory.org/whos-who-1922-oliver-chyan/)
- **Title:** `1922. Prof. Oliver Chyan 錢明仁教授` · **published:** 2017-10-25 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, record id 43858); the bibliographic counterpart work page is [[works/taiwaneseamericanhistory-org/whos-who-1922-oliver-chyan|TAH #1922]]
- Body carries the same form fields as Capture 1 (English/Hanji name, birth fields, U.S. arrival, family, education, employment, both Accomplishment entries, Publication, Hobby, and the `C.V. :錢明仁-VITA-1` line).

## Twin check (2026-11-14)
Normalized both artifacts (strip frontmatter and all `#`/whitespace): Capture 1 `page_text`
2,186 normalized chars, md5 `5e856aaad18e431200652f1906b806b9`; Capture 2 dump body
922 normalized chars, md5 `f40916c1eb5f192e15a593ea2625eb5d`. Neither is a substring of
the other (`post_in_json: False`, `json_in_post: False`); Capture 1 is the richer artifact,
carrying the 5-term profession class list, the `modified`/`Last updated: June 19, 2026`
stamp, `page_bytes`, and the footer summary block that Capture 2 omits. The shared field
content is **one editable self-report rendered twice** — agreement across two
serializations is NOT corroboration, which is why the record's own `Accomplishment`
claims stay `alleged`.

## Harvest provenance
- The person capture comes from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`); this slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this profile's payload thin at fetch time — consistent with the `--`-filled form fields above.

## What this capture does NOT establish
- No birth year (`--` in both artifacts); no spouse/children names (all three family fields blank, `family_filled: false`).
- No U.S. arrival year/city/state at all (`-/-/-` — unlike sibling profiles, nothing is filled).
- No publications or hobbies recorded (`--` in both artifacts); the named C.V. file `錢明仁-VITA-1` is not archived here.
- The `chemist` and `researcher` profession tags appear only in Capture 1's class list; no affiliation, grant, or organization is named for either tag beyond the Employment rows.
- The Siemens Westinghouse and UNT Developing Scholar awards are self-reported with no cited announcement — `alleged`, not `documented`.

## Related
- [[people/prof-oliver-chyan|Prof. Oliver Chyan 錢明仁教授]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-1922-oliver-chyan|1922. Prof. Oliver Chyan 錢明仁教授]] — vault work record of the encyclopedia entry (published 2017-10-25)
- [[organizations/tah-foundation|TAH Foundation]] — publisher
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
