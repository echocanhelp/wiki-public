---
title: "TAH Who's Who profile capture — Prof. Elaine Hsiao (蕭夷年)"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — Prof. Elaine Hsiao (蕭夷年)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 551
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-elaine-hsiao|Prof. Elaine Hsiao 蕭夷年教授]] — TAH Who's Who profile
  (WordPress post id 73403, type `tah_person`)

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-elaine-hsiao.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-elaine-hsiao/](https://taiwaneseamericanhistory.org/person/prof-elaine-hsiao/)
- **Record id:** 73403 · **type:** `tah_person` · **profession taxonomy**
  (`person_profession-*`): educator, microbiologist, professor, researcher, scientist
- **`modified` on source:** 2026-06-19T16:39:29 (page renders "Last updated: June 19, 2026") · page size 56,415 bytes
- **Verbatim fields (self-reported):** Birth Year `--` · Birth Place USA ·
  First year/city/State in U.S. `-/-/-` · Present Address CA
- **Family:** `1. Husband: —` · `2. Daughter: —` · `3. Son: —` · `4. Father/Mother: -/-` —
  all blank; sidecar `family_filled: false`, `family: []`
- **Education:** UCLA 2006 B.S., Science · Caltech M.S. (no year) · Caltech 2012 Ph.D.
- **Employment:** UCLA, Biology and Bioengineering — Assistant Professor (Present) ·
  California Institute of Technology Biology and Bioengineering — Assistant Professor (Present)
- **Accomplishment (self-reported, verbatim list):**
  1. Assistant Prof. of Integrative Biology & Physiology UCLA
  2. Recipient of Sloan Research Fellowships 2016
  3. Recipient of The National Institutes of Health Director's Early Independence Award,
     Distinction as Forbes' 30 Under 30 in Science and Healthcare 2014
  4. Recipient of Emerging Explorer of National Geographic Magazine 2014
  5. Packard Fellow in Science & Engineer 2015
  6. Fellowships from the National Institute of Mental Health and Autism Speaks
  7. Renowned Scholar in Autism Spectrum Disorder (ASD)
  8. Outstanding Taiwanese American Elected by T.A. Archives in 02/2019
- **Publication / Hobby:** `--` in both fields (label-inflation check: no withheld
  publication or hobby content in the record)
- **`content_html` on the profile JSON is empty** — the site-rendered `page_text` is the
  only narrative layer of this capture.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-840-elaine-hsiao.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-840-elaine-hsiao/](https://taiwaneseamericanhistory.org/whos-who-840-elaine-hsiao/)
- **Title:** `840. Prof. Elaine Hsiao 蕭夷年教授`
- Field set identical to Capture 1 (same education rows, same two Present employment rows,
  the same eight `Accomplishment` items, `Publication`/`Hobby` `--`).

## Twin check (2026-11-14)
Captures 1–2 are two renderings of **one self-report record family** on
taiwaneseamericanhistory.org. The containment test was run rather than a naive md5: the
`Accomplishment` list in Capture 2 is string-identical to the `Notable Accomplishments`
render block inside Capture 1's `page_text` (Capture 1 is the richer artifact — it also
carries the `modified` stamp, the profession taxonomy, and the empty `content_html`
field). Agreement across two serializations of one editable self-report is **not
corroboration**: every `Accomplishment` fact is labeled `alleged` on the subject page.

## Other corpus hits (2026-11-14 whole-corpus sweep)
`grep -rlF '蕭夷年' content knowledge` and case-insensitive `grep -rliF 'Elaine Hsiao'` return
the identical hit set: this capture's two artifacts plus `person/prof-elaine-hsiao.md`, the
two work-entity pages [[works/taiwaneseamericanhistory-org/whos-who-840-elaine-hsiao]] and
[[works/taiwaneseamericanhistory-org/ota-264]] (same person, two TAH entries), the
`people/index.md` and `sources/taiwaneseamericanhistory-org.md` hubs, an index-listing line
in `knowledge/web-archives/taiwaneseamericanhistory-org/pages/ota.md` (roster line only),
and three machine indexes (`tdm-page-title-index.json`,
`taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`) —
indexes are not sources. **No memoir, story-corpus article, or third-party record names
her.** `posts/ota-264.md` is a header-only dump (all fields render `-`); the only
datable content on this box for this subject is the self-report record itself.
