---
title: "TAH Who's Who profile capture — 2036. Prof. W.S. (Winston) Ho 何文壽教授"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2036. Prof. W.S. (Winston) Ho 何文壽教授

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 854
- wikilinks: 4


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-w-s-winston-ho|Prof. W.S. (Winston) Ho 何文壽教授]] — TAH Who's Who record #2036

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-w-s-winston-ho.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-w-s-winston-ho/](https://taiwaneseamericanhistory.org/person/prof-w-s-winston-ho/)
- **Record id:** 74531 · **type:** `tah_person` · **profession taxonomy (`person_profession`, 6 tags):** `chemical engineer` · `educator` · `engineer` · `professor` · `researcher` · `scientist`
- The `researcher` and `chemical engineer` taxonomy tags are **absent from the crawl sidecar**, which lists only `roles: [engineer, scientist, professor, educator]` — the taxonomy is the richer classification.
- **`modified` on source:** 2026-06-19T16:59:57 · **page size:** 58,040 bytes · **page banner:** `Who's Who Taiwanese American Profile — Last updated: June 19, 2026`
- **Verbatim fields (self-reported):** English Name `Prof. W.S. (Winston) Ho` · Hanji Name `何文壽教授` · Birth Year `1943` · Birth Place `Taipei, Taiwan` · First year/city/State in U.S. `-/-/-` · Address `OH`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three blank; `family: []`, `family_filled: false`
- **Education:** 1. National Taiwan Univ. — 1963–1966 — B.S., Chemical Engineering · 2. Univ. of Illinois at Urbana-Champaign — 1971 — Ph.D.
- **Employment:** 1. Univ. of Illinois — 1972–1984 — Associate Professor (1972–1976); Professor (1977–1984) · 2. Exxon Mobil Corporation — 1985–1999 — Director of R&D Dept. · 3. Univ. of Kentucky — 1999 — Professor of Chemical Engineering · 4. The Ohio State Univ. — 2002–present — Professor of Chemical Engineering
- **Accomplishment (8 dated items, restated verbatim under a second field `Notable Accomplishments`):**
  1. Industrial Research 100 Award, 1985
  2. Professional and Scholarly Publishing Award for the most outstanding engineering work, 1993
  3. National Academy of Engineering, U.S.A, 2002
  4. Perkin Elmer Professor R. Kumar Chemcon Distinguished Speaker Award, Indian Institute of Chemical Engineers, 2004
  5. Chemcon Distinguished Speaker Award, Indian Institute of Chemical Engineers, 2004
  6. Institute Award for Excellence in Industrial Gases Technology, American Institute of Chemical Engineers, 2006
  7. Elected as a member of the 30th Academia Sinica (Engineering Science Group), 2014
  8. Chemcon Distinguished Speaker Award, Indian Institute of Chemical Engineers, 2015
- **Publication:** `--` · **Hobby:** `--` — blank on the profile, so no crown fact is withheld in either field.
- **Submission provenance line (verbatim):** `Source from民報http://www.peoplenews.tw/news/f9f18bc3-a148-49d4-bb4e-9f43ec69654b` — the profile self-declares 民報 (Peoplenews.tw) as upstream. That article is **not archived on this box** (see GAPS below).

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2036-w-s-ho.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2036-w-s-ho/](https://taiwaneseamericanhistory.org/whos-who-2036-w-s-ho/)
- **Title:** `2036. Prof. W.S. (Winston) Ho 何文壽教授` · frontmatter `fetched: auto`, no fetch date
- Field set identical to Capture 1 (Education, Employment, the 8-item Accomplishment list, blank Publication/Hobby, and the same `Source from民報` provenance line).

## Twin check (2026-11-14)
Whitespace-stripped, frontmatter-excluded body md5 `ff5fab224b3d9bde2a6f4d7be80068ed` (3,072 norm chars —
Capture 1 incl. site chrome, the page banner, the repeated `Notable Accomplishments` block, the rendered
summary block, and the 2026-06-19 `modified` stamp) vs `e8a1a0c5be0e7b15d9d05174b0c8f32f` (1,296 norm chars —
Capture 2, the encyclopedia-entry dump). Containment test: neither is a substring of the other. The two
artifacts are **two serializations of one editable self-report** (same field values, same `Source from民報`
line), so agreement across them is **not** corroboration — which is why every dated honor below stays
`alleged` on the person page.

## What this capture does NOT establish
- No spouse, daughter, or son names — the three family fields are blank in both artifacts (`family_filled: false`).
- No U.S. arrival year — `First year / First city / State in U.S.` is `-/-/-`.
- No publication list and no hobbies — both fields are `--` on the profile.
- The 民報 article named in the profile's own `Source from` line is not archived in `knowledge/web-archives/`;
  `grep -rlF 'f9f18bc3'` over the vault returns only the subject's own artifacts (and the same-line copies on the
  adjacent 2018-02-19 batch records [[works/taiwaneseamericanhistory-org/whos-who-2037-wilson-ho|2037. Prof. Wilson Ho 何文程教授]]
  and [[works/taiwaneseamericanhistory-org/whos-who-2038-teh-hui-kao|2038. Prof. Teh Hui Kao 高德慧教授]], whose profiles print the same template provenance line).
- The works page [[works/taiwaneseamericanhistory-org/whos-who-2036-w-s-ho|TAH #2036]] is a bibliographic-only
  record (`value_band: B`, "Bibliographic record only. Full text stays in the vault") and carries none of the
  biographical fields above — the web-archive captures, not the works page, are the provenance for the person page.

## Whole-corpus sweep (2026-11-14, card t_ee344edb)
Non-machine greps over `content/` + `knowledge/` (machine indexes `units.jsonl`, `posts/index.jsonl`,
`ee-vault-index.v*` excluded as sources):
- `grep -rlF '何文壽'` → own person page, own works page #2036, the two web-archive captures, the sources hub
  roster line, `people/prof-wilson-ho.md` (adjacent-record HOLD note), plus machine/title indexes. No third-party record.
- `grep -rliF 'Winston Ho'` → own person page, sources hub, `taiwanjustice-net-priority-lexicon.json`,
  `taiwaneseamericanhistory-org-family.json` (machine). No third-party record.
- `grep -rliE 'W\.?S\.? Ho\b'` → no additional non-machine hit.
- Memoir/event posts (`posts/mystories*.md`, `posts/ourjourneys*.md`) grepped `-iF 'winston'`: every hit is a
  different Winston — Churchill (mystories173), Winston Salser/UCLA (mystories263), the 林真真 family sons
  (mystories507), Winston Lue (ourjourneys162), Winston Chen (ourjourneys37/38), Winston Tsai (ourjourneys76).
  All false positives, none is 何文壽教授.
