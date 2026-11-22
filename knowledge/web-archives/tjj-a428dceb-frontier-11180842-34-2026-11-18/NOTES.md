# Frontier NOTES — t_c0aac922 / FRONTIER-11180842-34

Target: TJJ article `articles/taiwanjustice-net/2018/20180721091303_2018_07_20_抗議-南加州台大校友會邀管中閔來年會做專題演講_a428dcebbceacf38` (tier 1, refs=2, dossier_refs=2, corpus=0, score=0).
Pass date: 2026-11-18. Worker: pinto (t_c0aac922). Do-not-publish (Tier-2 firewall target).

## Premise check (dangling target)

- The article exists on disk and is live-linked from 11+ people pages (柯賢清, 賴慧娜, 梁基典, 吳春紅, 鄭錦家, 林美華[HOLD], 邱勝宗, 劉惠麗, 楊美麗, 葉錦如, 葉秀卿) + organizations/taiwanese-association-of-m-kentucky (吳連四 continuity-gap row). Prior saturation: TJJ-A10060600-5 (2026-10-14, 12/12 subject links).
- Dangling side: no organization page existed for the event subject 南加州台大校友會 → minted.
  Missing people: 林美里, 鄭錫堃 (named actors in the event, no pages) → stubs minted.

## Arms (4/4)

1. **zh.wikipedia infobox+awards** — search `南加州台大校友會` (srlimit 10, 34 totalhits, zhwiki_ntuaasc.json): no association article (台大人文庫 etc. only). Event background: 「管中閔」(oldid 87456383) + 「2018年國立臺灣大學校長遴選事件」(Q54458709) confirmed; event article does NOT cover the SoCal annual-meeting protest → the TJJ corpus + CNA/三立/TT coverage is the surviving record of this sub-event. Verdict: **absorb (background only)**.
2. **Wikidata claims** — `管中閔` → Q6441079 (Kuan Chung-ming, 38 claims, wd_q6441079.json); `拔管` → Q54458709 (alias match, wd_baguan.json). Neither carries statements about the 2018-07-21 LA annual meeting or the 連署 → **no conflict; HOLD-on-conflict not triggered**. Verdict: **absorb (background only)**.
3. **official site / event page** — ntuaasc.org live fetch (ntuaasc-home-live.html, 2026-11-18): 第53屆年會 2026-07-11, 會長 林永森 / 第54屆 賴怡徽, NTU centennial fundraising (>$100k in 2 yrs; NC >$600k, NY >$400k), address Arcadia CA. CDX: site archived since 1999-10-02. 2018 event page itself not preserved (Wix-era site; 2016-era CDX captures are pre-Wix). Verdict: **absorb**.
4. **ZH press** — Taipei Times 2018-07-08 (live fetch, clean text), 三立 SETN 2018-07-20 CNA wire (live fetch), Newtalk 2018-07-21 same wire (Wayback 20180722113602id_), 中央社 CNA 2018-07-22 分裂報導 (Wayback 20180925104142id_ + live copy), 正報/中通社 2018-07-23 (fetch blocked first try — text held from search extract, flagged), 大紀元 2019-07-16 翌年年會 (Wayback 20250222010237id_). World Journal / 大紀元(2018 event-day) / 台灣日報: no 2018 event-day hits found upstream → those outlets remain **HOLD/miss** (searched 2026-11-18). Verdict: **absorb**.

## Key new facts (absorbed)

- 第45屆年會: 2018-07-21, Pacific Palms Resort; 會長 周述蓉; 朱文祥 監交接+致詞; 演說 14:30-16:30.
- 演說題目 2 versions → **HOLD** (「台大怎麼辦？台大校長遴選到台大精神重建」官方提供 vs「台大新價值、台灣新意志」中通社現場).
- 連署 counts by time: ~50 請願 (TT 7/8) → ~170 roster 全文登報 (TJJ 7/19-20) → 「200多位」 (CNA 7/20). Never collapse.
- 「台美人台大校友會」split announced at presser 2018-07-21; 發言人 前理事 林美里 讀聲明 (CNA).
- 賴慧娜 = 南加台大校友會永久會員, 具名受訪 7/20 with 鄭錫堃 (台大農業工程系) — strengthens 系所 agreement for hui-na-lin (alleged → documented-by-wire).
- 管中閔 quotes: 「我把他們的名字都背起來了」; deleted ~half of speech the night before due to protest; 「管爺加油」; 「不是大家太專心，就是全都睡著了」; 小圓石 poem; 陳維昭 quote (正報/中通社).
- 2019-07-13 翌年年會: 管中閔 as president, 王錦鴻 接任會長 (大紀元).

## HOLD ledger

- 演說題目 dual version (above).
- 創會年份 ~1974 inferred from 屆次 — alleged only.
- roster 內「林美里(歷史)」是否即前理事林美里 — HOLD (no comparable fields).
- 鄭錫堃 not in roster (only 鄭英松(農工)) — whether co-signer or interviewee-only — HOLD; his English romanization is ours, not sourced.
- 林美里(婦女信箱 1994 partner of 賴慧娜) = 林美里(2018 發言人) — same-person inference, alleged (both NTU alumni, SoCal, 婦女+台大多公共領域; no direct proof).

## GAPS (new)

- 台美人台大校友會 (split org) has no page and no post-2018 activity source found.
- 周述蓉, 朱文祥, 王錦鴻, 陳維昭-adjacent SoCal roles: no pages; not minted (not frontier targets here).
- 鄭錫堃 bio fields (EN name, grad year, occupation) — none found in any arm.

## ## Skipped (baked facts not used)

- 「Corpus works/articles: see co-occurrence count above (builder is offline)」— corpus=0, nothing to harvest; co-occurrence row unused.
- 「Dated archive lines: read at emit time; dry-run does not fetch」— the archive lines (archive_url/archive_ts/digest) were read from the article frontmatter and quoted into the capture bundle; no additional dated archive lines emitted.
- Wikidata conflict-HOLD machinery — no conflicting claims found, so the HOLD branch itself was unused (arms still recorded as miss/no-conflict).
- 大紀元 2019 年會報導的 photo caption (袁玫／大紀元) — not used (no image ingest in frontier pass).

## Files touched

- NEW content/sources/ntuaasc-2018-guan-speech-captures.md
- NEW content/organizations/ntu-alumni-association-of-southern-california.md
- NEW content/people/lin-mei-li.md
- NEW content/people/zheng-xikun.md
- EDIT content/people/hsien-ching-ko.md (From the record context row)
- EDIT content/people/hui-na-lin.md (From the record: named interview upgrade)
- NEW knowledge/web-archives/tjj-a428dceb-frontier-11180842-34-2026-11-18/ (17 captures: 8 HTML + 9 JSON incl. CDX evidence)

## Lint

dossier-lint.py EXIT=0 on all 6 touched pages (1 WARN simplified-char fixed).
