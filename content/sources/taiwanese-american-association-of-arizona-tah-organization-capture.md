---
title: "TAH directory capture — Taiwanese American Association of Arizona (TAAA)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH directory capture — Taiwanese American Association of Arizona (TAAA)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 734
- wikilinks: 2


Primary capture of the chapter's own records in the TAH Foundation organization directory and
story corpus, archived on this box. Preserved in full because both are editable first-party
self-reports.

## Subject
- [[organizations/taiwanese-american-association-of-arizona|Taiwanese American Association of Arizona (TAAA)]] — TAH organization directory record + story-corpus chapter post

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-american-association-of-arizona.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/taiwanese-american-association-of-arizona/](https://taiwaneseamericanhistory.org/organization/taiwanese-american-association-of-arizona/)
- **Record id:** 78039 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-12T18:41:36 (crawl-side capture of this file: on-disk mtime 2026-08-17)
- **`class_list` taxonomy:** `organization_type-civic-advocacy`, `organization_type-social` (plus WP boilerplate `post-78039`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — no profession/officer taxonomy for the chapter)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, single paragraph):** "The Taiwanese American
  Association of Arizona (TAAA) is a regional chapter of the Taiwanese Association of America
  (全美台灣同鄉會), serving the Taiwanese American community across the state of Arizona. As a TAA
  chapter, it operates within the national umbrella organization's network of hometown associations
  dedicated to community connection, cultural preservation, and civic engagement among Taiwanese
  Americans in the United States."

## Capture 2 — story-corpus chapter post (the never-opened rich twin)
- **Archive copy:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/arizona-chapter-taa.md`
  (on-disk mtime 2026-08-21; `fetched: auto`)
- **Original:** [https://taiwaneseamericanhistory.org/arizona-chapter-taa/](https://taiwaneseamericanhistory.org/arizona-chapter-taa/)
- **Index entry:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl` → `id: 27794`,
  `slug: arizona-chapter-taa`, `date: 2015-12-30`
- **Work page:** [[works/taiwaneseamericanhistory-org/arizona-chapter-taa|Taiwanese American Association of Arizona 亞利桑那州台灣同鄉會]]
  (value band B; its `## Subjects` already links this org)
- **Verbatim body (the fields the directory JSON drops):**
  - 「於1989年2月4日正式成立。」 (founding date)
  - `https://www.facebook.com/Taiwanese-American-Association-of-Arizona-1455311151348337/`
  - `http://taaa-taiwan.blogspot.com/`
  - `https://www.facebook.com/groups/299778418348318`
  - `Email: Taaa.taiwan@gmail.com`

## Twin / containment check (Capture 1 vs Capture 2)
Normalized both artifacts (strip frontmatter/HTML tags, fold quotes and whitespace;
run 2026-11-14, in-session): JSON body 371 normalized chars vs post body 385;
md5 `d5a15a285a15986a926aa0a525664924` vs `755919ddbe223ab52cadba21efe2f08d` — different,
**and neither contains the other; zero shared sentences**.
- Ruling: these are **two separate editable first-party submissions** (directory entry vs chapter
  post), not two serializations of one record. That means richer content, but still not
  third-party corroboration — every chapter fact from either side stays labeled `alleged`.

## Capture 3 — heritage-week post (print-citation carrier)
- **Archive copy:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/taiwanese-american-heritage-week-of-arizona.md`
  (on-disk mtime 2026-08-21; post id 46981, `date: 2018-03-16` in index.jsonl)
- Render carries 「Source from Taiwan Tribune #2066, 04/26/2005」 and 「Posted in 03/2018」 under the
  title 「Taiwanese American Heritage Week of Arizona 亞利桑那州台灣同鄉會」; the remaining body is site
  chrome and `-` placeholder rows — no further narrative.
- The cited paper (Taiwan Tribune #2066) is **not archived on this box**, so the print chain is one
  editable restatement → `alleged`.

## Directory-batch context (secondary, same crawl)
- Parent TAA record: `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-association-of-america.json`
  (id 77976, `modified` 2026-06-23T17:02:49): founded 1970, five geographic divisions, ~68 active
  chapters as of 2025, WFTA affiliation (1974) — parent self-report.
- NATWA Arizona chapter: `…/organization/north-america-taiwanese-womens-association-arizona-chapter.json`
  (id 78359, `modified` 2026-06-25T15:35:23, `organization_type-women`).
- FAPA Arizona: story post `…/posts/3-arizona-chapter-fapa.md` (index id 27174, `date` 2015-12-30).
- All are directory-batch siblings; same-batch directory authorship is not corroboration of the
  chapter's own facts.

## Whole-corpus sweep (2026-11-14, this card)
Checked `content/` + `knowledge/` per name form
(`grep -rliE 'TAAA|Association of Arizona|亞歷桑那州台灣同鄉會|亞利桑那州台灣同鄉會'`, machine indexes
`units.jsonl`/`posts/index.jsonl`/`ee-vault-index*`/`content-analysis/*` excluded):
- Own-record files: this org page, `content/organizations/index.md`, the work pages
  arizona-chapter-taa / heritage-week / natwa / fapa, `content/sources/taiwaneseamericanhistory-org.md`,
  the Capture 1–3 archive copies.
- TAAA hits that are **not this chapter**: 台美藝術協會 disambiguation set
  (`organizations/taiwanese-american-arts-association.md`, `works/…/taiwanese-american-arts-association-taaa`,
  person page `nami-yang.md` — TAAA president 2004–2005 belongs to the arts org; `dr-c-f-huang.md` —
  TAAA Greater Philadelphia Chapter; `peter-chen.md` — TAAA Dallas chapter mention). All pre-classified
  as other-chapter TAAA usage.
- Arizona hits: `mystories559.md` (a family's Phoenix residence mention, no chapter), taiwanjustice
  TSMC/state coverage, ourjourneys58/338 state-level statistics — no chapter facts.
- `grep` for the contact strings (`Taaa.taiwan`, `taaa-taiwan`) across the box: only the Capture 2 post.
- No third-party narrative record of this chapter exists on this box beyond the above.

## GAPS / NEED YOU
Sources checked and exhausted on this box (2026-11-14): the org JSON (id 78039), the chapter post
(id 27794), the heritage-week post (id 46981), the parent TAA and NATWA/FAPA Arizona sibling records,
posts/index.jsonl, and the whole-corpus greps listed above. Still missing, if a human can supply:
- Officer roster / president names / membership figures (directory and post carry none).
- The 2005-04-26 Taiwan Tribune #2066 issue (print citation exists; the paper is not archived here).
- Any crawl of the chapter's own `taaa-taiwan.blogspot.com` blog or Facebook page/group (known URLs,
  never fetched on this box).
