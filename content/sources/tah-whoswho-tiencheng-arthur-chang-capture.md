---
title: "TAH Who's Who profile capture — 1367. Tiencheng Arthur Chang 張幸吉"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1367. Tiencheng Arthur Chang 張幸吉

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/tiencheng-arthur-chang|Tiencheng Arthur Chang]] — TAH Who's Who record #1367

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/tiencheng-arthur-chang.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/tiencheng-arthur-chang/](https://taiwaneseamericanhistory.org/person/tiencheng-arthur-chang/)
- **Record id:** 73905 · **type:** `tah_person` · **`modified` on source:** 2026-06-02T17:21:58 · page size 54,293 bytes
- **`person_profession` taxonomy:** taxonomy ids `[2248, 2234, 2237, 1813, 2235]` rendering as `class_list` tags `person_profession-educator`, `-physician`, `-professor`, `-researcher`, `-scientist`. Note `researcher` appears **only** in this taxonomy and is absent from the sidecar roles (`scientist, physician, professor, educator`).
- **Verbatim fields (self-reported):** Name `-` / `Prof. Tiencheng Arthur Chang` · Birth Year `-` · Birth Place 台灣 · First arrival in U.S. `-/-/-` · Address `-/TX`
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; `family_filled: false`
- **Education:** 1. 台灣大學 — `-` — B.S. Animal Science · 2. University of Wisconsin-Madison — `-` — M.S. Endocrinology-Reproductive Physiology · 3. S University of Wisconsin-Madison — `-` — Ph.D. Endocrinology-Reproductive Physiology (the `S` prefix is a verbatim source typo, likely `U`)
- **Employment:** 1. Dept. of OB/GYN, Clinical Assisted Reproductive Technology Labs, University of Texas Health Science Center at San Antonio — present — Associate Professor & Director
- **Accomplishment / Publication (Non-professional) / Hobby / Website or Blog:** all `-` — no withheld crown facts; the self-report is fully harvested
- **Submission provenance:** `Source from http://www.symposium2016. ttbatw.org/` — the record was submitted from the TTBATW 2016 symposium site (note the verbatim stray space inside the URL)
- **Site-rendered second block** (below the form in `page_text`): Birthplace 台灣 · Residence TX · Education 台灣大學 B.S. Animal Science / University of Wisconsin-Madison … — a restatement of the same fields

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1367.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1367/](https://taiwaneseamericanhistory.org/whoswho1367/)
- **Title:** `1367. Tiencheng Arthur Chang / 2016/11` · published 2016-11-03 (per [[works/taiwaneseamericanhistory-org/whoswho1367]])
- Field set identical to Capture 1, including `Source from http://www.symposium2016. ttbatw.org/`.

## Twin check (2026-11-14)
Normalized (frontmatter stripped, `#`/whitespace stripped) md5 + char counts:
- Capture 1 `content_html`: `d41d8cd98f00b204e9800998ecf8427e` — **0 chars, empty** (profile page body empty in this crawl; only `page_text` carries content)
- Capture 2 post dump body: `c3a368b6aa571e2714616ca2a95689c9` — 699 chars
- Capture 1 `page_text`: `f94d3fa7eb94ecc022897f9c2ae1ce36` — 1,714 chars (site chrome + form + rendered block + `Last updated: June 2, 2026` stamp)
- Containment: post dump ⊂ `page_text`? **no**; `content_html` ⊂ both (vacuously, it is empty).
The `page_text` and the post dump are two serializations of **one editable self-report**;
agreement across them is **not** corroboration — which is why the `Source from … symposium2016`
submission line and every biographical field stay `alleged`.

## Same-number collision ruling (2026-11-14)
`knowledge/web-archives/taiwaneseamericanhistory-org/posts/publications-1367.md` shares the number
1367 but per its H1 is `1367. 我的足跡/張幸吉/10/2022/Autobiography/自傳` — a Publications post for a
**different** subject 張幸吉 (an October 2022 autobiography), with zero biographical fields about
this subject (all form fields render `-`). It is **not** a second source for this person. The
surname+given romanization also differs (Tiencheng vs Hsing-chi/幸吉); see also
[[works/taiwaneseamericanhistory-org/whos-who-2198-hsing-chi-chang]].

## Whole-corpus sweep (2026-11-14, this card)
`grep -rlF` per name form across **all** of `content/` + `knowledge/` (not only works/ + articles/):
- `Tiencheng` → own person page, own works page whoswho1367, own source hub, own crawl artifacts,
  plus machine indexes (`units.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`) — not sources.
  One stray hit `content/people/tien-chen-lin.md` is a different person (Tien-Chen Lin substring of
  the surname/given romanization), false positive.
- `張慶吉` / `張天成一` / `Tien-Cheng Chang` → 張慶吉 hits belong to [[people/prof-tien-cheng-chang]]
  (張典正教授, TAH #1948 — a different professor, same romanization class, false positive);
  no third-party record names this subject.
- No memoir (`mystoriesNNN`), roster, or community-coverage record names him on this box.

## What this capture does NOT establish
- No Chinese name, no birth year, no arrival year, no spouse/children names — blank in both artifacts.
- The symposium site itself is not archived in this vault beyond the URL string.
- Research publications, awards, and lab history are not in either capture and are not asserted here.
