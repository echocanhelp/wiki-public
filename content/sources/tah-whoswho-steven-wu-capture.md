---
title: "TAH Who's Who profile capture — 1619. Steven Wu 巫石增"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1619. Steven Wu 巫石增

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 786
- wikilinks: 4


Capture of the TAH Foundation Who's Who record titled **Steven Wu 巫石增** — a record that
shares the English name with the [[people/steven-wu|Taiwan Center 團體董事 Steven Wu (吳尚誠)]]
but carries a different Chinese name. This page exists so the identity-collision evidence is
archived, dated, and citable without polluting either biography.

## Subject
- Record title: `Steven Wu 巫石增` (TAH record id 74140 / story #1619)
- Board-entry counterpart under investigation: [[people/steven-wu|Steven Wu (吳尚誠)]], 團體董事 of
  [[organizations/taiwan-center|Taiwan Center]] — Chinese name **does not match** 巫石增

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/steven-wu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/steven-wu/](https://taiwaneseamericanhistory.org/person/steven-wu/)
- **Record id:** 74140 · **type:** `tah_person` · **page_bytes:** 55,683 · **`modified`:** 2026-06-19T16:52:46
- **`person_profession` taxonomy (5 tags):** aerospace engineer · community leader · electrical engineer · engineer · scientist (ids 2254, 2242, 323, 2227, 2235)
- **`sidecar.roles` drops 3 of the 5 taxonomy tags** — sidecar keeps only `engineer`, `scientist`;
  `aerospace engineer`, `electrical engineer`, `community leader` appear only in `class_list`/rendered page.
  Label-inflation proof: the taxonomy is richer than the machine summary.
- **Verbatim self-reported fields:** Name 巫石增 博士 / Dr. Steven Wu · Birth Year `-1998` · Birth Place 台灣 ·
  arrived US `1966/-/-` · Address Huntsville/AL
- **Family:** 1. Wife: 秀妹 · 2. Daughter ??? · 3. Son ??? · `family_filled: false`
- **Education:** 1. 台北工專 — B.S. · 2. University of Kansas — Ph.D. 電機工程
- **Employment (4 entries, all date/position fields withheld by the self-reporter):**
  1. Kansas Black & Votech Consulting Firm (Year-Year???, Position???) · 2. NASA Johnson Space Center (???) ·
  3. NASA John Stennis Center (???) · 4. NASA Marshall Space Flight Center
- **Accomplishment:** 1. FAPA阿拉巴馬州分會首任會長, 1994 · 2. Huntsville台灣同鄉會會長, 1995
- **Publication (non-professional):** `–` · **Hobby:** `–` · **Website or Blog:** `–` (blank-field roster: no crown fact withheld)
- **Print submission provenance printed by the record itself:** `Source from 台灣公論報第1626期 02/1998`
- **Rendered sidecar block appends a dated death field:** `Passed Away 1998` — which is what makes the
  self-reported `Birth Year` field read `-1998` (a form-entry artifact, NOT a birth year)

## Capture 2 — Who's Who encyclopedia dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/1619-steven-wu-%e5%b7%ab%e7%9f%b3%e5%a2%9e-201704.md`
- **Original:** [https://taiwaneseamericanhistory.org/1619-steven-wu-%e5%b7%ab%e7%9f%b3%e5%a2%9e-201704/](https://taiwaneseamericanhistory.org/1619-steven-wu-%e5%b7%ab%e7%9f%b3%e5%a2%9e-201704/)
- **Title:** `1619. Steven Wu 巫石增 / 2017/04` — field set identical to Capture 1, same
  `Source from 台灣公論報第1626期02/1998` footer

## Twin check (Capture 1 vs Capture 2)
- Normalization: frontmatter stripped, `#`/whitespace removed. Capture 1 `page_text` 2,062 raw chars
  (site chrome + sidecar block + footer); Capture 2 body 662 raw chars (form fields only,
  heading-padded). Containment test: Capture 2's field set is a **substring-equivalent of Capture 1's
  form section** — Capture 1 is the RICH artifact (adds the rendered sidecar `Passed Away 1998` block
  and the profession taxonomy that Capture 2 omits).
- These are two serializations of **one editable self-report** on one CMS. Agreement across them is
  NOT corroboration; that is why the 台灣公論報第1626期 (02/1998) print citation stays at `alleged`
  until the paper itself is archived.

## Third-party-adjacent vault record
- The reverend's page [[people/rev-chung-hsin-cho|Rev. Chung Hsin Cho 卓忠信]] records that his own Who's Who entry
  (#1620) was filed **the same day** as `1619. Steven Wu 巫石增` and `1618. Dr. Tom Chiu 邱崇德博士` — per
  `content/people/rev-chung-hsin-cho.md` (batch-submission context for #1619, 2017-04-23).

## What this capture does NOT establish
- It does **not** establish that 巫石增 and 吳尚誠 (Taiwan Center 團體董事) are the same person —
  the Chinese names differ and no vault record links them.
- No archived copy of 台灣公論報第1626期 (02/1998) exists on this box; the print citation is
  printed by the self-report itself.
- NASA positions and employment years were never filled in by the self-reporter (`Position???`),
  so employment is attested only at the institution-name level.
- `Birth Year -1998` is a form artifact (see `Passed Away 1998`); the real birth year is unknown.

## GAPS / NEED YOU — sources checked, 2026-11-14
Greps run (whole `content/` + `knowledge/`, controls counted, machine indexes excluded):
- `grep -rlF '吳尚誠'` → only the taiwancenter.org board cluster (board snapshot + 27 cohort stub pages + org page). No biography.
- `grep -rlF '巫石增'` → this record's own artifacts + work page #1619 + rev-chung-hsin-cho.md same-day note + machine indexes (`units.jsonl`, `posts/index.jsonl`, family json). No third-party biography.
- `grep -rli 'Steven Wu'` → same two clusters; no additional narrative hit.
- `knowledge/web-archives/taiwaneseamericanhistory-org/pages/ota.md` (Outstanding Taiwanese American roster) — no Steven Wu / 巫石增 entry.
- Not archived on this box (needed): 台灣公論報第1626期 02/1998; any NASA center directory or obituary for 巫石增;
  Wikipedia/華文 press searches for either name (see Online arms on the person page).
**NEED YOU:** if a member family holds a 巫石增 obituary (Huntsville AL, ~1998) or the Taiwan Center can confirm
whether 吳尚誠 has a NASA/Alabama background, this collision can be resolved.
