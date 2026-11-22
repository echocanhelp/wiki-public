---
title: "TAH Who's Who profile capture — 2292. William Shu 許子祥"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2292. William Shu 許子祥

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved because the biographical
fields are self-reported and the live site is editable, and because this is the
**only** source on this box for this person — no memoir, article, or community record
elsewhere in the corpus names him (see Twin & cross-check below).

## Subject
- [[people/william-shu|William Shu 許子祥]] — TAH Who's Who record #2292

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/william-shu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/william-shu/](https://taiwaneseamericanhistory.org/person/william-shu/)
- **Record id:** 74784 · **type:** `tah_person` · **profession taxonomy:** `entrepreneur` (`person_profession-entrepreneur` in `class_list`; numeric term id `person_profession: [2241]` — no taxonomy name→id map is archived on this box, so the class-list slug is the readable form)
- **`modified` on source:** 2026-06-19T17:04:21 · `page_bytes`: 53,520 (raw HTML; `page_text` in the JSON is the trafilatura-extracted text — the site chrome and the `Last updated: June 19, 2026` line sit inside the rendered content block, between the `Who's Who Taiwanese American Profile` marker and the `Travel the roads paved…` footer line)
- **Verbatim fields (self-reported):** Name `許子祥` / `William Shu` · Birth Year `1979` · Birth Place `Connecticut, USA`
- **U.S. arrival:** `-/-/-` — first year, first city and state unfilled on the record (consistent with US-born; the record itself does not say so)
- **Address:** `United Kingdom` — the footer block restates it as `Residence: United Kingdom`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three fields present and blank; JSON parses this as `family: []`, `family_filled: false`. Absence evidence: no relative is named anywhere on the record.
- **Education (2 rows):** `1. Northwestern Univ.` — `2001` — `B.S.` · `2. Wharton Business School` — `2010-2012` — `MBA` (the footer block restates the Wharton degree as `MBA (2012)`; the printed form is quoted as-is)
- **Employment (3 rows):** `1. S.A.C. Capital Advisors` — `-` — `Analyst` · `2. Morgan Stanley in New York City` — `2001` — `Investment banking analyst` · `3. Deliveroo` — `2013-present` — `Co-founder and CEO`
- **Accomplishment / Publication / Hobby:** `--` — unfilled. The three unfilled fields are themselves the record: no award, publication, or hobby fact is being withheld elsewhere on this capture.
- **No `Source from <org>` provenance line:** unlike sibling records (e.g. abby-hong's `Source from 美洲台灣日報…`), this record carries no upstream-source attribution, so no external article can be traced from it.
- **No website/blog field value** on the record — unlike howard-shu's capture, there is no self-reported external link to chase.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2292-william-shu.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2292-william-shu/](https://taiwaneseamericanhistory.org/whos-who-2292-william-shu/)
- **Title:** `2292. William Shu 許子祥` · **published:** 2020-11-18 (per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 67260) · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-2292-william-shu|TAH #2292]], `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Birth Year, Birth Place, Address, Family, Education, Employment, blank Accomplishment/Publication/Hobby). It is a second rendering of the same self-reported payload, not an independent source.

## Twin & containment check (2026-11-14)
Run per the profile-content-block rule (slice `page_text` from `Who's Who Taiwanese American
Profile` to `Travel the roads paved`, strip `#`/whitespace, then md5 + both containment
directions):
- profile content block: 819 normalized chars, md5 `11d819a41b11d630a441405424926977`
- post dump (frontmatter-stripped body): 486 normalized chars, md5 `cec2647183e0f3934dd69f231af24604`
- containment: neither direction is a substring — the profile block carries the **footer
  summary restatement** (`Residence: United Kingdom`, `MBA (2012)`, `Deliveroo Co-founder and
  CEO (2013-)`) that the dump omits; the dump is the pure form-field serialization.
- Field-level diff: every value in the dump appears verbatim in the profile block; the only
  deltas are the footer restatements and their year normalizations (`2010-2012` → `(2012)`).
- **Ruling:** one self-reported record rendered twice by one editable publisher, not two
  independent records. Agreement across the two serializations is **not** corroboration,
  which is why the dated career rows stay `alleged` on the subject page.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`).
- The profile's own `modified` stamp (2026-06-19T17:04:21) predates the harvest, so the capture is consistent with the record as published at fetch time.

## Whole-vault sweep (2026-11-14)
Single-pattern `grep -rlF` per name form over `content/` + `knowledge/`, machine indexes
(`units.jsonl`, `posts/index.jsonl`, `ee-vault-index*`, `content-analysis/*.jsonl`) excluded:
- `許子祥` → own page + own two captures + `content/sources/taiwaneseamericanhistory-org.md`
  (roster line 2170) + `knowledge/web-archives/taiwaneseamericanhistory-org/pages/whoswho.md`
  (directory listing line 38) + machine indexes (`tdm-page-title-index.json`,
  `taiwanjustice-net-priority-lexicon.json`) + the family-scan extract
  `knowledge/research/taiwaneseamericanhistory-org-family.json` (re-serializes Capture 1's
  `family: []` / `family_filled: false` — same payload, not a new source).
- `William Shu` → same set.
- `Deliveroo` → **zero hits** corpus-wide outside the two captures.
- `Delivery Hero` → only `knowledge/operational/news-wire.jsonl` (machine news feed, not a
  source), and it concerns the company, not the subject.
No memoir, no third-party article, no community roster outside TAH's own directory names this person.

## What this capture does NOT establish
- Whether he is US-born by self-declaration or inference — the record only leaves the U.S.-arrival
  fields blank (`-/-/-`) while printing `Birth Place: Connecticut, USA`; it never says 出生/immigrated.
- Any date for the S.A.C. Capital Advisors analyst row (`-` on the record) and whether it precedes
  or follows the 2001 Morgan Stanley row is unstated.
- `Deliveroo` `2013-present` is self-reported; no company-side or press record of the co-founder
  title is archived on this box (`Deliveroo` has zero corpus hits), so it stays `alleged`.
- No spouse/children names (fields present, blank); no family facts at all.
- Whether the residence `United Kingdom` is current as of the lint date — the only dated anchor
  is the record's own `modified` 2026-06-19 edit stamp, not a residence date.
- The TAH band-B #2292 entry carries no prose beyond the form fields — there is no narrative
  sentence in the whole corpus about this person.

## Related
- [[people/william-shu|William Shu 許子祥]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-2292-william-shu|2292. William Shu 許子祥]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
