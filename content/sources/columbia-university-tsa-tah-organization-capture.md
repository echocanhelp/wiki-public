---
title: "TAH organization directory capture — Columbia University Taiwanese Student Association"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Columbia University Taiwanese Student Association

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 631
- wikilinks: 1


Primary capture of the organization's own record in the TAH Foundation organization
directory, archived on this box. Preserved in full because the directory entry is an
editable first-party self-report.

## Subject
- [[organizations/columbia-university-taiwanese-student-association|Columbia University Taiwanese Student Association]] — TAH organization directory record

## Capture 1 — crawled organization JSON
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/columbia-university-taiwanese-student-association.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/columbia-university-taiwanese-student-association/](https://taiwaneseamericanhistory.org/organization/columbia-university-taiwanese-student-association/)
- **Record id:** 77549 · **type:** `tah_organization`
- **`modified` on source:** 2026-06-09T17:23:21 (crawl-side capture of this file: on-disk mtime 2026-08-17, 1,896 bytes)
- **`class_list` taxonomy:** `organization_type-student` (plus WP boilerplate `post-77549`, `tah_organization`, `type-tah_organization`, `status-publish`, `hentry`)
- **`person_profession`:** `[]` (empty — org records carry no profession taxonomy)
- **`excerpt`:** `null`
- **Verbatim `content_html` body (self-reported, three paragraphs):**
  1. "The Columbia University Taiwanese Student Association (CUTSA / 哥倫比亞大學臺灣同學會) is a non-profit, student-run organization at Columbia University composed of Taiwanese students currently enrolled at the university. It operates as a non-political, non-religious organization open to graduate students, faculty, and alumni, with a focus on supporting students from Taiwan who are studying in the greater New York area."
  2. "According to its official About page, CUTSA is dedicated to enhancing the social network among its members and assists prospective students in making a successful transition into life at Columbia. Its stated mission is to create a platform for members to exchange ideas, participate in activities with other organizations, broaden cultural exposure, and improve quality of life. The organization holds academic, cultural, and social events throughout the year."
  3. "CUTSA maintains an active Tumblr-based website (cutsa.tumblr.com) listing current board members, an Instagram account (@columbiatsa — 紐約哥倫比亞大學台灣學生會), and a Facebook group. The Tumblr site carries a copyright notice spanning 2015–2025, indicating continuous operation over at least a decade."

## Single-source status
- This JSON is the only first-party artifact for this org on the box. There is no `posts/<record>.md`
  encyclopedia dump twin (unlike Who's Who person records), so no twin/containment check against a
  second serialization is possible; every field above is one editable self-report → label `alleged`.
- The directory's paragraph 2 is itself a restatement of CUTSA's official About page — restatement ≠
  corroboration; it stays `alleged` until the About page/Tumblr is captured independently.

## Sibling containment check (2026-11-14)
Three Columbia orgs sit in the same crawl batch; checked bidirectionally for overlap:
- CU TASA (id 77548, undergraduate, `columbia-university-taiwanese-american-students-association.json`) —
  distinct text (undergrad, Columbia College/Engineering Activities Board), no shared sentences with CUTSA.
- CUTSA (id 77549, this record).
- TGSA (id 77550, graduate, `columbia-university-taiwanese-graduate-student-association.json`) —
  distinct text (LionLink, @columbiatgsa); names CUTSA only to state the relationship "is not clarified
  in available sources".
All three carry `modified` 2026-06-09T17:23:21 — same-batch authorship is NOT corroboration across the
three records; each remains a single editable self-report. No containment (neither substring direction)
between the CUTSA `content_html` and the sibling bodies.

## Whole-corpus sweep (2026-11-14, this card)
`grep -rlF` per name form over `content/` + `knowledge/` (machine indexes
`units.jsonl`/`index.jsonl`/`ee-vault-index.*`/`content-analysis/*.jsonl` excluded as non-sources):
- `CUTSA` → this org page + JSON, the TGSA page + JSON (disambiguation notes only).
- `哥倫比亞大學臺灣同學會` → this org page + JSON, TGSA page (disambiguation note only).
- `哥倫比亞大學台灣學生會` → TGSA page + both Columbia JSONs (Instagram handle string inside this
  record's own body; TGSA's Facebook name) — no third-party use.
- `cutsa` → adds `content/works/taiwaneseamericanhistory-org/ncutsa.md` (NCUTSA = North Carolina TSA,
  different org, bibliographic record only) and machine index `tahots-merge.jsonl` (non-source).
- `columbia-university-taiwanese-student` → adds `content/organizations/index.md`,
  `content/sources/taiwaneseamericanhistory-org.md` (index lines), person pages `will-tiao`,
  `jerry-jean`, `joanne-chang`, `andrew-yang` (context-only campus backlinks; membership not asserted),
  `knowledge/research/taiwanjustice-net-priority-lexicon.json` (machine lexicon), deepen-x slice logs
  (instrument output), `knowledge/operational/findings/floor.jsonl` (this card's own lint finding).
No memoir, article, or press record names CUTSA. Prior deepen-x stamps (2026-09-22 → 2026-10-03, seven
slices) also returned zero genuine hits; the 2026-11-14 sweep extended scope to all of `content/` +
`knowledge/`, not only `works/` + `articles/`.
