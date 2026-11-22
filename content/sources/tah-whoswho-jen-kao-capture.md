---
title: "TAH Who's Who profile capture — 176. Jen Kao 高嘉旎"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-13
---
# TAH Who's Who profile capture — 176. Jen Kao 高嘉旎

Primary capture of the subject's own self-reported TAH Foundation Who's Who record, archived
on this box as two distinct artifacts. Preserved because the biographical fields are
self-reported and the live site is editable, and because this is the **only** source on this
box for this person — no memoir, article, church, org, or event record elsewhere in the
corpus names her (see Twin & cross-check below).

## Subject
- [[people/jen-kao|Jen Kao 高嘉旎]] — TAH Who's Who record #176

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/jen-kao.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/jen-kao/](https://taiwaneseamericanhistory.org/person/jen-kao/)
- **Record id:** 72757 · **type:** `tah_person` · **profession taxonomy:** `artist`, `designer`
  (`person_profession-artist` / `person_profession-designer` in `class_list`; numeric term ids
  `person_profession: [2226, 1299]` — no taxonomy name→id map is archived on this box, so the
  class-list slugs are the readable form)
- **`modified` on source:** 2026-06-02T17:16:39 · `page_bytes`: 54,257 (raw HTML; `page_text`
  in the JSON is the trafilatura-extracted text — the site chrome and the
  `Last updated: June 2, 2026` line sit in the raw HTML, not the extracted text)
- **`content_html` and `excerpt` are empty** (`""`): the harvest captured no post body, only
  the rendered form fields in `page_text`. This is why the harvest grader marked the profile
  weak (see Harvest provenance).
- **Verbatim fields (self-reported):** Name `高嘉旎` / `Jen Kao` · Birth Year `1981` ·
  Birth Place `Los Angeles, CA`
- **U.S. arrival:** the field is absent from this record entirely (unlike sibling records which
  carry a `First year, first city and state in the U.S.` line) — nothing was ever filled.
- **Address:** `New York, NY` — the site's footer block restates it as `Residence: New York, NY`
- **Family:** `1.Husband:` · `2.Daughter:` · `3.Son:` · `4.Parents: Father 高民環Min Kao,
  Mother Yu-Fan Kao` — the JSON parses this as `family: []`, `family_filled: false`, i.e. the
  harvester treated the whole block as unfilled even though the parents line is populated. The
  spouse and children fields are present and blank; father and mother are the only named
  relatives.
- **Education (2 rows, no year ranges):** `1. New York University` — `B.A. Studio Art` ·
  `2. Parsons School of Design` — `M.A.`
- **Employment (1 row, no year range):** `Fashion designer`
- **Accomplishment (3 rows):**
  `1. Being inducted into the Council of Fashion Designers of America (CFDA), 2011` ·
  `2. Recipient of Vogue Talents Corner, 2011` ·
  `3. Recipient of Harvard Leadership in the Arts Award and the Stacy Nipps Alumni Award from
  Parsons, 2012`
- **Publication / Hobby:** blank — unfilled. The two unfilled fields are themselves the record:
  no publication or hobby fact is being withheld elsewhere on this capture.
- **Website:** [http://www.jenkao.com](http://www.jenkao.com) — self-reported; **not archived on
  this box**, so the live personal site is not verified against our capture.
- **Footer summary block (same page, rendered below the form):** Hanzi `高嘉旎` · Birth Year
  `1981` · Birthplace `Los Angeles, CA` · Residence `New York, NY` · Education
  `New York University — B.A. Studio Art` / `Parsons School of Design — M.A.` · Position
  `Fashion designer`, plus a `Notable Accomplishments` restatement of the three award rows.
  Restatement within one capture is not corroboration.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/176-jen-kao.md`
- **Original:** [https://taiwaneseamericanhistory.org/176-jen-kao/](https://taiwaneseamericanhistory.org/176-jen-kao/)
- **Title:** `176. Jen Kao` · **published:** 2014-12-28 (per
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`, post id 7913) ·
  vault work record: [[works/taiwaneseamericanhistory-org/176-jen-kao|TAH #176]],
  `value_band: B`
- The dump reproduces the Capture 1 form fields verbatim (Birth Year, Birth Place, Address,
  Family incl. the parents line, Education, Employment, the three Accomplishment rows, blank
  Publication/Hobby, the jenkao.com website line). It is a second rendering of the same
  self-reported payload, not an independent source.

## Cross-record corroboration — the father's record
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/min-kao.json` (record id
  72710, `modified` 2026-07-02T12:10:58) and its dump
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-min-kao.md`
  ([[people/min-kao|Dr. Min Kao 高民環博士]]).
- That record's `family` parses as `[{rel: wife, name: 趙郁芬}, {rel: daughter, name: 高嘉旎},
  {rel: son, name: 高凱麟}]`, `family_filled: true`. Her name appears there in the CJK form
  `高嘉旎`; her mother's name `趙郁芬` appears only there.
- **Directional check:** her own record names `Mother Yu-Fan Kao`; his record names wife
  `趙郁芬`. The two editable records agree on the *relationship* (she is his daughter) but no
  record on this box states that `Yu-Fan Kao` and `趙郁芬` are the same person — the romanized
  form is not pinned to the hanzi by any archived source.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org
  recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json`
  (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org).
- This slug appears in that manifest's `weak.person` list, i.e. the harvest grader marked this
  profile's payload thin at fetch time — consistent with the empty `content_html`/`excerpt` and
  the blank Publication/Hobby fields above.

## Twin & cross-check (2026-11-13)
Whole-vault sweep this pass — single-pattern `grep -rlF` / `grep -rliF` per name form, controls
counted: `高嘉旎` → 4 files in `content/`, and outside `content/` only the two TAH captures,
`knowledge/research/taiwaneseamericanhistory-org-family.json`, and crawler/analysis indexes
(`ee-vault-index.v1–v5.json`, `content-analysis/*.jsonl`, `tdm-page-title-index.json`,
`taiwanjustice-net-priority-lexicon.json`); `Jen Kao` → 4 / same set plus
`knowledge/research/taiwaneseamericanhistory-org/units.jsonl` and `posts/index.jsonl`.
Every non-index hit is one of: her own two TAH captures, the
[[works/taiwaneseamericanhistory-org/176-jen-kao|TAH #176]] work page, `people/index.md`, the
[[sources/taiwaneseamericanhistory-org|source hub]], `people/min-kao.md` (father's page, family
field), or the indexes above. `高凱麟` (brother) → only `people/min-kao.md`, the family index,
and the min-kao captures. `CFDA` / `Vogue Talents` / `jenkao.com` appear on this box **only** in
her two captures. **No memoir (《Our Journeys》 / My Stories), taiwandaily/TJJ article, church,
org, or event record names her.** The 2014-12-28 publication date of #176 is the closest thing
the corpus carries to a "first recorded" timestamp.

**Near-miss checked and excluded:** `knowledge/web-archives/taiwaneseamerican-org/asian-americans-climb-fashion-industry-ladder.md`
(a 2010-09-04 Eric Wilson NYT piece mirrored by TAH) matched a `Council of Fashion Designers`
grep and is a fashion-industry article — but the subject **does not appear in it**. It names
Jason Wu, Richard Chai, Alexander Wang, Thakoon, Prabal Gurung, Phillip Lim, Derek Lam, Anna
Sui, Vera Wang, Peter Som, Carmen Chen Wu. No Kao/高嘉旎. Not a source for this page.

**Namesake control:** `高嘉` hits in taiwanjustice articles are 高嘉瑜 (ROC legislator), an
unrelated namesake — confirmed again this pass, no co-occurrence with 高嘉旎 or Jen Kao.

**Twin check (the two artifacts are NOT byte-identical, and neither contains the other):**
normalized body md5 after stripping frontmatter and all `#`/whitespace — Capture 1 `page_text` =
`029ce60cf7ed4045ac12c744d97a779b` (1,562 chars), Capture 2 dump =
`f686423ad39d0fe765b73b159da1b62d` (501 chars); containment tested both directions, `False`
either way. Capture 1 is a superset in *content* (site chrome, `Last updated: June 2, 2026`
line, the profession taxonomy classes, the footer summary block and the `Notable
Accomplishments` restatement), differing in *serialization*. The form fields they share are one
payload, so shared fields are **not** corroboration of each other, and the record's own
`Accomplishment` rows are restated within the same editable page — restatement is not
corroboration.

## What this capture does NOT establish
- No U.S. arrival year/city (the field is absent from this record), and no dates for the
  degrees — no years for NYU or Parsons.
- Whether `Fashion designer` is current: no `present` marker; `modified` 2026-06-02 is an edit
  timestamp, not a career date.
- No spouse or children names (fields present, blank).
- **No independent verification of any of the three 2011–2012 honors.** CFDA induction, Vogue
  Talents Corner, and the Harvard Leadership in the Arts / Stacy Nipps Parsons awards appear on
  this box only in this one editable self-report, restated in its own footer block. No CFDA,
  Vogue, Harvard, or Parsons record is archived here, and the self-reported jenkao.com site is
  not captured.
- The mother's name exists in two non-linking forms — `Yu-Fan Kao` (her record) vs `趙郁芬`
  (father's record) — with no archived source pinning the romanization to the hanzi.
- The brother `高凱麟` and the parents have no page or third-party record in the corpus.

## Related
- [[people/jen-kao|Jen Kao 高嘉旎]] — subject page fed by this capture
- [[people/min-kao|Dr. Min Kao 高民環博士]] — father's record, corroborates the daughter relation
- [[works/taiwaneseamericanhistory-org/176-jen-kao|176. Jen Kao]] — vault work record
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher

## Absorb verification 2026-11-16
- sourced 2026-11-16: re-ran twin check — page_text md5 `029ce60cf7ed4045ac12c744d97a779b` and dump md5 `f686423ad39d0fe765b73b159da1b62d` re-hashed from knowledge/web-archives/taiwaneseamericanhistory-org/person/jen-kao.json and posts/176-jen-kao.md; both match the 2026-11-13 strings 「逐字一致」.
- sourced 2026-11-16: whole-corpus sweep re-run on this box — grep -rlF 「高嘉旎」 and "Jen Kao" return only her own two captures, the family index, and crawler/analysis indexes; zero memoir, taiwandaily/TJJ, church, org, or event hits outside knowledge/web-archives/taiwaneseamericanhistory-org.
- sourced 2026-11-16: CFDA / Vogue Talents / jenkao.com grep returned 0 files outside the subject's own two captures in knowledge/web-archives/taiwaneseamericanhistory-org — the three 2011–2012 honors remain single-self-report, verified absent of corroboration.
- sourced 2026-11-16: brother 「高凱麟」 and mother forms 「Yu-Fan Kao」/「趙郁芬」 re-grepped — hits only in knowledge/web-archives/taiwaneseamericanhistory-org/person/min-kao.json and posts/whos-min-kao.md (father's record), per [[people/jen-kao]] and [[people/min-kao]].
