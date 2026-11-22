---
title: "TAH Who's Who profile capture — 2076. Samuel Kao 高榮彬 / 03/2018"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 2076. Samuel Kao 高榮彬 / 03/2018

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/samuel-kao|Samuel Kao 高榮彬]] — TAH Who's Who record #2076

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/samuel-kao.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/samuel-kao/](https://taiwaneseamericanhistory.org/person/samuel-kao/)
- **Record id:** 74570 · **type:** `tah_person` · **profession taxonomy (`class_list`):** `person_profession-designer` · `person_profession-entrepreneur` (2 tags; the `designer` tag is absent from the sidecar `roles`, which lists only `entrepreneur`)
- **`modified` on source:** 2026-06-19T17:00:40 — the live profile is editable; page renders "Last updated: June 19, 2026"
- **Verbatim fields (self-reported):** Name `高榮彬 / Samuel Kao` · Birth Year `-` · Birth Place `台灣` · First year / First city / State in U.S. `-/-/CA` · Address `La Puente/CA`
- **Family (`family_filled: false`):** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` (placeholders only, no names)
- **Education:** `1.復興美工` (no dates)
- **Employment:** `1. JSK Custom Design — 2010-present — 創辦人` · `2. JSK Moto Company — 2010-present — 創辦人`
- **Accomplishment:** `獲重機車設計比賽4次冠軍`
- **Publication (Non-professional ones) / Hobby / Website or Blog:** `-` (all three blank — no crown fact is withheld elsewhere on the record)
- **Site-rendered `Notable Accomplishments` restatement (footer block, Capture 1 only):** `獲重機車設計比賽4次冠軍 (Won 4 championships in heavyweight motorcycle design competitions)` — the English gloss is generated from the same record, not an independent source
- **Tagline printed on the profile:** `Travel the roads paved by those who came before us.`
- **Sidecar:** `hanzi: '高榮彬'` · `birth_year: '-'` · `birthplace: '台灣'` · `roles: ['entrepreneur']`
- **`content_html` / `excerpt`:** empty in the crawl; the rendered `page_text` (52,191 `page_bytes`, 1,627 rendered chars) is the field-bearing artifact

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho2076.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho2076/](https://taiwaneseamericanhistory.org/whoswho2076/)
- **Title:** `2076. Samuel Kao 高榮彬 / 03/2018` · works-page publish date 2018-03-25 per `posts/index.jsonl` (post id 47165) and [[works/taiwaneseamericanhistory-org/whoswho2076|the works record]]
- Field set identical to Capture 1, incl. `Accomplishment: 獲重機車設計比賽4次冠軍` and the blank `Publication` / `Hobby` / `Website or Blog` fields.

## Twin check (2026-11-14)
Normalization: frontmatter stripped, then all `#` and whitespace removed; md5 of the result.
Captured values, re-derived this pass: the crawled profile page `c637297f874b198a9d7cd1c14a9dabf6` (1,254 norm chars, incl. site chrome, the 2-tag profession taxonomy, the 2026-06-19 `modified` stamp, the site-rendered second summary block, and the English `Notable Accomplishments` gloss) vs the encyclopedia-entry dump `963ab9054243993acb3e051fa77cba10` (333 norm chars). Containment tested both directions: False. Capture 1 is strictly the richer artifact. Both serialize the same editable self-report, so agreement across them is **not** corroboration — it is what keeps the record's own claims (companies, founding years, the 4-time championship) at `alleged`.

## What this capture does NOT establish
- No birth year (`Birth Year: -` in both captures and sidecar `birth_year: '-'`).
- No U.S. arrival year (`First year, first city and state arrived in the U.S.: -/-/CA` — only the state is filled).
- No family names (Wife / Daughter / Son placeholders only; harvester parsed `family: []`, `family_filled: false`).
- No website, publication list, or hobby (all three fields `-` in both captures).
- The 4-time heavyweight-motorcycle-design championship is self-reported; no competition-side record is archived on this box, and the record names no competition, year, or class.
- No community-organization membership, memoir, or press mention of him exists in the corpus
  (whole-vault sweep 2026-11-14, card t_d4e773a5: `grep -rlF` / `grep -rliF` per name form
  `高榮彬`, `Samuel Kao`, `JSK Custom Design`, `JSK Moto`, `獲重機車設計` over `content/` +
  `knowledge/` returns only his own page, the TAH #2076 work record
  `content/works/taiwaneseamericanhistory-org/whoswho2076.md`, the roster line in
  `content/sources/taiwaneseamericanhistory-org.md`, the two captures above, and the machine
  indexes `units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v1–v5.json`,
  `content-analysis/*.jsonl`, `tdm-page-title-index.json`,
  `taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json` —
  indexes are not sources). A `La Puente` grep adds only unrelated Hacienda-La Puente
  school-board figures; `JSK` hits outside his captures are base32 `archive_digest:` noise.
- Same-surname / same-English-name individuals are distinct people, not merged:
  [[people/jen-kao|Jen Kao 高嘉旎]] and [[people/min-kao|Dr. Min Kao 高民環]] (artist / semiconductor
  executive, unrelated to this subject), and the Rev. Samuel Kao who proofread Chinese lyrics
  in 吳英俊's 1994 choral collection `knowledge/web-archives/taiwaneseamericanhistory-org/posts/publication1309.md`
  — same English name, no biographical overlap (no designer/motorcycle/La Puente tie); a
  namesake, not this subject.
