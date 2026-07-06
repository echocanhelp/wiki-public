#!/usr/bin/env python3
"""
Echopedia Homepage Curator v1
Single Python script implementing the full workflow for daily homepage refresh.
Run as: python3 curator.py
"""

import os
import glob
import re
import time
from datetime import datetime

CONTENT_DIR = '/root/wiki-public/content'
INDEX_PUBLIC = '/root/wiki-public/content/index.md'
INDEX_DEPLOY = '/root/wiki-deploy/content/index.md'

EXCLUDE_PATTERNS = [
    r'^gstpc-', r'^echopedia-', r'^line-', r'^toward-', r'^good-shepherd-',
    r'^nechopedia-', r'^itpc-', r'^tahs-', r'society', r'historical-society',
    r'church', r'seminary', r'theological', r'tainan-', r'taiwan-',
    r'pasadena-', r'los-angeles-', r'irvine-', r'gstpc', r'chapter1',
    r'audiobook', r'verification-needed', r'senior-class', r'onboarding',
]

def is_excluded(basename, filepath):
    if '/event/' in filepath:
        return True
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, basename, re.IGNORECASE):
            return True
    return False

def parse_frontmatter_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                fm = content[3:end]
                match = re.search(r'^title:\s*(.+)$', fm, re.MULTILINE)
                if match:
                    return match.group(1).strip().strip('"').strip("'")
    except:
        pass
    return None

def get_display_name(filepath, basename):
    title = parse_frontmatter_title(filepath)
    if title:
        return title
    slug = os.path.splitext(basename)[0]
    return slug.replace('-', ' ').title()

def extract_current_people_links(content):
    """Extract ordered list of link targets from current Featured People section."""
    match = re.search(r'## Featured People\n\n.*?\[Explore more people →\]\(people\)', content, re.DOTALL)
    if not match:
        return []
    section = match.group(0)
    links = re.findall(r'\]\(([a-z0-9-]+)\)', section)
    return links

def main():
    files = glob.glob(os.path.join(CONTENT_DIR, '*-*.md'))
    candidates = []
    for f in files:
        basename = os.path.basename(f)
        if is_excluded(basename, f):
            continue
        try:
            lines = sum(1 for _ in open(f, encoding='utf-8', errors='ignore'))
            mtime = os.path.getmtime(f)
            display = get_display_name(f, basename)
            link = os.path.splitext(basename)[0]
            candidates.append({
                'path': f, 'basename': basename, 'lines': lines,
                'mtime': mtime, 'display': display, 'link': link
            })
        except Exception:
            continue

    candidates.sort(key=lambda x: (-x['lines'], -x['mtime']))
    top6 = candidates[:6]
    new_links = [c['link'] for c in top6]

    with open(INDEX_PUBLIC, 'r', encoding='utf-8') as f:
        content = f.read()

    current_links = extract_current_people_links(content)

    if current_links == new_links:
        print("[SILENT]")  # People list unchanged; notes preserved automatically
        return

    # Rebuild block, preserving note from old last entry if present
    old_last_note = ""
    if current_links and new_links and current_links[-1] == new_links[-1]:
        # Check if old last had a note
        m = re.search(rf'\]\({re.escape(new_links[-1])}\)(.*?)(\n|$)', content)
        if m and '—' in m.group(1):
            old_last_note = m.group(1).strip()

    new_block_lines = [
        "## Featured People",
        "",
        "Discover the individuals whose stories shape Taiwanese American history and community life.",
        "",
    ]
    for i, c in enumerate(top6):
        entry = f"- [{c['display']}]({c['link']})"
        if i == len(top6) - 1 and old_last_note:
            entry += f" {old_last_note}"
        new_block_lines.append(entry)
    new_block_lines.extend([
        "",
        "[Explore more people →](people)",
        ""
    ])
    new_block = "\n".join(new_block_lines)

    # Replace
    pattern = r'(## Featured People\n\n.*?\n\[Explore more people →\]\(people\)\n)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_block = match.group(1)
        new_content = content.replace(old_block, new_block)
        with open(INDEX_PUBLIC, 'w', encoding='utf-8') as f:
            f.write(new_content)
        with open(INDEX_DEPLOY, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated Featured People (list changed).")
    else:
        print("Pattern match failed.")

if __name__ == "__main__":
    main()
