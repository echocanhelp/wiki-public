## Site design audit — 2026-09-25 00:30

- pages_md=15083
- critical=0 high=2 medium=1
- heals_suggested=publish

### Summary
- **SITE_DESIGN_STATUS: ACTION**

### HIGH (2)
- **A3** MD without HTML: 19 (recent≤7d: 19) `[heal:publish]`
  - `people/hsu-hsin-liang.md`
  - `people/mei-xinyi.md`
  - `organizations/north-america-taiwanese-medical-association-foundation.md`
  - `organizations/taiwanese-american-student-association-at-ohio-state-university.md`
  - `organizations/taiwaneseamericanhistory-org.md`
  - `works/taiwaneseamerican-org/jess-eng-taitung-eats-book.md`
  - `works/taiwaneseamericanhistory-org/108-e8-a7-a3-e6-b0-b8-e5-8d-9a-e5-a3-ab-dr-ching-sze-hsieh.md`
  - `works/taiwaneseamericanhistory-org/135-e5-85-a8-e7-be-8e-e5-8f-b0-e7-81-a3-e5-90-8c-e9-84-8b-e6-9c-83-e7-b0-a1-e4-b.md`
- **B3** new/changed MD missing HTML (≤7d) `[heal:publish]`
  - `people/hsu-hsin-liang.md`
  - `people/mei-xinyi.md`
  - `organizations/north-america-taiwanese-medical-association-foundation.md`
  - `organizations/taiwanese-american-student-association-at-ohio-state-university.md`
  - `organizations/taiwaneseamericanhistory-org.md`
  - `works/taiwaneseamerican-org/jess-eng-taitung-eats-book.md`
  - `works/taiwaneseamericanhistory-org/108-e8-a7-a3-e6-b0-b8-e5-8d-9a-e5-a3-ab-dr-ching-sze-hsieh.md`
  - `works/taiwaneseamericanhistory-org/135-e5-85-a8-e7-be-8e-e5-8f-b0-e7-81-a3-e5-90-8c-e9-84-8b-e6-9c-83-e7-b0-a1-e4-b.md`

### MEDIUM (1)
- **F4** people/index.html is 1501992 bytes — heavy on mobile. Do NOT hand-edit content/people/index.md. Search-first is the IA; regen script only if links break.

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
- **B1** person/org touched ≤7d (rely on recency featured window): 2245
  - `people/a-n-liu.md`
  - `people/abby-hong.md`
  - `people/adam-chang.md`
  - `people/adrian-lin.md`
  - `people/agnes-hsiao.md`
  - `people/agnes-wu.md`
  - `people/ahhee-hsu.md`
  - `people/ai-jen-poo.md`

### Programmable heals
- publish

### P13 agent scope
- Only items marked AGENT_SUGGESTED or human-directed layout marker fixes.
- Canon: echopedia/SITE_DESIGN.md
