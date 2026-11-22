---
title: "TAH directory capture — Taiwanese Student Association at CU (Boulder TSA)"
type: source
tags:
  - source
  - tah-foundation
verification_status: verified
last_reviewed: 2026-11-14
---
# TAH directory capture — Taiwanese Student Association at CU (Boulder TSA)

Capture page for the FLOOR-ANCHOR pass on [[organizations/taiwanese-student-association-at-cu]] (card t_194ee670, 2026-11-14). Archives what was harvested and what was checked-and-empty, so the next pass does not re-grep.

## Harvested artifact
- `knowledge/web-archives/taiwaneseamericanhistory-org/organization/taiwanese-student-association-at-cu.json` — TAH crawl capture, record id **77595**, `type: tah_organization`, `modified: 2026-06-09T17:23:25`, `class_list` includes `organization_type-student`, `person_profession: []`, `excerpt: None`. On-disk capture mtime 2026-08-17 00:45 PT, 1,571 bytes. Live URL: https://taiwaneseamericanhistory.org/organization/taiwanese-student-association-at-cu/
- Facts lifted (all `alleged`, one editable record): recognized student organization at the University of Colorado Boulder serving students with ties to Taiwan; Chinese name 科羅拉多大學波德分校台灣學生會 appears on its Instagram profile (@cuboulder.tsa); listing on the university's official AAPI Heritage Month page (colorado.edu/studentlife/aapi) alongside other cultural and international student organizations; BuffConnect campus engagement platform recognized-student-organization listing; Facebook group facebook.com/groups/TsaAtCuBoulder; **Instagram account had 75 followers and 6 posts at research time — the org page previously carried only content_html ¶1 and omitted this entire ¶2**; the record's own negatives: no dedicated website, mission statement, or founding year confirmed from first-party sources.

## Twin / containment check
- Sibling artifact `…/organization/chinese-and-taiwanese-student-association.json` (id **77596**, same batch `modified` 2026-06-09T17:23:25, same `organization_type-student` tag, CATSA @bouldercatsa) is a **different organization** on the same campus.
- `content_html` containment test on tag-stripped/whitespace-folded text: TSA (933 chars) in CATSA (948) = **False**; CATSA in TSA = **False**. md5s differ (4dfa1c99… vs e1c0bf89…). Two separate records authored in the same TAH batch — same-batch authorship is **not** corroboration; neither page corroborates the other.
- ¶1 of the capture JSON is already verbatim on the org page (containment True); ¶2 was absent and is the harvest of this pass.
- Single editable self-report: every absorbed row stays `alleged` (restatement ≠ corroboration).

## Checked and empty (whole-corpus sweeps, 2026-11-14, `grep -rlF` / `grep -rliF` per form over `content/` + `knowledge/`, machine indexes excluded)
- `cuboulder.tsa` → 4 files: this org page, [[organizations/chinese-and-taiwanese-student-association]] (disambiguation note), [[sources/catsa-tah-directory-capture]] (twin ruling), own capture JSON.
- `TsaAtCuBoulder` → 2 files: [[sources/catsa-tah-directory-capture]] + own capture JSON (¶2 was never rendered on any page before this pass).
- `Taiwanese Student Association at CU` → this org page, CATSA org page, `organizations/index.md`, `sources/taiwaneseamericanhistory-org.md` (directory listings), own capture JSON + machine indexes (`taiwanjustice-net-priority-lexicon.json`, `ee-vault-index.v*`, `content-analysis/*.jsonl` — indexes, not sources).
- `科羅拉多大學波德分校台灣學生會` → this org page + own capture JSON only.
- `Boulder`/波德 across `content/works` + `content/articles` + `knowledge/web-archives`: taiwanjustice news wires (2021/2025 Boulder shooting, Bezos/Blue Origin, relocation stories — no TSA mention); May Flower 1969 Ft. Collins origin (ourjourneys76, already cross-referenced as Colorado context, not this club); ourjourneys58 TAA state rosters/distribution counts (Colorado 50 members, no CU TSA); ourjourneys37 Voice of Taiwan line reaching Colorado; Pew Taiwanese American statement roster (LiShin Chiu, TAA Colorado chapter). None names a CU Boulder student association.
- Prior deepen-x SKIP stamps 2026-09-22 → 2026-10-04 (slices 09220800-31 / 09240400-13 / 09250800-29 / 09300321-9) stand; this pass extends the sweep beyond their works+articles scope to all of `content/` + `knowledge/`.
- Online arms (wikipedia/維基/wikidata/官網/華文 press): see `## Online arms` on the org page; all four accounted, none yielded an independent source from this box.
