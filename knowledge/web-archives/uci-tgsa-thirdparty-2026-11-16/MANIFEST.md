# TGSA @ UC Irvine third-party capture manifest — 2026-11-16 (card t_4391f114)

Fetched live with curl (Mozilla UA) on 2026-11-16 ~04:20–04:25 PST from this box; each file's
on-disk mtime is the fetch time. Key strings verified per file before use.

| file | URL | fetched | status / key strings |
|---|---|---|---|
| wayback-clubs-uci-tgsa-20191209.html | http://web.archive.org/web/20191209145103/http://clubs.uci.edu:80/tgsa/ | 2026-11-16 | HTTP 200, 22,247 B. First-party club site snapshot, title 「UCI 研究所 台灣同學會 - TGSA - Taiwanese graduate student association at UCI」, nav 最新消息/關於我們/新生手冊/學術沙龍/聯絡我們, "UCI TGSA是加州大學爾灣分校註冊學生會(registered student organization)，由一群研究所學生組織", events 「UCI TGSA 農曆過年 圍爐啦」 dated **February 12, 2018** (頭獎現金 $66) and 「UCI TGSA 2017 跑關迎新」 dated **August 21, 2017** (關卡活動 09/24/2017 (Sun) 下午三點), contact **Email: tgsa@uci.edu**, **Copyright 2017** |
| wayback-google-sites-ucitgsa-20201017.html | http://web.archive.org/web/20201017125824/https://sites.google.com/site/ucitgsa/ | 2026-11-16 | HTTP 200, 40,711 B. First-party Google Sites snapshot, title 「UC Irvine 台灣研究生學生會 Taiwanese Graduate Student Association, UC-Irvine」, sections 新生特區/About Us/歷任會長-副會長/學生會幹部&Email/女性專區, **2017 會長 謝大洋 Diane (tayangh@uci.edu) / 袁則安 Joann (tzeany@uci.edu)**, three-goal mission statement (Promote understanding of Taiwanese culture; organize social/educational/academic/cultural/humanitarian activities; provide services to new Taiwanese graduate students), self-statement 「本網站已於2017年停止更新，請至新版官方網站：https://clubs.uci.edu/tgsa/」, news posts 2017/2016/2014/2013/2012/2011 新生說明會 + 2011 除夕圍爐, archive strip 「顯示 1 - 7 篇文章 (共 64 篇)」 |
| github-uci-tgsa-org.json | https://api.github.com/orgs/uci-tgsa | 2026-11-16 | HTTP 200. name "Taiwanese Graduate Student Association (TGSA) @ UCI", blog http://clubs.uci.edu/tgsa, location University of California, Irvine, public_repos 1, org created_at 2019-03-06T05:34:12Z, updated_at 2019-03-06T05:46:59Z |
| github-uci-tgsa-repos.json | https://api.github.com/orgs/uci-tgsa/repos?per_page=100 | 2026-11-16 | HTTP 200. single repo `uci-tgsa/newbie-guidebook`, created_at 2019-03-06T05:38:45Z, pushed_at **2023-04-30T14:37:37Z**, updated_at 2019-06-01T21:48:57Z (⇒ TAH ¶2 "last repository update June 2019" = the GitHub `updated_at` field, not the latest push) |
| github-newbie-guidebook-live.html | https://github.com/uci-tgsa/newbie-guidebook | 2026-11-16 | HTTP 200, 227,123 B. Repo page, branch master, README.md + index present |
| moe-la-contacts.html | https://depart.moe.edu.tw/la/cp.aspx?n=7FC7F97C86931EA0&s=6D36777C6E4F8C89 | 2026-11-16 | HTTP 200, 164,019 B. MOE 駐洛杉磯台北經濟文化辦事處教育組 美西南區同學會聯絡資料. UCI block: 「Taiwanese Graduate Student Association（TGSA/臺灣研究生同學會） 臉書社群：https://www.facebook.com/groups/6199015193/ https://www.facebook.com/groups/ucitgsa2024」; separate UCI TNO block (臺灣學生會, UCITNO) confirms distinct campus orgs |
| tah-org-page-live.html | https://taiwaneseamericanhistory.org/organization/taiwanese-graduate-student-association-at-uc-irvine/ | 2026-11-16 | HTTP 200, 51,782 B. Live TAH directory page adds vs the 2026-08-17 JSON capture: banner 「This organization is no longer active or its current status is unknown.」 and infobox (Abbreviation TGSA / Hanzi Name UCI台灣研究生學生會 / School University of California, Irvine / Primary Region Irvine, California / Website sites.google.com…) |
| ptt-ucirvine-2016-orientation.html / ptt-ucptt-2016-orientation-failed.html | http://cn.ucptt.com/article/studyabroad/1465892270/0E0 | 2026-11-16 | HTTP 200 but 163 B PHP fatal error page — mirror dead at fetch time, content NOT archived. Search-snippet-only corroboration (2016-06-14 PTT post 「UCIrvine 2016 新生说明会」 by Avle, UCI-TGSA 新生說明會 6/21 台北市立總圖11樓). Original ptt.cc URL 404; no Wayback snapshot for either URL |

## Corroboration ruling
The two Wayback captures are **first-party** TGSA-authored pages (club site + official Google
Sites) reached via URLs the TAH record itself names — they corroborate the Chinese self-name
(UCI 研究所 台灣同學會 / UC Irvine 台灣研究生學生會), a real mission statement, named 2017
officers, dated 2011–2018 activities, and the contact tgsa@uci.edu. The MOE LA education-division
directory is a **third-party** (ROC government) listing that independently confirms the org name,
abbreviation, and 2024-era Facebook handles (ucitgsa2024 → activity in 2024). The GitHub API
records are platform third-party records for the same org handle the TAH record claims.

## Searches run (budget ≤8, all on this org name/handles)
1. web_search `TGSA UC Irvine 台灣研究生學生會` → TAH live page, MOE LA list, echopedia, UCI sibling pages
2. web_search `"ucitgsa" OR "uci-tgsa" Taiwanese graduate student` → MOE LA, PTT 2016 mirror snippet, UCR/UCSD sibling TGSA (do not merge)
3. web_search `"UCI" OR "UC Irvine" "TGSA" 研究生同學會 活動` → same set; UCSD TGSA + UCR TGSA sibling hits only
4. Wayback availability API probes (not web searches): facebook.com/groups/ucitgsa → none; ucitgsa2024 → none; github.com/uci-tgsa → none; clubs.uci.edu/tgsa → 2019-12-09 (fetched); sites.google.com/site/ucitgsa → 2020-10-17 (fetched); cn.ucptt mirror → none
5. Live fetches (curl): MOE LA page, TAH live page, GitHub API ×2 + repo page, Wayback replays ×2, PTT mirror (failed)

Negatives: no Wikipedia/Wikidata article; no 華文 press (世界日報/大紀元/台灣日報) item naming UCI TGSA
surfaced; FB groups ucitgsa / ucitgsa2024 not archived and login-walled live; PTT 2016 post body not
archivable from this box (mirror PHP-fatal, original 404, no Wayback).
