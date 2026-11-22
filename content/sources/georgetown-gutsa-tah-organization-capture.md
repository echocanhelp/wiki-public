---
title: "TAH organization directory capture — Georgetown Taiwanese Student Association (GUTSA)"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
tier: M
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Georgetown Taiwanese Student Association (GUTSA)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): ~620
- wikilinks: 3

Capture page minted for the FLOOR-ANCHOR pass on
[[organizations/georgetown-taiwanese-student-association]] (card t_3011fa31, 2026-11-14).
It archives the one machine record this organization has on this box, plus the checked-and-empty
sweep, so the next pass does not re-grep. Sibling pattern:
[[sources/georgetown-tasa-tah-organization-capture]] (TASA capture, same lane, same day).

## Captured machine record (the organization's own directory entry)
- File: `knowledge/web-archives/taiwaneseamericanhistory-org/organization/georgetown-taiwanese-student-association.json`
- Record id **77629**, `type: tah_organization`, `status-publish`, taxonomy class slug
  `organization_type-student`; `person_profession` is the empty list `[]`; `excerpt` is `null`.
- `modified` stamp on source: **2026-06-09T17:23:28**; on-disk JSON on this box: 1,681 bytes
  (byte count re-derived 2026-11-14 with `wc -c`).
- Live URL of the same record: https://taiwaneseamericanhistory.org/organization/georgetown-taiwanese-student-association/
- Verbatim `content_html` (self-reported, site-editable, two paragraphs):
  1. "The Georgetown Taiwanese Student Association (GUTSA) was a student organization at Georgetown
     University that served students from Taiwan. A former vice president's personal website (dated
     April 2012) documents the organization as active during the 2011–2012 academic year, describing
     its purpose as advocating for Taiwanese culture through educational, social, and cultural
     activities within the Georgetown community. GUTSA also aimed to maintain connections with alumni
     worldwide and to build relationships with other Taiwanese student organizations."
  2. "Documented activities from that period included organizing welcome receptions for incoming
     Taiwanese students, hosting cultural festivals such as the Mid-Autumn Festival and Lantern
     Festival, and maintaining a communication link between Taiwanese students and the Taipei
     Economic and Cultural Office (TECRO). GUTSA does not appear in Georgetown's current official
     student organization directory, and no first-party web presence (website, Instagram, Facebook,
     or Linktree) has been identified as of 2026."
- Label: `alleged`. `content_html` is the only substantive field on the record, so every fact above
  traces to one editable self-report, not to corroboration.
- Coverage note: the org page carried only paragraph 1 before this pass; the whole second paragraph
  (2011–2012 activities, TECRO link, current-directory absence) was unreleased archive text now
  absorbed into [[organizations/georgetown-taiwanese-student-association]].

## Campus-name-neighbor check: the sibling TASA record
- Sibling record `knowledge/web-archives/taiwaneseamericanhistory-org/organization/georgetown-taiwanese-american-student-association.json`
  — id **77628**, "Georgetown Taiwanese American Student Association" (TASA), same `modified`
  **2026-06-09T17:23:28**, same `organization_type-student` taxonomy, same campus.
- Containment/md5 check on tag-stripped, whitespace-normalized `content_html` (re-run 2026-11-14,
  independently confirming the TASA-side capture): GUTSA 927 normalized chars (md5
  `59ff29848481944485d3db4ed15d694c`) vs TASA 911 (md5 `c687b31ceff7554a07e135c8852e31fb`) —
  md5-different **and neither string contains the other**: two separately authored directory records
  captured in one 2026-06-09 crawl batch, **not** two serializations of one self-report.
- Identity boundary: the two records describe different states (GUTSA: past tense "was", active
  2011–2012 per a former vice president's April 2012 personal website, absent from the current
  directory, no first-party web presence as of 2026; TASA: currently recognized, listed in the
  Georgetown directory, SOCA member, active socials). Neither record states any relationship to the
  other. The deepen-x lane has held them as possible near-duplicates (title jaccard 0.80, never
  auto-merged). They remain two pages; TASA is **not** corroboration for GUTSA facts and vice versa.

## Adjacent-Georgetown records in the vault (non-membership cross-references, counted as non-corroboration)
- `knowledge/web-archives/taiwaneseamericanhistory-org/person/` — eight Who's Who JSONs mention
  Georgetown only as an individual's education/employment: `dr-jia-huey-lin-yu.json` (#72733),
  `jeffrey-l-chen.json` (#73895), `john-chiang.json` (#72641), `ming-yen-hsu.json` (#73058),
  `nat-bellocchi.json` (#73402), `oliver-chen.json` (#73246), `sam-huang.json` (#73785),
  `ted-lieu.json` (#72737). None mentions a Taiwanese student association at Georgetown.
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/mystories124.md` — a 曾 family memoir
  naming a daughter who earned a political-science PhD at Georgetown University; no club mention.
- ITASA corpus (`content/works/taiwaneseamerican-org/*itasa*`, plus the
  `content/works/taiwaneseamericanhistory-org/` ITASA cluster): conference records 2009–2014 name no
  Georgetown chapter, so neither Georgetown page gains ITASA corroboration.
- TECRO / 台北經濟文化辦事處: the only vault files carrying a GUTSA×TECRO string are this capture,
  the GUTSA org page, and the GUTSA JSON — i.e. the same self-report, no independent record.

## Checked and empty (sweeps re-run 2026-11-14, `grep -rlF` over `content/` + `knowledge/`)
- `GUTSA` → GUTSA org page, this capture, the sibling TASA capture + TASA org page (HOLD-note
  cross-references), `organizations/index.md`, `sources/taiwaneseamericanhistory-org.md` directory
  listing, the GUTSA JSON, plus machine indexes only (`ee-vault-index*.json`,
  `content-analysis/*.jsonl`, `taiwanjustice-net-priority-lexicon.json`).
- `Georgetown Taiwanese Student Association` → same file set as above.
- Broad `Georgetown` → all `content/` hits unrelated (Georgetown, Texas / Georgetown, Guyana place
  names, a Georgetown University Press book, a journalist enrolled at Georgetown, university faculty
  quoted in taiwanjustice-net news translations), matching the deepen-x SKIP stamps of 2026-09-18 →
  2026-10-09; re-verified this pass with a co-occurrence scan (`Georgetown` ×
  `TASA|Taiwanese|GUTSA` in the same sentence) over `content/works`, `content/articles` and the
  whole `web-archives/taiwaneseamericanhistory-org/` tree → the single hit `posts/mystories124.md`
  is the PhD memoir above, not this club.
- Machine indexes were excluded as sources per lane rule.
