---
title: "TAH Who's Who profile capture — 1999. Prof. Pei-Jung Lin"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1999. Prof. Pei-Jung Lin

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 610
- wikilinks: 1


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/prof-pei-jung-lin|Prof. Pei-Jung Lin]] — TAH Who's Who profile (record id 74497), encyclopedia post #1999

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/prof-pei-jung-lin.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/prof-pei-jung-lin/](https://taiwaneseamericanhistory.org/person/prof-pei-jung-lin/)
- **Record id:** 74497 · **type:** `tah_person` · **profession taxonomy:** `educator`, `professor`, `public health`, `researcher` (`person_profession` term ids 2248/2237/348/1813) — note `public health` and `researcher` are tags the person-page sidecar (`roles: professor, educator`) drops
- **`modified` on source:** 2026-06-02T17:24:13 · page size 55,105 bytes · rendered page prints `Last updated: June 2, 2026`
- **Verbatim fields (self-reported):** English Name `Prof. Pei-Jung Lin` · Hanji Name `--` · Birth Year `--` · Birth Place `Taiwan` · Residence/Address `MA`
- **First year / First city / State in U.S.:** `-` / `Boston` / `MA` — first city and state filled, first year blank
- **Family:** `1. Husband: --` · `2. Daughter: --` · `3. Son: --` · `family_filled: false` — no family detail
- **Education:** 1. National Taiwan Univ. — B.S., Public Health · 2. Harvard School of Public Health — M.S., Health Policy and Management · 3. Univ. of North Carolina at Chapel Hill — Ph.D., Health Policy and Management (all three year fields blank)
- **Employment:** 1. Univ. of Maryland School of Pharmacy — 2008–2009 — Post-doctoral Fellow · 2. Tufts Medical Center — 2010–2017 — Assistant Professor · 2017–present — Associate Professor
- **Accomplishment:** `1. UNC Teaching Assistantship Award, 2007` · `2. Earl P. Charlton Fund Research Award, Tufts Univ. School of Medicine, 2011`
- **Notable Accomplishments:** the same two awards restated in a second, differently-named field of the same self-report — one source, not corroboration; label stays `alleged`
- **Publication / Hobby:** `--` — no crown fact withheld behind an empty field
- **Signature line on the record:** `Travel the roads paved by those who came before us.` (self-report tagline, not a third-party quote)

## Capture 2 — rendered Who's Who post
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1999-pei-jung-lin.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1999-pei-jung-lin/](https://taiwaneseamericanhistory.org/whos-who-1999-pei-jung-lin/)
- **Title line:** `1999. Prof. Pei-Jung Lin` — published 2018-01-31 per `knowledge/web-archives/taiwaneseamericanhistory-org/posts/index.jsonl` (id 45938)
- Field rows mirror Capture 1 (English Name, Hanji Name `—`, Birth Place Taiwan, First city Boston/MA, the three education rows, the three employment rows, the two awards, Publication/Hobby `—`).

## Twin check
Normalized (frontmatter stripped, `#`/whitespace removed) md5 + char counts:
- JSON `page_text`: `dbd2c4bd7b4d7a8114fefb4b7aa1a505`, 1,941 norm chars
- post dump body: `34eb9a52c70c5ce38d8e3744bda50dad`, 694 norm chars
- Containment test: neither string is a substring of the other; the JSON is the richer
  artifact (it alone carries the `modified` stamp, `page_bytes`, the profession taxonomy,
  and the site chrome including the `Last updated: June 2, 2026` render line).
- Agreement across two serializations of one editable self-report is NOT corroboration —
  both artifacts render the same editable record, so honor rows stay `alleged`.

## Skipped / not merged
- No zh-press, Wikipedia, or Wikidata hit for Prof. Pei-Jung Lin was located in the local
  archived corpora (whole-`content/` + whole-`knowledge/` `grep -rlF` 2026-11-14 per form
  `Pei-Jung Lin` / `佩容` / `佩蓉` / `林佩容` / `林佩蓉` / `林佩`): hits are only her own
  `person/prof-pei-jung-lin.json`, `posts/whos-who-1999-pei-jung-lin.md`, the machine
  indexes (`posts/index.jsonl`, `research/tdm-page-title-index.json`,
  `research/taiwanjustice-net-priority-lexicon.json`,
  `research/taiwaneseamericanhistory-org-family.json` — family rows empty, `name_zh: ""`),
  and same-name-disambiguation mentions of *other* people (`people/pei-ju-wang.md` names
  #1999 as 姓名相近之另一人; `people/jung-lin.md` lists this page in its Disambiguation
  block; `佩蓉` hits belong to pianist Peirong Lo; `林佩蓉` hits in `posts/tacec-2006.md`
  and `tacec-2011.md` are different people).
- `research/taiwanjustice-net-priority-lexicon.json` and other machine indexes are indexes,
  not sources.
