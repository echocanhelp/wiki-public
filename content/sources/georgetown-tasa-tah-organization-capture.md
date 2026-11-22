---
title: "TAH organization directory capture — Georgetown Taiwanese American Student Association"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Georgetown Taiwanese American Student Association

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 765
- wikilinks: 1


Capture page minted for the FLOOR-ANCHOR pass on
[[organizations/georgetown-taiwanese-american-student-association]] (card t_8b6a2094, 2026-11-14).
It archives the one machine record this organization has on this box, plus the checked-and-empty
sweep, so the next pass does not re-grep.

## Captured machine record (the organization's own directory entry)
- File: `knowledge/web-archives/taiwaneseamericanhistory-org/organization/georgetown-taiwanese-american-student-association.json`
- Record id **77628**, `type: tah_organization`, `status-publish`, taxonomy class slug
  `organization_type-student`; `person_profession` is the empty list `[]`; `excerpt` is `null`.
- `modified` stamp on source: **2026-06-09T17:23:28**; on-disk capture of the JSON on this box:
  2026-08-17 (1,688 bytes).
- Live URL of the same record: https://taiwaneseamericanhistory.org/organization/georgetown-taiwanese-american-student-association/
- Verbatim `content_html` (self-reported, site-editable, two paragraphs):
  1. "The Georgetown Taiwanese American Student Association (TASA) is a student organization at
     Georgetown University in Washington, D.C., dedicated to promoting Taiwanese culture through
     social, educational, and cultural programming. The organization is officially recognized by the
     university and is listed in Georgetown's student organization directory, where it is reachable at
     tasa@georgetown.edu. It is also a named member of the Students of Color Alliance (SOCA),
     Georgetown's umbrella coalition of cultural student organizations."
  2. "TASA has participated in Mid-Atlantic regional events and ITASA national conferences, and has
     historically served as a resource and support network for both Taiwanese American students and
     students from Taiwan interested in Taiwanese culture. The organization maintains active social
     media presences on Instagram (@georgetowntasa) and Facebook (georgetowntasa). Georgetown
     University has also highlighted TASA as one of the student groups that recognizes AAPI heritage
     with events across campus year-round."
- Label: `alleged`. `content_html` is the only substantive field on the record, so every fact above
  traces to one editable self-report, not to corroboration.

## Campus-name-neighbor check: the sibling GUTSA record
- Sibling record `knowledge/web-archives/taiwaneseamericanhistory-org/organization/georgetown-taiwanese-student-association.json`
  — id **77629**, "Georgetown Taiwanese Student Association" (GUTSA), same `modified`
  **2026-06-09T17:23:28**, same `organization_type-student` taxonomy, same campus.
- Containment/md5 check on tag-stripped, whitespace-normalized `content_html`:
  TASA 911 normalized chars (md5 `c687b31ceff7554a07e135c8852e31fb`) vs GUTSA 927
  (md5 `59ff29848481944485d3db4ed15d694c`) — md5-different **and neither string contains the
  other**. These are two separately authored directory records captured in one 2026-06-09 crawl
  batch, **not** two serializations of one self-report.
- Identity boundary: the two records describe different states (TASA: currently recognized, listed in
  the Georgetown directory, SOCA member, active socials; GUTSA: past tense "was", active
  2011–2012 per a former vice president's April 2012 personal website, absent from the current
  directory, no first-party web presence as of 2026). Neither record states any relationship to the
  other. The deepen-x lane has held them as possible near-duplicates (title jaccard 0.80, never
  auto-merged). They remain two pages; GUTSA is **not** corroboration for TASA facts and vice versa.

## Adjacent-Georgetown records in the vault (non-membership cross-references, counted as non-corroboration)
- `knowledge/web-archives/taiwaneseamericanhistory-org/person/` — eight Who's Who JSONs mention
  Georgetown only as an individual's education/employment: `dr-jia-huey-lin-yu.json` (#72733,
  Georgetown Univ. Associate Professor 1983–1996), `jeffrey-l-chen.json` (#73895, Georgetown Univ.
  School of Medicine 2006), `john-chiang.json` (#72641, Georgetown Univ. M.A. Law),
  `ming-yen-hsu.json` (#73058, Georgetown Univ. and Veteran Hospital 1967),
  `nat-bellocchi.json` (#73402, Georgetown Univ. B.A. 1954), `oliver-chen.json` (#73246,
  Georgetown Univ. B.S. Business Administration), `sam-huang.json` (#73785, Georgetown Univ.
  M.S. Organic Chemistry), `ted-lieu.json` (#72737, Georgetown Univ. Law Center J.D. 1994).
  None mentions a Taiwanese student association at Georgetown.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mystories124.md` — a 曾 family memoir
  naming a daughter who earned a political-science PhD at Georgetown University; no club mention.
- ITASA corpus (`content/works/taiwaneseamerican-org/*itasa*`, ~48 files, plus the
  `content/works/taiwaneseamericanhistory-org/` ITASA cluster): conference rosters for West Coast,
  Midwest, NorCal, SoCal and East Coast events (2009–2014 named) — none names Georgetown TASA,
  so the directory's own ITASA-participation claim stays `alleged` and uncorroborated.
- SOCA / "Students of Color Alliance": the only two vault files carrying the string are this org page
  and the org JSON itself.

## Checked and empty (sweeps re-run 2026-11-14, `grep -rlF` over `content/` + `knowledge/`)
- `Georgetown Taiwanese American Student Association` → own page, GUTSA page (HOLD-note
  cross-reference), `organizations/index.md`, `sources/taiwaneseamericanhistory-org.md` directory
  listing, the org JSON, plus machine indexes only (`ee-vault-index.v1–v5.json`,
  `content-analysis/*.jsonl`, `taiwanjustice-net-priority-lexicon.json`).
- `Georgetown Taiwanese Student Association` / `GUTSA` → GUTSA page + index + directory listing +
  JSON + machine indexes only.
- `georgetowntasa` → 0 files. `tasa@georgetown.edu` → own page only.
- Broad `Georgetown` → 19 files in `content/`, all classified unrelated (Georgetown, Texas /
  Georgetown, Guyana place names, a Georgetown University Press book, a journalist enrolled at
  Georgetown, university faculty quoted in taiwanjustice-net news translations), matching the
  deepen-x SKIP stamps of 2026-09-18 → 2026-10-09; re-verified this pass with a co-occurrence
  scan (`Georgetown` × `TASA|Taiwanese` in the same sentence) over `content/works`,
  `content/articles` and the whole `web-archives/taiwaneseamericanhistory-org/` tree → the single
  hit `posts/mystories124.md` is the PhD memoir above, not this club.
- Machine indexes were excluded as sources per lane rule.
