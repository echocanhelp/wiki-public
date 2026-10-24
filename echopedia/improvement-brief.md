## Echopedia self-improvement — 2026-10-24

### Ops check
- OPS_WARN: ingest-complete PARTIAL (About/History missing on a watched primary — not AUTO-fixed)
- OPS_WARN: INGEST_COMPLETE: PARTIAL
- OPS_WARN: - eastgatebarclay-org: primary History+Mission is 0 chars (need ≥400); intro archives exist: eastgatebarclay-org-delta-2026-09-27-aboutme.md
- DOCS_SUMMARY: status=WARN fail=0 warn=1 ok=14 crons=43 agent=2 links_missing=0
- DOCS_STATUS: WARN
- OPS_WARN: docs-sync WARN
- OPS_SUMMARY: fail=0 warn=4
- OPS_STATUS: WARN

### Deploy drift
- DRIFT_STALE_HTML: people/chen-zhaonan (md newer by ~135m)
- DRIFT_STALE_HTML: people/jonah-chang (md newer by ~101m)
- DRIFT_STALE_HTML: people/albert-s-lai (md newer by ~83m)
- DRIFT_SUMMARY: stale=3 missing_html=0
- DRIFT_STATUS: ACTION — run: bash ~/.hermes/scripts/echopedia-publish.sh

### Knowledge freshness
- FRESH_SUMMARY: stale=0 missing=0
- FRESH_STATUS: OK

### Entity hints sync
- HINTS_ADD: people/amy-li
- HINTS_ADD: people/anna-wang-diplomat
- HINTS_ADD: people/liao-hung-hsiang
- HINTS_ADD: people/tsai-wen-hui
- HINTS_ADD: people/ye-siya
- HINTS_ADD: organizations/taiwanese-american-citizens-league
- HINTS_ADD: sources/doublethinklab-about
- HINTS_ADD: sources/en-wp-shen-boyang
- HINTS_ADD: sources/gwytb-zhanghan-2026-10-21
- HINTS_ADD: sources/newtalk-anbao-timeline-2026-10-08
- HINTS_ADD: sources/takungpao-vway-hitpiece-2026-10-13
- HINTS_ADD: sources/tpoc-taipei-ai-sim-2026-10-2026-10-14
- HINTS_ADD: sources/tvbs-taipei-poll-oct-2026-10-08
- HINTS_ADD: sources/tvbs-taipei-polls-2026
- HINTS_ADD: sources/zhwp-shen-boyang
- HINTS_ADD: sources/zhwp-yuhan-su
- HINTS_SUMMARY: added=13
- HINTS_STATUS: UPDATED

### Intake opportunities
- INTAKE_DROP_FRAGMENT: n=63
- INTAKE_MISSING_PAGE: National Taiwan Univ (type: entity, mentioned 326x in: people/a-n-liu.md, people/agnes-wu.md, people/amanda-hsu.md (+323 more))
- INTAKE_MISSING_PAGE: Ho Chie (type: entity, mentioned 188x in: organizations/american-citizens-for-taiwan.md, organizations/democratic-progressive-party.md, organizations/north-america-taiwanese-womens-association.md (+185 more))
- INTAKE_MISSING_PAGE: Taiwan Justice (type: entity, mentioned 94x in: organizations/cornell-taiwanese-american-society.md, organizations/institute-for-taiwanese-studies.md, organizations/irvine-taiwanese-presbyterian-church.md (+91 more))
- INTAKE_MISSING_PAGE: Northern California (type: entity, mentioned 90x in: organizations/democratic-progressive-party.md, organizations/evergreen-class-by-irvine-taiwanese-presbyterian-church-laguna-hills-ca.md, organizations/north-america-taiwanese-womens-association-northern-california-chapter.md (+87 more))
- INTAKE_MISSING_PAGE: Hong Kong (type: entity, mentioned 90x in: organizations/fapa-los-angeles.md, organizations/taiwanese-association-of-america.md, organizations/taiwanjustice-net.md (+87 more))
- INTAKE_MISSING_PAGE: San Jose (type: entity, mentioned 79x in: organizations/south-bay-taiwanese-association-of-n-california.md, organizations/south-bay-taiwanese-association-of-s-california.md, organizations/taiwanese-american-center-of-northern-california.md (+76 more))
- INTAKE_MISSING_PAGE: Vice President (type: entity, mentioned 71x in: organizations/irvine-taiwanese-presbyterian-church.md, organizations/north-america-taiwanese-womens-association.md, organizations/taiwanese-american-historical-society.md (+68 more))
- INTAKE_MISSING_PAGE: Taiwanese American Conference (type: entity, mentioned 63x in: organizations/tah-foundation.md, organizations/taiwanese-american-student-association-at-uc-santa-barbara.md, organizations/taiwanese-association-of-america-las-vegas.md (+60 more))
- INTAKE_MISSING_PAGE: 全美台灣人權 (type: organization, mentioned 56x in: organizations/center-for-taiwan-international-relations-ctir.md, organizations/fapa-los-angeles.md, organizations/formosan-association-for-human-rights.md (+53 more))
- INTAKE_MISSING_PAGE: Evangelical Formosan Church (type: entity, mentioned 53x in: organizations/columbia-university-taiwanese-graduate-student-association.md, organizations/evangelical-formosan-church-of-norcal.md, organizations/evergreen-senior-university-by-evangelical-formosa-church-of-irvine-esu.md (+50 more))
- INTAKE_MISSING_PAGE: Musical Arts (type: entity, mentioned 49x in: people/agnes-hsu.md, people/amber-liao.md, people/amy-hsieh.md (+46 more))
- INTAKE_MISSING_PAGE: National Taiwan Normal University (type: entity, mentioned 47x in: people/alex-hsuan-yu-lee.md, people/ariel-wei.md, people/butteryfly-chong.md (+44 more))
- INTAKE_OK: no interaction name candidates
- INTAKE_SUMMARY: missing=4123 interaction=0
- INTAKE_STATUS: ACTION

### Cron selfcheck
- CRON_SUMMARY: fail=0 warn=0 jobs=0
- CRON_STATUS: OK

### Queue drain (programmable)
- DRAIN: people/bai-peiyu.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/nanfang-shuo.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/tang-peili.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/sang-pu.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/wang-shufen.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/xia-ming.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/zou-jingwen.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/george-lee.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/huang-yongcheng.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/kuan-cheng-lu.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/po-wei-lai.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/chao-sile.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/deng-shuzhen.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/林芸.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/karen-chia-ling-ho.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: organizations/evergreen-senior-university-by-evangelical-formosa-church-of-irvine-esu.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: organizations/global-hakka-un-ngo-applying-committee-un-ngo.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: organizations/north-america-pastel-artist-association.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/mei-li-chen.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/agnes-hsu.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/hsien-ann-meng.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/grace-chung.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/vera-hui-pin-hsu.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/dr-min-chin-mary-lee.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/jerry-jean.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/zheng-qinren.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/kerina-chang.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/hanchien-lee.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/mao-chung-lee.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/feng-hsu-lee.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: organizations/chhong-bi-memorial-fund.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: organizations/taiwanese-student-association-for-public-affairs.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/ching-fen-lin.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/janice-wong.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/amanda-shumin-yang.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/erh-jen-lee.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/wei-ling-chen.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/yi-hsin-lin.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/nancy-jan.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']
- DRAIN: people/shih-peng-chang.md → ['NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)']

### Drain detail
## Queue drain — 2026-10-24
- Items: **40**

- `people/bai-peiyu.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/nanfang-shuo.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/tang-peili.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/sang-pu.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/wang-shufen.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/xia-ming.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/zou-jingwen.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/george-lee.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/huang-yongcheng.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/kuan-cheng-lu.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/po-wei-lai.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/chao-sile.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/deng-shuzhen.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/林芸.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/karen-chia-ling-ho.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `organizations/evergreen-senior-university-by-evangelical-formosa-church-of-irvine-esu.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `organizations/global-hakka-un-ngo-applying-committee-un-ngo.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `organizations/north-america-pastel-artist-association.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/mei-li-chen.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/agnes-hsu.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/hsien-ann-meng.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/grace-chung.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/vera-hui-pin-hsu.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/dr-min-chin-mary-lee.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/jerry-jean.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/zheng-qinren.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/kerina-chang.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/hanchien-lee.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/mao-chung-lee.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/feng-hsu-lee.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `organizations/chhong-bi-memorial-fund.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `organizations/taiwanese-student-association-for-public-affairs.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/ching-fen-lin.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/janice-wong.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/amanda-shumin-yang.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/erh-jen-lee.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/wei-ling-chen.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/yi-hsin-lin.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/nancy-jan.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)
- `people/shih-peng-chang.md`: NO_SAFE_ACT (HOLD leftover — not fail-closed first-mention)

Fail-closed first-mention is AUTO (janitor). HOLD leftover ≠ human body-link batch.

### Intake detail
## Intake opportunities

### Missing pages (wiki cross-ref)
- `MISSING_PAGE: National Taiwan Univ (type: entity, mentioned 326x in: people/a-n-liu.md, people/agnes-wu.md, people/amanda-hsu.md (+323 more))`
- `MISSING_PAGE: Ho Chie (type: entity, mentioned 188x in: organizations/american-citizens-for-taiwan.md, organizations/democratic-progressive-party.md, organizations/north-america-taiwanese-womens-association.md (+185 more))`
- `MISSING_PAGE: Taiwan Justice (type: entity, mentioned 94x in: organizations/cornell-taiwanese-american-society.md, organizations/institute-for-taiwanese-studies.md, organizations/irvine-taiwanese-presbyterian-church.md (+91 more))`
- `MISSING_PAGE: Northern California (type: entity, mentioned 90x in: organizations/democratic-progressive-party.md, organizations/evergreen-class-by-irvine-taiwanese-presbyterian-church-laguna-hills-ca.md, organizations/north-america-taiwanese-womens-association-northern-california-chapter.md (+87 more))`
- `MISSING_PAGE: Hong Kong (type: entity, mentioned 90x in: organizations/fapa-los-angeles.md, organizations/taiwanese-association-of-america.md, organizations/taiwanjustice-net.md (+87 more))`
- `MISSING_PAGE: San Jose (type: entity, mentioned 79x in: organizations/south-bay-taiwanese-association-of-n-california.md, organizations/south-bay-taiwanese-association-of-s-california.md, organizations/taiwanese-american-center-of-northern-california.md (+76 more))`
- `MISSING_PAGE: Vice President (type: entity, mentioned 71x in: organizations/irvine-taiwanese-presbyterian-church.md, organizations/north-america-taiwanese-womens-association.md, organizations/taiwanese-american-historical-society.md (+68 more))`
- `MISSING_PAGE: Taiwanese American Conference (type: entity, mentioned 63x in: organizations/tah-foundation.md, organizations/taiwanese-american-student-association-at-uc-santa-barbara.md, organizations/taiwanese-association-of-america-las-vegas.md (+60 more))`
- `MISSING_PAGE: 全美台灣人權 (type: organization, mentioned 56x in: organizations/center-for-taiwan-international-relations-ctir.md, organizations/fapa-los-angeles.md, organizations/formosan-association-for-human-rights.md (+53 more))`
- `MISSING_PAGE: Evangelical Formosan Church (type: entity, mentioned 53x in: organizations/columbia-university-taiwanese-graduate-student-association.md, organizations/evangelical-formosan-church-of-norcal.md, organizations/evergreen-senior-university-by-evangelical-formosa-church-of-irvine-esu.md (+50 more))`
- `MISSING_PAGE: Musical Arts (type: entity, mentioned 49x in: people/agnes-hsu.md, people/amber-liao.md, people/amy-hsieh.md (+46 more))`
- `MISSING_PAGE: National Taiwan Normal University (type: entity, mentioned 47x in: people/alex-hsuan-yu-lee.md, people/ariel-wei.md, people/butteryfly-chong.md (+44 more))`

- No strong interaction name candidates

*Auto: no page creation — queue for human/ops.*
