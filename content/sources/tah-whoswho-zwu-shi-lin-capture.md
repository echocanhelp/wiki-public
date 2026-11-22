---
title: "TAH Who's Who profile capture — 1343. Zwu-Shi Lin 林竹信"
type: source
tags:
  - source
  - tah-foundation
  - tah-whos-who
verification_status: pending
last_reviewed: 2026-11-14
---
# TAH Who's Who profile capture — 1343. Zwu-Shi Lin 林竹信

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 593
- wikilinks: 2


Primary capture of the subject's own self-reported TAH Foundation Who's Who record,
archived on this box as two distinct artifacts, plus the one third-party story-corpus
record that names him. Preserved in full because the biographical fields are
self-reported and the live site is editable.

## Subject
- [[people/zwu-shi-lin|Zwu-Shi Lin 林竹信醫師]] — TAH Who's Who record #1343

## Capture 1 — crawled profile page
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/person/zwu-shi-lin.json`
- **Original:** [https://taiwaneseamericanhistory.org/person/zwu-shi-lin/](https://taiwaneseamericanhistory.org/person/zwu-shi-lin/)
- **Record id:** 73884 · **type:** `tah_person` · **profession taxonomy (`class_list`):** `neuroradiologist`, `physician`, `radiologist` — note the sidecar `roles` field drops two of the three tags and keeps only `physician`
- **`modified` on source:** 2026-06-19T16:48:19 · page size 53,023 bytes
- **Verbatim fields (self-reported):** Name 林竹信 醫師 / Dr. Zwu-Shi Lin · Birth Year `-` · Birth Place 台灣 · First arrival in the U.S. `-/-/-` · Address Allentown/PA
- **Family:** `1. Wife:-` · `2.Daughter:-` · `3.Son:-` — all three blank; `family_filled: false`
- **Education:** 1. 高雄醫學大學 — `-` — M.S.
- **Employment:** 1. Lehigh Valley Hospital放射線科 — present — staff · 2. Lehigh Magnet Imaging Center — Medical director · 3. Lehigh Valley Hospital — 神經放射科主任 · 4. 賓大放射線科 — 住院醫師及神經放射科
- **Accomplishment / Publication (Non-professional) / Hobby / Website or Blog:** all `-` — label-inflation proof: no honor, publication, hobby, or website is withheld in the record
- **Submission provenance line printed on the page:** 「Source from美東台灣人夏令會 2004」 — the profile traces to the subject's 2004 美東台灣人夏令會 submission
- **Site-rendered block** repeats Hanzi Name 林竹信 / Birthplace 台灣 / Residence Allentown, PA / the same Education and Employment rows, and glosses 神經放射科主任 as "Chief of Neuroradiology" and 賓大放射線科 住院醫師及神經放射科 as "University of Pennsylvania Radiology — Resident and Neuroradiology"

## Capture 2 — encyclopedia entry dump
- **File:** `knowledge/web-archives/taiwaneseamericanhistory-org/posts/whoswho1343.md`
- **Original:** [https://taiwaneseamericanhistory.org/whoswho1343/](https://taiwaneseamericanhistory.org/whoswho1343/)
- **Title:** `1343. Zwu-Shi Lin 林竹信 / 2016/10` · **published:** 2016-10-25 (per [[works/taiwaneseamericanhistory-org/whoswho1343]])
- Field set identical to Capture 1 (Name / Birth Year `-` / Birth Place 台灣 / Allentown/PA / 高雄醫學大學 M.S. / the four Employment rows / 「Source from美東台灣人夏令會 2004」).

## Twin check (2026-11-14)
Containment test, per the james-jean / theodore-ted-wing precedent, run on the profile's
CONTENT BLOCK (from the 「Who's Who Taiwanese American Profile」 marker to the
「Travel the roads paved…」 footer line), not the raw `page_text` with site chrome.
Capture 2's body is the field-for-field rendering of Capture 1's profile content
(Capture 1 additionally carries the `Last updated: June 19, 2026` stamp, the
`modified` metadata, and the site-rendered second block with the English glosses).
The two serializations of **one editable self-report** therefore agree — agreement
across two renderings of one record is **not** corroboration, which is why the
self-reported rows stay labeled `alleged`.

## Third-party records on this box (2026-11-14 harvest)
- `knowledge/web-archives/taiwaneseamericanhistory-org/posts/144-%e5%8f%b0%e7%be%8e%e4%ba%ba%e5%ae%97%e6%95%99%e7%a0%94%e7%bf%92%e6%9c%83%e7%ad%86%e8%a8%98-%e3%80%8e%e5%ae%97%e6%95%99%e4%bf%a1%e4%bb%b0%e5%bf%83%e8%b7%af%e6%ad%b7%e7%a8%8b%e3%80%8f.md` — 張信惠「宗教信仰心路歷程」 (黃哲陽筆記), 摘自 台美人宗教研習會 / 2012 Yearbook: 「林竹信醫師每次見到我一定給我new challenges,來鼓勵我認真努力來克服」 — named alongside 吳忠修醫師 (氣功) and 翁勝三醫師 (針灸) in her post-stroke recovery among 「在 Philadelphia 附近一群台灣朋友」. This is the only non-self-report record of 林竹信 on this box.

## Ruled out (do not re-open)
- `posts/publications1343.md` — number collision, NOT the subject: H1 is 「1343. THUS I CAME – VOICELESS SHORT STORIES / Tien C. Lee /-/2020/Life/生活」, a 2020 memoir by Prof. Tien C. Lee, zero mention of 林竹信 (same-number collision class, jyh-fa-kuo precedent).
- Machine indexes (`tdm-page-title-index.json`, `taiwanjustice-net-priority-lexicon.json`, `taiwaneseamericanhistory-org-family.json`, `MANIFEST.json`, deepen-x slice logs, scout jsonl) — index/operational files, not sources.
- Prior deepen-x SKIP stamps checked only `content/works` + `content/articles`; this pass re-swept all of `content/` + `knowledge/` per name form (林竹信 / Zwu-Shi) and posts/144 is the delta they never opened.
