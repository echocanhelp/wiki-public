## Site design audit — 2026-11-09 00:51

- pages_md=15243
- critical=0 high=1 medium=0
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (1)
- **A8** Explorer useSavedState not false on homepage (stale localStorage fileTree)
  - path: `/home/leedt/echo-system/index.html`

### LOW (1)
- **C1** spelling signals (sample): 2 `[AGENT_SUGGESTED]`
  - `penghu-info.md: ?ching`
  - `presbyterian-church-in-taiwan.md: teh→the`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 37
  - `people/c-y-hsu.md`
  - `people/chen-mei-hui.md`
  - `people/chen-po-kong.md`
  - `people/du-ao-cunfu.md`
  - `people/eddy-ji-xiao.md`
  - `people/fan-jiang-ti-ang.md`
  - `people/huang-diyin.md`
  - `people/jennifer-an.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
