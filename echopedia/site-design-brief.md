## Site design audit — 2026-11-25 00:35

- pages_md=15871
- critical=0 high=3 medium=0
- heals_suggested=publish

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (3)
- **A3** MD without HTML: 2 (recent≤7d: 2) `[heal:publish]`
  - `sources/newbloom-org.md`
  - `sources/taa-east-tennessee-frontier-11190824-35-2026-11-24.md`
- **B3** new/changed MD missing HTML (≤7d) `[heal:publish]`
  - `sources/newbloom-org.md`
  - `sources/taa-east-tennessee-frontier-11190824-35-2026-11-24.md`
- **A8** Explorer useSavedState not false on homepage (stale localStorage fileTree)
  - path: `/home/leedt/echo-system/index.html`

### LOW (1)
- **C1** spelling signals (sample): 3 `[AGENT_SUGGESTED]`
  - `lin-baohua.md: ?yueqing`
  - `黃逸豪.md: teh→the`
  - `tah-whoswho-prof-w-k-young-capture.md: ?substring`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 139
  - `people/ahhee-hsu.md`
  - `people/bob-yang.md`
  - `people/carol-cho.md`
  - `people/ching-sze-hsieh.md`
  - `people/christina-hu.md`
  - `people/david-lee.md`
  - `people/dew-chin-ghi-chang.md`
  - `people/ding-xiaowen-singer.md`

### Programmable heals
- publish

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
