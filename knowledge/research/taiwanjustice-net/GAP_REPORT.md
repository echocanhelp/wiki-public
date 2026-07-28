# GAP_REPORT — taiwanjustice.net residual archive gaps

**Generated:** 2026-07-28T16:47:01Z  
**Script:** `gap_fill.py 1.1`  
**Kanban:** `t_6b71e5a7` TJ-P4  

## Context

After Wayback bulk download (P2) + fail-retry (P2b), residual download-state fails were checked against secondary archives.

| Metric | Count |
|--------|------:|
| Residual fails (download-state) | 202 |
| Content URLs checked | 118 |
| Non-content skipped (media/feed/etc.) | 84 |
| Recoverable from ≥1 secondary source | 66 |
| Still missing all secondaries | 52 |
| Arquivo.pt hits | 26 |
| Ghostarchive per-URL hits | 26 |
| IA CDX recheck hits | 56 |
| Ghostarchive domain-level hits | 1 |

## Source availability (from pinto, this run)

- **Arquivo.pt CDX:** used as primary secondary index
- **Ghostarchive:** HTML search `?term=` works; domain search returned 1 hit(s)
- **Internet Archive CDX:** best-effort recheck (timeouts/503 possible)
- **Common Crawl index:** **unavailable** from this host — `('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))`
- **Memento TimeTravel (`timetravel.mementoweb.org`):** DNS resolve failed on pinto

## Ghostarchive domain captures

- [Wed, 17 Aug 2022 22:43:40 GMT](https://ghostarchive.org/archive/HVe5N) — `https://www.taiwanjustice.net/2022/08/15/%E4%BF%84%E4%BE%B5%E7%83%8F%E6%88%B0%E7%88%AD172%E5%A4%A9-%E6%B3%95%E5%9C%8B%E5%89%8D%E4%B8%8A%E6%A0%A1-%E6%8E%A5%E8%BF%91%E6%AD%90%E7%B1%B3%E8%8C%84%E9%BB%9E/`

## Recoverable residual content URLs (sample)

- `https://taiwanjustice.net/%E5%8F%B0%E7%81%A3%E6%BC%94%E7%BE%A9-20210509-%E5%98%89%E5%8D%97%E5%A4%A7%E5%9C%B3%E8%88%87%E5%85%AB%E7%94%B0%E8%88%87%E4%B8%80/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20250420103434id_/https://taiwanjustice.net/%E5%8F%B0%E7%81%A3%E6%BC%94%E7%BE%A9-20210509-%E5%98%89%E5%8D%97%E5%A4%A7%E5%9C%B3%E8%88%87%E5%85%AB%E7%94%B0%E8%88%87%E4%B8%80/
- `https://taiwanjustice.net/%E6%9C%89%E8%A9%B1%E5%A5%BD%E8%AA%AA-20200820-%E5%8F%B0%E7%81%A3%E5%B0%81%E6%AE%BA%E6%84%9B%E5%A5%87%E8%97%9D%EF%BC%81%E5%8F%8D%E5%88%B6%E4%B8%AD%E5%9C%8B%E5%A4%A7%E5%A4%96%E5%AE%A3%EF%BC%9F/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20250515185333id_/https://taiwanjustice.net/%E6%9C%89%E8%A9%B1%E5%A5%BD%E8%AA%AA-20200820-%E5%8F%B0%E7%81%A3%E5%B0%81%E6%AE%BA%E6%84%9B%E5%A5%87%E8%97%9D%EF%BC%81%E5%8F%8D%E5%88%B6%E4%B8%AD%E5%9C%8B%E5%A4%A7%E5%A4%96%E5%AE%A3%EF%BC%9F/
- `https://taiwanjustice.net/%E7%BE%8E%E5%9C%8B%E5%8B%99%E9%99%A2%E6%8E%A8%E6%96%87%E3%80%8C%E8%B4%88%E5%8F%B0%E7%96%AB%E8%8B%97%E5%87%BA%E7%99%BC%E4%BA%86%E3%80%8D%EF%BC%8C%E8%95%AD%E7%BE%8E%E7%90%B4%E8%A6%AA%E9%80%81%E6%A9%9F/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20250713113723id_/https://taiwanjustice.net/%E7%BE%8E%E5%9C%8B%E5%8B%99%E9%99%A2%E6%8E%A8%E6%96%87%E3%80%8C%E8%B4%88%E5%8F%B0%E7%96%AB%E8%8B%97%E5%87%BA%E7%99%BC%E4%BA%86%E3%80%8D%EF%BC%8C%E8%95%AD%E7%BE%8E%E7%90%B4%E8%A6%AA%E9%80%81%E6%A9%9F/
- `https://taiwanjustice.net/%E6%96%B0%E8%81%9E%E6%8C%96%E6%8C%96%E5%93%87-20220726-%E5%81%B7%E5%90%83%E4%BA%BA%E5%A6%BB%E6%AF%94%E8%BC%83%E7%88%BD%EF%BC%9F%E9%A6%AC%E6%96%AF%E5%85%8B%E4%B8%96%E7%95%8C%E9%A6%96%E5%AF%8C%E8%AE%8A/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20250808013426id_/https://taiwanjustice.net/%E6%96%B0%E8%81%9E%E6%8C%96%E6%8C%96%E5%93%87-20220726-%E5%81%B7%E5%90%83%E4%BA%BA%E5%A6%BB%E6%AF%94%E8%BC%83%E7%88%BD%EF%BC%9F%E9%A6%AC%E6%96%AF%E5%85%8B%E4%B8%96%E7%95%8C%E9%A6%96%E5%AF%8C%E8%AE%8A/
- `https://taiwanjustice.net/%E5%B9%B4%E4%BB%A3%E6%99%9A%E5%A0%B1-20220817-%E9%BB%83%E5%9C%8B%E6%98%8C%E6%8E%A7%E7%82%92%E5%9C%B0%E6%B5%B7%E6%92%881-2%E5%84%84-%E6%9E%97%E7%82%BA%E6%B4%B2%E8%81%B2%E6%98%8E%E5%96%8A%E5%91%8A/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20251010062933id_/https://taiwanjustice.net/%E5%B9%B4%E4%BB%A3%E6%99%9A%E5%A0%B1-20220817-%E9%BB%83%E5%9C%8B%E6%98%8C%E6%8E%A7%E7%82%92%E5%9C%B0%E6%B5%B7%E6%92%881-2%E5%84%84-%E6%9E%97%E7%82%BA%E6%B4%B2%E8%81%B2%E6%98%8E%E5%96%8A%E5%91%8A/
- `http://www.taiwanjustice.net/category/wikileaks/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20171109043224id_/http://www.taiwanjustice.net:80/category/wikileaks/
- `https://www.taiwanjustice.net/?cat=96651`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?feed=rss2&cat=31301`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?cat=58&filter_by=random_posts`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=249644`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=139855`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?cat=59&filter_by=featured`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=367346`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=114049`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=104128`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=381953`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?tag=%E4%BD%99%E5%BF%A0%E6%9D%91%E8%80%81%E5%B8%AB%E7%89%B9%E8%A3%BD%E8%97%9D%E8%A1%93%E5%93%81%E7%BE%A9%E8%B3%A3`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=114159`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=130455`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?tag=%E6%9F%AF%E6%96%87%E5%93%B2%E8%BE%B2%E5%9C%B0%E6%9C%AA%E6%94%B9%E5%96%84`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?cat=176581`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=51320`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=386880`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=385179`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?tag=%E5%87%B1%E9%81%94%E6%A0%BC%E8%98%AD%E5%AD%B8%E6%A0%A1`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=316314`
  - sources: arquivo, ghostarchive
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=390582`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?tag=china-airlines%E5%8F%B0%E7%81%A3%E8%8F%AF%E8%88%AA`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?tag=%E7%BE%8E%E5%8F%83%E9%99%A2%E6%8E%A8%E6%B3%95%E6%A1%88-%E5%8A%A0%E9%80%9F%E7%BE%8E%E6%AD%90%E5%B0%8D%E5%8F%B0%E7%A7%BB%E4%BA%A4%E6%AD%A6%E5%99%A8%E6%B5%81%E7%A8%8B`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=75950`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/?p=386799`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `http://www.taiwanjustice.net/2017/09/02/%E5%8F%8D%E6%94%BB%E5%A4%A7%E9%99%B8%EF%BC%9A%E8%94%A3%E4%BB%8B%E7%9F%B3%E7%9A%84%E7%BE%8E%E5%A4%A2%EF%BC%8C%E7%BE%8E%E5%9C%8B%E4%BA%BA%E7%9A%84%E5%99%A9%E5%A4%A2-%EF%BC%88%E4%BA%8C%EF%BC%89%E2%97%8E/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20171220121033id_/http://www.taiwanjustice.net:80/2017/09/02/%E5%8F%8D%E6%94%BB%E5%A4%A7%E9%99%B8%EF%BC%9A%E8%94%A3%E4%BB%8B%E7%9F%B3%E7%9A%84%E7%BE%8E%E5%A4%A2%EF%BC%8C%E7%BE%8E%E5%9C%8B%E4%BA%BA%E7%9A%84%E5%99%A9%E5%A4%A2-%EF%BC%88%E4%BA%8C%EF%BC%89%E2%97%8E/
- `https://www.taiwanjustice.net/2020/06/16/%e3%80%8c%e8%9d%99%e8%9d%a0%e3%80%8d%e6%8f%9b%e3%80%8c%e9%ae%ad%e9%ad%9a%e3%80%8d%e3%80%80%e3%80%8c%e6%ad%a6%e6%bc%a2%e7%97%85%e6%af%92%e3%80%8d%e5%85%a5%e4%be%b5%e5%8c%97%e4%ba%ac%e5%9f%8e-%e2%97%8e/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20200622092126id_/https://www.taiwanjustice.net/2020/06/16/%e3%80%8c%e8%9d%99%e8%9d%a0%e3%80%8d%e6%8f%9b%e3%80%8c%e9%ae%ad%e9%ad%9a%e3%80%8d%e3%80%80%e3%80%8c%e6%ad%a6%e6%bc%a2%e7%97%85%e6%af%92%e3%80%8d%e5%85%a5%e4%be%b5%e5%8c%97%e4%ba%ac%e5%9f%8e-%e2%97%8e/
- `https://www.taiwanjustice.net/2020/11/21/%E6%96%87%E7%B8%BD%E8%9E%8D%E5%90%88%E6%96%B0%E8%88%8A%E6%96%87%E5%8C%96-%E6%89%93%E9%80%A0%E8%90%AC%E8%8F%AF%E5%A4%A7%E9%AC%A7%E7%86%B1%E5%98%89%E5%B9%B4%E8%8F%AF%E5%BD%B1/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20201205145014id_/https://www.taiwanjustice.net/2020/11/21/%E6%96%87%E7%B8%BD%E8%9E%8D%E5%90%88%E6%96%B0%E8%88%8A%E6%96%87%E5%8C%96-%E6%89%93%E9%80%A0%E8%90%AC%E8%8F%AF%E5%A4%A7%E9%AC%A7%E7%86%B1%E5%98%89%E5%B9%B4%E8%8F%AF%E5%BD%B1/
- `https://www.taiwanjustice.net/2021/03/03/%E9%80%99%EF%BC%81%E4%B8%8D%E6%98%AF%E6%96%B0%E8%81%9E-20210303%E3%80%8Caz%E7%96%AB%E8%8B%97%E3%80%8D%E9%A3%9B%E5%9C%A8%E7%A9%BA%E4%B8%AD%E6%89%8D%E7%9F%A5%E8%B2%A8%E4%BE%86%E4%BA%86%EF%BC%81%E6%8A%B5/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20210419124846id_/https://www.taiwanjustice.net/2021/03/03/%E9%80%99%EF%BC%81%E4%B8%8D%E6%98%AF%E6%96%B0%E8%81%9E-20210303%E3%80%8Caz%E7%96%AB%E8%8B%97%E3%80%8D%E9%A3%9B%E5%9C%A8%E7%A9%BA%E4%B8%AD%E6%89%8D%E7%9F%A5%E8%B2%A8%E4%BE%86%E4%BA%86%EF%BC%81%E6%8A%B5/
- `https://www.taiwanjustice.net/2021/01/13/%E7%AA%81%E7%99%BC%E7%90%AA%E6%83%B3-20210113-%E7%9C%9F%E7%9A%84%E4%BA%82%E4%BA%86%E5%85%A8%E7%90%83%E6%B0%A3%E5%80%99%E8%B6%85%E8%A9%AD%E7%95%B0%E3%80%8C%E9%80%99%E4%BA%9B%E5%9C%B0%E6%96%B9/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20210121182619id_/https://www.taiwanjustice.net/2021/01/13/%E7%AA%81%E7%99%BC%E7%90%AA%E6%83%B3-20210113-%E7%9C%9F%E7%9A%84%E4%BA%82%E4%BA%86%E5%85%A8%E7%90%83%E6%B0%A3%E5%80%99%E8%B6%85%E8%A9%AD%E7%95%B0%E3%80%8C%E9%80%99%E4%BA%9B%E5%9C%B0%E6%96%B9/
- `https://www.taiwanjustice.net/?p=79527`
  - sources: arquivo, ghostarchive, internet_archive_cdx
  - snapshot: https://arquivo.pt/wayback/20190626053819/https://www.taiwanjustice.net/
- `https://www.taiwanjustice.net/2021/06/10/%E7%AA%81%E7%99%BC%E7%90%AA%E6%83%B3-20210610-%E9%BB%91%E7%AE%B1%EF%BC%81%E7%89%B9%E6%AC%8A%EF%BC%81%E6%8F%92%E9%9A%8A%EF%BC%81%E4%BA%BA%E6%B0%91%E8%8B%A6%E7%AD%89%E7%96%AB%E8%8B%97-%E5%90%84/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20210616072544id_/https://www.taiwanjustice.net/2021/06/10/%E7%AA%81%E7%99%BC%E7%90%AA%E6%83%B3-20210610-%E9%BB%91%E7%AE%B1%EF%BC%81%E7%89%B9%E6%AC%8A%EF%BC%81%E6%8F%92%E9%9A%8A%EF%BC%81%E4%BA%BA%E6%B0%91%E8%8B%A6%E7%AD%89%E7%96%AB%E8%8B%97-%E5%90%84/
- `https://www.taiwanjustice.net/2021/09/12/%E5%8F%B0%E7%81%A3%E6%8E%A8%E5%BB%A3%E8%8F%AF%E8%AA%9E%E6%95%99%E5%AD%B8%EF%BC%8C%E7%AB%A5%E6%8C%AF%E6%BA%90%E7%9B%BC%E5%9C%A8%E7%BE%8E%E5%9C%8B%E4%B8%BB%E6%B5%81%E7%A4%BE%E6%9C%83%E7%94%9F%E6%A0%B9/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20210927010548id_/https://www.taiwanjustice.net/2021/09/12/%E5%8F%B0%E7%81%A3%E6%8E%A8%E5%BB%A3%E8%8F%AF%E8%AA%9E%E6%95%99%E5%AD%B8%EF%BC%8C%E7%AB%A5%E6%8C%AF%E6%BA%90%E7%9B%BC%E5%9C%A8%E7%BE%8E%E5%9C%8B%E4%B8%BB%E6%B5%81%E7%A4%BE%E6%9C%83%E7%94%9F%E6%A0%B9/
- `https://www.taiwanjustice.net/2021/07/21/%E5%8F%B0%E7%81%A3%E6%B8%85%E8%8F%AF%E5%A4%A7%E5%AD%B8%E6%88%90%E7%AB%8B%E5%8D%8A%E5%B0%8E%E9%AB%94%E5%AD%B8%E9%99%A2-pk%E4%B8%AD%E5%9C%8B%E6%B8%85%E8%8F%AF/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20210724182559id_/https://www.taiwanjustice.net/2021/07/21/%E5%8F%B0%E7%81%A3%E6%B8%85%E8%8F%AF%E5%A4%A7%E5%AD%B8%E6%88%90%E7%AB%8B%E5%8D%8A%E5%B0%8E%E9%AB%94%E5%AD%B8%E9%99%A2-pk%E4%B8%AD%E5%9C%8B%E6%B8%85%E8%8F%AF/
- `https://www.taiwanjustice.net/2021/12/04/%E6%8B%9C%E7%99%BB%E5%85%A8%E7%90%83%E6%B0%91%E4%B8%BB%E5%B3%B0%E6%9C%83%E5%9C%A8%E5%8D%B3%EF%BC%8C%E5%8C%97%E4%BA%AC%E8%BE%A6%E3%80%8C%E9%AB%98%E7%AB%AF%E8%A8%8E%E8%AB%96%E6%9C%83%E3%80%8D%E4%BA%82/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220127024857id_/https://www.taiwanjustice.net/2021/12/04/%E6%8B%9C%E7%99%BB%E5%85%A8%E7%90%83%E6%B0%91%E4%B8%BB%E5%B3%B0%E6%9C%83%E5%9C%A8%E5%8D%B3%EF%BC%8C%E5%8C%97%E4%BA%AC%E8%BE%A6%E3%80%8C%E9%AB%98%E7%AB%AF%E8%A8%8E%E8%AB%96%E6%9C%83%E3%80%8D%E4%BA%82/
- `https://www.taiwanjustice.net/2021/02/06/%E3%80%90%E9%80%B1%E6%9C%AB%E6%BC%AB%E8%AB%87%E9%9F%B3%E6%A8%82-53%E3%80%91albert-einstein-%E7%9A%84%E9%9F%B3%E6%A8%82%E4%B8%96%E7%95%8C-%E5%B0%8D%E4%BD%9C%E6%9B%B2%E5%AE%B6%E7%9A%84%E8%A9%95/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20210303211917id_/https://www.taiwanjustice.net/2021/02/06/%E3%80%90%E9%80%B1%E6%9C%AB%E6%BC%AB%E8%AB%87%E9%9F%B3%E6%A8%82-53%E3%80%91albert-einstein-%E7%9A%84%E9%9F%B3%E6%A8%82%E4%B8%96%E7%95%8C-%E5%B0%8D%E4%BD%9C%E6%9B%B2%E5%AE%B6%E7%9A%84%E8%A9%95/
- `https://www.taiwanjustice.net/2021/09/13/%E7%AB%8B%E9%99%B6%E5%AE%9B%E5%A4%96%E9%95%B7%E8%A8%AA%E7%BE%8E%EF%BC%8C%E5%B0%87%E8%88%87%E5%B8%83%E6%9E%97%E8%82%AF%E8%A8%8E%E8%AB%96%E5%B0%8D%E4%B8%AD%E9%97%9C%E4%BF%82/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20211025202402id_/https://www.taiwanjustice.net/2021/09/13/%E7%AB%8B%E9%99%B6%E5%AE%9B%E5%A4%96%E9%95%B7%E8%A8%AA%E7%BE%8E%EF%BC%8C%E5%B0%87%E8%88%87%E5%B8%83%E6%9E%97%E8%82%AF%E8%A8%8E%E8%AB%96%E5%B0%8D%E4%B8%AD%E9%97%9C%E4%BF%82/
- `https://www.taiwanjustice.net/2021/12/21/%E5%85%B1%E5%90%8C%E7%A4%BE%EF%BC%9A%E5%AE%89%E5%80%8D%E7%99%BC%E8%A8%80%E6%8C%BA%E5%8F%B0%E5%BE%8C-%E4%B8%AD%E6%96%B9%E9%98%BB%E6%92%93%E6%97%A5%E6%9C%AC%E5%A4%A7%E4%BD%BF%E9%A4%A8%E6%B4%BB%E5%8B%95/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220518163021id_/https://www.taiwanjustice.net/2021/12/21/%E5%85%B1%E5%90%8C%E7%A4%BE%EF%BC%9A%E5%AE%89%E5%80%8D%E7%99%BC%E8%A8%80%E6%8C%BA%E5%8F%B0%E5%BE%8C-%E4%B8%AD%E6%96%B9%E9%98%BB%E6%92%93%E6%97%A5%E6%9C%AC%E5%A4%A7%E4%BD%BF%E9%A4%A8%E6%B4%BB%E5%8B%95/
- `https://www.taiwanjustice.net/2021/10/25/%E7%BE%8E%E5%9C%8B17%E9%96%93%E6%96%B0%E8%81%9E%E6%A9%9F%E6%A7%8B%E6%8F%AD%E9%9C%B2%E8%87%89%E6%9B%B8%E8%AB%B8%E5%A4%9A%E5%8D%B1%E6%A9%9F%E5%90%B9%E5%93%A8%E8%80%85%EF%BC%9A%E8%87%89%E6%9B%B8/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20211207112843id_/https://www.taiwanjustice.net/2021/10/25/%E7%BE%8E%E5%9C%8B17%E9%96%93%E6%96%B0%E8%81%9E%E6%A9%9F%E6%A7%8B%E6%8F%AD%E9%9C%B2%E8%87%89%E6%9B%B8%E8%AB%B8%E5%A4%9A%E5%8D%B1%E6%A9%9F%E5%90%B9%E5%93%A8%E8%80%85%EF%BC%9A%E8%87%89%E6%9B%B8/
- `https://www.taiwanjustice.net/2022/05/21/%E4%B8%96%E8%A1%9B%E8%A1%8C%E5%8B%95%E5%9C%98%E6%8A%B5%E9%81%94%E6%97%A5%E5%85%A7%E7%93%A6%EF%BC%9A%E8%AE%93%E5%9C%8B%E9%9A%9B%E7%9C%8B%E8%A6%8B%E5%8F%B0%E7%81%A3%E5%90%88%E4%BD%9C%E6%84%8F%E9%A1%98/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220813055222id_/https://www.taiwanjustice.net/2022/05/21/%E4%B8%96%E8%A1%9B%E8%A1%8C%E5%8B%95%E5%9C%98%E6%8A%B5%E9%81%94%E6%97%A5%E5%85%A7%E7%93%A6%EF%BC%9A%E8%AE%93%E5%9C%8B%E9%9A%9B%E7%9C%8B%E8%A6%8B%E5%8F%B0%E7%81%A3%E5%90%88%E4%BD%9C%E6%84%8F%E9%A1%98/
- `https://www.taiwanjustice.net/2022/01/06/%E6%9C%89%E8%A9%B1%E5%A5%BD%E8%AA%AA-20220106-%E7%96%AB%E8%8B%97%E4%BF%9D%E8%AD%B7%E5%8A%9B%E9%99%8D%EF%BC%81%E7%AC%AC-3-%E5%8A%91%E6%80%8E%E9%BA%BC%E6%89%93%EF%BC%9F%E5%9C%8B%E9%BC%8E%E6%96%B0/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220521163041id_/https://www.taiwanjustice.net/2022/01/06/%E6%9C%89%E8%A9%B1%E5%A5%BD%E8%AA%AA-20220106-%E7%96%AB%E8%8B%97%E4%BF%9D%E8%AD%B7%E5%8A%9B%E9%99%8D%EF%BC%81%E7%AC%AC-3-%E5%8A%91%E6%80%8E%E9%BA%BC%E6%89%93%EF%BC%9F%E5%9C%8B%E9%BC%8E%E6%96%B0/
- `https://www.taiwanjustice.net/2020/10/25/%E7%BE%8E%E5%9C%8B%E5%A4%A7%E9%81%B8%E5%B9%B4%E9%A2%A8%E6%B3%A2%E6%84%8F%E5%A4%96%E4%B8%8D%E6%96%B7%EF%BC%8C10%E5%80%8B%E9%97%9C%E9%8D%B5%E6%99%82%E5%88%BB%E4%B8%80%E6%AC%A1%E7%9C%8B/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220630080638id_/https://www.taiwanjustice.net/2020/10/25/%E7%BE%8E%E5%9C%8B%E5%A4%A7%E9%81%B8%E5%B9%B4%E9%A2%A8%E6%B3%A2%E6%84%8F%E5%A4%96%E4%B8%8D%E6%96%B7%EF%BC%8C10%E5%80%8B%E9%97%9C%E9%8D%B5%E6%99%82%E5%88%BB%E4%B8%80%E6%AC%A1%E7%9C%8B/
- `https://www.taiwanjustice.net/2022/01/10/%E7%BF%92%E8%BF%91%E5%B9%B3%E4%BB%BB%E5%91%BD%E6%96%B0%E7%96%86%E9%98%B2%E6%9A%B4%E8%AD%A6%E9%95%B7%E5%BD%AD%E4%BA%AC%E5%A0%82%E5%87%BA%E4%BB%BB%E9%A7%90%E6%B8%AF%E9%83%A8%E9%9A%8A%E5%8F%B8%E4%BB%A4/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220701165946id_/https://www.taiwanjustice.net/2022/01/10/%E7%BF%92%E8%BF%91%E5%B9%B3%E4%BB%BB%E5%91%BD%E6%96%B0%E7%96%86%E9%98%B2%E6%9A%B4%E8%AD%A6%E9%95%B7%E5%BD%AD%E4%BA%AC%E5%A0%82%E5%87%BA%E4%BB%BB%E9%A7%90%E6%B8%AF%E9%83%A8%E9%9A%8A%E5%8F%B8%E4%BB%A4/
- `https://www.taiwanjustice.net/2022/09/17/%E5%9C%8B%E9%9A%9B%E5%A4%A7%E9%86%9C%E8%81%9E%EF%BC%9A%E7%BF%92%E8%BF%91%E5%B9%B3%E8%90%BD%E8%B7%91%E4%B8%8A%E5%90%88%E7%B5%84%E7%B9%94%E6%99%9A%E5%AE%B4-%E2%97%8E-%E6%9E%97%E4%BF%9D%E8%8F%AF/`
  - sources: internet_archive_cdx
  - snapshot: https://web.archive.org/web/20220924231700id_/https://www.taiwanjustice.net/2022/09/17/%E5%9C%8B%E9%9A%9B%E5%A4%A7%E9%86%9C%E8%81%9E%EF%BC%9A%E7%BF%92%E8%BF%91%E5%B9%B3%E8%90%BD%E8%B7%91%E4%B8%8A%E5%90%88%E7%B5%84%E7%B9%94%E6%99%9A%E5%AE%B4-%E2%97%8E-%E6%9E%97%E4%BF%9D%E8%8F%AF/

## Still missing (content) — for Freeman if unique copies exist

These residual content URLs were not found in Arquivo.pt / Ghostarchive / IA CDX during this run.
They may still exist only on private disks, email newsletters, or social shares.

- https://taiwanjustice.net/%e9%bb%83%e4%bb%81%e5%8b%b3%ef%bc%8c%e4%ba%94%e6%9c%88%e5%a4%a9%e5%92%8c%e9%8d%be%e6%98%8e%e8%bb%92%e7%9a%84%e5%90%8c%e8%88%87%e4%b8%8d%e5%90%8c-%e2%97%8e%e6%b1%9f%e7%99%be%e9%a1%af/
- https://taiwanjustice.net/%E5%8F%B0%E7%81%A3%E6%BC%94%E7%BE%A9-20220731-%E9%95%B7%E9%9D%92%E6%AD%8C%E7%8E%8B-%E4%BD%99%E5%A4%A9/
- https://taiwanjustice.net/%E5%8F%B0%E7%81%A3%E6%BC%94%E7%BE%A9-20241104-%E5%B0%8F%E7%94%9F%E5%A4%A9%E6%88%90-%E8%97%9D%E7%95%8C%E9%95%B7%E9%9D%92-%E7%9F%B3%E8%8B%B1/
- https://taiwanjustice.net/%E9%9B%85%E7%90%B4%E7%9C%8B%E4%B8%96%E7%95%8C-20210207-ait%E8%99%95%E9%95%B7%E9%85%88%E8%8B%B1%E5%82%91%E5%A4%A7%E8%81%8A%E5%8F%B0%E7%81%A3%E6%96%87%E5%8C%96-%E8%A6%AA%E5%AF%AB%E6%9B%B8%E6%B3%95/
- https://taiwanjustice.net/%E9%BB%98%E5%85%8B%EF%BC%9Acovid-19%E5%8F%A3%E6%9C%8D%E8%97%A5-%E5%A4%A7%E5%B9%85%E9%99%8D%E4%BD%8E%E7%97%85%E6%82%A3%E7%97%85%E6%AF%92%E9%87%8F/
- https://taiwanjustice.net/%E5%85%AC%E8%A6%96%E6%99%9A%E9%96%93%E6%96%B0%E8%81%9E-20200215-%E6%8C%87%E6%8F%AE%E4%B8%AD%E5%BF%83%EF%BC%9A2-16%E8%B5%B7-303%E5%AE%B6%E8%A1%9B%E7%94%9F%E6%89%80%E8%B2%A9%E5%94%AE%E5%8F%A3%E7%BD%A9/
- https://taiwanjustice.net/%E5%8F%B0%E7%81%A330%E6%AD%B2%E4%BB%A5%E4%B8%8B%E9%96%8B%E6%88%B6%E6%95%B8%E5%8D%A0%E6%AF%94%E7%A0%B44%E6%88%90%EF%BC%8C%E5%88%B8%E5%95%86%E6%94%B9%E6%90%B6%E5%B9%B4%E8%BC%95%E6%97%8F%E5%95%86/
- https://taiwanjustice.net/%E6%97%A2%E5%B7%B2%E6%94%B9%E5%AB%81-%E9%82%84%E7%88%AD%E8%B2%9E%E7%AF%80%E7%89%8C%E5%9D%8A%EF%BC%9F-%E2%97%8E-%E9%99%B3%E8%8C%82%E9%9B%84/
- https://taiwanjustice.net/%E5%8F%B0%E7%81%A3%E5%95%9F%E7%A4%BA%E9%8C%84-20221225-%E7%95%99%E7%BE%8E%E6%AD%B8%E5%9C%8B%E4%B8%8D%E5%AD%9D%E5%A5%B3%E5%81%95%E7%94%B7%E5%8F%8B%E5%BC%92%E7%88%B6-%E8%AD%A6%E8%A1%9B%E7%88%B6%E4%B8%8D/
- https://taiwanjustice.net/%E7%BE%8E%E5%8F%83%E9%99%A2%E5%9C%8B%E9%98%B2%E6%8E%88%E6%AC%8A%E6%B3%95%E8%8D%89%E6%A1%88%EF%BC%8C%E7%BE%8E%E8%BB%8D%E6%87%89%E5%85%B7%E9%98%BB%E4%B8%AD%E5%A5%AA%E5%8F%B0%E8%83%BD%E5%8A%9B/
- https://taiwanjustice.net/%E5%B9%B4%E4%BB%A3%E5%90%91%E9%8C%A2%E7%9C%8B-20200103-%E9%BB%91%E9%B7%B9%E5%A4%B1%E4%BA%8B-ait%E9%99%8D%E5%8D%8A%E6%97%97%E5%93%80%E6%82%BC-%E7%BE%8E%E5%9C%8B%E5%8A%9B%E6%8C%BA%E5%8F%B0%E7%81%A3/
- https://taiwanjustice.net/%E6%96%87%E6%94%BB%E6%AD%A6%E5%9A%87%E5%B0%8D%E5%8F%B0%E7%84%A1%E6%95%88%EF%BC%8C%E7%BE%8E%E5%AD%B8%E8%80%85%EF%BC%9A%E7%BF%92%E8%BF%91%E5%B9%B3%E6%B2%92%E8%A6%BA%E9%86%92/
- https://taiwanjustice.net/%E5%BE%90%E5%9C%8B%E5%8B%87%EF%BC%9A%E5%9C%8B%E5%BE%BD%E6%9B%B4%E6%94%B9%E8%A9%95%E4%BC%B0%E5%A0%B1%E5%91%8A4-9%E5%89%8D%E5%A6%82%E6%9C%9F%E6%8F%90%E5%87%BA/
- https://taiwanjustice.net/%E5%85%AC%E8%A6%96%E6%99%9A%E9%96%93%E6%96%B0%E8%81%9E-20240329/
- https://taiwanjustice.net/%E6%96%B0%E8%81%9E%E6%8C%96%E6%8C%96%E5%93%87-20220720-%E8%B3%88%E6%B0%B8%E5%A9%95%E8%A6%AA%E4%BA%BA%E7%9A%84%E6%81%A9%E6%80%A8%E6%83%85%E4%BB%87%EF%BC%81/
- https://taiwanjustice.net/%E6%8D%B7%E5%85%8B%E8%88%87%E5%8F%B0%E7%81%A3%E8%88%AA%E5%A4%AA%E5%90%88%E4%BD%9C%EF%BC%8C%E5%8B%87%E9%B7%B9%E9%AB%98%E6%95%99%E6%A9%9F%E7%B3%BB%E5%87%BA%E5%90%8C%E9%96%80%E6%98%AF%E5%88%A9%E5%9F%BA/
- https://taiwanjustice.net/%E5%8F%B0%E7%81%A3%E6%BC%94%E7%BE%A9-20231022-%E4%BB%A5%E8%89%B2%E5%88%97%E7%9A%84%E5%89%8D%E4%B8%96%E4%BB%8A%E7%94%9F/
- https://taiwanjustice.net/%E5%89%8D%E9%80%B2%E6%96%B0%E5%8F%B0%E7%81%A3-20210805-%E5%8C%97%E5%B8%82%E4%B8%8D%E6%80%95%E4%BA%BA%E8%88%87%E4%BA%BA%E7%9A%84%E9%80%A3%E7%B5%90-%E8%90%AC%E8%8F%AF%E8%8C%B6%E5%AE%A4%E5%8A%9B/
- https://taiwanjustice.net/%E9%84%AD%E7%9F%A5%E9%81%93%E4%BA%86-20220806-%E6%88%B0%E7%8B%BC%E7%8F%BE%E5%BD%A2%EF%BC%81%E4%B8%AD%E9%A7%90%E6%B3%95%E5%A4%A7%E4%BD%BF%E7%9B%A7%E6%B2%99%E9%87%8E%E7%8B%82%E8%A8%80%E7%B5%B1%E4%B8%80/
- https://taiwanjustice.net/%E6%96%B0%E5%8F%B0%E7%81%A3%E5%8A%A0%E6%B2%B9-20210422-%E5%8F%8D%E5%88%B6%E4%B8%AD%E5%9C%8B%EF%BC%81%E7%BE%8E%E5%9C%8B%E9%80%9A%E9%81%8E%E6%88%B0%E7%95%A5%E7%AB%B6%E7%88%AD%E6%B3%95%E6%A1%88/
- https://taiwanjustice.net/%E6%8A%97%E7%96%AB%E6%96%B0%E6%9B%99%E5%85%89%EF%BC%8C%E7%B4%AB%E5%A4%96%E7%B7%9Ac%E7%87%88%E6%9C%89%E6%9C%9B%E6%AE%BA%E6%AD%BB%E6%AD%A6%E6%BC%A2%E8%82%BA%E7%82%8E%E7%97%85%E6%AF%92/
- https://taiwanjustice.net/%E7%AC%AC%E4%BA%8C%E6%B3%A2%E6%AD%A6%E6%BC%A2%E5%86%8D%E7%8F%BE%E5%80%92%E5%9C%B0%E4%B8%8D%E8%B5%B7-%E5%85%A8%E5%B8%82%E5%85%AB%E5%8D%80%E5%81%9C%E5%BF%AB%E9%81%9E%E4%B8%AD/
- https://taiwanjustice.net/%E8%AA%BF%E6%9F%A5%EF%BC%9A%E9%80%BE%E5%8D%8A%E5%8F%97%E8%A8%AA%E6%B8%AF%E4%BA%BA%E6%94%AF%E6%8C%81%E6%B0%91%E4%B8%BB%E6%B4%BE%E8%AD%B0%E5%93%A1%E9%9B%A2%E9%96%8B%E7%AB%8B%E6%B3%95%E6%9C%83/
- https://taiwanjustice.net/%E5%B7%9D%E6%99%AE%E7%A2%BA%E8%A8%BA%E6%AD%A6%E6%BC%A2%E8%82%BA%E7%82%8E%E6%9C%83%E5%B0%8D%E7%BE%8E%E5%9C%8B%E5%A4%A7%E9%81%B8%E7%94%A2%E7%94%9F%E6%80%8E%E6%A8%A3%E7%9A%84%E5%BD%B1%E9%9F%BF%EF%BC%9F/
- https://taiwanjustice.net/youtube%E5%B0%81%E9%8E%96%E4%BF%84%E7%BE%85%E6%96%AF%E5%AE%98%E5%AA%92%E9%A0%BB%E9%81%93-%E7%AF%84%E5%9C%8D%E6%93%B4%E5%8F%8A%E5%85%A8%E7%90%83/
- https://taiwanjustice.net/%E9%99%B3%E7%A0%B4%E7%A9%BA%E7%B8%B1%E8%AB%96%E5%A4%A9%E4%B8%8B-0311/
- https://www.taiwanjustice.net/category/videos/news-cheng/page/3/
- https://taiwanjustice.net/%E9%97%9C%E9%8D%B5%E6%99%82%E5%88%BB-20201008-%E6%8A%97%E4%B8%AD%E6%9C%80%E5%89%8D%E7%B7%9A%EF%BC%81%E5%B7%9D%E6%99%AE%E5%AE%89%E5%85%A8%E9%A1%A7%E5%95%8F%E4%BF%83%E5%8F%B0%E8%AE%8A%E3%80%8C%E7%AE%AD/
- https://taiwanjustice.net/category/videos/%E6%9D%8E%E5%9B%9B%E7%AB%AF%E7%9A%84%E9%9B%B2%E7%AB%AF%E4%B8%96%E7%95%8C/?filter_by=review_high
- https://www.taiwanjustice.net/tag/%E4%B8%AD%E5%85%B1%E8%97%89%E7%BE%8E%E8%A8%AA%E5%9C%98%E4%BE%86%E5%8F%B0%E5%AE%A3%E5%B8%83%E8%BB%8D%E6%BC%94/
- https://www.taiwanjustice.net/category/videos/%e6%b0%91%e8%a6%96%e7%95%b0%e8%a8%80%e5%a0%82/page/2/
- https://www.taiwanjustice.net/tag/2021%E5%B9%B4%E9%9B%BB%E8%85%A6%E5%8F%8A%E6%99%BA%E6%85%A7%E5%9E%8B%E6%89%8B%E6%A9%9F-ipad%E5%9F%BA%E7%A4%8E%E7%8F%AD%E8%AA%B2%E7%A8%8B%E6%8B%9B%E7%94%9F%E8%A3%9C%E5%85%85%E8%AA%AA%E6%98%8E/
- https://www.taiwanjustice.net/tag/%E5%A5%B3%E4%B8%8A%E7%94%B7%E4%B8%8B/
- https://www.taiwanjustice.net/tag/%E9%99%B3%E7%A0%B4%E7%A9%BA/page/51/
- https://www.taiwanjustice.net/category/internatinal/usa_news/page/2/?filter_by=popular
- https://taiwanjustice.net/tag/repression/
- https://taiwanjustice.net/tag/%E9%BE%8D%E5%B9%B4%E9%96%8B%E7%B4%85%E7%9B%A4%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%89%B5709%E5%85%83%E5%A4%A9%E5%83%B9-%E5%B8%82%E5%80%BC%E6%94%80%E8%87%B3%E6%96%B0%E5%8F%B0%E5%B9%A318-38%E5%85%86%E5%85%83/
- https://taiwanjustice.net/tag/%E8%97%8D%E7%99%BD-520%E5%BE%8C%E6%83%B3%E8%AE%93%E8%B3%B4%E6%B8%85%E5%BE%B7%E7%84%A1%E6%B3%95%E5%9F%B7%E6%94%BF/
- https://taiwanjustice.net/tag/%E5%8F%B0%E7%81%A3%E6%86%B2%E6%B3%95%E5%AD%B8/
- https://taiwanjustice.net/tag/%E5%9C%8B%E6%9C%83%E6%9C%80%E5%89%8D%E7%B7%9A/
- https://taiwanjustice.net/tag/%E9%81%93%E7%BE%A9%E5%80%BC%E5%A4%9A%E5%B0%91/
- https://taiwanjustice.net/tag/%E5%85%A7%E6%94%BF%E9%83%A8%E5%A4%A7%E4%BF%AE%E9%81%B8%E7%BD%B7%E6%B3%95/
- https://taiwanjustice.net/tag/%E8%B2%9D%E9%AD%AF%E7%89%B9%E5%A4%A7%E7%88%86%E7%82%B878%E6%AD%BB%E8%BF%914000%E5%82%B7/
- https://taiwanjustice.net/tag/%E3%80%88%E6%97%A5%E9%A0%AD%E8%8A%B1%E9%96%8B%E4%BA%86%E5%BE%8C%E3%80%89/
- https://taiwanjustice.net/tag/%E9%BB%83%E5%9C%8B%E6%98%8C/page/2/
- https://taiwanjustice.net/tag/%E5%B0%B1%E8%81%B7%E9%80%B1%E5%B9%B4/
- https://taiwanjustice.net/tag/%E8%8E%8A%E8%90%AC%E5%A3%BD/
- https://taiwanjustice.net/tag/%E7%A6%81%E5%8F%B0%E5%85%A5%E5%A2%83/
- https://taiwanjustice.net/tag/%E4%B8%AD%E5%9C%8B%E9%BB%A8%E6%94%BF%E9%83%A8%E9%96%80%E6%89%B9%E7%89%B9%E6%96%AF%E6%8B%89%E5%82%B2%E6%85%A2%E9%A9%95%E7%B8%B1/
- https://taiwanjustice.net/tag/%E5%85%A8%E7%90%83%E7%86%B1%E6%90%9C/
- https://www.taiwanjustice.net/2022/12/04/%E6%B0%91%E8%A6%96%E7%95%B0%E8%A8%80%E5%A0%82-20221205-%E6%8F%AD%E9%96%8B%E9%90%B5%E5%B9%95%EF%BC%8D%E5%A4%96%E5%BD%B9%E7%9B%A3-%E8%A2%AB%E9%9A%B1%E5%BD%A2%E7%9A%84%E5%80%99%E9%81%B8%E4%BA%BA/
- https://www.taiwanjustice.net/2021/05/23/%E6%B0%91%E8%A6%96%E5%8F%B0%E7%81%A3%E5%AD%B8%E5%A0%82-20210524-%E9%80%99%E4%BA%9B%E4%BA%BA%E9%80%99%E4%BA%9B%E4%BA%8B-%E7%82%BA%E5%8F%B0%E7%81%A3%E6%B0%91%E4%B8%BB%E7%8D%A8%E7%AB%8B%E7%9A%84/

## Artifacts

- `knowledge/web-archives/taiwanjustice-net/gap_fill_results.json`
- `knowledge/web-archives/taiwanjustice-net/gap_fill_summary.json`
- `knowledge/research/taiwanjustice-net/GAP_REPORT.md` (this file)

## Recommended next steps

1. Optionally fetch Arquivo/Ghostarchive bodies for recoverable URLs into `raw-html/` + re-run Tier2 converter.
2. Ask Freeman only for **still-missing content** titles if high-value.
3. Proceed TJ-P5 Tier-1 absorb on healthy Tier2 corpus (29k md) — do not block P5 on residual media fails.

