## Site design audit — 2026-11-13 00:48

- pages_md=15371
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
- **B1** person/org touched ≤7d (rely on recency featured window): 113
  - `people/albert-chapter1-audiobook-taiwanese-female.md`
  - `people/albert-chapter1-zh-hsiaochen-full-review.md`
  - `people/alexander-macdonald.md`
  - `people/alexander-yeh.md`
  - `people/alice-huang.md`
  - `people/allen-chao.md`
  - `people/amenda-wu.md`
  - `people/andrew-lin.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
