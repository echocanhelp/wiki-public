---
title: "TAH organization directory capture — Rice Taiwanese Graduate Student Association"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Rice Taiwanese Graduate Student Association

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 723
- wikilinks: 2


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/rice-taiwanese-graduate-student-association|Rice Taiwanese Graduate Student Association]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/rice-taiwanese-graduate-student-association.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/rice-taiwanese-graduate-student-association/](https://taiwaneseamericanhistory.org/organization/rice-taiwanese-graduate-student-association/)
- **Record id:** 77609 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:26 (crawl-side capture of this file: on-disk mtime 2026-08-17 00:45)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77609`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, two paragraphs):**
  1. "The Rice Taiwanese Graduate Student Association (RTGSA) is a student organization at Rice
     University serving master's, doctoral, and postdoctoral Taiwanese students. Its stated purpose
     centers on professional support — helping members prepare for job recruiting — as well as
     fostering connections with local Taiwanese community groups in the Houston area. The
     organization is registered on OwlNest, Rice's official student engagement platform, which
     serves as its primary public listing. No dedicated website, Instagram, or Facebook page was
     identified through available first-party sources."
  2. "RTGSA is listed among Rice's diversity-focused student organizations in the university's
     library research guide and is recognized by the Rice University Community of Asian Alumni
     (RUCAA) as part of the campus Asian student organization ecosystem. Its founding year is not
     documented in available first-party sources."

## Single-source status
- This JSON is the only first-party artifact for this org on the box. There is no `posts/<record>.md`
  encyclopedia-dump twin (unlike Who's Who person records), so no twin/containment check is possible;
  every field above is one editable self-report → label `alleged` on the org page.
- **Same-batch sibling is NOT corroboration:** the sister org
  [[organizations/rice-taiwanese-association|Rice Taiwanese Association]] is directory record id **77608**,
  one id below this record, with `modified` **2026-06-09T17:23:26** — byte-identical timestamp and same
  `class_list` shape. Both are one editor's same-minute directory batch, so RTA's text does not corroborate
  RTGSA's text and vice versa. Bidirectional containment check on the two `content_html` bodies (tag-stripped,
  quote-folded): neither is a substring of the other — they are two distinct self-reports, but of one authoring
  session, hence one evidentiary tier (`alleged`), not two.

## Whole-corpus sweep (2026-11-14, card t_e53df9d1)
Checked `content/` + `knowledge/` per name form; classification:
- `grep -rlF 'Rice Taiwanese Graduate Student Association' content knowledge` → 20 files: the org page
  itself, `content/organizations/index.md` and `content/sources/taiwaneseamericanhistory-org.md` directory
  index lines, three person pages wikilinking it as campus context
  (`people/chien-an-chen.md`, `people/rachel-chao.md`, `people/min-feng-hsin.md`), the org JSON above, and
  machine indexes (`knowledge/research/taiwanjustice-net-priority-lexicon.json` L4 entry `name_zh` empty,
  `ee-vault-index.v1–v5.json`, `content-analysis/2026-08-2x + 2026-10-2x.jsonl`) — no narrative record.
- `grep -rlF 'RTGSA' content knowledge` → 5 files: the org page, the org JSON, and three person pages
  (`l-w-cheng.md`, `wei-shou-hu.md`, `yuan-chuan-lee.md`) where the string appears only inside deepen-x SKIP
  note comments, not as content. Zero literal RTGSA mention in the memoir/story corpus, consistent with the
  five prior deepen-x SKIP stamps (2026-09-25 → 2026-10-08).
- `grep -rlF 'Rice Taiwanese Association' content knowledge` → 21 files: adds only the sibling RTA page/JSON
  and `knowledge/web-archives/taiwaneseamerican-org/taiwanese-student-association-at-rice-university-first-general-meeting.md`.
- Rice-adjacent records re-opened 2026-11-14 and ruled NOT about this org:
  the 2012-08-30 TSA@Rice first general meeting post (names **RTA**, not RTGSA; membership $5, Farnsworth
  Pavilion); `posts/9-ta-tung-rice-cooker.md` (Rice cooker appliance);
  `posts/174/175/176/308-maurice-hsu-*.md` (FAPA/TAA chapter records, name-adjacent only);
  `posts/whos-who-1774-beatrice-long.md`, `posts/whos-who-859-darice-lee.md` (name-substring false positives).
- Prior deepen-x stamps grepped only `works/` + `articles/` (+ later `sources/events/topics`); this sweep
  covered all of `content/` + `knowledge/` and found no additional citable narrative source.

## Gaps / NEED YOU
Sources checked on this box (all negative for founding year, officers, events, and Chinese name):
TAH org directory JSON 77609 + its sibling 77608; whole-corpus `content/` + `knowledge/` greps for
`Rice Taiwanese Graduate Student Association` / `RTGSA` / `Rice Taiwanese Association`; the 2012 TSA@Rice
event artifact; machine indexes. What would close the gaps:
- Rice **OwlNest** listing for RTGSA (the directory itself names it as the primary public listing) — not
  archived on this box; needs a live fetch.
- The Rice **library research guide** listing RTGSA among diversity-focused student organizations — not
  archived on this box.
- **RUCAA** (Rice University Community of Asian Alumni) recognition record — not archived on this box.
- Any RTGSA-founder submission or Houston-area Taiwanese community-group joint-event record in future
  TAH story-corpus dumps.
