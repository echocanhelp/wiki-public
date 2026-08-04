#!/usr/bin/env python3
"""
P1 Deepen: Enrich columnist/contributor pages with TJ citations.

Reads the priority-hits JSONL (6,773 hits), groups by columnist slug,
extracts citation data from top matching articles, and enriches each
columnist page with a "TJ Citations" section.

Processes in batches to avoid context overflow.

Usage:
  python3 enrich_columnist_pages.py --batch 1 --batch-size 5
  python3 enrich_columnist_pages.py --all
  python3 enrich_columnist_pages.py --columnist chen-po-kong
"""

import json
import os
import re
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Paths
REPO_ROOT = Path.home() / "echo-system"
HITS_FILE = REPO_ROOT / "knowledge/research/taiwanjustice-net-priority-hits.jsonl"
CONTENT_DIR = REPO_ROOT / "content"
PEOPLE_DIR = CONTENT_DIR / "people"
ARTICLES_DIR = CONTENT_DIR / "articles" / "taiwanjustice-net"

# Columnist slugs from the entities index (21 column authors)
COLUMNIST_SLUGS = [
    "chen-po-kong",      # 陳破空 - 463 articles
    "chen-maoxiong",     # 陳茂雄 - 475 articles
    "chen-zhaonan",      # 陳昭南 - 398 articles
    "lin-baohua",        # 林保華 - 241 articles
    "yu-jie",            # 余杰 - 99 articles
    "fan-jiang-ti-ang",  # 范姜提昂 - 66 articles
    "yang-ziqing",       # 楊子清 - 65 articles
    "huang-diyin",       # 黃帝穎 - 57 articles
    "he-qingxuan",       # 何清漣 - 50 articles
    "liao-qingshan",     # 廖清山 - 37 articles
    "jin-hegui",         # 金恆煒 - 9 articles
    "ku-chuan-min",      # 辜寬敏 - 8 articles (no page yet)
    "zeng-daoxiong",     # 曾道雄 - 6 articles
    "li-xiaofeng",       # 李筱峰 - 5 articles
    "hong-ya",           # 洪雅 - 4 articles
    "chen-rijun",        # 陳日君 - 4 articles (no page yet)
    "yi-si-an",          # 易思安 - 3 articles (no page yet)
    "fei-xue-li",        # 費學禮 - 2 articles (no page yet)
    "he-ruien",          # 何瑞恩 - 2 articles (no page yet)
    "tan-shenge",        # 譚慎格 - 1 article (no page yet)
    "du-ao-cunfu",       # 獨傲村夫 - articles
]

# Additional contributor slugs that have pages
ADDITIONAL_SLUGS = [
    "tang-peili",        # 唐培理
    "yang-yuanxun",      # 楊遠薰
    "yang-yueqing",      # 楊月清
    "li-jian",           # 李堅
    "nanfang-shuo",      # 南方朔
    "wang-dan",          # 王丹
    "wang-shufen",       # 王淑芬
    "wei-jingsheng",     # 魏景升
    "wu-lipei",          # 吳立埔
    "xia-ming",          # 小明
    "ye-siya",           # 葉思雅
    "zhang-xinhui",      # 張信惠
    "yuan-zhihui",       # 袁志輝
    "zheng-bingquan",    # 鄭炳全
    "li-rongsong",       # 林榮松
    "cai-shunyu",        # 蔡順宇
    "cao-changqing",     # 曹長青
    "chao-sile",         # 朝思樂
    "guan-renjian",      # 管仁健
    "huang-yongcheng",   # 黃永成
    "hu-ping",           # 胡平
    "kevin-lee",         # Kevin Lee
    "bai-peiyu",         # 白珮瑜
    "sang-pu",           # 桑普
    "shen-zizai",        # 沈子載
    "ian-easton",        # 易思安 (Ian Easton)
    "richard-d-fisher",  # 費學禮 (Richard D. Fisher)
    "john-j-tkacik",     # 譚慎格 (John J. Tkacik)
    "ryan-hass",         # 何瑞恩 (Ryan Hass)
    "jiang-bai-xian",    # 江百顯
    "gong-sun-le",       # 公孫樂
]

ALL_SLUGS = list(dict.fromkeys(COLUMNIST_SLUGS + ADDITIONAL_SLUGS))


def load_hits():
    """Load the priority-hits JSONL file."""
    hits = []
    with open(HITS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                hits.append(json.loads(line))
    return hits


def group_hits_by_slug(hits):
    """Group hits by columnist slug."""
    grouped = defaultdict(list)
    for hit in hits:
        for match in hit.get("matches", []):
            slug = match.get("slug")
            if slug and slug in ALL_SLUGS:
                grouped[slug].append(hit)
    return grouped


def extract_citation_from_article(article_path, hit):
    """Extract citation data from an article markdown file."""
    path = REPO_ROOT / article_path
    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse frontmatter
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not frontmatter_match:
        return None

    fm = frontmatter_match.group(1)
    fm_dict = {}
    for line in fm.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            fm_dict[key.strip()] = value.strip()

    title = fm_dict.get("title", hit.get("title", "Untitled"))
    post_date = fm_dict.get("post_date", "")
    source_url = fm_dict.get("source_url", "")
    archive_url = fm_dict.get("archive_url", "")

    # Extract body (after frontmatter)
    body_start = frontmatter_match.end()
    body = content[body_start:].strip()

    # Extract first paragraph (for snippet)
    # Skip navigation/menu content — look for actual article content
    # Article body starts after the frontmatter, skip nav links
    lines = body.split("\n")
    snippet = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Skip common nav/menu items
        if line in ("Home", "Sign in", "Welcome! Log into your account",
                     "your username", "your password", "Forgot your password? Get help",
                     "Password recovery", "your email", "A password will be e-mailed to you.",
                     "Taiwan Justice | 台灣公義報", "Search", "Wednesday, February 21, 2024"):
            continue
        # Skip pagination
        if re.match(r"^[0-9]+$", line):
            continue
        if line.startswith("Page 1 of"):
            continue
        # Skip category menu items
        if line in ("台灣頭條", "頭條總攬", "政黨輪替與轉型正義", "台灣文化",
                     "台灣人文藝術", "台灣鄉情與文化", "台灣史地", "台灣地方自古不屬中國",
                     "蓬萊島雜誌", "買票作票見聞錄", "美國頭梢", "南海東海風雲",
                     "川普時代", "美國新聞", "國際焦點", "頭條總覽", "國際要聞",
                     "世界人文", "科技新聞", "賈伯斯專輯", "中國新聞", "中國史地",
                     "English Pages", "世界史地", "義論", "專欄", "動畫", "影音",
                     "焦點影音", "關鍵時刻", "鄭 知道了", "新台灣加油", "前進新台灣",
                     "新聞面對面", "台灣新世紀文教基金會", "驚爆新聞線", "年代向錢看",
                     "新聞挖挖哇", "台灣演義", "我們的島", "台灣亮起來", "消失的國界",
                     "中天調查報告", "聚焦2.0", "台灣啟示錄", "看板人物", "李四端的雲端世界",
                     "突發琪想", "新聞深呼吸", "T觀點", "民視異言堂", "有話好說",
                     "海外台灣人", "藝文", "歷史必讀", "保健", "園藝", "大洛杉磯台灣會館",
                     "台灣會館會訊", "台美人影音頻道", "浮世繪", "我的肥皂箱",
                     "週末漫談音樂", "台語文天地", "Covid-19 浩劫餘生錄",
                     "美股台股消息", "美股", "台股", "老郎(老人)心天地"):
            continue
        # Skip columnist nav links
        if line.endswith("專欄") or line.endswith("觀點") or line.endswith("音樂教室"):
            continue
        if line in ("林保華專欄", "陳茂雄專欄", "陳昭南觀點", "何清漣專欄",
                     "獨傲村夫專欄", "廖清山專欄", "陳破空專欄", "黃帝穎專欄",
                     "范姜提昂專欄", "李堅專欄", "金恆煒專欄", "楊子清 Cliff Yang 音樂教室",
                     "楊遠薰專欄", "鄭炳全專欄"):
            continue
        # Skip "Most popular", "Latest", "Featured posts", etc.
        if line in ("Most popular", "Latest", "Featured posts", "7 days popular",
                     "By review score", "Random"):
            continue
        # Skip "林保華專欄" etc. as nav
        if re.match(r"^林保華專欄$|^陳茂雄專欄$|^陳昭南觀點$|^何清漣專欄$|^獨傲村夫專欄$|^廖清山專欄$|^陳破空專欄$|^黃帝穎專欄$|^范姜提昂專欄$|^李堅專欄$|^金恆煒專欄$|^楊子清 Cliff Yang 音樂教室$|^楊遠薰專欄$|^鄭炳全專欄$|^陳日君專欄$|^辜寬敏專欄$|^唐培理專欄$|^費學禮專欄$|^譚慎格專欄$|^何瑞恩專欄$|^易思安專欄$|^洪雅專欄$|^曾道雄專欄$|^李筱峰專欄$|^金恆煒專欄$", line):
            continue
        # Skip nav menu items with "/" (like "台灣地方自古不屬中國/李筱峰/系列;1-5")
        if "/" in line and len(line) < 60:
            continue
        # Found first content line — prefer lines with "◎" (article content marker)
        if "◎" in line:
            snippet = line[:200]
            break
        # Or date lines like "July 7, 2018"
        if re.match(r"^[A-Z][a-z]+ \d{1,2}, \d{4}$", line):
            snippet = line[:200]
            break
        # Or lines with author attribution like "陳破空/ 民報"
        if re.search(r"/.*(民報|自由時報|極光|聯合報|中評社|自由亞洲電台)", line):
            snippet = line[:200]
            break
        # Fallback: first non-nav line
        if not snippet:
            snippet = line[:200]

    # Extract date from post_date
    date_str = ""
    if post_date:
        # Format: "2017-11-13 03:43:37-08:00"
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", post_date)
        if date_match:
            date_str = date_match.group(1)

    return {
        "title": title,
        "date": date_str,
        "source_url": source_url,
        "archive_url": archive_url,
        "snippet": snippet,
        "score": hit.get("score", 0),
        "path": article_path,
    }


def enrich_columnist_page(slug, citations):
    """Enrich a columnist page with TJ citations."""
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        print(f"  SKIP: {slug} — no page exists")
        return False

    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has TJ Citations section
    if "## TJ Citations" in content:
        print(f"  SKIP: {slug} — already has TJ Citations section")
        return False

    # Check if has "## Source Notes" — insert before it
    # Otherwise insert before "## Related Pages"
    # Otherwise append at end

    # Sort citations by score descending, take top 10
    citations_sorted = sorted(citations, key=lambda x: x["score"], reverse=True)[:10]

    # Build the citations section
    citation_lines = []
    citation_lines.append(f"\n## TJ Citations\n")
    citation_lines.append(f"Top {len(citations_sorted)} articles from taiwanjustice.net mentioning {slug}:\n")

    for i, cite in enumerate(citations_sorted, 1):
        date_str = cite["date"] if cite["date"] else "undated"
        title = cite["title"]
        archive_url = cite["archive_url"]
        source_url = cite["source_url"]

        # Build citation entry
        if archive_url:
            citation_lines.append(f"{i}. **{date_str}** — [{title}]({archive_url})")
        elif source_url:
            citation_lines.append(f"{i}. **{date_str}** — [{title}]({source_url})")
        else:
            citation_lines.append(f"{i}. **{date_str}** — {title}")

        if cite["snippet"]:
            snippet = cite["snippet"].replace("\n", " ")[:150]
            citation_lines.append(f"   - *{snippet}...*")

        citation_lines.append(f"   - Score: {cite['score']}")

    citation_lines.append("")

    # Find insertion point
    # Insert before "## Source Notes" if it exists
    if "## Source Notes" in content:
        insert_before = "## Source Notes"
    elif "## Related Pages" in content:
        insert_before = "## Related Pages"
    else:
        # Append at end
        insert_before = None

    if insert_before:
        new_section = "\n".join(citation_lines) + "\n"
        content = content.replace(insert_before, new_section + insert_before)
    else:
        new_section = "\n".join(citation_lines)
        content = content.rstrip() + "\n" + new_section

    # Update last_reviewed date
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"last_reviewed: \d{4}-\d{2}-\d{2}",
        f"last_reviewed: {today}",
        content
    )

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  DONE: {slug} — enriched with {len(citations_sorted)} citations")
    return True


def main():
    parser = argparse.ArgumentParser(description="Enrich columnist pages with TJ citations")
    parser.add_argument("--batch", type=int, default=1, help="Batch number (1-based)")
    parser.add_argument("--batch-size", type=int, default=5, help="Pages per batch")
    parser.add_argument("--all", action="store_true", help="Process all pages")
    parser.add_argument("--columnist", type=str, help="Process a single columnist")
    parser.add_argument("--list-slugs", action="store_true", help="List all columnist slugs")
    args = parser.parse_args()

    if args.list_slugs:
        for slug in ALL_SLUGS:
            print(slug)
        return

    # Determine which slugs to process
    if args.columnist:
        slugs = [args.columnist]
    elif args.all:
        slugs = ALL_SLUGS
    else:
        # Batch mode
        start = (args.batch - 1) * args.batch_size
        end = start + args.batch_size
        slugs = ALL_SLUGS[start:end]

    if not slugs:
        print("No slugs to process in this batch.")
        return

    print(f"Loading priority hits from {HITS_FILE}...")
    hits = load_hits()
    print(f"  Loaded {len(hits)} hits")

    print(f"Grouping hits by slug...")
    grouped = group_hits_by_slug(hits)
    print(f"  Found hits for {len(grouped)} slugs")

    # Process each slug
    results = []
    for slug in slugs:
        print(f"\nProcessing: {slug}")
        slug_hits = grouped.get(slug, [])
        if not slug_hits:
            print(f"  SKIP: {slug} — no hits found")
            continue

        # Extract citations from articles
        citations = []
        for hit in slug_hits:
            cite = extract_citation_from_article(hit["path"], hit)
            if cite:
                citations.append(cite)

        if not citations:
            print(f"  SKIP: {slug} — no citations extracted")
            continue

        print(f"  Found {len(citations)} citations, enriching page...")
        success = enrich_columnist_page(slug, citations)
        results.append((slug, success, len(citations)))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for slug, success, count in results:
        status = "DONE" if success else "SKIPPED"
        print(f"  {slug}: {status} ({count} citations)")

    done = sum(1 for _, s, _ in results if s)
    print(f"\n  Total: {done}/{len(results)} pages enriched")


if __name__ == "__main__":
    main()
