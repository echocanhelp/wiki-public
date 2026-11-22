---
title: "TAH organization directory capture — NATWA Hawaii Chapter"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — NATWA Hawaii Chapter

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 709
- wikilinks: 3


Primary capture of the chapter's own record in the TAH Foundation organization directory,
archived on this box. Preserved in full because the directory entry is an editable
first-party self-report.

## Subject
- [[organizations/north-america-taiwanese-womens-association-hawaii-chapter|NATWA Hawaii Chapter]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/north-america-taiwanese-womens-association-hawaii-chapter.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/north-america-taiwanese-womens-association-hawaii-chapter/](https://taiwaneseamericanhistory.org/organization/north-america-taiwanese-womens-association-hawaii-chapter/)
- **Record id:** 78363 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-25T15:51:04 (crawl-side capture of this file: on-disk mtime 2026-08-17)
- **`class_list` taxonomy:** `organization_type-women` (plus WP boilerplate `post-78363`, `tah_organization`, `type-tah_organization`, `status-publish`, `has-post-thumbnail`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, single paragraph):** "North America Taiwanese
  Women's Association – Hawaii Chapter is a local chapter of the North America Taiwanese Women's
  Association (NATWA), serving Hawaii area."

## Capture 2 — encyclopedia-corpus bibliographic record
- **Work page:** [[works/taiwaneseamericanhistory-org/natwa-hawaii-chapter|6. Hawaii Chapter / NATWA 北美洲台灣婦女會夏威夷分會]]
  (record date 2015-12-26; value band B; `fetched: auto`)
- **Archive copy:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/natwa-hawaii-chapter.md`
  (on-disk mtime 2026-08-21)
- Field-by-field, the render is site chrome plus the title repeated twice
  ("… – History of Taiwanese American (T.A. Archives) 台美史料中心"); the 19 `-` placeholder rows
  prove **no biographical or narrative field was filled on the page** — bibliographic record only,
  consistent with the work page's own `_Bibliographic record only. Full text stays in the vault._`.

## Twin / containment check (Capture 1 vs Capture 2)
- Normalizing both artifacts (strip frontmatter/HTML tags, fold quotes and whitespace) and testing
  containment paragraph-by-paragraph: the JSON paragraph's sentence appears in the post render only
  as the page **title** (title tag / H1 / `###`), never as body prose. The JSON `content_html` is a
  strict serialization subset of the title strings; the post adds **zero** chapter-level facts.
- Ruling: the two artifacts are **one editable first-party directory record plus its bibliographic
  index entry** — agreement across two serializations of the same editable source is **not**
  corroboration, so directory facts stay labeled `alleged`.

## Capture 3 — third-party dated attestation (Pew statement)
- **Work page:** [[works/taiwaneseamerican-org/pew-research-center-taiwanese-american-statement|Response to Pew Research Reports Hiding Taiwanese Identity]]
  (`Record Date: 2021-05-01`, `Byline: Leona`, value band A)
- **Archive copy:** `knowledge/web-archives/taiwaneseamerican-org/pew-research-center-taiwanese-american-statement.md`
  (on-disk mtime 2026-08-20)
- The signatory block lists "Josephine Wu Vuylsteke, NATWA, Hawaii Chapter" — a dated third-party
  publication naming the chapter acting through a named representative. This is the only
  non-self-report record of this chapter on the box.

## Directory-listing attestations (secondary)
- `knowledge/web-archives/taiwaneseamericanhistory-org/pages/social-organizations.md` and
  `knowledge/web-archives/taiwaneseamericanhistory-org/pages/north-america-taiwanese-womens-association-natwa.md`
  each list "6. Hawaii Chapter / NATWA 北美洲台灣婦女會夏威夷分會" — the same 16-chapter NATWA roster
  rendered on two directory pages; numbering attests its position in the NATWA chapter roster.

## Whole-corpus sweep (2026-11-14, this card)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rlF '北美洲台灣婦女會夏威夷分會' content knowledge` → 23 files: the org page itself,
  `content/organizations/index.md`, the work page, `content/sources/taiwaneseamericanhistory-org.md`,
  the org JSON, the post dump, the two directory pages above, plus machine indexes only
  (`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `posts/index.jsonl`,
  `research/taiwaneseamericanhistory-org/units.jsonl`, `taiwanjustice-net-priority-lexicon.json`)
  — no narrative record beyond those captured above.
- `grep -rliE 'NATWA.{0,40}Hawaii|Hawaii.{0,40}NATWA'` (indexes excluded) → adds only the Pew
  statement (captured above), `content/people/dew-chin-ghi-chang.md` and
  `content/people/tah-p-e00ace0a3a.md` — both carry only deepen-x SKIP-note prose quoting this
  card's own grep ("NATWA Hawaii: no new NATWA/Hawaii-chapter mentions"), not chapter facts;
  and `content/organizations/taiwanese-american-association-of-arizona.md`, likewise a SKIP note.
- `grep -rli 'Josephine Wu' content knowledge` → only this org page, the Pew work page, and the Pew
  archive copy. No further record of the representative on this box.
- Sibling NATWA chapter JSONs (Arizona, Boston, Detroit, San Diego, Kansas, New Jersey, New York,
  Northern California, Ohio/Kentucky, Oregon/Southwest WA, Southern California, St. Louis,
  Wisconsin/Illinois) exist in the same directory crawl; the parent org JSON (id 78358,
  `modified` 2026-06-25T15:29:36) is the same batch on the same day — same-batch directory
  authorship is not corroboration.

## GAPS / NEED YOU
Sources checked and exhausted on this box (2026-11-14): the two org JSON/`posts` crawl copies, the
Pew statement archive copy, both NATWA directory pages, and whole-corpus greps per name form
listed above. Still missing, if a human can supply:
- A chapter-internal record (roster, founding year, chapter officers, activity reports) — none of
  the NATWA 聯誼通訊 issues (items 662–697 catalogued) name a Hawaii chapter activity on this box.
- Any Hawaii-local press coverage (台報/世界日報/台灣日報 archives) of the chapter — none archived here.
