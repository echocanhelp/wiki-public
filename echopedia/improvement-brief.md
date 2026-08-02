## Echopedia self-improvement — 2026-08-02

### Ops check
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-cdn-verify.sh
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-content-analysis-cron.sh
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-content-analyzer.py
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-evaluate-actions.py
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-extract-actions.py
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-generate-cards.py
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-index-sync.py
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-review-gate.py
- OPS_WARN: orphan script not in ops REQUIRED list: echopedia-scout-live.sh
- OPS_SUMMARY: fail=0 warn=9
- OPS_STATUS: WARN

### Deploy drift
- DRIFT_SUMMARY: stale=0 missing_html=0
- DRIFT_STATUS: OK

### Knowledge freshness
- FRESH_SUMMARY: stale=0 missing=0
- FRESH_STATUS: OK

### Entity hints sync
- HINTS_SUMMARY: added=0

### Intake opportunities
- ERROR running python3 /home/leedt/.hermes/scripts/echopedia-intake-opportunities.py

### Cron selfcheck
- CRON_SUMMARY: fail=0 warn=0 jobs=0
- CRON_STATUS: OK

### Queue drain (programmable)
- DRAIN: people/chen-meihui.md → ['NO_SAFE_ACT (needs human/agent for body links)']
- DRAIN: organizations/ntpc.md → ['NO_SAFE_ACT (needs human/agent for body links)']
- DRAIN: people/guo-yingyan.md → ['NO_SAFE_ACT (needs human/agent for body links)']
- DRAIN: articles/taiwanjustice-net/2026/20260209113555_連2天同台出席-外界解讀盧秀燕蔡其昌互相較勁_c2a5c76345831246.md → ['add last_reviewed', 'add Related Pages stub', 'WROTE']
- DRAIN: articles/taiwanjustice-net/2026/20260121000856_中國疫苗外交會不會重蹈口罩覆轍_3d385b738e35e94d.md → ['add last_reviewed', 'add Related Pages stub', 'WROTE']
- DRAIN_SUMMARY: items=5
- DRAIN_STATUS: DONE

### Drain detail
## Queue drain — 2026-08-02
- Items: **5**

- `people/chen-meihui.md`: NO_SAFE_ACT (needs human/agent for body links)
- `organizations/ntpc.md`: NO_SAFE_ACT (needs human/agent for body links)
- `people/guo-yingyan.md`: NO_SAFE_ACT (needs human/agent for body links)
- `articles/taiwanjustice-net/2026/20260209113555_連2天同台出席-外界解讀盧秀燕蔡其昌互相較勁_c2a5c76345831246.md`: add last_reviewed, add Related Pages stub, WROTE
- `articles/taiwanjustice-net/2026/20260121000856_中國疫苗外交會不會重蹈口罩覆轍_3d385b738e35e94d.md`: add last_reviewed, add Related Pages stub, WROTE

Safe programmable only — body first-mentions still human/local agent.

### Intake detail
## Intake opportunities

### Missing pages (wiki cross-ref)
- `MISSING_PAGE: Liao Shu (type: entity, mentioned 6x in: people/guo-shu-qing.md, people/liao-ji-chun.md, people/liao-shu-zong.md (+3 more))`
- `MISSING_PAGE: Peng Ming (type: entity, mentioned 5x in: organizations/democratic-progressive-party.md, people/liao-shu-zong.md, people/peng-ming-min.md (+2 more))`
- `MISSING_PAGE: Lin Qiong (type: entity, mentioned 5x in: people/guo-shu-qing.md, people/liao-ji-chun.md, people/liao-shu-zong.md (+2 more))`
- `MISSING_PAGE: Chen Shui (type: entity, mentioned 4x in: organizations/democratic-progressive-party.md, organizations/overseas-community-affairs-council.md, people/peng-ming-min.md (+1 more))`
- `MISSING_PAGE: National Cheng Kung University (type: entity, mentioned 4x in: people/chen-wenshi.md, people/li-mutong.md, people/mingyuan-hsu.md (+1 more))`
- `MISSING_PAGE: The Persistence (type: entity, mentioned 4x in: people/guo-shu-qing.md, people/liao-ji-chun.md, people/liao-shu-zong.md (+1 more))`
- `MISSING_PAGE: Northern California (type: entity, mentioned 3x in: organizations/taiwanese-american-historical-society.md, people/ho-chie-tsai.md, people/lin-fu-kun.md)`
- `MISSING_PAGE: Ethan Yang (type: entity, mentioned 3x in: organizations/taiwanese-american-historical-society.md, people/yang-zhengxiang.md, sources/2023-tahs-publication.md)`
- `MISSING_PAGE: Tsai Ing (type: entity, mentioned 3x in: organizations/democratic-progressive-party.md, people/li-mutong.md, people/wang-kexiong.md)`
- `MISSING_PAGE: West Chapter (type: entity, mentioned 3x in: organizations/democratic-progressive-party.md, people/ken-wu.md, sources/wikipedia-democratic-progressive-party.md)`
- `MISSING_PAGE: Executive Yuan (type: entity, mentioned 3x in: organizations/overseas-community-affairs-council.md, people/wang-kexiong.md, sources/ocac-gov-tw.md)`
- `MISSING_PAGE: Vice President (type: entity, mentioned 3x in: organizations/irvine-taiwanese-presbyterian-church.md, people/david-lee.md, people/wang-yao-ting.md)`

- No strong interaction name candidates

*Auto: no page creation — queue for human/ops.*
### Review gate: generated cards
- No generated cards this week

