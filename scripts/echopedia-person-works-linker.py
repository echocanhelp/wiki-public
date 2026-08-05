#!/usr/bin/env python3
"""
P1 Link: Automatically link Echopedia person pages to all their works.

Reads the priority-hits JSONL (or any hits file), groups by columnist slug,
and for each person page:

  1. Generates a COMPLETE ## Works section with ALL articles where the person
     appears in the TITLE (their own column articles), grouped by year.
     (NOT just top-10 — the existing enrich_columnist_pages.py only does top-10.)

  2. Adds wikilinks from each article back to the person page
     ([[people/<slug>|Author Name]]) in the article's frontmatter or body.

This runs as a no_agent cron job for automatic maintenance.

Usage:
  python3 echopedia-person-works-linker.py --all
  python3 echopedia-person-works-linker.py --columnist chen-po-kong
  python3 echopedia-person-works-linker.py --dry-run --all
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
LOG_DIR = REPO_ROOT / "echopedia" / "logs"

# Columnist slugs that have person pages
COLUMNIST_SLUGS = [
    "chen-po-kong",      # 陳破空
    "chen-maoxiong",     # 陳茂雄
    "chen-zhaonan",      # 陳昭南
    "lin-baohua",        # 林保華
    "yu-jie",            # 余杰
    "fan-jiang-ti-ang",  # 范姜提昂
    "yang-ziqing",       # 楊子清
    "huang-diyin",       # 黃帝穎
    "he-qingxuan",       # 何清漣
    "liao-qingshan",     # 廖清山
    "jin-hegui",         # 金恆煒
    "ku-chuan-min",      # 辜寬敏
    "zeng-daoxiong",     # 曾道雄
    "li-xiaofeng",       # 李筱峰
    "hong-ya",           # 洪雅
    "chen-rijun",        # 陳日君
    "du-ao-cunfu",       # 獨傲村夫
]

# Additional contributor slugs with person pages
ADDITIONAL_SLUGS = [
    "tang-peili", "yang-yuanxun", "yang-yueqing", "li-jian",
    "nanfang-shuo", "wang-dan", "wang-shufen", "wei-jingsheng",
    "wu-lipei", "xia-ming", "ye-siya", "zhang-xinhui",
    "yuan-zhihui", "zheng-bingquan", "li-rongsong", "cai-shunyu",
    "cao-changqing", "chao-sile", "guan-renjian", "huang-yongcheng",
    "hu-ping", "kevin-lee", "bai-peiyu", "sang-pu", "shen-zizai",
    "ian-easton", "richard-d-fisher", "john-j-tkacik", "ryan-hass",
    "jiang-bai-xian", "gong-sun-le",
]

# TAHS founding member slugs — these appear in articles but aren't columnists
# They need Chinese name body search to find their works
FOUNDING_MEMBER_SLUGS = [
    "yang-jia-you",      # Charles Yang (楊嘉猷) — founding president
    "becky-yang",        # Becky Yang — founding member
    "leonard-hsu-jr",    # Leonard Hsu Jr. (許景鴻) — current president
    "franklin-ping-cheng",  # Franklin Ping Cheng (程炳成) — 2014-2017 president
    "wang-gui-rong",     # Wang Gui-rong (王桂榮) — founding member
    "huang-gen-shen",    # Huang Gen-shen (黃根深) — founding member
    "zhou-wei-lin",      # Zhou Wei-lin (周威霖) — founding member
    "zhou-shi",          # Zhou Shi (周實) — founding member
    "chen-long",         # Chen Long (陳隆) — founding member
    "hong-zhu-mei",      # Hong Zhu-mei (洪珠美) — founding member
    "yang-ziqing",       # Yang Ziqing (楊子清) — founding member
    "liao-ji-chun",      # Liao Ji-chun (廖述宗) — founding member
    "zheng-bing-quan",   # Zheng Bing-quan (鄭炳全) — founding member
    "wang-ting-yi",      # Wang Ting-yi (王廷宜) — founding member
]

ALL_SLUGS = list(dict.fromkeys(COLUMNIST_SLUGS + ADDITIONAL_SLUGS + FOUNDING_MEMBER_SLUGS))

# Chinese name lookup for wikilinks
SLUG_TO_CHINESE = {
    "chen-po-kong": "陳破空",
    "chen-maoxiong": "陳茂雄",
    "chen-zhaonan": "陳昭南",
    "lin-baohua": "林保華",
    "yu-jie": "余杰",
    "fan-jiang-ti-ang": "范姜提昂",
    "yang-ziqing": "楊子清",
    "huang-diyin": "黃帝穎",
    "he-qingxuan": "何清漣",
    "liao-qingshan": "廖清山",
    "jin-hegui": "金恆煒",
    "ku-chuan-min": "辜寬敏",
    "zeng-daoxiong": "曾道雄",
    "li-xiaofeng": "李筱峰",
    "hong-ya": "洪雅",
    "chen-rijun": "陳日君",
    "du-ao-cunfu": "獨傲村夫",
    "tang-peili": "唐培理",
    "yang-yuanxun": "楊遠薰",
    "yang-yueqing": "楊月清",
    "li-jian": "李堅",
    "nanfang-shuo": "南方朔",
    "wang-dan": "王丹",
    "wang-shufen": "王淑芬",
    "wei-jingsheng": "魏景升",
    "wu-lipei": "吳立埔",
    "xia-ming": "小明",
    "ye-siya": "葉思雅",
    "zhang-xinhui": "張信惠",
    "yuan-zhihui": "袁志輝",
    "zheng-bingquan": "鄭炳全",
    "li-rongsong": "林榮松",
    "cai-shunyu": "蔡順宇",
    "cao-changqing": "曹長青",
    "chao-sile": "朝思樂",
    "guan-renjian": "管仁健",
    "huang-yongcheng": "黃永成",
    "hu-ping": "胡平",
    "kevin-lee": "Kevin Lee",
    "bai-peiyu": "白珮瑜",
    "sang-pu": "桑普",
    "shen-zizai": "沈子載",
    "ian-easton": "易思安",
    "richard-d-fisher": "費學禮",
    "john-j-tkacik": "譚慎格",
    "ryan-hass": "何瑞恩",
    "jiang-bai-xian": "江百顯",
    "gong-sun-le": "公孫樂",
    # TAHS founding members
    "yang-jia-you": "楊嘉猷",
    "becky-yang": "楊佩珊",
    "leonard-hsu-jr": "許景鴻",
    "franklin-ping-cheng": "程炳成",
    "wang-gui-rong": "王桂榮",
    "huang-gen-shen": "黃根深",
    "zhou-wei-lin": "周威霖",
    "zhou-shi": "周實",
    "chen-long": "陳隆",
    "hong-zhu-mei": "洪珠美",
    "liao-ji-chun": "廖述宗",
    "wang-ting-yi": "王廷宜",
}


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
    """Group hits by columnist slug, separating title mentions from body mentions.

    For founding members (who aren't columnists), also search article bodies
    for Chinese name mentions since they won't be in the priority-hits JSONL.
    """
    grouped = defaultdict(lambda: {"title": [], "body": []})

    # 1. Process existing hits from JSONL (columnists + additional slugs)
    for hit in hits:
        for match in hit.get("matches", []):
            slug = match.get("slug")
            if slug and slug in ALL_SLUGS:
                where = match.get("where", [])
                if "title" in where:
                    grouped[slug]["title"].append(hit)
                if "body" in where:
                    grouped[slug]["body"].append(hit)

    # 2. For founding members, search article bodies for Chinese name mentions
    #    (they won't appear in the priority-hits JSONL since they're not columnists)
    founding_member_slugs = set(FOUNDING_MEMBER_SLUGS)
    if founding_member_slugs:
        # Build Chinese name → slug lookup
        chinese_to_slug = {}
        for slug in founding_member_slugs:
            chinese_name = SLUG_TO_CHINESE.get(slug)
            if chinese_name:
                chinese_to_slug[chinese_name] = slug

        # Search all Taiwan Justice articles for Chinese name mentions
        articles_dir = CONTENT_DIR / "articles" / "taiwanjustice-net"
        if articles_dir.exists():
            for article_file in articles_dir.rglob("*.md"):
                try:
                    content = article_file.read_text(encoding="utf-8")
                    # Extract relative path for the hit structure
                    rel_path = str(article_file.relative_to(REPO_ROOT))

                    for chinese_name, slug in chinese_to_slug.items():
                        if chinese_name in content:
                            # Check if it's in the title (frontmatter)
                            title_match = re.search(
                                r'^title:\s*.*' + re.escape(chinese_name),
                                content, re.MULTILINE | re.DOTALL
                            )
                            hit = {
                                "path": rel_path,
                                "score": 1,
                                "matches": [{
                                    "slug": slug,
                                    "where": ["title"] if title_match else ["body"],
                                    "text": chinese_name
                                }]
                            }
                            if title_match:
                                grouped[slug]["title"].append(hit)
                            else:
                                grouped[slug]["body"].append(hit)
                except (OSError, UnicodeDecodeError):
                    continue

    return grouped


def extract_article_metadata(article_path):
    """Extract frontmatter metadata from an article markdown file."""
    path = REPO_ROOT / article_path
    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse frontmatter
    fm_match = re.match(r"^---\n(.*?)---\n", content, re.DOTALL)
    if not fm_match:
        return None

    fm = fm_match.group(1)
    fm_dict = {}
    for line in fm.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            fm_dict[key.strip()] = value.strip()

    title = fm_dict.get("title", "")
    post_date = fm_dict.get("post_date", "")
    source_url = fm_dict.get("source_url", "")
    archive_url = fm_dict.get("archive_url", "")

    # Extract date
    date_str = ""
    if post_date:
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", post_date)
        if date_match:
            date_str = date_match.group(1)

    # Extract year
    year = ""
    if date_str:
        year = date_str[:4]
    elif post_date:
        year_match = re.search(r"(\d{4})", post_date)
        if year_match:
            year = year_match.group(1)

    return {
        "title": title,
        "date": date_str,
        "year": year,
        "source_url": source_url,
        "archive_url": archive_url,
        "path": article_path,
        "filename": path.name,
        "content": content,
        "fm_match": fm_match,
        "fm_dict": fm_dict,
    }


def generate_works_section(slug, title_articles, body_articles):
    """Generate a complete ## Works section for a person page.

    Includes ALL articles where the person appears in the title (their own
    column articles), grouped by year. Also notes body-mention count.
    """
    chinese_name = SLUG_TO_CHINESE.get(slug, slug)
    total_title = len(title_articles)
    total_body = len(body_articles)

    lines = []
    lines.append(f"\n## Works\n")
    lines.append(f"**{chinese_name}** has **{total_title}** articles where they appear in the title "
                 f"(column articles) and **{total_body}** additional articles that mention them in the body.\n")

    # Group title articles by year
    by_year = defaultdict(list)
    for article in title_articles:
        meta = extract_article_metadata(article["path"])
        if meta:
            year = meta["year"] if meta["year"] else "Undated"
            by_year[year].append(meta)

    # Sort years descending
    sorted_years = sorted(by_year.keys(), reverse=True)

    for year in sorted_years:
        articles = by_year[year]
        # Sort by date within year
        articles.sort(key=lambda x: x["date"] if x["date"] else "0000-00-00", reverse=True)
        lines.append(f"\n### {year} ({len(articles)} articles)\n")
        for i, meta in enumerate(articles, 1):
            # Build link — prefer archive_url, fallback to source_url
            url = meta["archive_url"] if meta["archive_url"] else meta["source_url"]
            title = meta["title"] if meta["title"] else meta["filename"]
            date_str = meta["date"] if meta["date"] else "undated"

            if url:
                lines.append(f"{i}. **{date_str}** — [{title}]({url})")
            else:
                lines.append(f"{i}. **{date_str}** — {title}")

    # Add body mentions section
    if total_body > 0:
        lines.append(f"\n### Body Mentions ({total_body} articles)\n")
        lines.append(f"Articles by other authors that mention **{chinese_name}**: "
                     f"See [[sources/taiwanjustice-net|taiwanjustice.net source hub]] for the full "
                     f"article index. Top mentions by score:\n")
        # Show top 5 body mentions by score
        sorted_body = sorted(body_articles, key=lambda x: x.get("score", 0), reverse=True)[:5]
        for i, article in enumerate(sorted_body, 1):
            meta = extract_article_metadata(article["path"])
            if meta:
                url = meta["archive_url"] if meta["archive_url"] else meta["source_url"]
                title = meta["title"] if meta["title"] else meta["filename"]
                date_str = meta["date"] if meta["date"] else "undated"
                score = article.get("score", 0)
                if url:
                    lines.append(f"{i}. **{date_str}** — [{title}]({url}) (score: {score})")
                else:
                    lines.append(f"{i}. **{date_str}** — {title} (score: {score})")

    lines.append("")
    return "\n".join(lines)


def add_works_to_person_page(slug, title_articles, body_articles, dry_run=False):
    """Add or update the ## Works section on a person page."""
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        print(f"  SKIP: {slug} — no person page exists at {page_path}")
        return False

    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if ## Works section already exists
    works_pattern = r"\n## Works\n"
    if re.search(works_pattern, content):
        # Replace existing Works section
        # Find the section from "## Works" to the next "## " header or end of file
        works_match = re.search(r"\n## Works\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
        if works_match:
            new_section = generate_works_section(slug, title_articles, body_articles)
            content = content[:works_match.start()] + new_section + content[works_match.end():]
        else:
            # Can't find the section boundary, just replace the header
            new_section = generate_works_section(slug, title_articles, body_articles)
            content = re.sub(works_pattern, new_section, content)
    else:
        # Insert before "## Source Notes" or "## Related Pages" or at end
        new_section = generate_works_section(slug, title_articles, body_articles)

        if "## Source Notes" in content:
            content = content.replace("## Source Notes", new_section + "\n## Source Notes")
        elif "## Related Pages" in content:
            content = content.replace("## Related Pages", new_section + "\n## Related Pages")
        else:
            content = content.rstrip() + "\n" + new_section

    # Update last_reviewed date
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"last_reviewed: \d{4}-\d{2}-\d{2}",
        f"last_reviewed: {today}",
        content
    )

    if dry_run:
        print(f"  DRY-RUN: {slug} — would update {page_path}")
        return True

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  DONE: {slug} — {len(title_articles)} title articles, {len(body_articles)} body mentions")
    return True


def add_person_link_to_article(article_path, slug, dry_run=False):
    """Add a wikilink from an article back to the person page.

    Adds [[people/<slug>|Chinese Name]] to the article's frontmatter
    'authors' field or to the body as a first-mention link.
    """
    path = REPO_ROOT / article_path
    if not path.exists():
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has the wikilink
    wikilink = f"[[people/{slug}"
    if wikilink in content:
        return False

    chinese_name = SLUG_TO_CHINESE.get(slug, slug)
    full_wikilink = f"[[people/{slug}|{chinese_name}]]"

    # Try to add to frontmatter authors field
    if content.startswith("---"):
        fm_end = content.find("---\n", 5)
        if fm_end > 0:
            fm = content[:fm_end]
            if "authors:" in fm:
                # Add to existing authors list
                new_content = content.replace(
                    "authors:",
                    f"authors:\n  - {full_wikilink}",
                    1
                )
            else:
                # Add authors field after the last frontmatter line before ---
                # Insert before the closing ---
                new_fm = fm.rstrip() + f"\nauthors:\n  - {full_wikilink}\n"
                new_content = new_fm + content[fm_end:]

            if dry_run:
                return True

            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True

    return False


def process_columnist(slug, grouped_hits, dry_run=False):
    """Process a single columnist: update person page + link articles."""
    title_articles = grouped_hits.get(slug, {}).get("title", [])
    body_articles = grouped_hits.get(slug, {}).get("body", [])

    if not title_articles and not body_articles:
        print(f"  SKIP: {slug} — no hits found")
        return False

    # Update person page with Works section
    page_updated = add_works_to_person_page(slug, title_articles, body_articles, dry_run)

    # Link articles back to person page (title articles only — these are the person's own columns)
    articles_linked = 0
    for article in title_articles:
        if add_person_link_to_article(article["path"], slug, dry_run):
            articles_linked += 1

    return page_updated


def main():
    parser = argparse.ArgumentParser(description="Link Echopedia person pages to all their works")
    parser.add_argument("--all", action="store_true", help="Process all columnists")
    parser.add_argument("--columnist", type=str, help="Process a single columnist by slug")
    parser.add_argument("--dry-run", action="store_true", help="Don't write changes")
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
        print("Specify --all, --columnist <slug>, or --list-slugs")
        return

    if not slugs:
        print("No slugs to process.")
        return

    print(f"Loading priority hits from {HITS_FILE}...")
    hits = load_hits()
    print(f"  Loaded {len(hits)} hits")

    print(f"Grouping hits by slug...")
    grouped = group_hits_by_slug(hits)
    print(f"  Found hits for {len(grouped)} slugs")

    results = []
    for slug in slugs:
        print(f"\nProcessing: {slug}")
        success = process_columnist(slug, grouped, args.dry_run)
        results.append((slug, success))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for slug, success in results:
        status = "DONE" if success else "SKIPPED"
        print(f"  {slug}: {status}")

    done = sum(1 for _, s in results if s)
    print(f"\n  Total: {done}/{len(results)} pages processed")


if __name__ == "__main__":
    main()
