---
title: "TAH directory capture — UF Society of Taiwanese and Hong Kong Students (STAHKS)"
type: source
tags:
  - source
  - tah-foundation
verification_status: verified
last_reviewed: 2026-11-14
---
# TAH directory capture — UF Society of Taiwanese and Hong Kong Students (STAHKS)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 437
- wikilinks: 1


Capture page for the FLOOR-ANCHOR pass on [[organizations/uf-society-of-taiwanese-and-hong-kong-students]] (card t_a3d2520d, 2026-11-14). Archives what was harvested and what was checked-and-empty, so the next pass does not re-grep.

## Harvested artifact
- `knowledge/web-archives/taiwaneseamericanhistory-org/organization/uf-society-of-taiwanese-and-hong-kong-students.json` — TAH crawl capture, record id **77585**, `type: tah_organization`, `modified: 2026-06-09T17:23:24`, on-disk mtime 2026-08-17, 1,387 bytes, `class_list` includes `organization_type-student`, `excerpt: null`, `person_profession: []`. Live URL: https://taiwaneseamericanhistory.org/organization/uf-society-of-taiwanese-and-hong-kong-students/
- `content_html` carries **two** `<p>` paragraphs. The org page on disk carried **only ¶1 verbatim**; **¶2 was never absorbed** before this pass:

  > "No dedicated website, formal mission statement, or founding year has been located through first-party sources. The organization has documented officer roles, including an External Vice President position, suggesting an active organizational structure."

- Facts lifted (all `alleged`, one editable record): UF Gainesville student org; distinct from UF TWSA; focus on students of Taiwanese and Hong Kong heritage; Instagram `@ufstahks`; LinkedIn company profile under the full English name; the ¶2 negative claims (no dedicated website / mission statement / founding year located through first-party sources) and the External Vice President officer-role evidence.

## Twin / containment check
- `ls knowledge/web-archives/taiwaneseamericanhistory-org/posts/ | grep -iE 'uf-|stahks|hong-kong'` → only `4-taiwanese-writer-lecture-series-by-tuf-2015.md`, an unrelated TUF (Taiwanese American writer lecture) post. **No `posts/<slug>.md` story-corpus twin exists for this org** — the record is one editable self-report rendered once, so every row stays `alleged`.
- Same-batch sibling `…/organization/uf-taiwanese-student-association.json` (UF TWSA, mtime 2026-08-17, same crawl batch) shares only the University of Florida venue; `content_html` differs in both directions (no containment) → a distinct organization record, and it is the very org this page disambiguates *from*. NOT corroboration for STAHKS facts; same-batch authorship is not corroboration.
- Directory-page check: `grep -rl 'Society of Taiwanese and Hong Kong' knowledge/web-archives/taiwaneseamericanhistory-org/pages/` → zero hits (the numbered directory pages do not list this org).

## Checked and empty (whole-corpus sweeps, 2026-11-14, `grep -rlF`/`-rliF` per form over `content/` + `knowledge/`)
- `STAHKS` (case-sensitive) → 2 files: this org page + own capture JSON.
- `Society of Taiwanese and Hong Kong` → org page + `content/organizations/index.md` + `content/sources/taiwaneseamericanhistory-org.md` (listing pages) + `knowledge/research/taiwanjustice-net-priority-lexicon.json` (machine index, not a source) + own capture JSON.
- `UF Society` → same five files as above; no additional hit.
- `ufstahks` → 2 files: org page + own capture JSON.
- Florida/Gainesville mentions in the corpus are unrelated (黃碩文 UF lifetime-achievement award, South-FL chapter items) — consistent with the prior deepen-x SKIP stamps 2026-09-21 → 2026-10-09, which all grepped only `works/`+`articles/`+`sources/`+`events/`+`topics/`.
- Online arms (wikipedia/wikidata/官網/華文 press): see `## Online arms` on the org page; all four accounted, none yielded an independent source from this box.
