---
title: "TAH organization directory capture — Penn Taiwanese Student Association"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Penn Taiwanese Student Association

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 559
- wikilinks: 1


Capture page for the FLOOR-ANCHOR pass on [[organizations/penn-taiwanese-student-association]]
(card t_91e72477, 2026-11-14). Archives what was harvested and what was checked-and-empty,
so the next pass does not re-grep.

## Harvested artifact — crawled organization JSON

- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/penn-taiwanese-student-association.json`
  (on-disk mtime 2026-08-17 00:45, 1,372 bytes)
- **Original:** [https://taiwaneseamericanhistory.org/organization/penn-taiwanese-student-association/](https://taiwaneseamericanhistory.org/organization/penn-taiwanese-student-association/)
- **Record id:** 77556 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:21
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77556`,
  `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` · **`excerpt`:** `null` (org records carry no profession taxonomy)
- **Verbatim `content_html`** (two paragraphs, previously never absorbed):
  1. Penn Taiwanese Student Association is a Taiwanese student organization at the University of
     Pennsylvania, identified through its active Instagram account (@upenntsa), which carries the
     Chinese name 賓大台灣學生會. As of the time of research, the account had **271 followers and 56
     posts**. The organization's Instagram bio describes it as "Taiwanese Student Association
     @uofpenn."
  2. **"This organization appears to be distinct from both the undergraduate Penn Taiwanese Society
     (PTS) and the graduate-level TGAPSA, though the full scope of its membership (undergraduate,
     graduate, or open) and its programming could not be confirmed from available first-party
     sources. A Facebook page at facebook.com/UPennTSA was found but is currently unavailable or
     restricted."**
- The second paragraph was **absent from the page body** before this card — that is the real
  harvest (distinctness ruling vs PTS/TGAPSA, membership-scope unknown, restricted Facebook page).

## Twin check (2026-11-14, this card)

The `tah_organization` JSON class has no story-dump `posts/` twin: `ls posts | grep -i penn`
returns only `45-pennsylvania-chapter-chapter-fapa.md` (FAPA PA chapter, unrelated — number 45 is
a directory index item, title checked per the same-number collision rule). Containment check N/A:
one editable directory self-report → every absorbed row stays `alleged`.

## Sibling same-school artifacts (context, NOT corroboration)

Same-batch `modified` 2026-06-09T17:23:xx in the same crawl proves shared directory authorship,
which is **not** corroboration for this org's facts:
- `organization/penn-taiwanese-society.json` — undergrad PTS, "founded in 1990 according to the
  organization's own Instagram bio", listed on Penn PAACH + Penn Clubs.
- `organization/taiwanese-graduate-and-professional-student-association.json` — TGAPSA, "also
  referred to as UPenn TSA", graduate/professional, university-wide.
- `organization/upenn-tesol-taiwanese-student-association.json` — UTTSA (id 77558), GSE TESOL
  program org in PAACH Student Communities; "No dedicated website, Instagram, Facebook, or other
  independent online presence was found."

## Whole-corpus sweep (2026-11-14, this card; `grep -rlF` per name form over `content/` + `knowledge/`)

- `Penn Taiwanese Student Association` → 5 content files (the page itself,
  `organizations/index.md`, backlinks `people/huei-sheng-kao.md` timeline row + vault re-check
  note, `people/dr-fu-chen-lo.md` Philadelphia-orbit adjacency note — both wikilinks FROM corpus
  pages TO this org, no new facts —, `sources/taiwaneseamericanhistory-org.md` directory index)
  + machine indexes (`ee-vault-index.v*`, `content-analysis/*.jsonl`,
  `taiwanjustice-net-priority-lexicon.json`) — indexes are not sources.
- `賓大台灣學生會` → only this page + the org JSON.
- `upenntsa` → only this page + the org JSON. `UPennTSA` → only the org JSON.
- Earlier deepen-x SKIP stamps (2026-09-26, 2026-10-02, 2026-10-07) grepped only
  works/articles/sources/events/topics; this sweep extends to all of `content/` + `knowledge/`
  and confirms no memoir, article, or third-party record names the club.

## Gaps / NEED YOU

- No first-party (Instagram/Facebook) capture on this box; Instagram follower/post counts are the
  directory's 2026 snapshot restatement. A live web pass on `@upenntsa` (Instagram is login-walled)
  and the restricted `facebook.com/UPennTSA` page would be needed to confirm current status.
- Membership scope (undergrad vs grad vs open) and founding year: unknown in every local record.
