## Site design audit — 2026-11-07 00:55

- pages_md=15224
- critical=0 high=1 medium=0
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (1)
- **A8** Explorer useSavedState not false on homepage (stale localStorage fileTree)
  - path: `/home/leedt/echo-system/index.html`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 26
  - `people/c-y-hsu.md`
  - `people/chen-po-kong.md`
  - `people/eddy-ji-xiao.md`
  - `people/huang-diyin.md`
  - `people/kana-mimaki.md`
  - `people/li-jian.md`
  - `people/lin-baohua.md`
  - `people/pingtung-lai.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
