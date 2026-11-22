---
title: "TAH organization directory capture — UW iTaiwan Graduate Students and Professional Organization"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — UW iTaiwan Graduate Students and Professional Organization

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 564
- wikilinks: 1


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/uw-itaiwan-graduate-students-and-professional-organization|UW iTaiwan Graduate Students and Professional Organization]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/uw-itaiwan-graduate-students-and-professional-organization.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/uw-itaiwan-graduate-students-and-professional-organization/](https://taiwaneseamericanhistory.org/organization/uw-itaiwan-graduate-students-and-professional-organization/)
- **Record id:** 77570 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:23 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77570`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, two paragraphs):** ¶1 — the UW iTaiwan Graduate Students and
  Professional Organization (Chinese name: 西雅圖華大台灣研究生社) is listed as a Taiwanese student organization at
  the University of Washington on the UW Jackson School of International Studies Taiwan Studies Program community
  page, categorized alongside TSAUW and TOSAUW as one of three UW student organizations oriented toward the
  Taiwanese community on campus. ¶2 — *No independent website, Instagram, Facebook page, or other first-party
  digital presence was located for this organization during research. Details about founding, mission, membership,
  or current programming cannot be confirmed from available first-party sources and are therefore not included
  here.* (¶2 was never absorbed into the org page before this card.)

## Capture 2 — story-corpus encyclopedia post (title-only twin)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/uw-itaiwan-graduate-students-and-professional-association.md`
- **Original:** [https://taiwaneseamericanhistory.org/uw-itaiwan-graduate-students-and-professional-association/](https://taiwaneseamericanhistory.org/uw-itaiwan-graduate-students-and-professional-association/)
- Post title on site: `24. UW iTAIWAN Graduate Students and Professional Association 西雅圖華大台灣研究生社` — note
  **Association**, while the directory record says **Organization** (same Chinese name 西雅圖華大台灣研究生社).
- The post body carries no biographical content: every metadata field renders `-`, the rest is site navigation
  chrome. It contributes the numbered-encyclopedia listing (#24) and the alternate English name only.
- Directory-page listing confirmed at `knowledge/web-archives/taiwaneseamericanhistory-org/pages/political-organizations.md`
  line 117: `- 24. UW iTAIWAN Graduate Students and Professional Association 西雅圖華大台灣研究生社`.

## Twin / containment check (this card, 2026-11-14)
- Org JSON content block normalized (tags + whitespace stripped): **598 chars**, md5 `52234187958c6c239b8ce53e1b14cdd7`.
- Post file normalized: **5,019 chars**, md5 `b1236b4cbd01d98c7334712c2235120b` (dominated by nav chrome; no unique prose).
- Containment both directions: False / False. The post is not an independent record — it is the same self-report
  rendered as a numbered encyclopedia stub. Both artifacts come from one editable site → every row `alleged`.

## Whole-corpus sweep (2026-11-14, this card)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -ril 'UW iTaiwan'` (md/json, excluding machine indexes) → the org page, works index, own work page,
  sources hub, `content/organizations/index.md`, the two crawl artifacts above, the political-organizations
  directory page, and `knowledge/research/taiwanjustice-net-priority-lexicon.json` (machine lexicon, not a source).
- `grep -rlF '西雅圖華大'` → adds `2023-tahs-publication-part1.md`, `taiwandaily-net-6670-6670.md`,
  `my-stories-692/711/896.md` — all classified **false positives**: 西雅圖華大 there is prose meaning
  "University of Washington" (鄭紹良's PhD and 台灣同鄕會 founding; 楊牧/陳少聰 UW faculty move; an author's
  1966 UW urban-planning study). None names 西雅圖華大台灣研究生社.
- Prior deepen-x stamps (2026-09-22/24/25/26, 10-07, 10-09) already ruled the 2025 OCAC 僑委會 "iTaiwan"
  article a different referent (the OCAC iTaiwan service window); re-grep 2026-11-14 did not recur it.
- Machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.*`, `content-analysis/*.jsonl`) excluded as sources.

## Verdict
No third-party record of this club exists on this box. The citable harvest is the directory JSON (¶2 never
absorbed), its `modified`/`class_list` metadata, and the numbered story-corpus post stub carrying the
alternate "Association" title.
