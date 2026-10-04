## Site design audit — 2026-10-04 00:30

- pages_md=15105
- critical=0 high=2 medium=1
- heals_suggested=publish

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (2)
- **A3** MD without HTML: 2 (recent≤7d: 2) `[heal:publish]`
  - `people/林芸.md`
  - `works/taiwaneseamerican-org/vincent-chu-nice-places.md`
- **B3** new/changed MD missing HTML (≤7d) `[heal:publish]`
  - `people/林芸.md`
  - `works/taiwaneseamerican-org/vincent-chu-nice-places.md`

### MEDIUM (1)
- **F4** people/index.html is 1514464 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

### INFO (2)
- **B2** pinned featured pages: 6 (cap 6 people + 3 orgs; overflow hides recency)
  - `people/albert-s-lai.md`
  - `people/liao-shu-zong.md`
  - `people/lin-fu-kun.md`
  - `people/lin-yuan-ching.md`
  - `people/yang-jia-you.md`
  - `people/yang-xin.md`
- **B1** person/org touched ≤7d (rely on recency featured window): 1653
  - `people/a-n-liu.md`
  - `people/abby-hong.md`
  - `people/adam-chang.md`
  - `people/adrian-lin.md`
  - `people/agnes-hsiao.md`
  - `people/agnes-wu.md`
  - `people/ai-jen-poo.md`
  - `people/alan-su.md`

### Programmable heals
- publish

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
