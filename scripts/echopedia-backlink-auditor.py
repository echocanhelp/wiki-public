#!/usr/bin/env python3
"""
echopedia-backlink-auditor.py — Generate ## Network section for person pages.

Reads .wiki-index.md to find backlinks, then generates a ## Network section
listing all pages that link to a given person, grouped by type.

Usage:
  python3 echopedia-backlink-auditor.py --all
  python3 echopedia-backlink-auditor.py --person yang-jia-you
  python3 echopedia-backlink-auditor.py --dry-run --all
"""
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path.home() / "echo-system"
CONTENT_DIR = REPO_ROOT / "content"
PEOPLE_DIR = CONTENT_DIR / "people"
WIKI_INDEX = CONTENT_DIR / ".wiki-index.md"

# Chinese name lookup — expanded from TAHS priority roster
SLUG_TO_CHINESE = {
    "alan-thian": "田詒鴻",
    "paul-chen": "陳柏宇",
    "yang-jia-you": "楊嘉猷",
    "gene-tsai": "蔡錦榮",
    "xu-shihuan": "許世環",
    "linda-liu": "劉玲華",
    "leonard-hsu-jr": "許景鴻",
    "roger-tsai": "蔡漢成",
    "bai-weiwei": "白偉瑋",
    "john-yang": "楊錦忠",
    "yi-sen-lee": "李意盛",
    "phoenix-ko": "柯貝昀",
    "freeman-huang": "黃樹人",
    "tzetsai-eric-shen": "沈梓在",
    "sunu-tsai": "蔡淑女",
    "david-lee": "李東璞",
    "ken-wu": "吳兆峯",
    "rex-chen": "陳乃光",
    "ashton-hsu": "許思敦",
    "albert-s-lai": "賴信雄",
    "willy-pan": "潘建宇",
    "franklin-ping-cheng": "程炳成",
    "chen-wenshi": "陳文石",
    "huang-gen-shen": "黃根深",
    "liao-shu-zong": "廖述宗",
    "bai-peiyu": "白佩玉",
    "cao-changqing": "曹長青",
    "zhang-xinhui": "張信惠",
    "chao-sile": "趙思樂",
    "chen-bozhi": "陳博志",
    "chen-zhaonan": "陳昭南",
    "chen-maoxiong": "陳茂雄",
    "chen-po-kong": "陳破空",
    "zheng-qinren": "鄭欽仁",
    "zheng-wenlong": "鄭文龍",
    "jin-hegui": "金恆煒",
    "du-ao-cunfu": "獨傲村夫",
    "fan-jiang-ti-ang": "范姜提昂",
    "gong-sun-le": "公孫樂",
    "he-qingxuan": "何清漣",
    "hu-ping": "胡平",
    "huang-diyin": "黃帝穎",
    "huang-yongcheng": "黃永成",
    "guan-renjian": "管仁健",
    "li-xiaofeng": "李筱峰",
    "li-jian": "李堅",
    "liao-qingshan": "廖清山",
    "lin-baohua": "林保華",
    "lin-rongsong": "林榮松",
    "nanfang-shuo": "南方朔",
    "sang-pu": "桑普",
    "tang-peili": "唐培理",
    "zou-jingwen": "鄒景雯",
    "wang-qiaoling": "王峭嶺",
    "wang-dan": "王丹",
    "wang-shufen": "王淑芬",
    "wei-jingsheng": "魏京生",
    "wu-lipei": "吳澧培",
    "xia-ming": "夏明",
    "yang-yuanxun": "楊遠薰",
    "yang-yueqing": "楊月清",
    "yang-ziqing": "楊子清",
    "ye-siya": "葉思雅",
    "yu-jie": "余杰",
    "yuan-zhihui": "袁智慧",
    "zheng-bingquan": "鄭炳全",
}


def parse_wiki_index():
    """Parse .wiki-index.md to extract backlink information.

    Returns dict: slug -> list of {path, type, title}
    """
    if not WIKI_INDEX.exists():
        print(f"WARNING: {WIKI_INDEX} not found")
        return {}

    content = WIKI_INDEX.read_text(encoding="utf-8")
    backlinks = defaultdict(list)

    # Find all person entries with their backlink sections
    # Pattern: - **people/<slug>** ← N pages:
    person_pattern = re.compile(
        r'- \*\*people/(\w[\w-]*)\*\* ← (\d+) pages:',
        re.MULTILINE
    )

    for match in person_pattern.finditer(content):
        slug = match.group(1)
        page_count = int(match.group(2))

        # Find the backlink entries after this header
        section_start = match.end()
        # Find the next person entry or end of file
        next_person = person_pattern.search(content, section_start)
        section_end = next_person.start() if next_person else len(content)
        section = content[section_start:section_end]

        # Parse backlink entries: - `path/to/file.md` (indented with 2 spaces)
        link_pattern = re.compile(r'^\s+- `([^`]+)`', re.MULTILINE)
        for link_match in link_pattern.finditer(section):
            path = link_match.group(1)
            # Determine type from path
            if path.startswith("people/"):
                link_type = "person"
            elif path.startswith("organizations/"):
                link_type = "organization"
            elif path.startswith("articles/"):
                link_type = "article"
            elif path.startswith("sources/"):
                link_type = "source"
            else:
                link_type = "other"

            backlinks[slug].append({
                "path": path,
                "type": link_type,
                "title": Path(path).stem
            })

    return backlinks


def generate_network_section(slug, backlinks):
    """Generate a ## Network section for a person page."""
    chinese_name = SLUG_TO_CHINESE.get(slug, slug)

    # Group by type
    by_type = defaultdict(list)
    for link in backlinks:
        by_type[link["type"]].append(link)

    lines = []
    lines.append(f"\n## Network\n")
    lines.append(f"Pages that link to **{chinese_name}** ({slug}):\n")

    total = len(backlinks)
    type_labels = {
        "person": "People",
        "organization": "Organizations",
        "article": "Articles",
        "source": "Sources",
        "other": "Other"
    }

    for type_key in ["person", "organization", "article", "source", "other"]:
        items = by_type.get(type_key, [])
        if items:
            label = type_labels.get(type_key, type_key)
            lines.append(f"\n### {label} ({len(items)})\n")
            for i, item in enumerate(items, 1):
                path = item["path"]
                title = item["title"]
                # Create wikilink (strip .md extension — Quartz wiki-links don't use it)
                clean_path = path.removesuffix('.md')
                lines.append(f"{i}. [[{clean_path}|{title}]]")

    lines.append("")
    return "\n".join(lines)


def add_network_to_person_page(slug, backlinks, dry_run=False):
    """Add or update the ## Network section on a person page."""
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        print(f"  SKIP: {slug} — no person page exists at {page_path}")
        return False

    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not backlinks:
        print(f"  SKIP: {slug} — no backlinks found")
        return False

    new_section = generate_network_section(slug, backlinks)

    # Check if ## Network section already exists
    if re.search(r"\n## Network\n", content):
        # Replace existing section
        pattern = r"\n## Network\n(.*?)(?=\n## |\Z)"
        content = re.sub(pattern, new_section, content, flags=re.DOTALL)
        action = "updated"
    else:
        # Insert before "## Source Notes" or "## Related Pages" or at end
        insert_before = None
        for header in ["## Source Notes", "## Related Pages", "## Revision History"]:
            idx = content.find(header)
            if idx > 0:
                insert_before = idx
                break

        if insert_before:
            content = content[:insert_before] + new_section + "\n" + content[insert_before:]
        else:
            content = content.rstrip() + "\n" + new_section

        action = "added"

    if dry_run:
        print(f"  DRY-RUN: {slug} — would {action} ## Network section")
        return True

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  {action.upper()}: {slug} — {len(backlinks)} backlinks in ## Network")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate ## Network sections for person pages")
    parser.add_argument("--all", action="store_true", help="Process all people with backlinks")
    parser.add_argument("--person", type=str, help="Process a specific person slug")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without writing")
    args = parser.parse_args()

    print("Parsing .wiki-index.md for backlinks...")
    backlinks = parse_wiki_index()
    print(f"  Found backlinks for {len(backlinks)} people")

    if args.person:
        slugs = [args.person]
    elif args.all:
        slugs = list(backlinks.keys())
    else:
        print("  Use --all or --person <slug>")
        return

    print(f"\nProcessing {len(slugs)} people...")
    for slug in slugs:
        links = backlinks.get(slug, [])
        if links:
            add_network_to_person_page(slug, links, dry_run=args.dry_run)
        else:
            print(f"  SKIP: {slug} — no backlinks")

    print("\nDone.")


if __name__ == "__main__":
    main()
