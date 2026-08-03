#!/usr/bin/env python3
"""
Vault Connector Suggestions

Scans the Echopedia vault for connection suggestions between pages:
1. Co-citation: Two pages both link to the same target(s) — they may relate
2. Co-mention: Two pages mention each other by name but no wikilink connects them
3. Shared tags: Pages share 3+ common tags in frontmatter

Output: structured text digest + JSON state file
LOCAL_ONLY: No external calls, no LLM.

Usage:
  python3 vault-connector-suggestions.py [--dry-run] [--json]
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
CONTENT_DIR = Path(os.environ.get("ECHOPEDIA_CONTENT", "/home/leedt/echo-system/content"))
OUTPUT_DIR = Path(os.environ.get("INTELLIGENCE_DIR", "/home/leedt/echo-system/knowledge/operational/intelligence"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Pitfall: Popular targets (Taiwan Center) create N*(N-1)/2 pairs.
# Cap at max_pairs_per_target per target to avoid explosion.
MAX_PAIRS_PER_TARGET = 3
# Skip non-content types
SKIP_TYPES = {"index", "media"}
# Minimum shared tags to suggest a connection
MIN_SHARED_TAGS = 3
# Only scan these subdirectories (avoid content/articles which has 29k+ Tier2 pages)
SCAN_PATHS = {"people", "organizations", "sources", "events"}


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def extract_body(content):
    """Extract body text (after frontmatter)."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return content


def extract_wikilinks(content):
    """Extract [[wikilinks]] from content. Returns list of link targets."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)


def parse_tags(fm):
    """Parse tags from frontmatter. Tags can be comma-separated string or list."""
    tags_str = fm.get("tags", "")
    if not tags_str:
        return []
    tags = re.split(r'[,\s]+', tags_str.strip())
    return [t.strip() for t in tags if t.strip()]


def should_scan(rel_path):
    """Only scan people, organizations, sources, events directories."""
    parts = rel_path.parts
    if len(parts) < 2:
        return False
    return parts[0] in SCAN_PATHS


def build_vault_index():
    """
    Build a comprehensive index of all wiki pages.
    Returns dict keyed by page path (relative to content dir).
    """
    pages = {}
    folder_path_set = set()

    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith("."):
            continue
        if not should_scan(rel):
            continue

        content = md_file.read_text()
        fm = extract_frontmatter(content)
        body = extract_body(content)

        page_type = fm.get("type", "unknown")
        if page_type in SKIP_TYPES:
            continue

        title = fm.get("title", md_file.stem)
        tags = parse_tags(fm)
        wikilinks = extract_wikilinks(body)

        pages[str(rel)] = {
            "path": str(rel),
            "title": title,
            "type": page_type,
            "tags": tags,
            "wikilinks": wikilinks,
            "body": body,
            "folder": str(rel.parent) if str(rel.parent) != "." else "",
        }

        folder_path_set.add(str(rel.parent))

    return pages, folder_path_set


def build_co_citation_matrix(pages):
    """
    Build co-citation matrix: for each target page, find all pages that link to it.
    Then suggest connections between pairs of pages that co-cite the same target.

    Pitfall: Popular targets create N*(N-1)/2 pairs. Cap at MAX_PAIRS_PER_TARGET.
    Pitfall: Skip self-referencing pairs (p1.name == p2.name).
    """
    citation_map = defaultdict(list)

    for path, page in pages.items():
        for link in page["wikilinks"]:
            citation_map[link].append(path)

    suggestions = []
    seen_pairs = set()

    for target, citing_pages in citation_map.items():
        if len(citing_pages) < 2:
            continue

        pairs = []
        for i in range(len(citing_pages)):
            for j in range(i + 1, len(citing_pages)):
                p1, p2 = citing_pages[i], citing_pages[j]
                if p1 == p2:
                    continue
                if p2 in pages[p1]["wikilinks"] or p1 in pages[p2]["wikilinks"]:
                    continue
                # Deduplicate: skip if this pair was already suggested for this target
                pair_key = (p1, p2, target)
                if pair_key in seen_pairs:
                    continue
                seen_pairs.add(pair_key)
                pairs.append((p1, p2))

        pairs = pairs[:MAX_PAIRS_PER_TARGET]

        for p1, p2 in pairs:
            suggestions.append({
                "type": "CO-CITATION",
                "page1": p1,
                "page2": p2,
                "shared_target": target,
                "page1_title": pages[p1]["title"],
                "page2_title": pages[p2]["title"],
                "shared_targets_count": len(citing_pages),
            })

    return suggestions


def build_co_mention_suggestions(pages):
    """
    Detect pages that mention each other by name but have no wikilink.

    Optimized: Build a word-set from each page's body, then check if other
    page titles appear as word sequences. This avoids O(n^2) regex.
    """
    # Build a lookup of clean title -> path
    title_to_path = {}
    for path, page in pages.items():
        title = page["title"]
        clean_title = re.sub(r'[\[*\#\-[\]|]', '', title).strip()
        if len(clean_title) >= 4:
            title_to_path[clean_title] = path

    if not title_to_path:
        return []

    # Pre-tokenize each page body into a set of words (lowercased)
    # For multi-word titles, we'll check if all words appear
    page_words = {}
    for path, page in pages.items():
        words = set()
        for word in re.findall(r'\b\w+\b', page["body"].lower()):
            words.add(word)
        page_words[path] = words

    # Build title word sets
    title_words = {}
    for clean_title, path in title_to_path.items():
        words = set(re.findall(r'\b\w+\b', clean_title.lower()))
        if len(words) >= 2:  # Multi-word titles
            title_words[clean_title] = words

    suggestions = []
    seen_pairs = set()

    for path, page in pages.items():
        existing_links = set(page["wikilinks"])
        body_words = page_words[path]

        # Check single-word titles
        for clean_title, other_path in title_to_path.items():
            if other_path == path or other_path in existing_links:
                continue
            words = re.findall(r'\b\w+\b', clean_title.lower())
            if len(words) == 1:
                if words[0] in body_words:
                    key = tuple(sorted([path, other_path]))
                    if key not in seen_pairs:
                        seen_pairs.add(key)
                        suggestions.append({
                            "type": "CO-MENTION",
                            "page1": path,
                            "page2": other_path,
                            "page1_title": page["title"],
                            "page2_title": pages[other_path]["title"],
                            "mention_text": clean_title,
                        })

        # Check multi-word titles
        for clean_title, words in title_words.items():
            other_path = title_to_path[clean_title]
            if other_path == path or other_path in existing_links:
                continue
            if words.issubset(body_words):
                key = tuple(sorted([path, other_path]))
                if key not in seen_pairs:
                    seen_pairs.add(key)
                    suggestions.append({
                        "type": "CO-MENTION",
                        "page1": path,
                        "page2": other_path,
                        "page1_title": page["title"],
                        "page2_title": pages[other_path]["title"],
                        "mention_text": clean_title,
                    })

    return suggestions


def build_shared_tags_suggestions(pages):
    """
    Detect pages that share 3+ common tags in frontmatter.
    """
    suggestions = []
    seen = set()

    for path, page in pages.items():
        page_tags = set(page["tags"])
        if len(page_tags) < MIN_SHARED_TAGS:
            continue

        for other_path, other_page in pages.items():
            if other_path == path:
                continue

            other_tags = set(other_page["tags"])
            shared = page_tags & other_tags

            if len(shared) >= MIN_SHARED_TAGS:
                key = tuple(sorted([path, other_path]))
                if key not in seen:
                    seen.add(key)
                    suggestions.append({
                        "type": "SHARED_TAGS",
                        "page1": path,
                        "page2": other_path,
                        "page1_title": page["title"],
                        "page2_title": other_page["title"],
                        "shared_tags": sorted(shared),
                    })

    return suggestions


def build_orphan_folder_suggestions(pages, folder_path_set):
    """
    Detect folders with pages that have no internal links between them.
    """
    suggestions = []

    folder_pages = defaultdict(list)
    for path, page in pages.items():
        folder = page["folder"]
        folder_pages[folder].append(path)

    for folder, page_list in folder_pages.items():
        if len(page_list) < 3:
            continue

        internal_links = 0
        pages_with_links = 0
        for path in page_list:
            page = pages[path]
            links = set(page["wikilinks"])
            folder_links = [l for l in links if l.startswith(folder + "/") or folder == ""]
            if folder_links:
                pages_with_links += 1
            internal_links += len(folder_links)

        if pages_with_links < len(page_list) * 0.5:
            avg_links = internal_links / len(page_list)
            if avg_links < 2:
                suggestions.append({
                    "type": "ORPHAN_FOLDER",
                    "folder": folder,
                    "page_count": len(page_list),
                    "avg_internal_links": round(avg_links, 1),
                    "pages_with_links": pages_with_links,
                })

    return suggestions


def format_suggestions(co_citation, co_mention, shared_tags, orphan_folders):
    """Format all suggestions into a structured text digest."""
    lines = []
    lines.append("=== VAULT CONNECTOR SUGGESTIONS ===")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    lines.append(f"[CO-CITATION] {len(co_citation)} suggestions")
    for s in co_citation:
        lines.append(f"  {s['page1']} <-> {s['page2']}")
        lines.append(f"    Both link to: {s['shared_target']}")
        lines.append(f"    ({s['page1_title']} <-> {s['page2_title']})")
        lines.append("")

    lines.append(f"[CO-MENTION] {len(co_mention)} suggestions")
    for s in co_mention:
        lines.append(f"  {s['page1']} <-> {s['page2']}")
        lines.append(f"    \"{s['mention_text']}\" mentioned in both pages")
        lines.append("")

    lines.append(f"[SHARED_TAGS] {len(shared_tags)} suggestions")
    for s in shared_tags:
        lines.append(f"  {s['page1']} <-> {s['page2']}")
        lines.append(f"    Common tags: {', '.join(s['shared_tags'])}")
        lines.append("")

    lines.append(f"[ORPHAN_FOLDER] {len(orphan_folders)} suggestions")
    for s in orphan_folders:
        lines.append(f"  {s['folder']} - {s['page_count']} pages, avg {s['avg_internal_links']} links")
        lines.append("")

    return "\n".join(lines)


def main():
    dry_run = "--dry-run" in sys.argv
    json_output = "--json" in sys.argv

    pages, folder_path_set = build_vault_index()

    co_citation = build_co_citation_matrix(pages)
    co_mention = build_co_mention_suggestions(pages)
    shared_tags = build_shared_tags_suggestions(pages)
    orphan_folders = build_orphan_folder_suggestions(pages, folder_path_set)

    text_output = format_suggestions(co_citation, co_mention, shared_tags, orphan_folders)

    state = {
        "generated_at": datetime.now().isoformat(),
        "pages_scanned": len(pages),
        "suggestions": {
            "co_citation": co_citation,
            "co_mention": co_mention,
            "shared_tags": shared_tags,
            "orphan_folders": orphan_folders,
        },
        "summary": {
            "co_citation_count": len(co_citation),
            "co_mention_count": len(co_mention),
            "shared_tags_count": len(shared_tags),
            "orphan_folder_count": len(orphan_folders),
        },
    }

    if json_output:
        print(json.dumps(state, indent=2))
    else:
        print(text_output)
        print(f"\n=== SUMMARY ===")
        print(f"Pages scanned: {len(pages)}")
        print(f"Co-citation: {len(co_citation)}")
        print(f"Co-mention: {len(co_mention)}")
        print(f"Shared tags: {len(shared_tags)}")
        print(f"Orphan folders: {len(orphan_folders)}")

    if not dry_run:
        output_file = OUTPUT_DIR / "connector-suggestions.md"
        output_file.write_text(text_output)

        state_file = OUTPUT_DIR / "connector-suggestions.json"
        state_file.write_text(json.dumps(state, indent=2))

        print(f"\nOutput written to:")
        print(f"  {output_file}")
        print(f"  {state_file}")


if __name__ == "__main__":
    main()
