#!/usr/bin/env python3
"""
echopedia-quote-extractor.py — Generate ## Quotes section for person pages.

Searches article bodies for Chinese name mentions and extracts surrounding
text to build a ## Quotes section with citations.

Usage:
  python3 echopedia-quote-extractor.py --person yang-jia-you
  python3 echopedia-quote-extractor.py --person yang-jia-you --dry-run
"""
import re
import argparse
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path.home() / "echo-system"
CONTENT_DIR = REPO_ROOT / "content"
PEOPLE_DIR = CONTENT_DIR / "people"
ARTICLES_DIR = CONTENT_DIR / "articles"

SLUG_TO_CHINESE = {
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

# Minimum context length around the name mention
CONTEXT_CHARS = 80


def extract_title_from_frontmatter(content):
    """Extract title from frontmatter."""
    match = re.search(r'^title:\s*(.+)', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def extract_date_from_path(path):
    """Extract date from article path."""
    match = re.search(r'(\d{4})/(\d{8})', str(path))
    if match:
        date_str = match.group(2)
        try:
            from datetime import datetime
            dt = datetime.strptime(date_str, "%Y%m%d")
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def extract_date_from_frontmatter(content):
    """Extract date from frontmatter."""
    match = re.search(r'^date:\s*"?(\d{4}-\d{2}-\d{2})"?', content, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def find_quotes(slug, chinese_name):
    """Find quotes from articles mentioning this person.

    Extracts text surrounding Chinese name mentions to build quote entries.
    Filters out non-substantive mentions (e.g., just appearing in a byline).
    """
    quotes = []

    if ARTICLES_DIR.exists():
        for article_file in ARTICLES_DIR.rglob("*.md"):
            try:
                content = article_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            if chinese_name not in content:
                continue

            # Skip frontmatter
            body_start = content.find("---", content.find("---") + 3)
            if body_start > 0:
                body = content[body_start + 3:].strip()
            else:
                body = content

            # Find all occurrences of the Chinese name in the body
            for match in re.finditer(re.escape(chinese_name), body):
                start = max(0, match.start() - CONTEXT_CHARS)
                end = min(len(body), match.end() + CONTEXT_CHARS)
                context = body[start:end].strip()

                # Skip if context is too short or just a byline
                if len(context) < 20:
                    continue

                # Skip if it's just a byline (e.g., "◎ 楊嘉猷")
                if re.match(r'^◎\s*' + re.escape(chinese_name), context):
                    continue

                # Skip if it's just in a title tag or metadata
                if context.startswith("title:") or context.startswith("author:"):
                    continue

                # Clean up the context — remove excessive whitespace
                context = re.sub(r'\s+', ' ', context).strip()

                # Extract article metadata
                title = extract_title_from_frontmatter(content)
                date = extract_date_from_frontmatter(content)
                if not date:
                    date = extract_date_from_path(article_file)

                quotes.append({
                    "quote": context,
                    "date": date or "unknown",
                    "source": title or article_file.stem,
                    "path": str(article_file.relative_to(REPO_ROOT)),
                })

    # Deduplicate by quote text
    seen = set()
    unique_quotes = []
    for q in quotes:
        if q["quote"] not in seen:
            seen.add(q["quote"])
            unique_quotes.append(q)

    # Sort by date
    unique_quotes.sort(key=lambda x: x["date"] if x["date"] != "unknown" else "9999")

    return unique_quotes


def generate_quotes_section(slug, quotes):
    """Generate a ## Quotes section for a person page."""
    chinese_name = SLUG_TO_CHINESE.get(slug, slug)

    lines = []
    lines.append("\n## Quotes\n")
    lines.append(f"Notable quotes and mentions of **{chinese_name}** in Taiwan Justice articles:\n")

    if not quotes:
        lines.append("\nNo quotes found.\n")
        return "\n".join(lines)

    # Group by year
    by_year = defaultdict(list)
    for quote in quotes:
        year = quote["date"][:4] if quote["date"] != "unknown" else "Unknown"
        by_year[year].append(quote)

    for year in sorted(by_year.keys(), reverse=True):
        year_quotes = by_year[year]
        lines.append(f"\n### {year} ({len(year_quotes)} quotes)\n")
        for i, q in enumerate(year_quotes[:10], 1):
            # Truncate long quotes
            quote_text = q["quote"]
            if len(quote_text) > 200:
                quote_text = quote_text[:200] + "..."
            lines.append(f'{i}. "{quote_text}"')
            lines.append(f"   — {q['source']} ({q['date']})")

    if len(quotes) > 10:
        lines.append(f"\n*...and {len(quotes) - 10} more quotes*")

    lines.append("")
    return "\n".join(lines)


def add_quotes_to_person_page(slug, quotes, dry_run=False):
    """Add or update the ## Quotes section on a person page."""
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        print(f"  SKIP: {slug} — no person page exists at {page_path}")
        return False

    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not quotes:
        print(f"  SKIP: {slug} — no quotes found")
        return False

    new_section = generate_quotes_section(slug, quotes)

    # Check if ## Quotes section already exists
    if re.search(r"\n## Quotes\n", content):
        # Replace existing section
        pattern = r"\n## Quotes\n(.*?)(?=\n## |\Z)"
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
        print(f"  DRY-RUN: {slug} — would {action} ## Quotes section ({len(quotes)} quotes)")
        return True

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  {action.upper()}: {slug} — {len(quotes)} quotes in ## Quotes")
    return True


def main():
    parser = argparse.ArgumentParser(description="Generate ## Quotes sections for person pages")
    parser.add_argument("--person", type=str, required=True, help="Person slug")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without writing")
    args = parser.parse_args()

    slug = args.person
    chinese_name = SLUG_TO_CHINESE.get(slug)

    if not chinese_name:
        print(f"ERROR: No Chinese name mapping for slug '{slug}'")
        return

    print(f"Finding quotes for {chinese_name} ({slug})...")
    quotes = find_quotes(slug, chinese_name)
    print(f"  Found {len(quotes)} quotes")

    if quotes:
        for q in quotes[:5]:
            print(f"  {q['date']} — {q['quote'][:80]}")
        if len(quotes) > 5:
            print(f"  ... and {len(quotes) - 5} more")

        add_quotes_to_person_page(slug, quotes, dry_run=args.dry_run)
    else:
        print("  No quotes found.")

    print("\nDone.")


if __name__ == "__main__":
    main()
