---
title: "TAH organization directory capture — Emory TSA"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH organization directory capture — Emory TSA

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 579
- wikilinks: 1


Capture page minted for the FLOOR-ANCHOR pass on
[[organizations/emory-tsa]] (card t_97c35f54, 2026-11-14). It archives the one
machine record this organization has on this box, plus the checked-and-empty
sweep, so the next pass does not re-grep.

## Captured machine record (the organization's own directory entry)
- File: `knowledge/web-archives/taiwaneseamericanhistory-org/organization/emory-tsa.json`
- Record id **77626**, `type: tah_organization`, `status-publish`, taxonomy class slug
  `organization_type-student`; `person_profession` is the empty list `[]`;
  `excerpt` is `null`.
- `modified` stamp on source: **2026-06-09T17:23:27**.
- On-disk mtime of the capture file: **2026-08-17 00:45 -0700** (crawl-side capture date).
- File size on disk: 1,259 bytes.
- Live URL of the same record: https://taiwaneseamericanhistory.org/organization/emory-tsa/
- Verbatim `content_html` substance (self-reported, site-editable, two paragraphs):
  Emory TSA (台灣學生會, Taiwanese Student Association) is a student organization at
  Emory University's Atlanta campus; it maintains an active Instagram presence under
  the handle @emory.tsa, where it identifies itself as "Emory TSA 台灣學生會 ."; no
  dedicated website, Facebook page, or Linktree was located through available
  first-party sources; no founding year could be confirmed. Second paragraph: the
  Chinese name 台灣學生會 indicates the organization primarily serves students from
  Taiwan, distinguishing it from the separately organized Emory TASA (Taiwanese
  American Student Association), which focuses on Taiwanese American cultural
  identity; both organizations are present on Emory's Atlanta campus.
- Label: `alleged`. `content_html` is the only substantive field on the record, so
  every fact above traces to one editable self-report, not to corroboration.

## Single-source status / twin check
- This JSON is the only first-party artifact for this org on the box
  (`grep -rilF 'emory-tsa'` → the org page, `organizations/index.md`,
  `sources/taiwaneseamericanhistory-org.md`, this capture page, the JSON, and
  machine indexes only). There is no `posts/<record>.md` encyclopedia-dump twin
  (unlike Who's Who person records), so no twin/containment check is possible.

## Campus-name-neighbor check: Emory TASA
- Sibling record `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-american-student-association-at-emory-university.json`
  — record id **77625**, same `modified` **2026-06-09T17:23:27**, same
  `organization_type-student` taxonomy, same Emory Atlanta campus.
- Body-length comparison (HTML tags + `#`/whitespace stripped): 965 characters for
  TASA versus 615 for Emory TSA, and neither string contains the other — so these are
  two separately authored directory records captured in one 2026-06-09 crawl batch,
  **not** two serializations of one self-report. Shared campus and crawl batch are
  recorded here as an identity-collision hazard; same-batch authorship is **not**
  corroboration for either page's facts.
- The only relationship claim anywhere on the box is Emory TSA's own `content_html`
  sentence distinguishing itself from Emory TASA — a first-party claim about the
  sibling, kept on this page, not promoted to either org's dated record.

## Checked and empty (sweeps re-run 2026-11-14, `grep -ril`/`-rlF` over `content/` + `knowledge/`)
- `Emory TSA` → 19 files: the org page itself, `organizations/index.md`,
  `organizations/the-north-america-taiwanese-students-association-tsa-na.md`
  (same-kind club reference line only), `people/janice-wong.md` (Emory piano-faculty
  note linking both Emory club pages), `sources/taiwaneseamericanhistory-org.md`
  (directory listing wikilink), the org JSON above,
  `knowledge/research/taiwanjustice-net-priority-lexicon.json`,
  `knowledge/operational/ee-vault-index.v1–v5.json` and
  `knowledge/operational/content-analysis/2026-08-{17,21,22,23},2026-10-{23,24,25}.jsonl`
  — the latter are machine indexes, not sources. No narrative club record.
- `emory.tsa` → 2 files: the org page and the org JSON (handle known only from the
  self-report).
- `emory-tsa` → same set as `Emory TSA` (registry/slug rows only).
- `台灣學生會` → 88 files, all other campuses' TSA pages, works pages, taiwanjustice-net
  articles, and machine indexes; none names an Emory 台灣學生會 beyond this record.
- `emory` (case-insensitive) over `knowledge/web-archives/taiwaneseamericanhistory-org/posts`
  → ~40 files, all substring false positives ("in Memory of", "Flash Memory Summit",
  "Memory and Identity") or university-geography mentions in unrelated Who's Who /
  memoir records; re-checked 2026-11-14 and consistent with the 2026-10-07/10-09
  page-level re-verification notes. No Emory TSA club material.
