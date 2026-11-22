---
title: "TAH organization directory capture — LKGT (老康健)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — LKGT (老康健)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 741
- wikilinks: 1


Capture page for the FLOOR-ANCHOR pass on [[organizations/lkgt]] (card t_cae4f43e, 2026-11-14).
Archives what was harvested and what was checked-and-empty, so the next pass does not re-grep.

## Harvested artifacts (two serializations of the org's own submission)

### Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/lkgt.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/lkgt/](https://taiwaneseamericanhistory.org/organization/lkgt/)
- **Record id:** 72490 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-19T16:24:19 (crawl-side capture of this file: on-disk mtime 2026-08-17)
- **`class_list` taxonomy:** `organization_type-senior` (plus WP boilerplate `post-72490`, `tah_organization`,
  `type-tah_organization`, `status-publish`, `has-post-thumbnail`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body** (sanitized rewrite of the directory copy): informal senior social group of
  Taiwanese Americans in the **San Leandro, California** area; shared interests include **Taiwan politics,
  travel, and other hobbies**; established **more than ten years** before the 2016-04-04 publication;
  approximately **twenty families**; regular **Monday gatherings from noon to three o'clock**, indoors or
  outdoors; most members hold **PhDs in various fields**; **every other month** a member delivers a speech at
  a **Taiwanese church in San Leandro**; **not officially registered**, no formal president — **one member is
  selected each year** to coordinate group activities.

### Capture 2 — story-corpus encyclopedia post #26 (the RICHER artifact)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/lkgt.md`
- **Original:** [https://taiwaneseamericanhistory.org/lkgt/](https://taiwaneseamericanhistory.org/lkgt/) (post id **28217**, title `26. LKGT 「老康健」`)
- **Index row:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl` — `{"id": 28217, "slug": "lkgt", "date": "2016-04-04"}`
- Facts present **only in this artifact** (absent from the directory rewrite above):
  - **`Stanly Sun's couple is one of the initiators`** — the only named-person fact in the corpus for LKGT.
  - **`Source form George Chiang`** — first-party submission byline (sic, "form" = "from").
  - **`Posted in 04/2016`** — submission-side publication stamp.
  - Attendance is flexible, normally **more than twenty persons attend**; the group **welcomes anyone interested**;
    sometimes the **pastor is invited to speak** as well.

## Twin / containment check (2026-11-14, this card)
- Normalization: HTML tags stripped, typographic quotes folded, whitespace collapsed, lowercased.
  JSON content: **653** normalized chars (md5 `eeb4c2443574f1abe1710795fbc9a582`); post body: **969** chars
  (md5 `c1e89627a691975b9e9e4407070e1c9f`). md5 differs; containment was tested per paragraph.
- Result: **neither side contains the other** paragraph-for-paragraph — the two copies were independently
  rewritten (wording diverges), but they describe one organization from one first-party submission. The post
  (#26) is the RICH artifact (initiator name, byline, posted-in stamp, attendance detail); the org JSON is the
  sanitized directory rewrite that drops all names. Agreement across these two serializations of one editable
  self-report is **NOT corroboration** → every absorbed row stays `alleged`.

## Directory listing (absence-of-registration context)
- `knowledge/web-archives/taiwaneseamericanhistory-org/pages/senior-organizations.md` (capture of
  https://taiwaneseamericanhistory.org/organizations-archive/senior-organizations/, on-disk mtime 2026-08-21)
  lists `- 26. LKGT 「老康健」` — the TAH senior-organizations index position that gives the record its number 26.

## Checked and empty / coincidental (whole-corpus sweeps, 2026-11-14, `grep -rlF` per form over `content/` + `knowledge/`)
- `老康健` → **23 files**: the org page, `content/organizations/index.md`, the work page, the sources hub row,
  the two own artifacts above + `posts/index.jsonl`, `pages/senior-organizations.md`, and machine indexes
  (`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `units.jsonl`, `priority-lexicon.json`,
  `findings/floor.jsonl`) — plus one coincidental hit below. No memoir/press narrative.
- `LKGT` (case-insensitive) → **54 files**: adds deepen-x slice state files (this card's prior SKIP stamps),
  `extract-stub-state/tahots-merge.jsonl`, and **3 mp3 media files** whose binary frames contain the byte
  sequence incidentally — machine noise, not mentions.
- **Coincidental (verified, re-confirmed this pass):** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/setaa-2006.md`
  contains 老康健 inside 「何康潔醫師…演講中，穿插許多故鄕的風景片」-adjacent prose as `老康健之道` — a generic
  phrase ("the way of aging healthfully") in 何康潔's talk title 「Return of Dr. Omega-3」 at SETAA 2006. It is a
  substring coincidence, not this San Leandro group. Do not absorb.
- **Coincidental (prior passes, still true):** `...6WLKGTYDQXBVLK` / `...D6WLKGTYDQXBVLK` archive-hash substring
  in a 2024-02-21 taiwanjustice.net root-page capture frontmatter (`archive_digest:` field, not prose);
  臨港 (Shanghai 臨港 semiconductor park; 「法國軍艦臨港壓境」) hits in unrelated articles.
- Named-person follow-ups (2026-11-14): `grep -ril 'Stanly Sun'` → `content/people/cossette-sun.md` (husband
  "Dr. Stanly Sun") and its index row — a Castro Valley/Alameda civic figure; San Leandro is adjacent to Castro
  Valley, but **no file states they are the same person**, so no identity link was made (would be invention).
  `George Chiang` hits are his own Who's Who / donation records — none mentions LKGT.
- 2023-TAHS-publication PDF (`knowledge/web-archives/2023-tahs-publication-p001-065.pdf`): grep hit is binary
  noise; text-layer search finds no LKGT/老康健 mention.

## Verdict
One first-party submission, rendered twice (directory JSON + story #26). Absorbed: initiator couple, byline,
posted-in date, attendance/invite details, taxonomy, modified timestamp. No third-party record of LKGT exists
on this box; GAPS/NEED YOU is recorded on the org page.
