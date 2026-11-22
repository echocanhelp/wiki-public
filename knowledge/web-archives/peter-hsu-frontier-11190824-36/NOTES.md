# peter-hsu — frontier 11190824-36 (card t_982e5a1d), 2026-11-19

Target: `works/taiwaneseamericanhistory-org/whos-who-1670-peter-hsu` (tier M, refs=1 dossier_refs=1 corpus=1 score=1).
Dangling-target frontier pass (re-pass 4 for this subject; prior: 11180842-1/t_4edb6fd5, 11180842-29/t_f6c25e3b, 11190824-1/t_d04ba1bf).
Do NOT publish (card rule); commit only. Person page `people/peter-hsu` already links the work page (Subjects) and vice versa.

## Arms run (2026-11-19)
1. **zh.wikipedia infobox+awards — MISS.** API `list=search srsearch="徐學猷"` (exact quoted) → totalhits **0** (`wp-zh-exact.json`); unquoted `srsearch=徐學猷` → 29 hits, all Ming/Qing/calligraphy-token noise (崔荆南/李喬/吳應琦/袁汝萃/程材/黃昭道/高一志/何顯/柳公權/王民順), no article for the subject. `en.wp srsearch="Peter Hsu" Lansdale` → totalhits **0** (`wp-en-peter-hsu-lansdale.json`). No infobox exists to fetch. `miss (searched "徐學猷", 2026-11-19)`.
2. **Wikidata claims — MISS.** `list=search srsearch=insource:"徐學猷"` → totalhits **0** (`wd-insource-zh.json`); `wbsearchentities search="Peter Hsu Enterprises"` (en) → `search: []` (`wd-entity-peter-hsu-enterprises.json`). No item ⇒ no claims to HOLD, no conflict with vault rows. `miss (searched insource:"徐學猷", 2026-11-19)`.
3. **Official site / event page — MISS.** Searches `Peter Hsu Enterprises` + California / `Peter Hsu` `GTI` Lansdale OR Philadelphia founder: aggregators only (b2bhint, governmentbidders, whereorg, uszm, ylistus, siclists, wholesale-nondurable, netstate, DRPA DBE directory); still no company website anywhere. GTI re-probe: no GTI entity for this subject (hits: 2024/2026 SCCA Solo Nationals driver `Peter Hsu`, Minneapolis, 2019 Honda Type R — same-name exclusion; `2013 Chevrolet Corvette Z06, San Rafael CA` is the Minneapolis driver's co-entrant class rows, not ours; `Matthew Meyer ... Volkswagen GTI, Harleysville PA` is a car-model token collision, not a GTI entity). `miss (searched "Peter Hsu Enterprises" official / GTI, 2026-11-19)`.
   - **GAPS lead re-check (CA SOS branch):** B2BHint relation graph `PETER HSU ENTERPRISES, INC. California` *branch of* 0000716477 re-shown in the search snippet (2026-11-19). Direct fetch of b2bhint page → **403** bot-block (`b2bhint-716477-2026-11-19.html`); CA SOS `bizsearch.sos.ca.gov` Services API → **HTTP 000** (unreachable from this box); `bizfile.ca.gov` portal via browser → daemon navigate timeout ×2; `opencorporates` CA query → **403**. The California branch entity therefore remains **unverified aggregator pointer** — GAPS line stays open, no fact row drawn.
4. **ZH press (World Journal / 大紀元 / 台灣日報) — MISS.** Searches `徐學猷` (± 費城/大費城/TAA/世界日報/台灣日報/大紀元): hit set = already-archived sources only — TAH 2018 園遊會 report (+ its 大紀元 duplicate n10365125, verbatim 李彥輝費城報道 wire text, simplified 徐学猷), TAA-50 歷屆會長 roster PDF (1999 徐學猷), TCCNA 16th/19th rosters, plus echopedia self-pages. No new WJ/台灣日報/大紀元 record. `miss` for new facts (searched `徐學猷`, 2026-11-19).

## Registry pre-check (dangling-target class gate, `_brain_retrieve`)
- `Peter Hsu` → **hit** `people/peter-hsu` (collision with own person page = dangling target already resolved; no mint needed)
- `徐學猷` → **hit** `people/peter-hsu` (same)
- `Peter Hsu Enterprises` → **hit** `people/peter-hsu` (entity mentioned on person page; no standalone org page — org-page mint candidate noted, not minted on a do-not-publish card)

## Wayback re-anchor check (single-copy risk from 11180842-29)
- `camcinc.org/international_fest/borek.pdf`: CDX `[]`, availability API `{"archived_snapshots": {}}` — still **NO Wayback capture** as of 2026-11-19 (`wayback-camcinc-borek-cdx.json`, `wayback-camcinc-borek-avail.json`). Local copy `knowledge/web-archives/peter-hsu-frontier-11180842-29/camcinc-borek-isf-email-chain-2009.md` remains likely sole render.

## Baked-fact dispositions
- Corpus works/articles (corpus=1 on this card): not re-harvested — builder offline at emit; corpus lane verified-saturated by the 2026-10-07/10-08 DEEPEN-X greps + 2026-11-14 whole-corpus sweep. Under ## Skipped on the person page.
- Dated archive lines: dry-run does not fetch; none baked into the card body. Already absorbed on the person page From-the-record table. Under ## Skipped.
- zh.wp infobox / Wikidata FETCH lines: run as arms 1–2, both miss.

## New same-name exclusions this pass
- SCCA Solo Nationals `Peter Hsu`, Minneapolis MN, 2019 Honda Type R (DS class), 2024 + 2026 entries, Badlands Region — motorsport driver, different person; excluded, no fact imported.

## Result
No new From-the-record rows this pass (all web hits duplicate already-archived sources; CA branch lead blocked at 3 registry surfaces). Arms: zh.wp miss / Wikidata miss / official miss / ZH press miss. Registry pre-check: 3/3 collision with own person page (target resolved). Wayback single-copy risk persists. Ledger receipt: `content/sources/peter-hsu-frontier-11190824-36-2026-11-19.md`.
