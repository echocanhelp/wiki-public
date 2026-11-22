# English name harmony — continuation plan

Sweep of Echopedia person and organization pages (there is no `content/places/` tree; churches, chapters, and city associations live under `content/organizations/`).

**Do not mark a page `harmonized` because a mechanical check passed.** Missing `name_en` is normal — the English name often lives in the title. A trailing field-label, CJK glued into the English field, or two sources disagreeing is a real defect. A community's own spelling (安雅堡 for Ann Arbor, used in their own newsletters) is not a defect.

## Rules

1. Vault first. Web only when the vault disagrees with itself or a listing looks like a typo.
2. High confidence = two independent sources agree, and they do not contradict the page's own archive. One website is not enough to overwrite a community's own name.
3. The person's or org's own English name wins over a pinyin gloss. Do not replace Harmony Yang with Yang Xinxin.
4. Keep the wrong form as `aka` or an "also seen" line. Do not pretend the typo was never published.
5. Do not rename a slug unless you leave a `redirect_to` stub. A display-name fix does not require a slug change.
6. Do not delete fragment pages (卓榮泰指, 嚴查, 高雄-as-person) in this lane. They are queued as junk-entity, not name fixes.
7. Subsequent runs: read `state.jsonl`, skip `harmonized`, `not-a-defect`, `hold`, and `out-of-lane`. Work remaining `queue` first. Do not rewrite old rows except to change `queue`.

## This run (2026-10-25)

Universe: 2,461 people + 440 organizations. 22 redirects skipped. Mechanical pass on ~2,133 pages is **not** a harmony stamp.

Fixed (high confidence):

- `people/p-f-yu` — TAH field label `Name` stripped (prior commit `2d390e196d7`)
- `people/harmony-yang` — checked, no change. English is her own name.
- `organizations/asian-american-social-welfaer-foundation` — display name is Welfare. Own site + IRS EIN 27-1674704. Slug still says Welfaer on purpose.
- `people/hsu-ching-chun` — title now leads with Christine Hsu. zh.wikipedia and TAH both use that English name. Romanization kept as aka.
- `people/c-a-chou` — `哲 安` unglued. TAH title is `C. A. Chou 周明(哲)安`.
- `people/sandra-wright-shen` — broken `‧‧沈` prefix removed. English from TAH #70; Chinese from TAH #688.
- `people/theodore-chuang` — `．莊` unglued. `Havard` → Harvard (same table already said Harvard Law School).

## Next queue

See `state.jsonl` rows with `"status": "queue"`. Do those before any new slice.

## Queue pass (2026-10-25, second run)

Closed from the vault, not from a new web bio:

- `people/teng-chieh-teng` — title now Megan Teng. Source sentence 初見鄧立潔（Megan Teng）.
- `people/tah-p-400b8fbb05` — title now Yan-Yu Shih. TAH #269 title. `Sierrra` → Sierra. Era label left blank.
- `people/i-fang-tsai` — title now Yvonne I-Fang Tsai. TAH artist #17. Shorter Who's Who form kept as aka.

Still queued: Billy Chang / Zhang Xuanxin only. Do not merge.

## Queue pass (2026-10-25, third run)

- `organizations/taiwan-hotel-and-motel-association-of-southern-california` — `&Motel` spaced to `& Motel`. Sibling pages already use the spaced form. Slug unchanged.
- `organizations/tacl-toastmaster-club` — archived title is singular Toastmaster Club. One body sentence had been normalized to the parent brand Toastmasters. Aligned to the record. Parent stays Toastmasters International.
- `organizations/taiwanese-america-seniors-association-of-southern-california-tasa` — HOLD. TAH #2/#5/#78 consistently spell Taiwanese-America. Taiwan Center spells American. Not merged.
- Great Richmond, Pharmaceutics, Interculture, Arizona English, STC English, Shee English: not corrected. They are directory forms or already-labeled disagreements.
- Junk-entity pages moved to `out-of-lane`. Do not delete them here.
- He Qinglian display marked harmonized. Slug `he-qingxuan` still held.

## Snapshot pass (2026-10-25, fourth run)

Detector: unstamped person pages whose Identity **English** line disagrees with the title, after dropping honorifics and ignoring a short form that is only a subset of the longer form. 2,403 unstamped people. Six disagreements. Three were real.

- `people/fan-qingliang` — title now Chris Fan (范清亮). 2023 roster pinyin kept. Slug unchanged. Publication transcription left as printed.
- `people/yang-zhengxiang` — title now Ethan Yang (楊正光). Pinyin kept.
- `people/zhang-aihui` — title now Esther Pan (張愛惠). NTPC invitation says Elder Esther Pan. Romanization kept. Chinese roster lines unchanged.
- Katherine Huang, Martha VanDriel, Tiffany Huang: middle names or initials only. Not corrected.
- Butteryfly Chong: HOLD. Who's Who and the oral history disagree.
- Six Albert audiobook scratch pages under `people/` marked `out-of-lane`. Not renamed.

Next run: do not re-scan Identity-English disagreements; that class is closed on unstamped pages. Next class is a title that is pinyin while the body (not the Identity line) uses a different English name.

## Body-name pass (2026-10-25, fifth run)

A surname-sharing scan mostly found relatives. The real hits were a wrong romanization, and titles that hid a known English name behind the Chinese.

- `people/choan-guo-huei` — Ching-chiang Kuo. Our Journeys 37/75/76 English texts agree. Chuan-jiang was 清 read as 川.
- `people/edgar-chun-yi-lin` — Prof. Edgar Lin. TAH #174 and his byline. Jun-Yi stays as the Who's Who form.
- Joyce Lin, Lynn Alan Miles, Irene Fang, Lee Teng-hui — English was already in `name_en`. Title and the people index now lead with it.

Not touched: six titles that still lead with Chinese and put a pinyin or Wade-Giles gloss in parentheses (Chen Wenxue, Li Mutong, Tai Cheng-te, Tsai Jung-fang, Wang Kexiong, Xu Zongbang). Promoting that gloss is not a fix. Next run should check those romanizations against a memoir English, not reorder them.

## Romanization pass (2026-10-25, sixth run)

Checked the six against TAH titles and English memoirs. Three had a real English name. Pages not merged.

- `people/xu-zongbang` — Dr. Charles C. Hsu. TAH #274 signs Charles Hsu, MD. Who's Who #1047 agrees. Twin `charles-c-hsu` left in place.
- `people/wang-kexiong` — Kenneth Wang. TAH #1127. Our Journeys 352 says Ken Wang. Twin `kenneth-wang` left in place.
- `people/li-mutong` — Dr. Tom Lee. TAH #101 and #703 agree. Twin `tom-lee` left in place.
- `people/tai-cheng-te` — Rev. Tai Cheng-te was already the form in the reprint text. Title now leads with it.
- `people/tsai-jung-fang` — HOLD. The page says the romanization is provisional.
- `people/chen-wenxue` — HOLD. Only the 2023 roster uses that pinyin. No memoir English.

Next run: other 2023-roster pinyin pages that already have a TAH Who's Who English twin. Do not invent an English name when the roster is the only source.

## 2023 roster pass (2026-10-25, seventh run)

Where a TAH title already pairs an English name with the Chinese, the person page now leads with that English. Pinyin stays as also-seen. Twins were not merged. The 2023 source page still transcribes the roster as printed.

- Catherine Yang, Shao Liang Cheng, Jeff Chen & Julie Chen, Prof. Sze-ya Yeh & Grace H. Yeh, Dr. Franklin Cheng, Y. T. Wang, Ching Sze Hsieh & Perry B. Shieh.
- Peng Ming-min, Gene Tsai, and Stone Chen were already the right English. Not changed.
- Held, no English invented: Wang Taihe, Zheng Dazhi, Yang Chengwei.
- Not opened: `wang-yao-ting-xie-xiulan`. Xie Xiulan has no TAH English title yet.

The 2023 roster pinyin-vs-TAH-title class is closed except those holds. Next run starts a new class: Who's Who titles whose person page still leads with a different romanization, outside this roster.

## Taiwan surname + TAH English (2026-10-25, eighth run)

Display rule, now in the lexicon: Taiwan surname class, not Hanyu, not Hong Kong. A person's own printed spelling wins. Given-name syllables are not invented from the map. Lookup: `scripts/english-name-from-tah.py` reads `surname_taiwan` and returns `hanyu-gloss` instead of copying a mainland surname.

Surname displays corrected (old form kept as also-seen; slugs unchanged; TAH listing titles left as printed):

- Ehin-Lin Kuo, Kuo Shu-qing, Kuo Yingyan, Hsieh Li-fa, Tsai Wen-hui, Hsu Shitan, Yue-Juan Joanne Kuo, Tseng Dao-xiong, Cheng Quansheng, Cheng Dazhi, William Chou (周威廉), Chou Wei-lin.

TAH English now leads the title (vault title pair, not a web bio):

- Neng-Hsiang Wang (TAH #51; xiang was Hanyu)
- Matthew Lin (TAH #467)
- Jackson Yang (already in the lead; TAH #269)
- Cliff Yang (bylines + TAH #269)
- Dr. Fu-Kuen Lin (TAH #8; kun was Hanyu)
- Shiau-uen Ding (body and TAH #64 already used this)

Held, not overwritten:

- `wanying-heather-zhang` — Tier E charging-document spelling. Do not rename.
- `zhang-xuanxin` — Billy Chang disagreement stays queued. Do not merge.
- `wenhsiung-luke-huang` — the Peter Huang hit is the 1970 event title. This page is the physician. Do not merge.
- `shu-lai` — Taiwan Center board prints Shu Lai. TAH #159 Shu-Yuan Lai is also-seen only.
- `w-j-james-chung` — Who's Who says Chung. Encyclopedia #344 says Chuang. Split.

The 2023 source page still transcribes the roster as printed (Zheng Dazhi). Do not "correct" that transcription.

Next run: the remaining TAH-title disagreements that this pass did not open (word-order-only and married-name pages were skipped). Do not treat an adjacent Latin name in the works index as the person's English without reading the title.

## Wrong-surname pass (2026-10-25, ninth run)

SSOT: `echopedia-romanization-audit.py` no longer keeps its own surname list. It reads `surname_taiwan` from the lexicon. Both script copies were cmp'd identical after the edit.

One real wrong surname, not a married-name false positive:

- `people/ding-yi-wang` — display is Dr. Ding-I Yang. TAH #104 and #105. "Ding Yi Wang" was TAH #273. 王 is his wife's surname (王瑞華), not his. Slug unchanged. Lexicon heal is `display`, so the nightly audit will put the title back if it drifts.

Read and not changed:

- Chen Chao-nan vs Chao-Nan Chen is word order only.
- Katherine Kai-Yi Huang stays. TAH #1213 says Catherine. Her firm name is Katherine.
- Chung Chen Paul Hsu stays. Sharon Hsu on the same title is his wife.
- Karen Chia-Ling Ho stays. Jia-Ling He is the Hanyu gloss of the same person.
- A mechanical "English surname ≠ first Chinese character" scan returned 171 hits. Almost all are married names or a romanization shared by two characters (Chang for 章 and 張, Chien for 簡, Lu for 盧, Hsu for 徐). Do not mass-fix that list.

Next run: open one unread TAH title at a time. Skip married-name surname mismatches unless the archive English and the Chinese surname agree that our display surname is the wrong character.

## Same-characters pass (2026-10-25, tenth run)

Opened `people/wen-s-charlie-chern`. Display name stays Wen S. (Charlie) Chern. TAH #292 and the Who's Who URL agree. Dr. Winston H. Chen is a different 陳文雄 (Air Force One, 1991). That fact had been written onto this page. Removed from Sources, Related Pages, and the role paragraph. Subject lines on TAH #35, #267, and #896 no longer point here. No Winston person page yet. Do not create one from the character match.

The named unread list from the tenth run is closed. Do not reopen these four.

## Two splits read (2026-10-25, eleventh run)

- `people/alexander-k-young` — display stays Alexander K. Young. TAH #220's Alexandra Yang is one title. Memorials, the 1979 book, and the family list (wife Setsuko, son Alexander T.) use Alexander. Not a second person.
- `people/cherng-jia-huang` — HOLD. Who's Who #1140 says Huang. TAH #60, the Diamond Award, and Our Journeys English say Hwang. Both stay on the page. Not picked.

## Four remaining titles closed (2026-10-25, twelfth run)

- `people/christina-yung-chin-mollard` — display is Christina (Yung-Chin) Mollard, the 2016 Who's Who form. Yung-Chin Hsieh is the 2014 maiden name. Not a second person.
- `people/dou-hwei-su-liu` — display stays Dou-Hwei Su Liu. TAH #665 writes Su, Dou-Hwei Liu. Same name, order only.
- `people/min-tenmilton-lee` — display is now Dr. Min-Ten (Milton) Lee. Memoir #381 and collection #84 agree. "Min Ten" was scrape spacing. Dr. Ming Lee stays a video-credit HOLD, not merged.
- `people/tsan-hung-george-chang` — display stays Tsan-hung George Chang. TAH #56's Professor George Chang and the 2017 photo's Prof. Tsan-hung Chang are the same man. Neither part dropped.

The named unread list from the tenth run is closed. Next run starts a new class. Do not reopen these four.

## Glue class (2026-10-25, thirteenth run)

A scan of unstamped titles found four English fields with a stray mark or a broken Chinese character glued on. All four were stripped. Real spellings were not rewritten.

- `people/nellie-gephardt-amondson` — English is Nellie Gephardt Amondson. The ‧ belongs in TAH #1614's Chinese, 納莉‧艾默森.
- `people/paul-b-hshieh` — 六 was 六 from 謝博六. Hshieh stays. No second source to rewrite it as Hsieh. 博士 dropped from the Chinese name field.
- `people/w-d-lee` — 李 was 李. TAH #1403 is W. D. Lee 李武達.
- `organizations/houston-taiwanese-golden-club` — 樂部 stripped from the English. The short Chinese form stays a truncation HOLD.

This glue class is closed. Do not reopen these four. Next run starts another class.

## TAH title versus page title (2026-10-25, fourteenth run)

Compared unstamped person titles with the works-index English for the same 漢名. Thirty-two disagreed. Most were the page being fuller, or a split. Five displays changed. One was held.

- `people/julius-shu-05` — Julius Shu. "05" was May from TAH #429, 05/2015.
- `people/wu-lipei` — display is now Li Pei Wu. TAH #21, #122, #271, and #269 agree. Wu Li-pei stays as the harvest order.
- `people/tah-p-0e321dc33f` — title now leads with Pei Chung Tsai. The English was already in the identity. TAH #228.
- `people/tah-p-bebef2fc0f` — Bing-Heng Chen. TAH #283 is all caps. Title case is not a different spelling.
- `people/tah-p-f5d7338384` — Y. L. Lin. Initials only, from TAH #1711. Not expanded.
- `people/yang-yuanxun` — HOLD. TAH #25 is Carole Yang. TAH #279 is Carole Hsu. Display stays Yang Yuan-xun.

Do not reopen these six. The other disagreements in that scan were left because the page English was already fuller, or the TAH form was Hanyu. Next run: Chinese-only Who's Who titles whose TAH English is one form and not a mainland surname. Skip splits.

## Chinese-only Who's Who titles (2026-10-25, fifteenth run)

Eight unstamped Who's Who pages still led with Chinese only. Each had one works-index English, and the surname was not on the mainland list. The archive spelling was copied. It was not converted.

- `people/tah-p-2f601a3b72` — Yu-Miao Wen. TAH #173.
- `people/tah-p-372f20f9ee` — Fu-Yu Lin. TAH #238.
- `people/tah-p-957ce8befb` — Cing-Ru Shih. TAH #276 prints Cing-Ru. Not rewritten.
- `people/tah-p-9af7a1ae9e` — Jin Song Chen. TAH #223's own spelling. Not converted.
- `people/tah-p-b256f6296d` — Hong-Yi Lai. TAH #294's own spelling. Not converted.
- `people/tah-p-b3e363fd2d` — Ci-Yao Chen. TAH #171's own spelling. Not converted.
- `people/tah-p-b5dfddaa1e` — Ray-Yun Huang Tsai. TAH #277. Both surnames kept.
- `people/tah-p-dbd0edebb9` — S. H. Huang. Initials only, TAH #1660. Not expanded.

This passing set is closed. Do not reopen these eight. Next run: the Chinese-only Who's Who titles that remain. If the only TAH English uses a mainland surname (Ye, Du, and the lexicon list), stamp hold and do not copy it. If there is no Latin title, do not invent one.

## Glued English, no space (2026-10-25, sixteenth run)

The last scan required a space between the English and the Chinese. Five Who's Who titles had the English stuck to the characters. One more English was a collection title, with a pen name glued onto the Chinese. Two mainland surnames were held.

- `people/tah-p-0c2b755a64` — Pei-Yao Wang. TAH #242.
- `people/tah-p-0f50cf1291` — Yueh-Mei Wu Rowen. TAH #368. Married name kept.
- `people/tah-p-1bf2083742` — Helena Wei. TAH #125.
- `people/tah-p-850ffab5db` — Jonathan Jou. TAH #297 prints Jou. Not rewritten to Chou.
- `people/tah-p-9078eeef12` — Hui-Jin Wang. TAH #338's own spelling. Not converted.
- `people/tah-p-096c81c4f5` — Charmian Cheng. Collection #51. 夏眉 is the pen name. Cheng not rewritten to Hsieh.
- `people/tah-p-23744668d9` — HOLD. TAH #325 is Meng-Yun Ye. Not copied.
- `people/tah-p-f29b98a03f` — HOLD. TAH #253 is Wan-Shan Du. Not copied.

Do not reopen these eight. Next run: remaining Chinese-only Who's Who titles. A role word on the line (Pianist, Violinist) is not a name. Do not invent English. If the only Latin form is a mainland surname, hold it.

## English already on the page (2026-10-25, seventeenth run)

Five Chinese-only Who's Who titles already had the person's own English in the page or in a cited vault record. The title now leads with it. A son's name and a different man's name were not copied.

- `people/tah-p-3496456ca5` — John Chou. Already on the identity. Works-index #189 and #607 are Chinese-only.
- `people/tah-p-7e080ca41d` — Dr. Chung-Chih Li. His byline on Green Island Secrets. Who's Who #647 is Chinese-only.
- `people/tah-p-8c33cb949b` — David Lai. His contact block in Our Journeys 290. Who's Who #633 is Chinese-only.
- `people/tah-p-f831dcdf3e` — Abe Chen. Hakka roster and his own TAH profile. Who's Who #728 is Chinese-only.
- `people/tah-p-04e87d0c6a` — Kuo Yu-hsin. Wade-Giles in the English text of Our Journeys #321. Not Guo Yu.

Not copied: William Ko is the son of 柯承家. Kang-Lu Wang is 王康陸, not 王康厚. A name in a deepen-x search comment is not the subject's English.

Do not reopen these five. Next run: remaining Chinese-only Who's Who titles. Read the page before copying a Latin name from the body. A relative, a namesake, or a search-probe string is not the subject.

## Title-word glue (2026-10-25, eighteenth run)

Ten Who's Who titles still had a rank or a field label glued onto the Chinese name. Those words were stripped. No English was invented.

- `people/tah-p-161a8a78cc` — 劉青藜. 博士 dropped.
- `people/tah-p-230622a660` — 李秉林. 博士 dropped.
- `people/tah-p-26d063c006` — 李台光. 博士 dropped.
- `people/tah-p-464a81f5f0` — 葉英堃. 博士 dropped.
- `people/tah-p-4b7e8e54e2` — 陳昭俊. 博士 dropped.
- `people/tah-p-5e9ef27eba` — 陳宜蓁. 博士 dropped.
- `people/tah-p-78afe78c03` — 陳玲玉. 博士 dropped.
- `people/tah-p-de93a9fd26` — 黃聖祐. 博士 dropped.
- `people/tah-p-f2a1bb4ac0` — 李玉琛. 醫師 dropped.
- `people/tah-p-a2aa6c2089` — 李泰雄. 筆名 was a field label. 南鄉泰 stays the pen name, TAH #65 and #24. Not an English name.

The source-hub label for 施彥伃 was still 施彥伃博士. The person page already leads with Yan-Yu Shih. The hub label was aligned. No new English.

Do not reopen these ten. English is still missing on the nine Chinese titles. Do not invent it. Next run: remaining Chinese-only Who's Who titles whose body names the subject, not a relative or a search probe.

## One sourced English, one false gloss (2026-10-25, nineteenth run)

The remaining Chinese-only Who's Who titles were read for the subject's own English. A parenthetical in a boilerplate sentence is not a source. One page outside that set already had the English in the frontmatter.

- `people/沈伯洋` — display is now Puma Shen. Shen Pao-yang stays also-seen. Both were already on the page. 撲馬 is the nickname.
- `people/tah-p-8c5a93b3d4` — HOLD. The line "Wang Kang-hou" is not in TAH #375. The URL is Chinese only. Not copied. Kang-Lu Wang remains 王康陸.

Do not reopen these two. Next run: do not invent English for the remaining Chinese-only Who's Who titles. A URL slug, a search probe, or a boilerplate romanization is not a name. Move to another class only after that rule is kept.

## Organization English the page already states (2026-10-25, twentieth run)

Chinese-only Who's Who titles were not given invented English. The next class was organizations whose own history names a current English the title does not use.

- `organizations/taiwanese-american-federation-of-n-california` — display is now Taiwanese American Federation of Northern California. The 2003 festschrift says that name stayed. N. California is the directory form. NCFF is the 1973 name. Chinese on the title had been truncated to 北加州.
- `organizations/taiwanese-american-association-of-capital-district-new-york` — display is now Taiwanese American Association of the Capital District. The founding history says the 1984 name is still in use. The directory form dropped "the".
- `organizations/north-america-taiwanese-medical-association-southern-california-chapte` — display is now North American Taiwanese Medical Association — Southern California Chapter. The parenthetical "verify EN name" was a workflow note, not part of the name. TAH yearbooks use North American. Slug was not renamed.
- `organizations/greater-washington-taiwan-culture-center` — HOLD. Directory order and "Taiwan Culture Center of Greater Washington D.C." both stay. Not picked.

Do not reopen these four. Next run: other organization pages whose own record names a current English the title does not use. Do not invent. Do not pick a word-order split.

## Bylaw and own-record English (2026-10-25, twenty-first run)

Scanned unstamped organization pages for an English name the page itself states (英文名稱 / English name / rename verbs / parenthetical after the CJK name in the lead) that the title does not carry. The parenthetical-after-CJK detector is mostly noise — person names, event titles, and neighboring organizations sit in parentheses too. Read every candidate; only the page's own statement of its own current name counts.

- `organizations/national-taiwanese-presbyterian-council` — display is now National Taiwanese Presbyterian Council, Presbyterian Church (U.S.A.) (NTPC). The bylaw page quoted on the page gives that as the 英文名稱. The short form is kept as also-seen. Slug unchanged.
- `organizations/taiwanese-association-of-indiana` — checked, no change. The title is already the 2023-04-17 IRS-approved name the chapter's own memoir states. The 1978 founding English stays as history.
- `organizations/friends-of-taiwan` — not corrected. The English is the org's own TAH form. A memorial's parenthetical (Friend of Taiwan) is a body translation variant. The 社/會 HOLD stays.

Do not reopen these three. Next run: the remaining organization pages were only scanned for self-stated English, not read. The parenthetical detector surfaced predecessor names (Formosan Club of the Univ. of Michigan on the Michigan TWSA page) — a predecessor name is history, not a defect. Do not promote one into a title.
