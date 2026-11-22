---
title: "TAH Who's Who profile capture — 322. Amenda Wu 2015/03"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-16
---
# TAH Who's Who profile capture — 322. Amenda Wu 2015/03

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 955
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/amenda-wu|Amenda Wu]] — TAH Who's Who profile record id 72893 · story-corpus record #322

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/amenda-wu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/amenda-wu/](https://taiwaneseamericanhistory.org/person/amenda-wu/)
- **Record id:** 72893 · **type:** `tah_person` · **profession taxonomy:** `community leader` + `musician` (`person_profession-community-leader`, `person_profession-musician`)
- **`modified` on source:** 2026-06-02T17:17:20 · page size 52,227 bytes
- **Verbatim fields (self-reported):** Name `Amenda Wu` · 漢文名 blank · Birth Year blank · Birth Place `Bay Area, CA` · First year, first city and state in the U.S. blank · Address `CA`
- **Family:** `1. Husband:` · `2. Daughter:` · `3. Son:` — all three blank; `family_filled: false`
- **Education:** 1. UC Davis — Music
- **Employment:** 1. San Francisco Symphony — Donor relations coordinator · 2. UC Berkeley symphony Orchestra — Member
- **Accomplishment / Publication (Non-professional) / Hobby / Website or Blog:** all blank
- **Site-rendered second block** (below the table) restates the same fields: Birthplace `Bay Area, CA` · Residence `CA` · Education UC Davis Music · Position San Francisco Symphony Donor Relations Coordinator / UC Berkeley Symphony Orchestra Member — capitalized `Relations Coordinator` and normalized `symphony`→`Symphony`, i.e. a re-serialization of the same record, not a second report.
- **Sidecar diff (label-inflation check):** `sidecar.birth_year` carries the literal string `Birth Place` (a form-label leak, not a year); `sidecar.roles` is `[]` while the page's `class_list` carries two profession tags — the taxonomy drops both roles the page displays. No withheld crown fact: the rich fields (漢文名, Birth Year, Family, Accomplishment, Hobby, Website) are blank on the record itself.

## Capture 2 — story-corpus encyclopedia dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/322-amenda-wu-201503.md`
- **Original:** [https://taiwaneseamericanhistory.org/322-amenda-wu-201503/](https://taiwaneseamericanhistory.org/322-amenda-wu-201503/)
- **Title:** `322. Amenda Wu 2015/03` · **published:** 2015-03-08
- Field set identical to Capture 1 (heading-padded render of the same profile table); no narrative prose, no byline.

## Twin check (2026-11-16)
Content-block (site-chrome-stripped, `#`/whitespace-normalized) md5 `708578c09409`
(910 chars, Capture 1 profile block) vs `a060cb4f3e2b` (321 chars, Capture 2 dump).
Neither contains the other as a normalized string, because Capture 1 carries the
site-rendered restatement block and Capture 2 the `###` heading padding; a field-level
diff shows Capture 2 is a strict serialization subset of Capture 1 — every value in the
dump appears verbatim in the profile block. These are **one self-reported record rendered
twice by the same editable site**, not two independent sources. Corroboration grade for
every fact above: `alleged` (self-report only).

## Near-duplicate counterpart record (id 72894 — Amanda Wu, Bassist)
- **Files:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/amanda-wu.json` +
  `knowledge/web-archives/taiwaneseamericanhistory-org/posts/165-amanda-wu-bassist-201503.md`
- Record id **72894** — numerically adjacent to 72893 — and **`modified` is byte-identical
  (`2026-06-02T17:17:20`)**, i.e. the same crawl batch on the same editable site.
- Profession taxonomy: `community leader` + `musician` **+ `performer`** (one extra tag).
- Page size 55,602 bytes; its profile block carries the narrative bio paragraph absent
  from Capture 1 (UC Davis music major, bass performance under Thomas Derthick, minor in
  Communications and Education, violin/piano ~8 years, Donor Relations Coordinator in the
  Development Division at the San Francisco Symphony, UC Berkeley Symphony Orchestra member,
  San Francisco Wind Ensemble Board of Directors).
- Companion dump `165. Amanda Wu, Bassist` shares the same publication date 2015-03-08.
- Normalized block md5s `bbd159d461a7` (2,241 chars) / `affecc2dd3af` (533 chars); neither
  amenda block is a substring of either amanda block (the amanda side adds the bio
  paragraph; the amenda side the restatement block).
- **Ruling:** adjacent ids + identical `modified` + same submission form on one editable
  site = same-batch authorship, **not** corroboration, and not proof of same-person either.
  The identity merge stays on HOLD on [[people/amenda-wu]] and [[people/amanda-wu]]; no
  Amanda Wu bio fact is imported into the Amenda Wu dossier as fact.

## Search budget ledger (FLOOR-ANCHOR t_e33474a0, 2026-11-16) — 6 of 8 spent
- Web (4 queries, this name only): `"Amenda Wu" "San Francisco Symphony" donor relations UC Davis` ·
  `"Amenda Wu" musician Bay Area Taiwanese American` · `"Amenda Wu" -echopedia -taiwaneseamericanhistory orchestra OR symphony OR "donor relations"` ·
  `"Amenda Wu" 吳 音樂 舊金山` — returns are the same TAH profile, its #322 dump, our own two
  Echopedia pages, and the TAH `musician` profession index page (which lists Amanda Wu and
  Amenda Wu as **separate entries, both 2015-03-08**). No third-party press hit.
- Web (2 more): `"Amenda Wu" "UC Berkeley Symphony" OR "Berkeley Symphony" member` ·
  `"Amenda Wu" linkedin OR facebook OR instagram` — same closed set, plus two same-name
  rejections below.
- Whole-box sweep (grep -rlF, per name form, `content/` + `knowledge/`): `Amenda Wu` → 6
  content files (own page, own work page #322, index, amanda-wu cross-ref, source hub,
  `.wiki-index.md`) + machine indexes (`units.jsonl`, `ee-vault-index.v1–v5`,
  `posts/index.jsonl`, `taiwaneseamericanhistory-org-family.json`) + the two crawl artifacts.
  `amenda-wu` → same set plus deepen-x slice logs and linker state (operational, not sources).

## Same-name rejections
- **LinkedIn `amenda wu` (aberaeon decoration, 台灣, Marketing Manager, 2017–present)** — Taiwan-based
  marketing role, no Bay Area / Symphony / UC Davis field; not this subject.
- **Mixcloud `amenda5` (Amenda Wu, 5 followers, no shows)** — no locational or institutional anchor;
  unverifiable identity tie. Not used.
- Other `吳`-surname hits in the corpus are unrelated people (吳明源, 吳瑟民, Arthur H. Wu 吳漢南,
  De Min Wu — roster recorded on [[people/amanda-wu]], deepen-x slice 09160221 class).

## What this capture does NOT establish
- No Chinese name, no birth year, no arrival year, no spouse/children — blank in both artifacts.
- No performance, award, or commission record anywhere on this box.
- Whether Amenda Wu (72893) and Amanda Wu (72894) are one person — open HOLD, needs owner
  verification against TAH.
