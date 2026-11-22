---
title: "TAH organization directory capture — Taiwanese Association of West Michigan"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Taiwanese Association of West Michigan

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 635
- wikilinks: 2


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/taiwanese-association-of-west-michigan|Taiwanese Association of West Michigan (西密西根台灣同鄉會)]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-association-of-west-michigan.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-association-of-west-michigan/](https://taiwaneseamericanhistory.org/organization/taiwanese-association-of-west-michigan/)
- **Record id:** 78016 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-12T18:41:30 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45, MANIFEST `fetched_at` 2026-08-17, method `wp-json`)
- **`class_list` taxonomy:** `organization_type-civic-advocacy`, `organization_type-social` (plus WP boilerplate `post-78016`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `None` (null — no summary blurb recorded)
- **Verbatim `content_html` body (self-reported, one paragraph):**
  1. "The Taiwanese Association of West Michigan (西密西根台灣同鄉會) is a regional chapter of the Taiwanese Association of America (TAA, 全美台灣同鄉會), the national umbrella organization serving Taiwanese American communities across the United States. The chapter serves the Taiwanese American community in the West Michigan area and is listed under the TAA's Mid-Western (美中西) regional grouping."

## Single-source status
- This JSON is the only first-party artifact for this org on the box. There is no `posts/<record>.md`
  encyclopedia-dump twin (unlike Who's Who person records), so no twin/containment check against a dump
  is possible; every field above is one editable self-report → label `alleged` on the org page.
- **Twin/containment check vs the local West Michigan / Grand Rapids records (measured 2026-11-14):**
  the tag-stripped, whitespace-collapsed `content_html` is 325 normalized chars, md5
  `b591b12c72f12e643cf2cb6123247e38`. Against each of `posts/ourjourneys74.md` (6,595 norm chars),
  `posts/ourjourneys123.md` (11,547), `posts/ourjourneys258.md` (2,034), and `posts/our-journeys-377.md`
  (1,648): the bio is neither a substring of any of them nor do they appear in it → the directory
  self-report and the Our Journeys records are independent texts, but only the Our Journeys records are
  third-party-ish narrative, and none of them names this chapter. The self-report stays one record
  (`alleged`).
- **Same-batch neighbor is NOT corroboration:** Michigan-area org siblings in the same crawl batch —
  `michigan-taiwanese-student-association.json`, `taiwanese-american-student-association-at-the-university-of-michigan.json`,
  `taiwan-student-association-at-the-university-of-michigan.json` — are Ann Arbor / UM records (East Lansing–Ann Arbor
  corridor, 300+ km from Grand Rapids) and none carries West Michigan content; they neither corroborate nor
  duplicate this record.

## Whole-corpus sweep (2026-11-14, card t_87a06276)
Checked `content/` + `knowledge/` per name/token form (machine indexes `ee-vault-index*`,
`content-analysis/*.jsonl`, `units.jsonl`, `taiwanjustice-net-priority-lexicon.json` excluded as indexes):
- `grep -rlF '西密西根'` → `content/`: this org page, `organizations/index.md`, `sources/taiwaneseamericanhistory-org.md`,
  `people/dr-hong-chien-lin.md` (NATMA founding at 西密西根大學 — the university, not this chapter),
  `people/wellington-welly-yang.md` (same NATMA record restated); `knowledge/`: the org JSON above,
  `posts/ourjourneys74.md` (NATMA founding), plus the excluded machine indexes. No chapter-level (officer/event) record.
- `grep -rliF 'Taiwanese Association of West Michigan'` → only the org page, the two index rows above,
  `people/dr-po-fang-philip-hsieh.md` (see below), the org JSON, and excluded indexes. No narrative hit.
- **Same-name false-positive check (dr-po-fang-philip-hsieh.md, line 40):** it lists "Employment record
  Western Michigan Univ.（1964–2000）… [[organizations/taiwanese-association-of-west-michigan]]" — a campus
  adjacency wikilink, not an affiliation record by this chapter or its members. Classified **not a hit**
  for chapter-level facts; the wikilink stands as venue-neighborhood, not corroboration.
- `grep` over `pages/*` directory pages (`social-organizations`, `miscellaneous-organizations`,
  `organizations-archive`, `activities-of-ta*`, `taiwanese-association`, `history-of-t-a-organization`,
  `t-a-archives-center`) for `West Michigan` / `西密西根` → zero hits; the chapter appears in the crawl only
  as the org JSON.
- Prior deepen-x SKIP stamps (2026-09-20 → 2026-10-03, seven passes, works+articles scope) are consistent
  with this sweep; the stamps' scope never covered `knowledge/web-archives/.../organization/`, which is
  where the only substantive record sat — harvested here for the first time.

## NEED YOU (what would close this)
- TAA (全美台灣同鄉會) Mid-Western regional roster or convention minutes naming 西密西根台灣同鄉會 officers or delegates.
- Any chapter-hosted event record (picnic, 年会, 會長 list) in the TAH story corpus, NATWA 通訊, or 華文 press.
- The live TAA website chapter page (not archived on this box).
