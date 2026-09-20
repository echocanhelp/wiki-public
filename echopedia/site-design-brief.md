## Site design audit — 2026-09-20 06:07

- pages_md=15066
- critical=0 high=2 medium=1
- heals_suggested=publish

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (2)
- **A3** MD without HTML: 2 (recent≤7d: 2) `[heal:publish]`
  - `people/mei-xinyi.md`
  - `works/taiwaneseamerican-org/jess-eng-taitung-eats-book.md`
- **B3** new/changed MD missing HTML (≤7d) `[heal:publish]`
  - `people/mei-xinyi.md`
  - `works/taiwaneseamerican-org/jess-eng-taitung-eats-book.md`

### MEDIUM (1)
- **F4** people/index.html is 1501992 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 2411
  - `people/a-n-liu.md`
  - `people/abby-hong.md`
  - `people/adam-chang.md`
  - `people/adrian-lin.md`
  - `people/agnes-hsiao.md`
  - `people/agnes-hsu.md`
  - `people/agnes-wu.md`
  - `people/ahhee-hsu.md`

### Programmable heals
- publish

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
