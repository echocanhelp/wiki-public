#!/usr/bin/env python3
"""
echopedia-thin-page-audit.py — Audit Echopedia person pages for thinness.

Scans all content/people/*.md files and flags pages that are:
- Under 5,000 chars (thin)
- Missing key sections: ## Works, ## Timeline, ## Network, ## Quotes

Outputs a ranked list to stdout (for morning brief integration).

Usage:
  python3 echopedia-thin-page-audit.py
  python3 echopedia-thin-page-audit.py --threshold 8000
  python3 echopedia-thin-page-audit.py --json
"""
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path.home() / "echo-system"
CONTENT_DIR = REPO_ROOT / "content"
PEOPLE_DIR = CONTENT_DIR / "people"

# Required sections for a complete person page
REQUIRED_SECTIONS = [
    "## Works",
    "## Timeline",
    "## Network",
    "## Quotes",
]

# Default threshold for "thin" pages
DEFAULT_THRESHOLD = 5000


def audit_person_page(page_path):
    """Audit a single person page for thinness and missing sections."""
    try:
        content = page_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    char_count = len(content)
    sections = re.findall(r"^## (.+)", content, re.MULTILINE)

    # Check for required sections
    missing_sections = []
    for req in REQUIRED_SECTIONS:
        if req not in content:
            missing_sections.append(req)

    # Extract title from frontmatter
    title_match = re.search(r'^title:\s*(.+)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else page_path.stem

    # Extract Chinese name from content
    chinese_match = re.search(r'（([^）]+)）', title)
    chinese_name = chinese_match.group(1) if chinese_match else ""

    # Check if page is published
    status_match = re.search(r'^status:\s*(\w+)', content, re.MULTILINE)
    status = status_match.group(1) if status_match else "unknown"

    # Count backlinks (from ## Network section)
    backlink_count = 0
    if "## Network" in content:
        network_section = content[content.index("## Network"):]
        next_section = network_section.find("## ", 10)
        if next_section > 0:
            network_section = network_section[:next_section]
        backlink_count = len(re.findall(r"\[\[([^\|]+)\|", network_section))

    # Count works (from ## Works section)
    works_count = 0
    if "## Works" in content:
        works_section = content[content.index("## Works"):]
        next_section = works_section.find("## ", 10)
        if next_section > 0:
            works_section = works_section[:next_section]
        # Count numbered list items
        works_count = len(re.findall(r"^\d+\.", works_section, re.MULTILINE))

    return {
        "slug": page_path.stem,
        "title": title,
        "chinese_name": chinese_name,
        "char_count": char_count,
        "status": status,
        "sections": sections,
        "missing_sections": missing_sections,
        "backlink_count": backlink_count,
        "works_count": works_count,
        "thin": char_count < DEFAULT_THRESHOLD,
        "path": str(page_path.relative_to(REPO_ROOT)),
    }


def main():
    parser = argparse.ArgumentParser(description="Audit Echopedia person pages for thinness")
    parser.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD,
                        help=f"Char threshold for thin pages (default: {DEFAULT_THRESHOLD})")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if not PEOPLE_DIR.exists():
        print(f"ERROR: {PEOPLE_DIR} not found")
        return

    # Scan all person pages
    pages = sorted(PEOPLE_DIR.glob("*.md"))
    results = []
    for page in pages:
        audit = audit_person_page(page)
        if audit:
            results.append(audit)

    # Filter thin pages
    thin_pages = [r for r in results if r["char_count"] < args.threshold]

    # Sort by char count (ascending — thinnest first)
    thin_pages.sort(key=lambda x: x["char_count"])

    if args.json:
        print(json.dumps(thin_pages, indent=2))
        return

    # Text output
    print(f"=== Echopedia Thin Page Audit ===")
    print(f"Total person pages: {len(results)}")
    print(f"Thin pages (<{args.threshold} chars): {len(thin_pages)}")
    print(f"Pages with all required sections: {len([r for r in results if not r['missing_sections']])}")
    print()

    if thin_pages:
        print(f"{'Slug':<25} {'Chars':>6} {'Works':>5} {'Backlinks':>9} {'Missing':>20} {'Status':>10}")
        print("-" * 80)
        for p in thin_pages[:30]:
            missing = ", ".join(p["missing_sections"][:2]) if p["missing_sections"] else "none"
            print(f"{p['slug']:<25} {p['char_count']:>6} {p['works_count']:>5} {p['backlink_count']:>9} {missing:>20} {p['status']:>10}")

        if len(thin_pages) > 30:
            print(f"\n... and {len(thin_pages) - 30} more thin pages")
    else:
        print("No thin pages found!")

    print(f"\nDone.")


if __name__ == "__main__":
    main()
