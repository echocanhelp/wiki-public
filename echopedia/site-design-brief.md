## Site design audit — 2026-11-01 22:46

- pages_md=15208
- critical=0 high=1 medium=0
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (1)
- **A8** Explorer useSavedState not false on homepage (stale localStorage fileTree)
  - path: `/home/leedt/echo-system/index.html`

### LOW (1)
- **C1** spelling signals (sample): 1 `[AGENT_SUGGESTED]`
  - `lai-ching-te.md: ?ching`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 51
  - `people/c-a-chou.md`
  - `people/chen-po-kong.md`
  - `people/chen-zhefu-xu-chunhui.md`
  - `people/choan-guo-huei.md`
  - `people/edgar-chun-yi-lin.md`
  - `people/fan-jiang-ti-ang.md`
  - `people/fan-qingliang.md`
  - `people/hsu-ching-chun.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
