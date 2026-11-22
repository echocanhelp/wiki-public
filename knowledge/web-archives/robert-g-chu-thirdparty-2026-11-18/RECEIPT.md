# Frontier harvest receipt — Robert G. Chu 朱靜懷 (FRONTIER-11180842-24)

Date: 2026-11-18 (PST). Tier M. Do-not-publish; commit only. Target: [[people/robert-g-chu|Robert G. Chu 朱靜懷]].
Dangling target closed: `works/taiwaneseamericanhistory-org/whos-who-2144-robert-g-chu`.

## Arm verdicts (searched 2144. Robert G. Chu 朱靜懷 / 朱靜懷 / "Robert G. Chu", 2026-11-18)

1. **zh.wikipedia infobox+awards — MISS.** API `action=query&list=search&srsearch=朱靜懷` → totalhits 10,477, all
   fuzzy-token rows (朱慈煥, 朱慈炤, 成穆貴妃, 明穆宗… Ming-dynasty / singer / list pages; same negative as the
   2026-11-17 pass); `srsearch="朱靜懷"` (exact quoted) → **totalhits 0**. `en.wikipedia` `srsearch="Robert G. Chu"`
   → totalhits 0; `srsearch="Robert Chu" judge` → totalhits 2 (`Betty Tom Chu`, `Pan Nam` — different people).
   No WP article for this subject exists. Archived: `wp-zh-zhu-jing-huai.json`, `wp-zh-zhu-jing-huai-quoted.json`,
   `wp-en-robert-g-chu-quoted.json`, `wp-en-robert-chu-judge.json`.
2. **Wikidata claims — MISS.** `wbsearchentities` (en) `Robert G. Chu` → `search: []`; `朱靜懷` → `search: []`;
   `Robert Chu judge` → `search: []`. No item, so no conflicting claims; nothing to HOLD on conflict.
   (A missing item is a NEED, not a negative finding about the person.)
   Archived: `wd-robert-g-chu.json`, `wd-zhujinghuai.json`, `wd-search-Robert%20Chu%20judge.json`.
3. **Official site / event page — ABSORB (primary).** The Governor's own appointment press release is live on the
   State of California archive: `https://archive.gov.ca.gov/archive/gov39/2018-06-27/governor-brown-appoints-10-superior-court-judges/index.html`
   (curl-fetched 2026-11-18, 66,258 B → `gov-ca-variantA.html`; note the working URL has NO trailing slash — the
   slash form 404s, and Wayback has NO capture of it: `gov-ca-wayback-avail.json` = `{}`, CDX empty `gov-ca-cdx*.json`).
   Row facts (gov release, 2018-06-27): "Robert G. Chu, 38, of Valencia, has been appointed to a judgeship in the
   Los Angeles County Superior Court… deputy public defender… since 2006, where he has held several positions,
   including a supervising deputy public defender. He was an associate at Masry and Vititoe in 2006. Chu earned a
   Juris Doctor degree from the Southwestern Law School and a Bachelor of Arts degree from the University of
   California, Los Angeles. He fills the vacancy created by the conversion of a court commissioner position on
   March 1, 2018. Chu is a Democrat." This is the PRIMARY source that the 2026-11-17 pass cited only via
   secondary renders (Ballotpedia + Southwestern letter + Daily Journal).
   - Corroborating republics of the same release, archived this pass: `socal-appellate-2018-06.html`
     (socal-appellate.blogspot.com, verbatim release text), `californianewswire-appoints-10.html`.
   - **hometownstation (KHTS Santa Clarita) 2018-06-28** — local press re-report: adds the four-appointee LA
     context (Puente-Porras, Roberts, Garcia Uhrig), "$200,042 annually", "All of the judge appointees are
     Democrats", and the six-year-term/election mechanics explainer. `hometownstation-valencia.html`.
   - Ballotpedia `Robert_Chu` re-fetched cleanly this pass (90,933 B, was blocked on 11-17):
     `ballotpedia-robert-chu.html` — tenure 2018–Present, Term ends 2027, appointed 2018-06-27, 2026 canceled
     primary/general win without appearing on ballot, 2020 sole-filer default win, career ladder, no endorsements,
     2020/2026 Candidate Connection surveys not completed.
   - Southwestern letter re-anchored to a NEWER Wayback capture than the 11-17 pass used:
     `swlaw-wayback-avail.json` closest = `20251015053533`; body archived `swlaw-letter-wayback.html` (125 KB).
     11-17 pass used `20250116091008`. Content unchanged for our quoted rows.
   - Still blocked: `dailyjournal.com/judicial_profile/9104` (Sucuri) — 11-17 secondary render stands;
     `goodparty.org` (Vercel shell) — not re-attempted this pass.
4. **ZH press (World Journal / 大紀元 / 台灣日報) — MISS (re-confirmed, 3 searches 2026-11-18).** Queries
   `「朱靜懷」 法官 洛杉磯`, `「Robert G. Chu」 judge … appointed Brown 2018`, and
   `"Robert Chu" Valencia judge 華語 法官 台裔 洛杉磯 任命`: every 朱靜懷 row is the TAH record itself, its own
   site mirrors/pagination pages, or the mainland 朱静怀 信用合作社 article author (cqvip.com, 2010 — excluded,
   see page `## Name collision`). No 世界日報 / 大紀元 / 台灣日報 coverage of the 2018 Brown appointment exists
   as of this date. **The hanzi↔English bridge therefore still rests on the TAH record alone — GAPS open.**

## Identity note

Bridge tuple unchanged and consistent across all fetched artifacts this pass: `Robert G. Chu` + Valencia CA +
age 38 at 2018-06-27 + LA County Superior Court + Southwestern Law School J.D. + UCLA + PD 2006–2018 +
Masry & Vititoe 2006 (gov release, KHTS, Southwestern letter, Ballotpedia all agree). Hanzi 朱靜懷 appears only
with the TAH record — merge rule: English-corroborated facts absorbed; hanzi-linked facts stay `alleged`.

## Skipped (baked facts not used)

- **Corpus works/articles co-occurrence:** not re-run — builder offline; 8 prior DEEPEN-X sweeps
  (2026-09-18 → 10-08) verified-saturated on all name forms.
- **Dated archive lines:** dry-run emitted none to read at emit time (builder offline).
- **judicialfinder.com/judges/robert-chu** (search-surfaced aggregator; merit-selection boilerplate,
  tenure/education already primary-sourced) — not fetched.
- **change.org "Chu Seat" petitions page** (non-biographical) — not fetched.
- **Ballotpedia `Judges_appointed_by_Jerry_Brown`** (0 bytes to curl on 11-17): the gov release itself is now
  archived, which supersedes this NEED row for our subject only.
