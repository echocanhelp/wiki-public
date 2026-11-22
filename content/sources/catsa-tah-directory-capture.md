---
title: "TAH directory capture — Chinese and Taiwanese Student Association (CATSA)"
type: source
tags:
  - source
  - tah-foundation
verification_status: verified
last_reviewed: 2026-11-14
---
# TAH directory capture — Chinese and Taiwanese Student Association (CATSA)

Capture page for the FLOOR-ANCHOR pass on [[organizations/chinese-and-taiwanese-student-association]] (card t_011b55b4, 2026-11-14). Archives what was harvested and what was checked-and-empty, so the next pass does not re-grep.

## Harvested artifact
- `knowledge/web-archives/taiwaneseamericanhistory-org/organization/chinese-and-taiwanese-student-association.json` — TAH crawl capture, record id **77596**, `type: tah_organization`, `modified: 2026-06-09T17:23:25`, `class_list` includes `organization_type-student`, `person_profession: []`, `excerpt: None`. Live URL: https://taiwaneseamericanhistory.org/organization/chinese-and-taiwanese-student-association/
- Facts lifted (all `alleged`, one editable record): recognized student organization at University of Colorado Boulder for students of Chinese and Taiwanese backgrounds; listing on the university's official AAPI Heritage Month page (colorado.edu/studentlife/aapi) under its full name; BuffConnect campus events listing alongside other CU Boulder cultural organizations; Instagram handle **@bouldercatsa** exists and is consistent with the CATSA abbreviation, but the public profile returned **no bio text or additional detail at the time of research**; **no dedicated website, mission statement, founding year, or Facebook page could be confirmed from first-party sources**; CATSA is explicitly stated to be a **distinct organization** from the separately listed Taiwanese Student Association at CU.

## Twin / containment check
- Sibling artifact `…/organization/taiwanese-student-association-at-cu.json` (id **77595**, same batch `modified` 2026-06-09T17:23:25, same `organization_type-student` tag) is a **different organization** (TSA, @cuboulder.tsa, Facebook group TsaAtCuBoulder).
- `content_html` containment test: CATSA (1,033 chars) in TSA (1,018 chars) = **False**; TSA in CATSA = **False**. md5s differ (87e11e02… vs 7a03a853…). Two separate records authored in the same TAH batch — same-batch authorship is **not** corroboration; neither page corroborates the other.
- Absence evidence inside the record itself: `excerpt: None`, `person_profession: []`, and the record's own negatives (no website / mission statement / founding year / Facebook; empty Instagram bio) — printed as dated `## From the record` rows on the org page.

## Checked and empty (whole-corpus sweeps, 2026-11-14, `grep -rlF` per form over `content/` + `knowledge/`, machine indexes excluded)
- `Chinese and Taiwanese Student Association` → 6 files: org page, `content/organizations/index.md`, `content/sources/taiwaneseamericanhistory-org.md` (directory listings), `knowledge/research/taiwanjustice-net-priority-lexicon.json` + `knowledge/operational/intelligence/connector-suggestions.json` (machine indexes, not sources), and the capture JSON itself. No press/memoir hit.
- `CATSA` → 2 files: org page + capture JSON.
- `bouldercatsa` → 1 file: capture JSON only.
- `Colorado Boulder` → CATSA pages + sibling TSA page + two unrelated CU-alumni whoswho pages ([[people/prof-shi-kuei-wu]], [[people/prof-frank-s-t-hsiao]] and their captures — degree bios, no org mention).
- `University of Colorado` additional people hits (chun-hsin-jenny violin degree, dr-edward-t-s-huang 2000–2004 research post, shih-han-erika-chiu bassoon TA, marlene-tseng-yu 1967 MFA) — all campus-affiliation bios; none names a Taiwanese/Chinese student association at CU. mystories278's sole Colorado mention is one daughter working as a doctor at University of Colorado Medical School (already ruled non-overlap on the org page 2026-10-01).
- 科羅拉多 hits in `content/works` + `content/articles` are TAA-Colorado chapter/newsletter records, other-campus TSA records, Colorado Hakka, and unrelated taiwanjustice news wires (2021/2025 Boulder shooting, relocation stories) — none about CATSA.
- Prior deepen-x SKIP stamps 2026-09-22 → 2026-10-09 (slices 09171300-29 / 09180400-16 / 09210906-25 / 09232232-22 / 09261405-7 / 09251054-17 / 10052158-11 / 10070717-19) stand.
- Online arms (wikipedia/維基/wikidata/官網/華文 press): see `## Online arms` on the org page; all four accounted, none yielded an independent source from this box.
