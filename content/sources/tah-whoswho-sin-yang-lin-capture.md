---
title: "TAH Who's Who profile capture — 2289. Sin-Yang Lin 林欣陽"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2289. Sin-Yang Lin 林欣陽

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/sin-yang-lin|Sin-Yang Lin 林欣陽]] — TAH Who's Who record #2289

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/sin-yang-lin.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/sin-yang-lin/](https://taiwaneseamericanhistory.org/person/sin-yang-lin/)
- **Record id:** 74781 · **type:** `tah_person` · **profession taxonomy (`class_list`):** `community leader`, `electrical engineer`, `engineer`, `entrepreneur` (`person_profession` ids 2242, 323, 2227, 2241) — note the site taxonomy carries **community leader**, a tag the crawl sidecar (`roles: [engineer, entrepreneur]`) drops
- **`modified` on source:** 2026-06-19T17:04:19 · page size 53,072 bytes
- **Verbatim fields (self-reported):** English Name Sin-Yang Lin · Hanji Name 林欣陽 · Birth Year `--` · Birth Place `--` · First year / First city / State in U.S. `1978/-/CA` · Address `CA`
- **Family:** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` — all three blank; `family_filled: false`
- **Education:** 1. UC San Diego — `-` — Electrical Engineer
- **Employment:** 1. Self-Employed (Hotel) — `-` — Owner
- **Accomplishment:** 1. President of FAPA-San Diego Chapter · 2. President of Taiwanese Chamber of Commerce San Diego Branch (加州聖地牙哥台灣商會會長) · 3. Winner of 2004 Taiwan Chamber of Commerce Outstanding Leader Award
- **Publication / Hobby:** both `--` — no publication or hobby facts are withheld elsewhere
- **Print provenance line:** `Source from Taiwan Tribune (4/21/1999)` — the submitter's own citation of the upstream print article; the Tribune article itself is not in the vault
- **Site-rendered second block** repeats Name / Residence CA / Education UC San Diego Electrical Engineer / Position Self-Employed (Hotel) Owner / Community FAPA-San Diego Chapter President + Taiwanese Chamber of Commerce San Diego Branch President

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2289-sin-yang-lin.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2289-sin-yang-lin/](https://taiwaneseamericanhistory.org/whos-who-2289-sin-yang-lin/)
- **Title:** `2289. Sin-Yang Lin 林欣陽`
- Field set identical to Capture 1 (first-US-year `1978/-/CA`, UC San Diego, Self-Employed (Hotel) Owner, the three accomplishments, `Source from Taiwan Tribune (4/21/1999)`).

## Twin check (2026-11-14)
Whitespace/heading-normalized, frontmatter-excluded bodies: Capture 1 = 1,647 norm chars (incl. site
chrome, the repeated site-rendered block, and the 2026-06-19 `modified` stamp) vs Capture 2 = 620 norm
chars. Neither is a substring of the other (`json in post: False`, `post in json: False`) — they are two
serializations of **one editable self-report**, not independent records. Per this lane's rule, agreement
across the two captures is **not** corroboration; that is why the record's own
`Source from Taiwan Tribune (4/21/1999)` line stays at `alleged` and the awards/presidencies are labeled
`self-reported` on the person page.

## What this capture does NOT establish
- No birth year, birth place, spouse/children names, or hotel name — blank in both artifacts.
- No dates or titles for UC San Diego study or the hotel ownership (both year fields are `--`).
- The FAPA-San Diego and Taiwanese Chamber of Commerce San Diego branch presidencies are **not**
  corroborated by any other vault record: whole-corpus greps for `林欣陽`, `Sin-Yang Lin`,
  `FAPA-San Diego`, and `加州聖地牙哥台灣商會` return only this subject's own artifacts, machine
  indexes, and the roster mirror `knowledge/web-archives/taiwaneseamericanhistory-org/pages/whoswho.md`
  (line 41: `2289. Sin-Yang Lin 林欣陽`). Sibling San Diego chapter records
  ([[works/taiwaneseamericanhistory-org/10-california-san-diego-chapter-fapa|10. FAPA 聖地牙哥分會]] and
  [[works/taiwaneseamericanhistory-org/san-diego-chapter-tap|9. TAP 聖地牙哥分會]]) do not name him.
- The 2004 Outstanding Leader Award is named only in his own self-report; the corpus's Taiwan Chamber of
  Commerce records (New Jersey / New England / New Orleans / TCCNA newsletter) do not name him.
- The upstream print source, Taiwan Tribune 4/21/1999, is not archived on this box.
- The works page [[works/taiwaneseamericanhistory-org/whos-who-2289-sin-yang-lin|TAH #2289]] is
  bibliographic-only (`value_band: B`, "Bibliographic record only") and carries none of the biographical
  fields above.
