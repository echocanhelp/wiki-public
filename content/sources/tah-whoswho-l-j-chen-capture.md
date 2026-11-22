---
title: "TAH Who's Who profile capture — 1062. L. J. Chen 陳柳江"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 1062. L. J. Chen 陳柳江

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 610
- wikilinks: 4

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.
Minted by FLOOR-ANCHOR card t_47b08dc8 (2026-11-13); the two crawl artifacts below
had never been opened by the DEEPEN-X lane that repeatedly stamped the person page
saturated — its SKIP stamps grepped only `works/ articles/ sources/ events/ topics/`.

## Subject
- [[people/l-j-chen|L. J. Chen 陳柳江]] — TAH Who's Who record #1062

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/l-j-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/l-j-chen/](https://taiwaneseamericanhistory.org/person/l-j-chen/)
- **Record id:** 73619 · **type:** `tah_person` · **profession taxonomy:** `person_profession` term ids `[2242, 2234]` with class_list `person_profession-community-leader` + `person_profession-physician` — **two** taxonomy labels, while the editable form's sidecar `roles` carries only `["physician"]`; the `community leader` label exists nowhere but this site taxonomy
- **`modified` on source:** 2026-06-19T16:43:26 (on-page: `Last updated: June 19, 2026`) · `page_bytes` 52,545 · `content_html` empty · `excerpt` empty
- **Verbatim fields (self-reported):** Name 陳柳江 醫師 · Birth Year `-` · Birth Place 台灣 · First year / first city / state arrived in the U.S. `-/-/-` · Address `-`/CA
- **Family:** `1. Wife:洪美和 · 2.Daughter:Emmeline · 3.Son:-` — harvester parsed `family: [wife 洪美和, daughter Emmeline]`, `family_filled: true`
- **Education:** 台大醫學院 · 1966 · B.S.
- **Employment:** VA Palo Alto Medical Center · `-` · Doctor
- **Accomplishment:** `北加州台灣長輩會會長, 2014` — the one field the person page never absorbed before this card
- **Publication (Non-professional ones) / Hobby / Website or Blog:** all `-` (blank)
- **Posted in:** 2016/06 (per the bibliographic counterpart [[works/taiwaneseamericanhistory-org/whoswho1062]])

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1062.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1062/](https://taiwaneseamericanhistory.org/whoswho1062/)
- **Title:** `1062. L. J. Chen 陳柳江 / 2016/06` (685 bytes)
- Field set identical to Capture 1 (Name 陳柳江 醫師 · 台灣 · family rows · 台大醫學院 1966 B.S. · VA Palo Alto Doctor · `Accomplishment 北加州台灣長輩會會長, 2014` · Publication/Hobby/Website `-`).
- No `Source from <org> <MM/YYYY>` submission-provenance line is printed on either artifact.

## Twin check (2026-11-13)
Normalized both artifacts by stripping frontmatter and all `#`/whitespace, then ran
md5 + containment (stdlib, this card):

| Artifact | Normalized chars | md5 |
|---|---|---|
| Capture 1 `page_text` | 1,176 | `1266a708bc988b966fd79de6b21026aa` |
| Capture 2 post dump | 306 | `f6126592dc7baa1a257e8d46ee4317d8` |

Containment test both directions: **False** (the post dump drops the site chrome, the
`community leader` taxonomy line and the `Last updated` stamp the profile renders; the
profile omits the post dump's `###` label layout — after whitespace normalization neither
string contains the other). They are **distinct serializations of one editable
self-report**, not two records: agreement across them is **not corroboration**. Capture 1
is the richer artifact on taxonomy (it uniquely carries the `community leader` class and
the 2026-06-19 edit stamp); Capture 2 is the cleaner bibliographic dump of the form
fields. This is why the `Accomplishment: 北加州台灣長輩會會長, 2014` line is labeled
`alleged` (one editable record, restatement ≠ corroboration) on the person page.

## Absorb verification 2026-11-16
- sourced 2026-11-16: twin-check re-run this card — Capture 1 `page_text` normalized md5 「1266a708bc988b966fd79de6b21026aa」 matches the 2026-11-13 table verbatim, so the absorb rows in [[people/l-j-chen]] still trace to an unchanged artifact (artifact: knowledge/web-archives/taiwaneseamericanhistory-org/person/l-j-chen.json).
- sourced 2026-11-13: Capture 2 post dump normalized md5 「f6126592dc7baa1a257e8d46ee4317d8」 reconfirmed unchanged; containment still False both directions, so the 2014 「北加州台灣長輩會會長」 honor stays one editable self-report — labeled `alleged`, never corroboration (artifact: knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1062.md).
- sourced 2026-11-16: person-page absorb verification — every dated row of the `## From the record` table in [[people/l-j-chen]] names one of the two artifact paths above or a knowledge post path, disk lint measured anchored=19/links=19 EXIT-0, and the fleet `--alert` report greps 0 for this slug (script: echo-system/scripts/substance-lint.py).

## What this capture does NOT establish
- No birth year, no US arrival year/city/state, no street address (only state `CA`).
- No publication, hobby, or personal website — blank in both artifacts (absence evidence).
- No dates or degree detail for the VA Palo Alto line (start/end `-`).
- The `community leader` label exists only as a site taxonomy class on Capture 1, not as
  a stated role in the editable form.
- Third-party corroboration lives separately in
  [[sources/l-j-chen-thirdparty-capture|the third-party corroboration capture]]; this
  page is the self-report side only.
