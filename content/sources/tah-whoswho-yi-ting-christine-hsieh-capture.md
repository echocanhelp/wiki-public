---
title: "TAH Who's Who profile capture — 2141. Yi-Ting (Christine) Hsieh"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2141. Yi-Ting (Christine) Hsieh

Primary capture of the subject's own self-reported [[organizations/tah-foundation|TAH Foundation]] Who's Who record
(record #2141), archived on this box as two serializations of one editable form — the crawled profile JSON and the
encyclopedia entry dump — plus the 2018 musician-series story record. Preserved because the biographical fields are
self-reported and the live site is editable.

## Subject
- [[people/yi-ting-christine-hsieh|Yi-Ting Christine Hsieh]] — TAH Who's Who record #2141
- Duplicate page note: [[people/yi-ting-hsieh|Yi-Ting Hsieh]] documents the same person from the same TAH records
  (crawl id 74630, one record below this one); merge is held for a maintainer (see GAPS on the person page).

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/yi-ting-christine-hsieh.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/yi-ting-christine-hsieh/](https://taiwaneseamericanhistory.org/person/yi-ting-christine-hsieh/) · site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]]
- **Record id:** 74631 · **type:** `tah_person` · **profession taxonomy:** `clarinetist`, `educator`, `musician`, `pianist` (`person_profession-*` in `class_list`; numeric term ids `person_profession: [2281, 2248, 2250, 2251]` — no taxonomy name→id map is archived on this box, so the class-list slugs are the readable form). The crawled `sidecar.roles` kept only `artist`, `educator` — `clarinetist` / `musician` / `pianist` survive only in `class_list`/`page_text`, which is why the taxonomy line here is richer than the page's Identity Snapshot. Note the sibling record id 74630 (the duplicate person page) carries one extra class-list tag, `person_profession-performer`, absent here.
- **`modified` on source:** 2026-06-02T17:24:41 · `page_bytes`: 53,728 (raw HTML; the `Last updated: June 2, 2026` line sits in the rendered page text)
- **Verbatim fields (self-reported):** Name `Yi-Ting (Christine) Hsieh` · Hanji Name `--` · Birth Year `--` · Birth Place `Taiwan`
- **U.S. arrival:** `-/-/-` (first year, first city and state all blank) · **Address:** `MA`
- **Family:** `1. Husband: --` · `2. Daughter: --` · `3. Son: --` — JSON parses this as `family: []`, `family_filled: false`. No family names are recorded.
- **Education (2 rows):** `1. National Taichung Univ.` — `2014` — `B.S., Clarinet and Piano Performance` · `2. Peabody Institute of the Johns Hopkins Univ. in Baltimore` — `2016` — `M.S., Music`
- **Employment (1 row):** company `-` · `2012-` · `Piano and Clarinet teacher`
- **Accomplishment:** `1st Place in the Taiwanese National Student Competition of Music and 3rd Place in the Young Artist Music Competition of Taiwan 2010-2014`
- **Publication / Hobby:** `--` — unfilled (absence evidence: the self-reported form withholds no other crown field content).
- **`content_html` is empty**, i.e. the profile carries no free-text biography beyond the form fields — the form fields above are the whole payload.
- **Provenance:** no `Source from …` submission line is present on this record (unlike sibling capture pages such as `sources/tah-whoswho-jolan-hsieh-capture`).

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2141-yi-ting-hsieh.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2141-yi-ting-hsieh/](https://taiwaneseamericanhistory.org/whos-who-2141-yi-ting-hsieh/)
- **Vault work record:** [[works/taiwaneseamericanhistory-org/whos-who-2141-yi-ting-hsieh|TAH #2141]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (English Name, blank Hanji/Birth Year, Birth Place `Taiwan`,
  Address `MA`, blank family rows, the two Education rows, the one Employment row, the Accomplishment string, blank
  Publication/Hobby). It is a second rendering of the same self-reported payload, not an independent source.

## Capture 3 — 2018 musician-series story (the richer free-text side)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/musician430.md`
- **Original:** [https://taiwaneseamericanhistory.org/musician430/](https://taiwaneseamericanhistory.org/musician430/) · published 2018-06-30
- **Vault work record:** [[works/taiwaneseamericanhistory-org/musician430|TAH musician #430]], `value_band: B`
- Carries the free-text biography the profile JSON omits (`content_html` empty): performance range (solo, orchestral,
  chamber, in Taiwan and the United States), collaborative-pianist role, the exact degree names (Bachelor of Music in
  Clarinet and Piano Performance from **National Taichung University of Education**; Master of Music from **Peabody
  Institute of the Johns Hopkins University in Baltimore**), the greater-Boston professional-chamber/orchestra
  activity, and the private piano/clarinet studio.
- **Upstream attribution:** `Source from http://musical1204.wixsite.com/yitinghsieh/biography` — the story itself is
  attributed to the subject's own (now-defunct) Wix biography site, so it is self-reported material restated by TAH,
  not third-party corroboration; the wixsite URL is not archived on this box.

## Twin & cross-check (2026-11-14)
Containment/md5 tests on the serializations of the one self-report (frontmatter stripped, `#`/whitespace normalized):
- Profile content block (sliced from the `Who's Who Taiwanese American Profile` marker to the footer line) = 1,278
  normalized chars (md5 `9d534a480fde5aa5379cec8ee8fbd3a9`) vs encyclopedia dump
  `posts/whos-who-2141-yi-ting-hsieh.md` = 570 normalized chars (md5 `14873a4d7cdbfc4ac6102d12ab383166`).
  **md5-different and neither is a substring of the other** — because the two serializations render blank fields
  differently (`--` in the profile render vs `—` em-dash in the dump) the strict containment test fails even though a
  per-field presence diff shows the dump's fields are a strict subset of the profile's (all 22 probe fields — Hanji,
  BirthYear, BirthPlace, Firstyear, Address, Husband/Daughter/Son, both Education rows, the Employment row, the
  Accomplishment string, Publication, Hobby — present in both). So the dump is a leaner render of the same editable
  form, not an independent record; the profile JSON is the richer artifact (it adds the `Last updated: June 2, 2026`
  line, the four-tag profession taxonomy, and the rendered `Notable Accomplishments` restatement block).
- Story `musician430` body (969 normalized chars, md5 `98bf5eafb6cfa3cc9cae2df1b4853259`) is not a substring of the
  form renders either: it carries free-text facts absent from the form (Boston-area ensemble activity,
  collaborative-pianist role, exact degree names). Agreement across the two form serializations of one editable
  self-report is NOT corroboration — that is what keeps the record's fields at `alleged`-grade provenance; #430 is a
  later restatement of the same self-report chain (TAH story ← subject's own wixsite bio).

## Ruled-out hits (read, different persons or non-sources)
- `content/works/taiwaneseamerican-org/from-ilha-formosa-…` — Yi-Ting **Chang**, Chiayi Univ. tourism researcher.
- `content/works/taiwaneseamerican-org/taiwanese-american-jing-mei-memorial-park.md` — Yi-Ting **Chung**, historian.
- `content/works/taiwaneseamericanhistory-org/ourjourneys305.md` — TPC rosters name `Ya-Hueh Tina Chang Hsieh` and
  `Christine Shen Shieh`, different people.
- `content/works/taiwaneseamericanhistory-org/christines-creative-performing-arts-studio.md` — "Christine's Creative
  Performing Arts Studio"; no surname, no date, no field on the subject's record links to it — unresolved name
  overlap, not treated as her studio (MA address vs. no geography on that page). Candidate only, see GAPS.
- Jen Chan clarinet record in the musician series — different musician.
- Machine indexes carrying only name forms from the harvest, no biographical content:
  `knowledge/research/tdm-page-title-index.json`, `knowledge/research/taiwanjustice-net-priority-lexicon.json`,
  `knowledge/research/taiwaneseamericanhistory-org-family.json`,
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`.

## Harvest provenance
Profile and posts captures are from the taiwaneseamericanhistory.org harvest recorded in
`knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`method: wp-json`).

## Related Pages
- Subject: [[people/yi-ting-christine-hsieh|Yi-Ting Christine Hsieh]] · duplicate: [[people/yi-ting-hsieh|Yi-Ting Hsieh]]
- Work records: [[works/taiwaneseamericanhistory-org/whos-who-2141-yi-ting-hsieh|TAH #2141]] · [[works/taiwaneseamericanhistory-org/musician430|TAH musician #430]]
- Site hub: [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org (TAH Foundation)]] · publisher [[organizations/tah-foundation|TAH Foundation]]
