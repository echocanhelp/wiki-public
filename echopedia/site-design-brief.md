## Site design audit — 2026-10-20 00:39

- pages_md=15144
- critical=0 high=0 medium=1
- heals_suggested=none

### Summary
- **SITE_DESIGN_STATUS: WARN**

### MEDIUM (1)
- **F4** people/index.html is 1539120 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

### LOW (1)
- **C1** spelling signals (sample): 2 `[AGENT_SUGGESTED]`
  - `leonard-hsu-jr.md: ?ching`
  - `tah-p-a2aa6c2089.md: ?substring`

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 392
  - `people/ahhee-hsu.md`
  - `people/alexander-k-young.md`
  - `people/alvina-ling.md`
  - `people/amy-hsu.md`
  - `people/an-su-gao-lai.md`
  - `people/andrew-y-lee.md`
  - `people/andrew-yang.md`
  - `people/andy-chang.md`

### Programmable heals
- (none)

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
