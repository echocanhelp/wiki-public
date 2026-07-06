#!/usr/bin/env python3
"""
Find all broken [[wiki links]] in the wiki content directory.

A link is broken if the target doesn't resolve to an existing .md file,
either directly or under known category prefixes.

Usage: python3 scan-broken-links.py [content_dir]
  Default content_dir: /root/wiki-public/content

Output: List of broken links in format: FILE -> [TARGET] | DISPLAY (MISSING)
"""
import os
import re
import sys

content_dir = sys.argv[1] if len(sys.argv) > 1 else "/root/wiki-public/content"

LINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|([^]]*?))?\]\]')

# Known category prefixes for auto-resolution
CATEGORIES = ['person/', 'organization/', 'location/', 'event/', 'award/', 'publication/', 'language/', 'concept/']

# Build set of existing pages
existing = set()
for root, dirs, files in os.walk(content_dir):
    for f in files:
        if f.endswith('.md') and f != 'index.md':
            existing.add(os.path.relpath(os.path.join(root, f), content_dir))

# Scan for broken links
broken = []
for root, dirs, files in os.walk(content_dir):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r') as fh:
            content = fh.read()
        for m in LINK_RE.finditer(content):
            target = m.group(1).strip()
            possible = [target + '.md']
            if '/' not in target:
                for prefix in CATEGORIES:
                    possible.append(f'{prefix}{target}.md')
            if not any(p in existing for p in possible):
                display = m.group(2).strip() if m.group(2) else ''
                broken.append((f, target, display))

if broken:
    print(f"Broken links found: {len(broken)}")
    for f, target, display in broken:
        print(f"  {f} -> [{target}] {'| ' + display if display else ''} (MISSING)")
else:
    print("No broken links found!")
