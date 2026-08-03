# TAHS priority roster (L1 gold list)

**Purpose:** Human-curated TAHS leadership + titled volunteers + members who should rank highest when scoring the taiwanjustice.net archive for Echopedia absorb.

**Privacy:** Operational file under `knowledge/operational/`. Do **not** paste private emails/phones/LINE U-ids here. Display names + public person slug only.

**Source:** TAHS 2025 organization chart (台美人歷史協會組織表 2025), Tax ID 46-4005384 — names/roles only; phones redacted. Plus LINE-group members onboarded 2026-06 onward (owner-introduced, Echopedia-verified). Publication-mention adds only when the person is Taiwanese-American / US-based community — **not** ROC/PRC political figures or non-US residents.

After editing, re-run:

```bash
python3 ~/echo-system/scripts/taiwanjustice_priority_score.py --root ~/echo-system --rebuild-lexicon
```

## L1 — 2025 officers & titled roles

| name_en | name_zh | slug | role / notes |
|---------|---------|------|----------------|
| Alan Thian | 田詒鴻 | alan-thian | 會務指導主席 (Affairs guidance chair) 2025 |
| Paul Chen | 陳柏宇 | paul-chen | 財務指導主席 (Finance guidance chair) 2025 |
| Gene Tsai | 蔡錦榮 | gene-tsai | 顧問 (Advisor) 2025 |
| Hsu Shih-huan | 許世環 | xu-shihuan | 顧問 (Advisor) 2025; EN romanization provisional |
| Leonard Hsu Jr. | 許景鴻 | leonard-hsu-jr | 會長 (President) 2025 |
| Roger Tsai | 蔡漢成 | roger-tsai | 副會長 (Vice President) 2025 |
| Wei Wei Bai | 白偉瑋 | bai-weiwei | 副會長 (Vice President) 2025 |
| John Yang | 楊錦忠 | john-yang | 特別助理 (Special assistant) 2025 |
| Li Yi-sheng | 李意盛 | li-yisheng | 特別助理 (Special assistant) 2025; EN romanization provisional |
| Charles Yang | 楊嘉猷 | yang-jia-you | 財務長 (Treasurer) 2025; also founding president |
| Freeman Huang | 黃樹人 | freeman-huang | 秘書 (Secretary) 2025; taiwanjustice.net publisher |
| Cai Shu-nu | 蔡淑女 | cai-shunyu | 總務 (General affairs) 2025; EN romanization provisional |
| Shen Zi-zai | 沈梓在 | shen-zizai | 資訊 (Information / IT) 2025; EN romanization provisional |

## L1 — recently added LINE-group members (2026-06 onward)

Owner-introduced in the TAHS LINE core group; canonical Echopedia pages verified. Display names + public slugs only.

| name_en | name_zh | slug | role / notes |
|---------|---------|------|----------------|
| Becky Yang | 楊 | becky-yang | TAHS community member; family partner of founding president (2026-08) |
| David Lee | 李東璞 | david-lee | TAHS CTO scope pending confirmation; VP InfoSec Light & Wonder (2026-07) |
| Ken Wu | 吳兆峯 | ken-wu | TAHS member; Taiwan Center Foundation SG, FAPA-LA chapter president (2026-07) |
| Linda Liu | 劉玲華 | linda-liu | TAHS member; board listing source Taiwan Center (2026-07) |
| Rex Chen | 陳乃光 | rex-chen | TAHS member, onboarded via LINE intro (2026-06) |
| Franklin Ping Cheng | 程炳成 | franklin-ping-cheng | TAHS President 2014– (successor to Charles Yang) |
| Chen Wenshi | 陳文石 | chen-wenshi | Artist / cultural advocate (2026-07) |
| Huang Gen-shen | 黃根深 | huang-gen-shen | Art teacher; UFAI founding member, 51-yr activist (2026-07) |
| Liao Shu-zong | 廖述宗 | liao-shu-zong | Biochemist; NATPA founder; democratic movement supporter (2026-07) |

## L1 — 2017/2023 publication mentions (community only)

**Filter (owner 2026-08):** only Taiwanese-American / US-based community people. Removed ROC/PRC political figures, historical leaders, Taiwan-only politicians/commentators, and non-community subjects who appear in articles but do **not** reside in America / are not TAHS community.

Columnists (陳破空, 陳茂雄, 陳昭南, 林保華, 余杰, 范姜提昂, 楊子清, 黃帝穎, 何清漣, 廖清山, …) stay **L3** via scorer `SEED_L3` — not L1.

Duplicates of officers / LINE members above are omitted here.

| name_en | name_zh | slug | role / notes |
|---------|---------|------|----------------|
| Bai Peiyu | 白佩玉 | bai-peiyu | 2017 看板人物 community feature |

## Optional — orgs / chapters to boost (free text aliases)

```
# alias lines (uncomment to enable — or add to lexicon manually)
# 南加台美人 | regional
台美人歷史協會 | TAHS
```

## Status

- Template created: 2026-08-02
- Filled from 2025 org chart: 2026-08-03
- Extended with LINE-group members: 2026-08-03
- Publication-mention purge (non-US politicians / non-community): 2026-08-03
- Owner: Leonard Hsu Jr.
- Consumed by: `scripts/taiwanjustice_priority_score.py` → band **L1**
- Echopedia pages: officer + LINE L1 slugs under `content/people/` (2026-08-03); 白佩玉 thin page if missing
