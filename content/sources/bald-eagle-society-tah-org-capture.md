---
title: "TAH org-record capture — Bald Eagle Society 白首老鷹社"
type: source
tags:
  - source
  - tah-foundation
  - tah-organization-record
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH org-record capture — Bald Eagle Society 白首老鷹社

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 604
- wikilinks: 3


Capture page for the citable artifacts on this box backing
[[organizations/bald-eagle-society|Bald Eagle Society 白首老鷹社]].
Preserved because the live TAH site is editable and these are the only
organization-side records for this society on this box.

## Artifact 1 — crawled organization record (site DB export)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/organization/bald-eagle-society.json`
- **Original:** [https://taiwaneseamericanhistory.org/organization/bald-eagle-society/](https://taiwaneseamericanhistory.org/organization/bald-eagle-society/)
- **Record id:** 72402 · **type:** `tah_organization` · **modified:** `2026-06-19T16:23:21` (crawl-side last-modified stamp)
- **Site taxonomy:** `class_list` carries `organization_type-senior` — the site classifies the society under **Senior Organizations**; `person_profession` is empty `[]` (expected for an org record).
- **Content block:** the English mission blurb — founded 2014, Southern California, monthly lectures on the second Friday, topics 人文/歷史/藝術/科學/文化.

## Artifact 2 — crawled story-corpus post (zh self-report)
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/bald-eagle-society.md`
- **Original:** [https://taiwaneseamericanhistory.org/bald-eagle-society/](https://taiwaneseamericanhistory.org/bald-eagle-society/)
- Work page: [[works/taiwaneseamericanhistory-org/bald-eagle-society|10. Bald Eagle Society 白首老鷹社 (published 2015-02-23, band B)]]
- **Content:** the Chinese self-report — 「Bald Eagle Society是2014年由一群在南加州對生命充滿熱情，志同道合的人，希望建立一個平台,互相學習,因此於每個月第二個星期的星期五舉辦演講…」

## Artifact 3 — senior-organizations directory roster
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/pages/senior-organizations.md`
- **Original:** [https://taiwaneseamericanhistory.org/organizations-archive/senior-organizations/](https://taiwaneseamericanhistory.org/organizations-archive/senior-organizations/)
- Lists 「10. Bald Eagle Society 白首老鷹社」 as entry **10 of the 32** Senior Organizations archive (between #11 Houston Taiwanese Golden Club and #9 Houston Taiwan Institute for Senior Citizens). Confirms Artifact 1's `organization_type-senior` classification from a second site surface.

## Twin / containment check
Normalized both self-report sides (strip frontmatter, all `#` and whitespace; JSON side additionally stripped of HTML tags):
- The English org-record blurb and the Chinese corpus post are the **same self-report rendered twice** (one editable organization entry published to two site surfaces). They agree on every fact: 2014 founding, Southern California, second-Friday monthly lectures, the humanities/history/arts/science/culture topic list.
- Agreement across two serializations of one editable self-report is **not corroboration** — dated rows on the person page therefore stay `alleged`/`self-report`.
- Fields withheld by both: no named founders/officers, no member counts, no venue city, no website/Facebook, no lecture roster.

## Third-party records naming the society (corpus-side corroboration)
Whole-corpus sweep 2026-11-14 (from `~/echo-system`, per skill floor-anchor rule: ALL of `content/` + `knowledge/`, single-pattern `-F` per name form, not the DEEPEN-X lane's `works/`+`articles/` habit):
- `grep -rlF '白首老鷹' content knowledge` → **22 files**; `grep -rliF 'bald eagle' content knowledge` → **26 files** (superset).
- Classification of the hit set:
  - Own artifacts: this page, `content/organizations/index.md`, the work page, `content/sources/taiwaneseamericanhistory-org.md` (roster backlinks), the 3 crawl artifacts above.
  - Machine indexes (not sources, per rule): `knowledge/research/taiwaneseamericanhistory-org/units.jsonl`, `knowledge/research/taiwanjustice-net-priority-lexicon.json` (L4 entity entry), `knowledge/operational/ee-vault-index.v1–v5.json`, `knowledge/operational/content-analysis/*.jsonl`, `knowledge/web-archives/.../posts/index.jsonl`.
  - Same-token false positives (the bird, not the society): `content/articles/taiwanjustice-net/2025/20251205024142_美國律師_中國偽造證件販賣口罩情況常見_66f1ee32cbea61d8.md`, `knowledge/web-archives/taiwandaily-net-146172-146172.md` (Oh-Bear + Bald Eagle parade float), `knowledge/web-archives/taiwandaily-net-138045-138045.md` (birdwatching essay).
  - **No third-party community record, memoir, or press mention of the society exists on this box.**

## Related-but-unconfirmed: 白首老鷹論壇 / White Eagle Forum
- [[people/dr-jeffrey-tsai|Dr. Jeffrey Tsai 蔡長宗醫師]]'s TAH profile lists 「Founder of the White Eagle Forum (白首老鷹論壇發起人)」 under Accomplishment — per `knowledge/web-archives/taiwaneseamericanhistory-org/person/dr-jeffrey-tsai.json` (`modified 2026-06-19T17:03:39`) and its story-corpus twin `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whos-who-2248-jeffrey-tsai.md` (post published 2020-03-23).
- Only the 4-char prefix 白首老鷹 overlaps; 論壇 (forum) ≠ 社 (society). Listed as a **lead, not identity** — no document on this box links the two names. Do not merge.

## Web arms searched 2026-11-14 (for the arms section on the org page)
- Google-class backend: `"白首老鷹社" 南加州 演講` and `"Bald Eagle Society" Taiwanese American Southern California lectures 2014` — returned only the two TAH surfaces above, this Echopedia page, the 2019 TAH Organizations PDF (roster hit only; society text not in the indexed excerpt), and TAH archive/category listings of the same 2015-02-23 post.
- `"白首老鷹論壇"` — only Dr. Jeffrey Tsai's own profile surfaces.
- Wayback (web.archive.org, 2023 snapshots of both URLs): content identical to the current crawl — the site has never carried founder names or a lecture roster.
