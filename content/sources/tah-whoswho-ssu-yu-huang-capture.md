---
title: "TAH Who's Who profile capture — 2177. Ssu-Yu Huang 黃思瑜"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2177. Ssu-Yu Huang 黃思瑜

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 620
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/ssu-yu-huang|Ssu-Yu Huang 黃思瑜]] — TAH Who's Who record #2177

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/ssu-yu-huang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/ssu-yu-huang/](https://taiwaneseamericanhistory.org/person/ssu-yu-huang/)
- **Record id:** 74668 · **type:** `tah_person`
- **Profession taxonomy (`person_profession` [2264, 2250, 2265, 2251] → `class_list`):**
  `composer` · `musician` · `organist` · `pianist` — the composer/organist/pianist tags are
  absent from the person-page sidecar, which renders `"roles": []`.
- **`modified` on source:** 2026-06-19T17:02:22 · page size 54,490 bytes
- **Site-rendered "Last updated: June 19, 2026"** appears in `page_text` above the profile header.
- **Verbatim fields (self-reported):** English Name Ssu-Yu Huang / Hanji Name 黃思瑜 · Birth Year 1970 ·
  Birth Place Kaohsiung, Taiwan · First year / First city / State in U.S. `2007/-/RI` · Address `RI`
- **Family:** `1. Husband: --` · `2. Daughter: --` · `3. Son: --` — all three blank; `family_filled: false`
- **Education:** 1. Tainan Univ. of Technology — `-` — Major in Electronic Organ and Piano ·
  2. Chinese Culture Univ. — 1993–1996 — B.S., Theoretical Composition ·
  3. Univ. of Rhode Island — 2007 — Major in Theoretical Composition
- **Employment:** 1. `-` — `-` — Musician (company name and year range blank)
- **Accomplishment:** 1. The Call for Score of National Symphony Orchestra in Taiwan.(Winner) 2010 ·
  2. IBLA Grand Prize (Most Distinguished Composer Award) 2013 ·
  3. 2015 and 2016 American Prize (semi-finalist) ·
  4. Maurice Ravel International Composition Competition (semi-finalist) 2016
- **Notable Accomplishments:** the same four strings restated verbatim in a second field
- **Publication:** `--` · **Hobby:** `--` (blank-field roster: no crown fact withheld)
- **`content_html` / `excerpt`:** both empty in the JSON — the site-rendered `page_text` is the richer
  serialization and is what carries the full field set.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2177-ssu-yu-huang.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2177-ssu-yu-huang/](https://taiwaneseamericanhistory.org/whos-who-2177-ssu-yu-huang/)
- **Title:** `2177. Ssu-Yu Huang 黃思瑜`
- Field set identical to Capture 1 (Birth Year 1970, Kaohsiung, `2007/-/RI`, three blank family
  fields, same three education rows, same four accomplishments, `Publication —`, `Hobby —`),
  without the site chrome, the profession taxonomy, or the 2026-06-19 `modified` stamp.

## Twin check (2026-11-14)
Containment test, not md5: the Capture-2 body is a normalization-equivalent subset of Capture 1's
`page_text` — every verbatim field string in the dump occurs in the crawled profile text, and
Capture 1 strictly adds the navigation chrome, the profession taxonomy, the `Last updated:
June 19, 2026` line, and the restated Notable Accomplishments block. The two artifacts are therefore
**two serializations of one editable self-report, not corroboration** — which is why the achievement
rows are held at `alleged` on the person page.

## What this capture does NOT establish
- No U.S. city, employer name, ensemble, or work titles — the Employment company/year fields and the
  entire Publication field are blank in both artifacts.
- No spouse/children names (all three family fields blank, `family_filled: false`).
- The four prize rows are known only from the subject's own editable submission — no third-party
  announcement of the 2010 NSO call-for-score win, the 2013 IBLA Grand Prize, the 2015/2016 American
  Prize semi-finalist placements, or the 2016 Maurice Ravel semi-finalist placement was found in
  `content/` or `knowledge/`.
- Whole-corpus grep 2026-11-14 `grep -rlF '黃思瑜'` and `grep -rliF 'Ssu-Yu Huang'` over `content/` +
  `knowledge/` (machine indexes `units.jsonl`, `posts/index.jsonl`, `ee-vault-index.*`,
  `content-analysis/*.jsonl` excluded) returned only: this person page, the #2177 work page, the
  `sources/taiwaneseamericanhistory-org` hub, the two crawl artifacts above, and three research
  machine indexes (`tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`,
  `taiwaneseamericanhistory-org-family.json`). No memoir, article, or third-party mention.
