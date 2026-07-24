# 2023 TAHS Publication Depth Pass Plan

## Goal
Deepen 16 B-tier person pages from section dump text to meet depth floor requirements.

## Background
The 2023 publication person pages were created from structured facts (facts-clean.json) but lack full narrative text. Section dumps exist in `knowledge/research/tahs-2023-section-dumps/` but pages haven't been deepened.

## Depth Floor Rules
| Section lines | Min facts | Min body chars |
|---------------|-----------|----------------|
| < 80 | 6 | ≥ 900 |
| 80–200 | 10 | ≥ 1400 |
| > 200 | 15 | ≥ 2000 or Overview + Career/Legacy |

## Pages to Deepen (16 B-tier, FAIL status)

### Section 3 profiles (2720 lines, ~54KB text)
These 13 profiles share one section dump file. Need to extract individual narrative from the combined text.

1. **Ye Siya & Zhang Xinhui** (`ye-siya-zhang-xinhui.md`) — 1,128 bytes → target 2,000+
2. **Xu Zongbang** (`xu-zongbang.md`) — 1,650 bytes → target 2,000+
3. **Li Mutong** (`li-mutong.md`) — 1,632 bytes → target 2,000+
4. **Chen Wenxue** (`chen-wenxue.md`) — 1,621 bytes → target 2,000+
5. **Wang Kexiong** (`wang-kexiong.md`) — 1,606 bytes → target 2,000+
6. **Wang Yao-ting & Xie Xiulan** (`wang-yao-ting-xie-xiulan.md`) — 1,697 bytes → target 2,000+
7. **Chen Wenshi** (`chen-wenshi.md`) — 1,642 bytes → target 2,000+
8. **Yang Huiqiao** (`yang-huiqiao.md`) — 1,647 bytes → target 2,000+
9. **Cai Jinrong** (`cai-jinrong.md`) — 1,642 bytes → target 2,000+
10. **Xie Qingzhi & Xie Poyi** (`xie-qingzhi-xie-poyi.md`) — 1,741 bytes → target 2,000+
11. **Yang Chengwei** (`yang-chengwei.md`) — 1,652 bytes → target 2,000+
12. **Zheng Dazhi** (`zheng-dazhi.md`) — 1,930 bytes → target 2,000+
13. **Wang Taihe** (`wang-taihe.md`) — 1,617 bytes → target 2,000+

### Fan Qingliang section (2760 lines, ~54KB text)
14. **Fan Qingliang** (`fan-qingliang.md`) — 1,652 bytes → target 2,000+

### Ethan Yang section (937 lines, ~18KB text)
15. **Yang Zhengxiang** (`yang-zhengxiang.md`) — 1,667 bytes → target 2,000+

### Section 2 profiles (649 lines, ~12KB text)
16. **Chen Zhefu & Xu Chunhui** (`chen-zhefu-xu-chunhui.md`) — 1,448 bytes → target 2,000+

## Approach
1. Parse section dump text to extract individual profile narratives
2. Deepen each page with: Overview + Career/Legacy sections
3. Use only facts from the section dump text (no invented bios)
4. Maintain `verification_status: pending`
5. Run link hygiene after each page
6. Commit + publish

## Execution
- Use worker model (pinto) for page creation
- Parent verifies each page (stat + re-read)
- No concurrent edits on same file
- Publish after all pages deepened

## Status: PLANNED
