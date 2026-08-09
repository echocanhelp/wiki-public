#!/usr/bin/env python3
"""
echopedia-timeline-builder.py — Generate ## Timeline section for person pages.

Extracts dates from article frontmatter and content to build a chronological
timeline of key events for a person.

Usage:
  python3 echopedia-timeline-builder.py --person yang-jia-you
  python3 echopedia-timeline-builder.py --person yang-jia-you --dry-run
"""
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

REPO_ROOT = Path.home() / "echo-system"
CONTENT_DIR = REPO_ROOT / "content"
PEOPLE_DIR = CONTENT_DIR / "people"
ARTICLES_DIR = CONTENT_DIR / "articles"

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


def extract_date_from_path(path):
    """Extract a date from an article path like content/articles/.../2024/20240715150935_root.md"""
    # Pattern: YYYY/YYYYMMDDHHMMSS_
    match = re.search(r'(\d{4})/(\d{8})', str(path))
    if match:
        year = match.group(1)
        date_str = match.group(2)
        try:
            dt = datetime.strptime(date_str, "%Y%m%d")
            return dt.strftime("%Y-%m-%d"), year
        except ValueError:
            pass
    return None, None


def extract_date_from_frontmatter(content):
    """Extract date from frontmatter."""
    # Pattern: date: YYYY-MM-DD or date: "YYYY-MM-DD"
    match = re.search(r'^date:\s*"?(\d{4}-\d{2}-\d{2})"?', content, re.MULTILINE)
    if match:
        date_str = match.group(1)
        year = date_str[:4]
        return date_str, year
    # Also check post_date: YYYY-MM-DD (used by TJ articles)
    match = re.search(r'^post_date:\s*"?(\d{4}-\d{2}-\d{2})"?', content, re.MULTILINE)
    if match:
        date_str = match.group(1)
        year = date_str[:4]
        return date_str, year
    return None, None


def extract_title_from_frontmatter(content):
    """Extract title from frontmatter."""
    match = re.search(r'^title:\s*(.+)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def find_timeline_events(slug, chinese_name):
    """Find timeline events from articles mentioning this person.

    Looks for articles that mention the person's Chinese name or English name
    in the title or content, and extracts dates from frontmatter or path.
    Also checks the priority-hits JSONL for pre-scored matches.
    """
    events = []

    # Build search names: Chinese name + English name from slug
    search_names = [chinese_name] if chinese_name else []
    # Convert slug to English name (e.g., albert-s-lai → Albert S. Lai)
    if slug:
        en_name = slug.replace('-', ' ').title()
        # Handle common patterns
        en_name = en_name.replace('S Lai', 'S. Lai').replace('Hsu Jr', 'Hsu Jr.')
        search_names.append(en_name)

    # Load priority hits for this slug (pre-scored matches)
    hits_file = REPO_ROOT / "knowledge/research/taiwanjustice-net-priority-hits.jsonl"
    hit_paths = set()
    if hits_file.exists():
        try:
            with open(hits_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    hit = json.loads(line)
                    for match in hit.get("matches", []):
                        if match.get("slug") == slug:
                            hit_paths.add(hit.get("path"))
                            break
        except (OSError, json.JSONDecodeError):
            pass

    # Search all articles
    if ARTICLES_DIR.exists():
        for article_file in ARTICLES_DIR.rglob("*.md"):
            try:
                content = article_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            # Check if this person is mentioned
            rel_path = str(article_file.relative_to(REPO_ROOT))
            mentioned = False

            # Check priority hits first (pre-scored)
            if rel_path in hit_paths:
                mentioned = True

            # Also search for Chinese or English name in content
            if not mentioned:
                for name in search_names:
                    if name and name in content:
                        mentioned = True
                        break

            if not mentioned:
                continue

            # Extract date
            date_str, year = extract_date_from_frontmatter(content)
            if not date_str:
                date_str, year = extract_date_from_path(article_file)

            if not date_str:
                continue

            # Extract title
            title = extract_title_from_frontmatter(content)
            if not title:
                title = article_file.stem

            # Determine event type based on content keywords
            event_type = "appearance"
            content_lower = content.lower()
            if any(kw in content_lower for kw in ["founding", "establish", "創立", "成立"]):
                event_type = "founding"
            elif any(kw in content_lower for kw in ["election", "elect", "選舉", "當選"]):
                event_type = "election"
            elif any(kw in content_lower for kw in ["speech", "lecture", "演講", "座談"]):
                event_type = "speech"
            elif any(kw in content_lower for kw in ["health", "illness", "病", "健康"]):
                event_type = "health"
            elif any(kw in content_lower for kw in ["transition", "succeed", "接任", "交接"]):
                event_type = "transition"
            elif any(kw in content_lower for kw in ["memorial", "memorial", "追思", "紀念"]):
                event_type = "memorial"

            # Extract a short description (first 100 chars of content after frontmatter)
            # Skip frontmatter
            body_start = content.find("---", content.find("---") + 3)
            if body_start > 0:
                body = content[body_start + 3:].strip()
            else:
                body = content

            # Get first meaningful sentence
            desc = title
            if len(desc) > 80:
                desc = desc[:80] + "..."

            events.append({
                "date": date_str,
                "year": year,
                "type": event_type,
                "title": title,
                "description": desc,
                "path": str(article_file.relative_to(REPO_ROOT)),
            })

    # Sort by date
    events.sort(key=lambda x: x["date"])

    # Deduplicate by date + title
    seen = set()
    unique_events = []
    for e in events:
        key = (e["date"], e["title"])
        if key not in seen:
            seen.add(key)
            unique_events.append(e)

    return unique_events


def generate_timeline_section(slug, events):
    """Generate a ## Timeline section for a person page."""
    chinese_name = SLUG_TO_CHINESE.get(slug, slug)

    lines = []
    lines.append("\n## Timeline\n")
    lines.append(f"Chronological events for **{chinese_name}**:\n")

    if not events:
        lines.append("\nNo timeline events found.\n")
        return "\n".join(lines)

    # Group by year
    by_year = defaultdict(list)
    for event in events:
        by_year[event["year"]].append(event)

    # Sort years descending (most recent first)
    for year in sorted(by_year.keys(), reverse=True):
        year_events = by_year[year]
        lines.append(f"\n### {year} ({len(year_events)} events)\n")
        for event in year_events:
            type_label = {
                "founding": "🏛️",
                "election": "🗳️",
                "speech": "🎤",
                "health": "🏥",
                "transition": "🤝",
                "memorial": "🕯️",
                "appearance": "📰",
            }.get(event["type"], "📄")

            lines.append(f"- **{event['date']}** {type_label} {event['description']}")

    lines.append("")
    return "\n".join(lines)


def add_timeline_to_person_page(slug, events, dry_run=False):
    """Add or update the ## Timeline section on a person page."""
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        print(f"  SKIP: {slug} — no person page exists at {page_path}")
        return False

    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not events:
        print(f"  SKIP: {slug} — no timeline events found")
        return False

    new_section = generate_timeline_section(slug, events)

    # Check if ## Timeline section already exists
    if re.search(r"\n## Timeline\n", content):
        # Replace existing section
        pattern = r"\n## Timeline\n(.*?)(?=\n## |\Z)"
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
        print(f"  DRY-RUN: {slug} — would {action} ## Timeline section ({len(events)} events)")
        return True

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  {action.upper()}: {slug} — {len(events)} events in ## Timeline")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate ## Timeline sections for person pages")
    parser.add_argument("--person", type=str, required=True, help="Person slug")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without writing")
    args = parser.parse_args()

    slug = args.person
    chinese_name = SLUG_TO_CHINESE.get(slug)

    if not chinese_name:
        print(f"ERROR: No Chinese name mapping for slug '{slug}'")
        print("Add it to SLUG_TO_CHINESE in the script.")
        return

    print(f"Finding timeline events for {chinese_name} ({slug})...")
    events = find_timeline_events(slug, chinese_name)
    print(f"  Found {len(events)} events")

    if events:
        # Show preview
        for e in events[:5]:
            print(f"  {e['date']} — {e['description'][:80]}")
        if len(events) > 5:
            print(f"  ... and {len(events) - 5} more")

        add_timeline_to_person_page(slug, events, dry_run=args.dry_run)
    else:
        print("  No events found.")

    print("\nDone.")


if __name__ == "__main__":
    main()
