---
title: "TAH Who's Who profile capture — 1521. W. S. Chen 陳務憲 / 2017-02"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1521. W. S. Chen 陳務憲 / 2017-02

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 905
- wikilinks: 3


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two artifacts. This is the **only** citable source on this box
for this person — see Whole-corpus sweep below. The record carries an upstream
provenance line (`Source from 台灣公論報1554期 1997/05`), but that newspaper issue is
**not** archived on this box, so it is a citation, not a second source.

## Subject
- [[people/w-s-chen|W. S. Chen 陳務憲]] — TAH Who's Who record #1521 (published 2017-02-19)
- **Do not merge** with W. S. Chen 陳文祥 (record #1658,
  [[works/taiwaneseamericanhistory-org/whoswho1658|1658. W. S. Chen 陳文祥 / 2017-05]]) —
  a different person sharing the same English initials. 陳文祥 has no `people/` dossier on
  this box yet (verified 2026-11-14: `grep -l '陳文祥' content/people/*.md` returns only this
  subject's page, which names him solely as the do-not-merge note), so no wikilink target exists.

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/w-s-chen.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/w-s-chen/](https://taiwaneseamericanhistory.org/person/w-s-chen/)
- **Record id:** 74050 · **type:** `tah_person` · **on-disk mtime:** 2026-10-08 (capture date)
- **Profession taxonomy (`class_list`):** `person_profession-chemical-engineer`,
  `person_profession-community-leader`, `person_profession-engineer` (numeric term ids
  `person_profession: [270, 2242, 2227]`; no taxonomy name→id map is archived on this box,
  so the class-list slugs are the readable form). **Label-inflation note:** the `sidecar`
  records only `roles: ['engineer']` — the site taxonomy carries two further tags,
  `chemical-engineer` and `community-leader`, that the sidecar drops.
- **`modified` on source:** `2026-06-19T16:51:09` · **`page_bytes`:** 52,823
- **`content_html` is empty** and **`excerpt` is empty** — the profile carries no free-text
  biography beyond the form fields; the form fields below are the whole payload.
- **Verbatim form fields (self-reported):** Name `陳務憲` / `W. S. Chen` · Birth Year `--`
  · Birth Place `台灣` · First year, first city and state arrived in the U.S. `-/-/-`
  (all arrival fields blank) · Address `Baton Rouge / LA`
- **Family:** `1. Wife: 張淑花` · `2.Son: 陳彥豪` · `3.Son: --` — parsed as
  `family: [{rel: wife, name: 張淑花}, {rel: son, name: 陳彥豪}]`, `family_filled: true`.
- **Education:** `1.台灣大學` — `B.S.化工` (no year range)
- **Employment:** `Mansanto Chemical Co` — `--` / `--` (title and dates blank).
  The employer string is the site's own; the chemical spelling `Mansanto` (not `Monsanto`)
  is reproduced verbatim from the record and is **not** corrected here.
- **Accomplishment:** `Baton Rouge, Louisiana台灣同鄉會會長` (President of the Baton Rouge,
  Louisiana Taiwanese Association) — the only community-role fact on the record.
  **Not** in the sidecar and **not** on the pre-2026-11-14 Echopedia page.
- **Publication (Non-professional ones):** `--` · **Hobby:** `--` · **Website or Blog:** `--`
  (three blank fields = absence evidence that no further field-level material is withheld)
- **Provenance line:** `Source from 台灣公論報1554期 1997/05` — the submitter's own
  attribution of the profile content to 台灣公論報 issue #1554, May 1997. The paper itself
  is not in the vault (see sweep), so every field stays `alleged`.
- **Footer restatement block (same page, rendered below the form):** Hanzi `陳務憲` ·
  Birthplace `台灣` · Residence `Baton Rouge, LA` · Education `台灣大學 / B.S. 化工` ·
  Position `Mansanto Chemical Co` · Community `Baton Rouge, Louisiana 台灣同鄉會 / 會長`.
  Restatement inside one capture is not corroboration.
- **Site-rendered `Last updated:` line:** `June 19, 2026` — matches `modified`, i.e. the
  record was re-saved on 2026-06-19, months after the 2017-02 publication of #1521.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1521.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1521/](https://taiwaneseamericanhistory.org/whoswho1521/)
- **Work page:** [[works/taiwaneseamericanhistory-org/whoswho1521|1521. W. S. Chen 陳務憲 / 2017-02]]
- Content: the same form fields, rendered as the published encyclopedia entry, ending with
  `### Source from 台灣公論報1554期 1997/05`. No extra biographical field.

## Twin & containment check (run 2026-11-14)
Both artifacts serialize **one editable self-report**, rendered twice. Test performed on the
profile page's own CONTENT BLOCK (sliced from the `Who's Who Taiwanese American Profile`
marker to the `Travel the roads paved by those who came before us.` footer line), not the raw
`page_text` (which carries ~1 KB of site chrome the dump lacks).
- Normalization: frontmatter stripped, all `#` and whitespace stripped, case-folded.
- **Result:** the dump's field set is a strict subset of the profile content block. The
  profile is the **richer** artifact — it alone carries the `modified` timestamp
  (`2026-06-19T16:51:09`), `page_bytes` (52,823), the 3-tag `class_list` taxonomy, and the
  `sidecar`/`family` structured parse. The dump adds nothing except its own URL identity.
- **Ruling:** two serializations of one self-report are **not** two corroborating sources.
  The upstream print citation (`台灣公論報1554期 1997/05`) is restated by the same submitter
  inside both artifacts, so it stays `alleged` until the newspaper issue itself is in the vault.

## Whole-corpus sweep (run 2026-11-14, supersedes the DEEPEN-X stamps)
Prior `DEEPEN-X SKIP` stamps on the person page (2026-10-02, 2026-10-07, 2026-10-08) grepped
only the five `content/` corpus dirs. This sweep covered **all of `content/` + `knowledge/`**,
single-pattern `-F` per name form:
- `grep -rlF '陳務憲' content knowledge` → **15 files**
- `grep -rliF 'W. S. Chen' content knowledge` → **17 files**
- Classification of every hit: the subject's own artifacts (`content/people/w-s-chen.md`,
  `content/works/.../whoswho1521.md`, both crawl captures, `content/sources/taiwaneseamericanhistory-org.md`);
  the **distinct same-initials person** 陳文祥 record #1658 and its dump (excluded — different person);
  and machine indexes (`knowledge/research/taiwaneseamericanhistory-org/units.jsonl`,
  `knowledge/research/tdm-page-title-index.json`,
  `knowledge/research/taiwanjustice-net-priority-lexicon.json`,
  `knowledge/research/taiwaneseamericanhistory-org-family.json`,
  `knowledge/operational/ee-vault-index.v1–v5.json`,
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl`).
- **Zero** hits in `knowledge/web-archives/*/posts/mystoriesNNN.md` memoirs, oral histories,
  or community/newsletter rosters. No 台灣公論報 1997/05 issue is archived on this box.
- Machine indexes are not sources; the same-initials record is not this person.
- **Verdict:** no third-party citable source for 陳務憲 exists on this box beyond the TAH
  self-report and its print provenance citation.
