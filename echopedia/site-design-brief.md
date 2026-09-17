## Site design audit — 2026-09-17 04:45

- pages_md=15057
- critical=0 high=0 medium=1
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: WARN**

### MEDIUM (1)
- **F4** people/index.html is 1498808 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

### LOW (1)
- **C1** spelling signals (sample): 3 `[AGENT_SUGGESTED]`
  - `zhang-aihui.md: ?yunching`
  - `ching-ih-wang.md: ?ching`
  - `hsin-yun-huang.md: ?youming`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 853
  - `people/agnes-hsu.md`
  - `people/ahhee-hsu.md`
  - `people/alan-thian.md`
  - `people/albert-chapter1-zh-hsiaochen-full-review.md`
  - `people/albert-zh-sku-b-publisher-review.md`
  - `people/alex-hsuan-yu-lee.md`
  - `people/alice-chen.md`
  - `people/alice-yu.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
