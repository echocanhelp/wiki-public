## Site design audit — 2026-09-07 04:27

- pages_md=5297
- critical=0 high=0 medium=1
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: WARN**

### MEDIUM (1)
- **F4** people/index.html is 1489175 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

### LOW (1)
- **C1** spelling signals (sample): 1 `[AGENT_SUGGESTED]`
  - `tahs-member-onboarding.md: ?onboarding`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 18
  - `people/chao-sile.md`
  - `people/chen-meihui.md`
  - `people/chen-po-kong.md`
  - `people/du-ao-cunfu.md`
  - `people/fan-jiang-ti-ang.md`
  - `people/guan-renjian.md`
  - `people/hsu-ching-chun.md`
  - `people/huang-diyin.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
