#!/usr/bin/env python3
"""Scan knowledge/ files and flag ones that look wiki-worthy.

Usage:
    python3 classify.py [--verbose]

Output:
    - Markdown report to stdout
    - Same report written to knowledge/classification-report.md
"""

import os
import re
import sys

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

KNOWLEDGE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge"
)
CONTENT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content"
)
REPORT_PATH = os.path.join(KNOWLEDGE_DIR, "classification-report.md")

# Person/org name indicators in file titles (H1 / frontmatter title)
TITLE_PERSON_PATTERNS = [
    r"\bDr\.\b",
    r"\bRev\.\b",
    r"\bProf\.\b",
    r"\bPresident\b",
    r"\bElder\b",
    r"\bPastor\b",
    r"\bMdm\.\b",
    r"\bMs\.\b",
    r"\bMr\.\b",
    r"\bMrs\.\b",
    r"\bMs\b",
    r"\b赖",
    r"\b林",
    r"\b陳",
    r"\b黃",
    r"\b張",
    r"\b李",
    r"\b王",
    r"\b蔡",
    r"\b陳",
    r"\b鄭",
    r"\b黃",
    r"\b許",
    r"\b吳",
    r"\b周",
    r"\b徐",
    r"\b劉",
    r"\b楊",
    r"\b謝",
    r"\b宋",
    r"\b郭",
    r"\b羅",
    r"\b廖",
    r"\b蕭",
    r"\b蔡",
    r"\b彭",
    r"\b曾",
    r"\b何",
    r"\b施",
    r"\b洪",
    r"\b賴",
    r"\b馮",
    r"\b杜",
    r"\b葉",
    r"\b方",
    r"\b田",
    r"\b沈",
    r"\b韓",
    r"\b曹",
    r"\b彭",
    r"\b陸",
    r"\b阮",
    r"\b江",
    r"\b史",
    r"\b耿",
    r"\b姚",
    r"\b邵",
    r"\b湛",
    r"\b汪",
    r"\b毛",
    r"\b邱",
    r"\b白",
    r"\b華",
    r"\b金",
    r"\b夏",
    r"\b戴",
    r"\b唐",
    r"\b袁",
    r"\b鄧",
    r"\b馮",
    r"\b蘇",
    r"\b潘",
    r"\b葛",
    r"\b奚",
    r"\b羅",
    r"\b邱",
    r"\b薛",
    r"\b侯",
    r"\b龍",
    r"\b陸",
    r"\b杭",
    r"\b樊",
    r"\b翁",
    r"\b熊",
    r"\b紀",
    r"\b舒",
    r"\b舒",
    r"\b屈",
    r"\b項",
    r"\b祝",
    r"\b段",
    r"\b雷",
    r"\b滕",
    r"\b殷",
    r"\b狄",
    r"\b米",
    r"\b冉",
    r"\b郤",
    r"\b宴",
    r"\b酒",
    r"\b漆",
    r"\b茹",
    r"\b印",
    r"\b都",
    r"\b耿",
    r"\b慕",
    r"\b單",
    r"\b杭",
    r"\b蒙",
    r"\b平",
    r"\b黃",
    r"\b虎",
    r"\b全",
    r"\b掌",
    r"\b班",
    r"\b司",
    r"\b年",
    r"\b固",
    r"\b樂",
    r"\b俞",
    r"\b雙",
    r"\b雙",
    r"\b雙",
    r"\b雙",
]

TITLE_ORG_PATTERNS = [
    r"\bChurch\b",
    r"\b教会",
    r"\b教會",
    r"\bSociety\b",
    r"\b协会",
    r"\b協會",
    r"\bFoundation\b",
    r"\b基金会",
    r"\b基金會",
    r"\bCouncil\b",
    r"\b委员会",
    r"\b委員會",
    r"\bAssociation\b",
    r"\b联盟",
    r"\b聯盟",
    r"\bInstitute\b",
    r"\b学院",
    r"\b學院",
    r"\bUniversity\b",
    r"\b大学",
    r"\b大學",
    r"\bCenter\b",
    r"\b中心",
    r"\b中心",
    r"\bGroup\b",
    r"\b集团",
    r"\b集團",
    r"\bCommission\b",
    r"\b委员会",
    r"\bCommission\b",
    r"\bMinistry\b",
    r"\b教会",
    r"\b教会",
    r"\bPresbyterian\b",
    r"\b长老",
    r"\b長老",
    r"\bTaiwanese\b",
    r"\b台湾",
    r"\b台灣",
    r"\bFormosa\b",
    r"\b中华",
    r"\b中華",
    r"\b中国",
    r"\bChina\b",
    r"\bAmerican\b",
    r"\b美国",
    r"\b美國",
    r"\bTaiwan\b",
    r"\b台湾\b",
    r"\b台灣\b",
    r"\bTaiwan\b",
    r"\bTaiwan\b",
    r"\bChurch\b",
    r"\b教会\b",
    r"\b教會\b",
    r"\bSociety\b",
    r"\b协会\b",
    r"\b協會\b",
    r"\bFoundation\b",
    r"\b基金会\b",
    r"\b基金會\b",
    r"\bCouncil\b",
    r"\b委员会\b",
    r"\b委員會\b",
    r"\bAssociation\b",
    r"\b联盟\b",
    r"\b聯盟\b",
    r"\bInstitute\b",
    r"\b学院\b",
    r"\b學院\b",
    r"\bUniversity\b",
    r"\b大学\b",
    r"\b大學\b",
    r"\bCenter\b",
    r"\b中心\b",
    r"\bGroup\b",
    r"\b集团\b",
    r"\b集團\b",
    r"\bCommission\b",
    r"\b委员会\b",
    r"\bMinistry\b",
    r"\b教会\b",
    r"\b教会\b",
    r"\bPresbyterian\b",
    r"\b长老\b",
    r"\b長老\b",
    r"\bTaiwanese\b",
    r"\b台湾\b",
    r"\b台灣\b",
    r"\bFormosa\b",
    r"\b中华\b",
    r"\b中華\b",
    r"\b中国\b",
    r"\bChina\b",
    r"\bAmerican\b",
    r"\b美国\b",
    r"\b美國\b",
    r"\bTaiwan\b",
    r"\b台湾\b",
    r"\b台灣\b",
]

# Content-level person/org indicators
CONTENT_PERSON_PATTERNS = [
    r"\bRev\.\b",
    r"\bDr\.\b",
    r"\bProf\.\b",
    r"\bElder\b",
    r"\bPresident\b",
    r"\bPastor\b",
    r"\bBishop\b",
    r"\bFounder\b",
    r"\bDirector\b",
    r"\bChairman\b",
    r"\bChairwoman\b",
    r"\bChair\b",
    r"\bSecretary\b",
    r"\bVice\s+President\b",
    r"\bMinister\b",
    r"\bDeacon\b",
    r"\bMissionary\b",
    r"\bTheologian\b",
    r"\bTheologian\b",
    r"\bauthor\b",
    r"\bwriter\b",
    r"\bpublisher\b",
    r"\bnarrator\b",
]

CONTENT_ORG_PATTERNS = [
    r"\bChurch\b",
    r"\b教会",
    r"\b教會",
    r"\bSociety\b",
    r"\b协会",
    r"\b協會",
    r"\bFoundation\b",
    r"\b基金会",
    r"\b基金會",
    r"\bCouncil\b",
    r"\b委员会",
    r"\b委員會",
    r"\bAssociation\b",
    r"\b联盟",
    r"\b聯盟",
    r"\bInstitute\b",
    r"\b学院",
    r"\b學院",
    r"\bUniversity\b",
    r"\b大学",
    r"\b大學",
    r"\bCenter\b",
    r"\b中心",
    r"\b中心",
    r"\bGroup\b",
    r"\b集团",
    r"\b集團",
    r"\bCommission\b",
    r"\b委员会",
    r"\bMinistry\b",
    r"\b教会",
    r"\b教会",
    r"\bPresbyterian\b",
    r"\b长老",
    r"\b長老",
    r"\bTaiwanese\b",
    r"\b台湾",
    r"\b台灣",
    r"\bFormosa\b",
    r"\b中华",
    r"\b中華",
    r"\b中国",
    r"\bChina\b",
    r"\bAmerican\b",
    r"\b美国",
    r"\b美國",
    r"\bTaiwan\b",
    r"\b台湾\b",
    r"\b台灣\b",
    r"\bTaiwan\b",
    r"\bTaiwan\b",
]

# Operational doc indicators (not wiki-worthy)
OPERATIONAL_INDICATORS = [
    r"script",
    r"release.?note",
    r"production.?schedule",
    r"checklist",
    r"consent",
    r"metadata",
    r"distributor",
    r"status",
    r"master.?plan",
    r"next.?action",
    r"readme",
    r"README",
    r"amendment",
    r"freeze",
    r"scratch",
    r"narration",
    r"loudness",
    r"loudness",
    r"QC",
    r"audio.?script",
    r"chapter.?map",
    r"closing.?credit",
    r"opening.?credit",
    r"preface",
    r"back.?matter",
    r"front.?matter",
    r"chapter.*script",
    r"shell",
    r"store.?description",
    r"voice.?consent",
    r"permission.?log",
    r"kickoff",
    r"agenda",
    r"ISRC",
    r"bitrate",
    r"sample.?rate",
    r"wav",
    r"mp3",
    r"m4b",
    r"m4b",
    r"chapter.*map",
    r"production",
    r"audiobook",
    r"release",
    r"schedule",
    r"release.?schedule",
    r"90.?day",
    r"90.?D",
    r"ALBERT_KICKOFF",
    r"PRODUCTION_SCHEDULE",
    r"STORE_DESCRIPTION",
    r"PERMISSION_LOG",
    r"VOICE_CONSENT",
    r"DISTRIBUTOR_CHECKLIST",
    r"NEXT_ACTIONS",
    r"MASTER_PLAN",
    r"STATUS",
    r"FREEZE",
    r"CHAPTER_MAP",
    r"closing_credits",
    r"opening_credits",
    r"scripts_retail",
    r"AMT_v1",
    r"scratch",
    r"narration",
    r"loudness",
    r"QC",
    r"audio.?script",
    r"chapter.?map",
    r"closing.?credit",
    r"opening.?credit",
    r"preface",
    r"back.?matter",
    r"front.?matter",
    r"shell",
    r"store.?description",
    r"voice.?consent",
    r"permission.?log",
    r"kickoff",
    r"agenda",
    r"ISRC",
    r"bitrate",
    r"sample.?rate",
    r"wav",
    r"mp3",
    r"m4b",
    r"production",
    r"audiobook",
    r"release",
    r"schedule",
    r"90.?day",
    r"90.?D",
]

# Known operational subdirectories (skip these entirely)
OPERATIONAL_DIRS = {"operational"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter (--- delimited) and return a dict."""
    result = {}
    text = text.lstrip()
    if not text.startswith("---"):
        return result

    # Find the closing ---
    rest = text[3:]
    end_idx = rest.find("\n---")
    if end_idx == -1:
        return result

    fm_block = rest[:end_idx]
    for line in fm_block.splitlines():
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip().lower()
            value = value.strip().strip('"').strip("'")
            result[key] = value
    return result


def extract_title(text: str, frontmatter: dict) -> str:
    """Extract title from frontmatter title field or H1 heading."""
    if frontmatter.get("title"):
        return frontmatter["title"]
    # Fall back to first H1
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return "(no title)"


def extract_category(frontmatter: dict) -> str:
    """Extract category from frontmatter."""
    cat = frontmatter.get("category", "")
    if cat:
        return cat
    return "(uncategorized)"


def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def content_summary(text: str, max_len: int = 300) -> str:
    """Return first max_len characters of content (after frontmatter)."""
    # Strip frontmatter
    stripped = text.lstrip()
    if stripped.startswith("---"):
        end = stripped.find("\n---")
        if end != -1:
            stripped = stripped[end + 4:]
    stripped = stripped.lstrip()
    if len(stripped) > max_len:
        return stripped[:max_len] + "..."
    return stripped


def has_person_org_in_content(text: str) -> bool:
    """Check if content contains person/org indicators."""
    lower = text.lower()
    for pattern in CONTENT_PERSON_PATTERNS + CONTENT_ORG_PATTERNS:
        if re.search(pattern, lower):
            return True
    return False


def has_person_org_in_title(title: str) -> bool:
    """Check if the title looks like a person or organization name."""
    lower = title.lower()
    for pattern in TITLE_PERSON_PATTERNS + TITLE_ORG_PATTERNS:
        if re.search(pattern, lower):
            return True
    return False


def is_operational_file(filepath: str) -> bool:
    """Check if the file is in an operational directory or looks like an operational doc."""
    # Check directory path
    rel = os.path.relpath(filepath, KNOWLEDGE_DIR)
    parts = rel.split(os.sep)
    if len(parts) > 1 and parts[0] in OPERATIONAL_DIRS:
        return True
    # Check filename for operational indicators
    fname = os.path.basename(filepath).lower()
    for indicator in OPERATIONAL_INDICATORS:
        if re.search(indicator, fname):
            return True
    return False


def is_already_wiki_page(title: str) -> bool:
    """Check if a wiki page already exists for this title."""
    # Convert title to slug and check if file exists
    slug = slugify(title)
    for subdir in ("people", "organizations"):
        path = os.path.join(CONTENT_DIR, subdir, slug + ".md")
        if os.path.exists(path):
            return True
    return False


def slugify(text: str) -> str:
    """Convert a title to a wiki-style slug."""
    # Lowercase, replace spaces with hyphens, remove special chars
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    return slug


def is_wiki_page_file(filepath: str) -> bool:
    """Check if the file itself is a wiki page (has type: person or type: organization)."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    fm = extract_frontmatter(text)
    if fm.get("type") in ("person", "organization"):
        return True
    return False


def classify_file(filepath: str, verbose: bool = False) -> dict:
    """Classify a single file and return its classification dict."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()

    fm = extract_frontmatter(text)
    title = extract_title(text, fm)
    category = extract_category(fm)
    wc = word_count(text)
    summary = content_summary(text)

    # Strip frontmatter for content analysis
    stripped = text.lstrip()
    if stripped.startswith("---"):
        end = stripped.find("\n---")
        if end != 1:
            stripped = stripped[end + 4:]
    stripped = stripped.lstrip()

    has_person_org_content = has_person_org_in_content(stripped)
    has_person_org_title = has_person_org_in_title(title)
    operational = is_operational_file(filepath)
    already_wiki = is_already_wiki_page(title)
    is_wiki_page = is_wiki_page_file(filepath)

    # Classification logic
    if operational or is_wiki_page:
        classification = "not-wiki-worthy"
        reason = "operational doc" if operational else "already a wiki page"
        return {
            "filepath": filepath,
            "title": title,
            "category": category,
            "word_count": wc,
            "summary": summary,
            "classification": classification,
            "reason": reason,
            "has_person_org_content": has_person_org_content,
            "has_person_org_title": has_person_org_title,
            "operational": operational,
            "already_wiki": already_wiki,
            "is_wiki_page": is_wiki_page,
        }

    # Not operational, not already a wiki page
    if has_person_org_title and has_person_org_content and wc > 200:
        classification = "wiki-worthy"
        reason = "Has person/org name in title and content, sufficient content"
        return {
            "filepath": filepath,
            "title": title,
            "category": category,
            "word_count": wc,
            "summary": summary,
            "classification": classification,
            "reason": reason,
            "has_person_org_content": has_person_org_content,
            "has_person_org_title": has_person_org_title,
            "operational": operational,
            "already_wiki": already_wiki,
            "is_wiki_page": is_wiki_page,
        }

    if (has_person_org_title or has_person_org_content) and wc > 50:
        classification = "needs-review"
        missing = []
        if not has_person_org_title:
            missing.append("clear person/org name in title")
        if not has_person_org_content:
            missing.append("person/org references in content")
        if wc <= 200:
            missing.append(f"low word count ({wc} words, >200 recommended)")
        return {
            "filepath": filepath,
            "title": title,
            "category": category,
            "word_count": wc,
            "summary": summary,
            "classification": classification,
            "reason": "needs more info",
            "missing": missing,
            "has_person_org_content": has_person_org_content,
            "has_person_org_title": has_person_org_title,
            "operational": operational,
            "already_wiki": already_wiki,
            "is_wiki_page": is_wiki_page,
        }

    classification = "not-wiki-worthy"
    reason = "no person/org indicators found"
    return {
        "filepath": filepath,
        "title": title,
        "category": category,
        "word_count": wc,
        "summary": summary,
        "classification": classification,
        "reason": reason,
        "has_person_org_content": has_person_org_content,
        "has_person_org_title": has_person_org_title,
        "operational": operational,
        "already_wiki": already_wiki,
        "is_wiki_page": is_wiki_page,
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(results: list[dict], verbose: bool = False) -> str:
    """Generate the markdown report string."""
    lines = []
    lines.append("# Knowledge Base Classification Report")
    lines.append("")
    lines.append(f"*Generated on {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")

    # Summary
    total = len(results)
    wiki_worthy = [r for r in results if r["classification"] == "wiki-worthy"]
    needs_review = [r for r in results if r["classification"] == "needs-review"]
    not_worthy = [r for r in results if r["classification"] == "not-wiki-worthy"]

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total files scanned | {total} |")
    lines.append(f"| Wiki-worthy | {len(wiki_worthy)} |")
    lines.append(f"| Needs review | {len(needs_review)} |")
    lines.append(f"| Not wiki-worthy | {len(not_worthy)} |")
    lines.append("")

    # Wiki-worthy list
    lines.append("## Wiki-Worthy Files")
    lines.append("")
    if wiki_worthy:
        lines.append("| Title | Category | Word Count | Reason |")
        lines.append("|-------|----------|------------|--------|")
        for r in wiki_worthy:
            title_escaped = r["title"].replace("|", "\\|")
            lines.append(
                f"| {title_escaped} | {r['category']} | {r['word_count']} | {r['reason']} |"
            )
    else:
        lines.append("*No files classified as wiki-worthy.*")
    lines.append("")

    # Needs-review list
    lines.append("## Needs Review")
    lines.append("")
    if needs_review:
        lines.append("| Title | Category | Word Count | What's Missing |")
        lines.append("|-------|----------|------------|----------------|")
        for r in needs_review:
            title_escaped = r["title"].replace("|", "\\|")
            missing_str = "; ".join(r.get("missing", ["unclear"]))
            lines.append(
                f"| {title_escaped} | {r['category']} | {r['word_count']} | {missing_str} |"
            )
    else:
        lines.append("*No files need review.*")
    lines.append("")

    # Not-wiki-worthy list
    if not_worthy:
        lines.append("## Not Wiki-Worthy Files")
        lines.append("")
        lines.append("| Title | Category | Word Count | Reason |")
        lines.append("|-------|----------|------------|--------|")
        for r in not_worthy:
            title_escaped = r["title"].replace("|", "\\|")
            lines.append(
                f"| {title_escaped} | {r['category']} | {r['word_count']} | {r['reason']} |"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    verbose = "--verbose" in sys.argv

    # Collect all .md files
    md_files = []
    for root, dirs, files in os.walk(KNOWLEDGE_DIR):
        for fname in sorted(files):
            if fname.endswith(".md") and fname != "classification-report.md":
                md_files.append(os.path.join(root, fname))

    md_files.sort()

    if not md_files:
        print("No .md files found in", KNOWLEDGE_DIR)
        return

    # Classify each file
    results = []
    for fpath in md_files:
        result = classify_file(fpath, verbose=verbose)
        results.append(result)
        if verbose:
            status = result["classification"].upper()
            print(f"  [{status}] {fpath} — {result['title']}")

    # Generate report
    report = generate_report(results, verbose=verbose)

    # Write to file
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    # Print to stdout
    print(report)
    print(f"\nReport also written to: {REPORT_PATH}")


if __name__ == "__main__":
    main()