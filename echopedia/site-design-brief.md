## Site design audit — 2026-09-18 04:30

- pages_md=15058
- critical=0 high=0 medium=1
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: WARN**

### MEDIUM (1)
- **F4** people/index.html is 1500410 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

### LOW (1)
- **C1** spelling signals (sample): 1 `[AGENT_SUGGESTED]`
  - `david-s-chen.md: ?pastoring`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 1334
  - `people/a-n-liu.md`
  - `people/adrian-lin.md`
  - `people/agnes-hsu.md`
  - `people/ahhee-hsu.md`
  - `people/alan-thian.md`
  - `people/albert-chapter1-audiobook-taiwanese-female.md`
  - `people/albert-zh-sku-b-publisher-review.md`
  - `people/alex-hsuan-yu-lee.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
