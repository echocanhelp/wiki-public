---
title: "TAH Who's Who profile capture — 1851. Rev. J. S. Chou 周再賜牧師"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1851. Rev. J. S. Chou 周再賜牧師

Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts. Preserved in full because the
biographical fields are self-reported and the live site is editable.

## Subject
- [[people/rev-j-s-chou|Rev. J. S. Chou 周再賜牧師]] — TAH Who's Who record #1851

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/rev-j-s-chou.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/rev-j-s-chou/](https://taiwaneseamericanhistory.org/person/rev-j-s-chou/)
- **Record id:** 74357 · **type:** `tah_person` · **profession taxonomy (`class_list`):** educator · **minister** · professor (3 tags; the `minister` tag is absent from the page's printed `Core roles`, which list only `professor, educator` — for a person whose whole record is pastoral, the class list is the fuller self-reported role set)
- **`modified` on source:** 2026-06-19T16:56:46 — the live profile is editable; page renders "Last updated: June 19, 2026"
- **`page_bytes`:** 55,214 (raw HTML; `page_text` in the JSON is the extracted text)
- **Verbatim fields (self-reported):** English Name `Rev. J. S. Chou` · Hanji Name `周再賜牧師` · Birth Year `1888-1969` · Birth Place `Pingtung, Taiwan`
- **U.S. arrival:** `1915/Oberlin/OH` (first year / first city / State in U.S.) — the person page carried **none** of these three fields before this capture was opened
- **Address:** `--` — unfilled
- **Family:** `1. Wife: 勝見千代` · `2. Daughter: --` · `3. Son: --` — JSON parses `family: [{rel: wife, name: 勝見千代}]`, `family_filled: true`; children fields blank
- **Education:** 1. Doshisha Univ. (同志社大學) — 1910-1915 — B.S. · 2. Oberlin Univ. — 1915- — B.D., Theology · 3. Chicago Univ. — `-` — M.S., Theology
- **Employment:** 1. Doshisha Univ. (同志社大學) — 1921- — Assistant Professor of Theology · 2. United Church of Christ in Japan (日本組合教會) — 1923- — Pastor · 3. KYOAI GAKUEN (共愛女學校) — 1925-1965 — Principal
- **Accomplishment:** 1. The First Taiwanese to pursue a degree in theology in the United States (首位台灣人在美國攻讀神學學位者) · **2. The First Taiwanese to obtain the qualifications of a pastor abroad (Japan), 1923 (第一位在國外（日本）取得牧師資格的台灣人)** — row 2 was missing from the person page before this capture
- **Publication:** `--` · **Hobby:** `--` — blank; no publication or hobby content is withheld elsewhere on the form
- **Notable Accomplishments:** the same two accomplishment strings repeated verbatim in a second field
- **Footer block (restates the form):** `Rev. J. S. Chou` · Hanzi `周再賜牧師` · Birth Year `1888` · Birthplace `Pingtung, Taiwan` · Passed Away `1969` · Education + Position rows as above. Restatement within one editable record is not corroboration.
- **No provenance line:** unlike sibling records (e.g. `Source from 美洲台灣日報…` on other profiles), this record carries no upstream-source attribution.

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-1851-j-s-chou.md`
- **Original:** [https://taiwaneseamericanhistory.org/whos-who-1851-j-s-chou/](https://taiwaneseamericanhistory.org/whos-who-1851-j-s-chou/)
- **Title:** `1851. Rev. J. S. Chou 周再賜牧師` · vault work record: [[works/taiwaneseamericanhistory-org/whos-who-1851-j-s-chou|TAH #1851]] (publish date 2017-08-17 per that record)
- Field set identical to Capture 1 (Address `—`, children `—`, Publication/Hobby `—`), including both Accomplishment rows. It is a second rendering of the same self-reported payload, not an independent source.

## Twin check (2026-11-14, in-process)
Frontmatter stripped, `#`/whitespace normalized: profile `page_text` = 1,950 normalized chars, md5 `a9e5a0f7cfe96b938152f27f06362867`; dump body = 718 normalized chars, md5 `a10284be8fb8bb6bb26c51f20cf25934`. Neither contains the other — the difference is **not** biographical: the dump drops the site chrome and the site-generated footer block (`Passed Away 1969`, the `Rev. J. S. Chou` English block) and the 2026-06-19 `modified`/`Last updated` stamp that survive only in the JSON's `page_text`. The JSON is the richer serialization; both serialize **one** editable self-report, so agreement across them is **not** corroboration — that is what keeps the record's own claims (the two "first Taiwanese" distinctions, the KYOAI principalship) at `alleged`.

## Harvest provenance
- Both captures come from the 2026-08-17 `wp-json` harvest of taiwaneseamericanhistory.org recorded in `knowledge/web-archives/taiwaneseamericanhistory-org/MANIFEST.json` (`fetched_at: 2026-08-17`, `method: wp-json`, expected 2,212 person / 339 org).
- This slug **does** appear in that manifest's `weak.person` list — the harvest grader already flagged this profile's payload as thin at fetch time. That is why the person page stayed at one lone Accomplishment row for so long; the unopened captures still hold the U.S.-arrival field, the second accomplishment, and the `minister` taxonomy tag the page never carried.

## What this capture does NOT establish
- No death-place, ordination-denomination detail beyond the self-reported `日本組合教會` row, no publication list (Publication `--`), and no children's names.
- No third-party/community record of him exists on this box (whole-vault sweep 2026-11-14, card t_f5771ef6: `grep -rlF '周再賜'`, `-rlF 'J. S. Chou'`, `-rlF '周再赐'`, `-rlF '共愛女學校'`, `-rlF 'KYOAI'` over `content/` + `knowledge/` return only his own page, the TAH #1851 work record, the roster line in `content/sources/taiwaneseamericanhistory-org.md`, the two web-archive captures above, and machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index.v*`, `content-analysis/*.jsonl`, `tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`) — indexes are not sources.
- Earlier deepen-x sweeps (2026-09-17 → 2026-10-08, 11 stamps) checked `works/` + `articles/` only; the 2026-10-07 stamp additionally ruled out the two stray 再賜 hits (publications355 Chen Ching-Jung memoir; eastgatebarclay devotional) as the common word 再賜 ("again-bestow"), not this person.

## Related
- [[people/rev-j-s-chou|Rev. J. S. Chou 周再賜牧師]] — subject page fed by this capture
- [[works/taiwaneseamericanhistory-org/whos-who-1851-j-s-chou|1851. Rev. J. S. Chou 周再賜牧師]] — vault work record of the profile
- [[sources/taiwaneseamericanhistory-org|taiwaneseamericanhistory.org — source hub]]
- [[sources/taiwaneseamericanhistory-org-story-corpus|TAH story corpus hub]]
- [[organizations/tah-foundation|TAH Foundation]] — publisher
