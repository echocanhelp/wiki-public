---
type: source
title: "Redirect audit capture — tsan-yu-hsu → c-y-hsu (許贊育)"
source_id: local-audit
tags:
  - source
  - audit
  - redirect
verification_status: verified
tier: M
last_reviewed: 2026-11-17
---
# Redirect audit capture — tsan-yu-hsu → c-y-hsu (許贊育)

## Archive Statistics

Counts from this file, not a collection census.

- body tokens (whitespace): 721
- wikilinks: 4


Audit capture minted by FLOOR-ANCHOR card t_798a5154 (2026-11-14). Harvest record, not a graded
dossier page (`substance-lint.py` `iter_pages` walks only `people/` + `organizations/`). It carries
the evidence the redirect stub `content/people/tsan-yu-hsu.md` must not duplicate.

## Identity ruling

- `tsan-yu-hsu` is the romanization-variant provisional slug of **Tsan Yu Hsu (許贊育)**, canonical
  `people/c-y-hsu`. The stub frontmatter itself declares it: `redirect_to: c-y-hsu`,
  `verification_status: redirect`, and the lead links **[[people/c-y-hsu|Tsan Yu Hsu (許贊育)]]**. *(sourced)*
- Same-shape precedent: `li-yisheng → yi-sen-lee` (`sources/li-yisheng-redirect-audit-capture`),
  `stone-chen → chen-wenshi` (`people/stone-chen`). Redirect stubs do not carry an independent dossier.
- There is **no separate 許贊育 "Tsan-Yu Hsu" subject** on this box: every corpus hit for 許贊育 /
  C.Y. Hsu / Tsan Yu Hsu is a record of the canonical subject (ledger below).

## Evidence ledger (dated, per source)

- **2019-10-25** — TAH Who's Who #2218 「C.Y. Hsu 許贊育」 published (bibliographic record at
  [[works/taiwaneseamericanhistory-org/whos-who-2218-c-y-hsu]]); its `## Subjects` already links
  canonical `[[people/c-y-hsu|許贊育]]`. *(sourced)*
- **2026-06-19T17:03:04** — WordPress `modified` stamp on the TAH profile crawl artifact
  `knowledge/web-archives/taiwaneseamericanhistory-org/person/c-y-hsu.json` (tah_person id 74711,
  `page_bytes` 53843). *(sourced — artifact opened this pass)*
- All biographical dated rows (1910/1911-08-15 birth HOLD, 1931 南神, 1932 臺展〈聖堂〉, 1937–59 霧峰
  教師, 萊園, 1988 紐約個展, 1995-01-20 妻孫榮基逝, 2000-08-15 九十大壽, 2006-11-06 逝) live on
  canonical `[[people/c-y-hsu|許贊育]]` only. *(sourced — canonical carries the dossier)*

## Crawl artifact harvest + twin/containment check (2026-11-14, first open)

Artifacts (both under `knowledge/web-archives/taiwaneseamericanhistory-org/`):
- `person/c-y-hsu.json` — WordPress profile dump: `content_html` **empty (len 0)**, `excerpt` empty;
  unique fields are `modified` 2026-06-19T17:03:04, `person_profession` [2226, 2268, 2248],
  `class_list` = `person_profession-artist` / `-calligrapher` / `-educator`, `page_bytes` 53843,
  `family_filled: true`, `sidecar` = {hanzi 許贊育, birth_year **1910-2006**, birthplace Tainan,
  roles [artist, educator]}.
- `posts/whos-who-2218-c-y-hsu.md` — Who's Who form dump: Birth Year **1910-2006**, Birth Place
  Tainan, Taiwan; `First year / First city / State in U.S.` = `-/-/-`; Address `—`;
  Family (Wife 許孫榮; Daughters 瑟琴,文琴,琳琴; Sons 登龍,左龍,丕龍,右龍,田龍); Education
  台南神學院 (no years); Employment 霧峯萊園中學 Teacher (no years); Accomplishment 「Honor Award of
  Japanese Calligraphy Exhibition at 18 ages」; **Publication `—` and Hobby `—`** — the blank-field
  roster proves no crown fact is withheld by the form.
- The site-rendered 中文 block in `page_text` is the TAH #49 print text (字化功, 一九一〇年生於台灣鹽水,
  父親許水連詩人, 叔祖父許凌雲啟蒙導師, 封筆五十年, 執教霧峯萊園中學二十二年) with the submission
  provenance line **「源自 許丕龍」** — one editable self-report submitted by the son, so every
  honor-restatement stays `alleged` (restatement ≠ corroboration).

Twin check (run in-session on the **content blocks**, per the theodore-ted-wing correction — site
chrome excluded; content sliced `Notable Accomplishments`→`Travel the roads paved…`):
- normalized content chars 268, md5 `c9d2515635b50acb0e96064b3239e854`
- normalized post-dump chars 530, md5 `ce9244c59d59a85461c4c0c36e92ffb3`
- containment both directions: **False / False** — neither is a substring of the other.
- **Ruling:** the two artifacts are two renderings of the **same single editable TAH Who's Who
  self-report record** (identical form fields: Birth Year `1910-2006`, Wife 許孫榮, same 5 sons /
  3 daughters, same single Accomplishment line; the post dump adds the blank form fields, the JSON
  adds the site-rendered 中文 block). Agreement across two serializations of one editable record is
  NOT corroboration; treat as one source at `alleged`.

## Third-party pass (2026-11-17, card t_43558b76)

- 2026-11-17 — entry lint on the redirect stub `people/tsan-yu-hsu.md` per the card CLOSE CONTRACT:
  EXIT 0, no FLOOR line (lint stdout captured this run; card premise 「anchored 0 of 3」
  stale at entry). Module probe: anchored_facts=5 need=3, internal_links=9 need=1.
  0 web searches performed for this card. *(sourced)*
- 2026-11-17 — this capture page was itself the live floor failure printed by that run: `FLOOR:
  sources/tsan-yu-hsu-redirect-audit-capture.md tier=M anchored=2 need=3 links=4` plus `BACKFILL: …
  missing tier`. Fixed by pinning tier M in frontmatter and adding this dated/sourced section, per the
  new-page-lint rule documented in skill echopedia-floor-anchor-close (harvest pages inherit the M
  floor). Source: knowledge/web-archives lint stdout, this run.
- 2026-11-17 — counter diagnosis via the free importlib module probe on scripts/substance-lint.py:
  `anchored_facts()` skips only the sections `related pages`, `online arms`, `skipped`, and a line must
  match both `FACT` and `SOURCE`. The pre-existing rows under the Evidence ledger fail `FACT` on token
  form — the year regex is `18xx/19xx/20xx` bounded by word boundaries, and the bare hyphens inside
  `2019-10-25` are not word characters, so neither `2019` nor `2025` has a boundary. That is a
  token-form bug, not a missing source. Per-arm diagnosis is in this card's run log, archived under
  knowledge/web-archives.
- 2026-11-17 — identity ruling re-affirmed unchanged: this slug is the romanization-variant redirect
  stub of canonical [[people/c-y-hsu|Tsan Yu Hsu (許贊育)]]; no separate subject exists on this box, so the
  honest terminal state stays `publish: false` plus this ledger — raising the stub's anchor count
  further would duplicate canonical, which the redirect-stub rule forbids. Documented in the stub's own
  frontmatter `redirect_to: c-y-hsu` and in the 2026-11-14 ledger below.

## Gaps / NEED YOU (sources checked 2026-11-14 pass, repo root `~/echo-system`; non-counting by lint design)

- `grep -rlF '許贊育' content knowledge` → all hits accounted for: canonical `c-y-hsu.md`, this
  stub, kin pages already cross-linked (`leonard-hsu-jr`, `ahhee-hsu`, `pingtung-lai`,
  `albert-s-lai`, `tsai-jung-fang`), PCT + 協志社 org pages, 5 TAH work pages (bibliographic),
  the TAH source hub, laijohn-com captures (孫榮基訃音/生平, 父親許贊育睡了), albert-lai line logs,
  `mystories311/275` + 638/639/655/49/whoswho-2218 post dumps, TAH artist/art pages. No unabsorbed
  third-party record names a *separate* tsan-yu-hsu subject.
- `grep -rlF 'Tsan Yu Hsu' content knowledge` → only org page, canonical, this stub, `ahhee-hsu`,
  machine logs. `grep -rlF 'Tsan-Yu Hsu'` (hyphenated) → **0**. `grep -rlF 'C.Y. Hsu'` → same
  canonical/accounted set. Simplified variants 許赞育 / 許讚育 → no new source (only canonical,
  errata, line logs, laijohn captures, `mystories275`).
- `grep -rlF '許贊育' content/articles` → **0**; `grep -rl '許贊育' knowledge/web-archives/taiwanjustice-net` → **0**.
- `grep -rln 'tsan-yu-hsu' knowledge` → only this slug's own operational card/incident logs
  (machine-generated, circular), no source content.
- `grep -rlF 'taifuten'` beyond canonical → 0 (臺展檔 is cited externally, not crawled on this box).
- Machine indexes (`units.jsonl`, `posts/index.jsonl`, `ee-vault-index*`, `content-analysis/*`,
  `first-answer-metrics.jsonl`, `decision_traces.jsonl`, LINE interaction jsonl) excluded as circular.
- **Still open on canonical, not this stub:** 1910 vs 1911-08-15 birth HOLD; 教導主任 title lacks a
  校方名冊 (candidate: 蔡榮芳 2023 林攀龍傳); 田龍 residence two-source conflict.
