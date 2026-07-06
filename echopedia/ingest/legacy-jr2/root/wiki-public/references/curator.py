#!/usr/bin/env python3
"""
Echopedia Homepage Curator v1
Daily refresh of Featured People section in index.md
"""

import os
import re
import glob
import yaml
from datetime import datetime
from pathlib import Path

CONTENT_DIR = "/root/wiki-public/content"
PUBLIC_INDEX = "/root/wiki-public/content/index.md"
DEPLOY_INDEX = "/root/wiki-deploy/content/index.md"
EXCLUDES = [
    "gstpc-", "echopedia-", "line-", "toward-", "good-shepherd-",
    "nechopedia-", "itpc-", "tahs-", "society", "church", "seminary",
    "theological", "tainan-", "taiwan-", "pasadena-", "los-angeles-",
    "irvine-", "gstpc", "chapter1", "audiobook", "verification-needed",
    "senior-class", "onboarding"
]

def is_person_page(path):
    basename = os.path.basename(path)
    if any(ex in basename.lower() for ex in EXCLUDES):
        return False
    if "/event/" in path:
        return False
    if not re.match(r'^[a-z].*-[a-z].*\.md$', basename):
        return False
    return True

def get_frontmatter_title(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            fm = yaml.safe_load(match.group(1))
            if fm and 'title' in fm:
                return fm['title'].strip()
        except:
            pass
    # fallback to slug
    basename = os.path.basename(filepath).replace('.md', '')
    return basename.replace('-', ' ').title()

def get_link_slug(filepath):
    return os.path.basename(filepath).replace('.md', '')

def collect_person_pages():
    candidates = []
    for mdfile in glob.glob(os.path.join(CONTENT_DIR, "*-*.md")):
        if is_person_page(mdfile):
            try:
                lines = len(open(mdfile, 'r', encoding='utf-8').readlines())
                mtime = os.path.getmtime(mdfile)
                title = get_frontmatter_title(mdfile)
                slug = get_link_slug(mdfile)
                candidates.append({
                    'path': mdfile,
                    'slug': slug,
                    'title': title,
                    'lines': lines,
                    'mtime': mtime
                })
            except Exception as e:
                print(f"Error processing {mdfile}: {e}")
    return candidates

def rank_pages(pages):
    return sorted(pages, key=lambda x: (-x['lines'], -x['mtime']))[:6]

def extract_current_featured_slugs(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find the Featured People section and extract link slugs
    section_match = re.search(r'## Featured People\n\n(.*?)\n\n\[Explore more people →\]', content, re.DOTALL)
    if not section_match:
        return []
    links = re.findall(r'\]\(([^\)]+)\)', section_match.group(1))
    return [l for l in links if not l.startswith('people')]

def rebuild_featured_block(top_pages, current_slugs, current_content):
    lines = []
    lines.append("## Featured People\n")
    lines.append("Discover the individuals whose stories shape Taiwanese American history and community life.\n")
    for i, p in enumerate(top_pages):
        display = p['title']
        link = p['slug']
        line = f"- [{display}]({link})"
        # Preserve trailing note if this is the last entry and it was in previous
        if i == len(top_pages) - 1 and len(current_slugs) > 0 and current_slugs[-1] == link:
            # Check if previous had a note
            note_match = re.search(rf'\[{re.escape(display)}\]\({re.escape(link)}\)(.*)', current_content)
            if note_match and note_match.group(1).strip():
                line += note_match.group(1).strip()
        lines.append(line)
    lines.append("\n[Explore more people →](people)\n")
    return "\n".join(lines)

def update_index(index_path, new_block):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace the entire Featured People section
    pattern = r'## Featured People\n\n.*?\n\n\[Explore more people →\]\(people\)'
    new_content = re.sub(pattern, new_block.strip(), content, flags=re.DOTALL)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return new_content != content  # changed?

def main():
    pages = collect_person_pages()
    top6 = rank_pages(pages)
    new_slugs = [p['slug'] for p in top6]

    current_slugs = extract_current_featured_slugs(PUBLIC_INDEX)
    if new_slugs == current_slugs:
        print("[SILENT]")
        return

    # Read current content for note preservation
    with open(PUBLIC_INDEX, 'r', encoding='utf-8') as f:
        current_content = f.read()

    new_block = rebuild_featured_block(top6, current_slugs, current_content)

    # Update both
    changed_public = update_index(PUBLIC_INDEX, new_block)
    changed_deploy = update_index(DEPLOY_INDEX, new_block)

    if changed_public or changed_deploy:
        # Now handle wiki-deploy git
        os.chdir("/root/wiki-deploy")
        os.system("git add content/index.md")
        commit_msg = f"chore(echopedia): rotate Featured People ({datetime.now().strftime('%Y-%m-%d')})"
        os.system(f'git commit -m "{commit_msg}"')
        branch = os.popen("git branch --show-current").read().strip()
        os.system(f"git push origin {branch}")
        print(f"Updated and pushed. New top people: {new_slugs}")
    else:
        print("[SILENT]")

if __name__ == "__main__":
    main()