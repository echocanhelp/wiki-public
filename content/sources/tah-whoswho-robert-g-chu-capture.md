---
title: "TAH Who's Who profile capture — 2144. Robert G. Chu 朱靜懷"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2144. Robert G. Chu 朱靜懷

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/robert-g-chu|Robert G. Chu 朱靜懷]] — TAH Who's Who record #2144

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/robert-g-chu.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/robert-g-chu/](https://taiwaneseamericanhistory.org/person/robert-g-chu/)
- **Record id:** 74634 · **type:** `tah_person` · **profession taxonomy (`person_profession`: [356, 2261, 2259]; `class_list`):** judge · lawyer · politician (3 tags; the `judge` and `politician` tags are absent from the page's printed `Core roles` of `lawyer`)
- **`modified` on source:** 2026-06-19T17:01:45 — the live profile is editable; page renders "Last updated: June 19, 2026"
- **Verbatim fields (self-reported):** English Name `Robert G. Chu` · Hanji Name `朱靜懷` · Birth Year `1979` · Birth Place `CA/USA` · First year / First city / State in U.S. `-/-/-` · Address `CA`
- **Family (`family_filled: true`):** `1. Wife: --` · `2. Daughter: --` · `3. Son: --` · `4. Father/Mother: 朱明威/蔡珠美` — spouse/children fields are blank in both captures
- **Education:** 1. UCLA — 1998 — B.S., Arts · 2. Southwestern Law School — J.D. (year fields `–`)
- **Employment:** 1. Los Angeles County Public Defender's Office — 2006-2018 — Deputy Public Defender · 2. Los Angeles County Superior Court — 2018- — Judge
- **Accomplishment / Publication / Hobby:** `--` (all three blank — no crown fact is withheld elsewhere on the record)
- **Second site-rendered summary block:** `Hon. Robert G. Chu` with Hanzi/Birth Year/Birthplace/Residence/Education/Position restated — same facts, honorific `Hon.` rendered by the site
- **Sidecar:** `hanzi: '朱靜懷'` · `birth_year: '1979'` · `birthplace: 'CA/USA'` · `roles: ['lawyer']`
- **`content_html` / `excerpt`:** empty in the crawl; the rendered `page_text` (53,329 page_bytes) is the field-bearing artifact

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2144-robert-g-chu.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-2144-robert-g-chu/](https://taiwaneseamericanhistory.org/whos-who-2144-robert-g-chu/)
- **Title:** `2144. Robert G. Chu 朱靜懷` · works-page publish date 2018-07-04 per [[works/taiwaneseamericanhistory-org/whos-who-2144-robert-g-chu|the works record]]
- Field set identical to Capture 1 (name, birth, family, education, employment, blank Accomplishment/Publication/Hobby).

## Twin check (2026-11-14)
Normalized (frontmatter stripped, `#`/whitespace stripped) md5 `3468122ee9538210639183c7e55cffd1`
(460 norm chars, the encyclopedia-entry dump) vs `a991fbe3e60fc36f89eb8bcf2bf03d35`
(1,419 norm chars, the crawled profile page incl. site chrome, the 3-tag profession
taxonomy, the 2026-06-19 `modified` stamp, and the second site-rendered summary block).
Containment test: the dump is **not** a substring of the profile page (site-chrome
sandwiches break strict containment), but all 12 dump field labels
(`English Name` … `Hobby`) are present in the profile `page_text`. Capture 1 is the
richer artifact. Both serialize the same editable
self-report, so agreement across them is **not** corroboration — it is what keeps the
record's own claims (degrees, posts, family names) at `alleged`.

## What this capture does NOT establish
- No U.S. arrival year/city/state (`First year / First city / State in U.S.: -/-/-`).
- No spouse/children (all three family fields `--` in both captures).
- No accomplishments, publications, or hobbies (all three fields `--` in both captures).
- No J.D. graduation year (Southwestern Law School year field prints `–`).
- No community-organization membership, memoir, or press mention of him exists in the corpus
  (whole-vault sweep 2026-11-14, card t_bcb9bb03: `grep -rlF` per name form `朱靜懷`,
  `Robert G. Chu`, `Robert Chu`, `朱明威`, `蔡珠美`, plus field probes `Southwestern Law`,
  `Deputy Public Defender`, `LA County Superior Court judge` over `content/` + `knowledge/`
  returns only his own page, the TAH #2144 works record, the roster line in
  `content/sources/taiwaneseamericanhistory-org.md`, the two web-archive captures above,
  machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`,
  `content-analysis/*.jsonl`, `taiwanjustice-net-priority-lexicon.json`,
  `tdm-page-title-index.json`, `taiwaneseamericanhistory-org-family.json` — indexes are not
  sources), and the same-name-disambiguation records for **Robert Chung 鐘博盈**
  ([[works/taiwaneseamericanhistory-org/whoswho1411|whoswho1411]],
  [[people/robert-chung|Robert Chung]],
  `content/sources/tah-whoswho-robert-chung-capture.md`) — a substring `Chu`/`Chung`
  collision, a distinct person, excluded.
- Earlier deepen-x sweeps (2026-09-18, 09-20, 09-21, 09-25 ×2, 10-07 slice 10051918-32,
  10-08 slice 10070600-16) re-verified the same hit set; this pass extended the sweep to
  all of `content/` + `knowledge/`.
