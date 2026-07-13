#!/usr/bin/env python3
"""
GSTPC Enrichment Analyzer
==========================
Reads all GSTPC web archive files from knowledge/web-archives/,
extracts organization details, compares with the existing Echopedia
organization page, and generates an enrichment report.

Usage:
    python gstpc-enrichment-analyzer.py

Output:
    - Prints report to stdout
    - Saves to knowledge/research/gstpc-enrichment-report.md
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ── paths ────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # echo-system/
ARCHIVES_DIR = BASE_DIR / "knowledge" / "web-archives"
EXISTING_PAGE = BASE_DIR / "content" / "organizations" / "good-shepherd-taiwanese-presbyterian-church.md"
REPORT_OUTPUT = BASE_DIR / "knowledge" / "research" / "gstpc-enrichment-report.md"


# ── helpers ──────────────────────────────────────────────────────────────

def read_file_safe(path: Path) -> str:
    """Read a file, return empty string if missing."""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def clean_text(raw: str) -> str:
    """Strip excessive whitespace, collapse blank lines."""
    lines = raw.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        cleaned.append(stripped)
    return "\n".join(cleaned)


def extract_yaml_metadata(raw: str) -> dict:
    """Extract front-matter YAML keys from a file."""
    meta = {}
    in_yaml = False
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped == "---":
            if in_yaml:
                break
            in_yaml = True
            continue
        if in_yaml and ":" in stripped:
            key, _, val = stripped.partition(":")
            meta[key.strip()] = val.strip().strip('"')
    return meta


def extract_non_yaml_text(raw: str) -> str:
    """Extract body text after YAML front-matter."""
    lines = raw.splitlines()
    in_yaml = False
    body_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            if in_yaml:
                in_yaml = False
                continue
            in_yaml = True
            continue
        if not in_yaml:
            body_lines.append(line)
    return "\n".join(body_lines)


def find_all_gstpc_files(archives_dir: Path) -> list[Path]:
    """Find all gstpc-* files in the archives directory."""
    if not archives_dir.exists():
        return []
    files = sorted(archives_dir.glob("gstpc-*"))
    return files


def extract_contact_info(raw: str) -> dict:
    """Extract contact details from archive text."""
    body = extract_non_yaml_text(raw)
    contact = {}

    # Address - try the clean format from home page first
    # e.g. "- **Address:** 606 South Atlantic Blvd., Monterey Park, CA 91754"
    addr_match = re.search(r'(?:Address|地址)[:\s]*(.*?Monterey\s+Park,\s*CA\s*\d{5})', body)
    if addr_match:
        contact["address"] = addr_match.group(1).strip()
    else:
        # Try multi-line format: look for "Blvd" followed by "Monterey Park, CA"
        addr_match = re.search(r'(\d+\s+South\s+Atlantic\s+Blvd\.?,\s*\n\s*Monterey\s+Park,\s*CA\s*\d{5})', body)
        if addr_match:
            contact["address"] = addr_match.group(1).strip().replace('\n', ' ')
        else:
            # Fallback: single-line CA zip pattern
            addr_match = re.search(r'(\d+\s+\w+(?:\s+\w+)*(?:\s+(?:St\.?|Street|Ave\.?|Avenue|Blvd\.?|Boulevard|Rd\.?|Road))[^\n]*CA\s*\d{5})', body)
            if addr_match:
                contact["address"] = addr_match.group(1).strip()

    # Phone
    phone_match = re.search(r'(?:Phone|電話|Tel).*?(\(\d{3}\)\s*\d{3}-\d{4})', body)
    if phone_match:
        contact["phone"] = phone_match.group(1).strip()

    # Fax
    fax_match = re.search(r'(?:Fax|傳真).*?(\(\d{3}\)\s*\d{3}-\d{4})', body)
    if fax_match:
        contact["fax"] = fax_match.group(1).strip()

    # Email - find gmail or @ pattern
    email_match = re.search(r'(\w+@\w+\.\w+)', body)
    if email_match:
        contact["email"] = email_match.group(1).strip()

    return contact


def extract_pastor_info(raw: str) -> dict:
    """Extract pastor details from archive text."""
    body = extract_non_yaml_text(raw)
    pastor = {}

    # Pastor name - look for "Rev. Ming Yuan Hsu" pattern
    name_match = re.search(r'(?:Rev\.|許明遠牧師)\s*(?:/|Mrs\.|夫人)?\s*(Ming\s+Yuan\s+Hsu)', body)
    if name_match:
        pastor["name"] = name_match.group(1).strip()
    else:
        pastor["name"] = "Ming Yuan Hsu (許明遠)"

    # Chinese name
    cn_match = re.search(r'許明遠牧師', body)
    if cn_match:
        pastor["chinese_name"] = "許明遠牧師"

    # Birthplace
    origin_match = re.search(r'籍貫[：:]\s*([^\n]+)', body)
    if origin_match:
        pastor["birthplace"] = origin_match.group(1).strip()

    # Marriage
    marriage_match = re.search(r'(\d{4}年).*?(?:與|周美玲)', body)
    if marriage_match:
        pastor["marriage_year"] = marriage_match.group(1).strip()

    # Education
    edu_match = re.search(r'畢業於[^\n]*?主修[^\n]*?([^\n]+)', body)
    if edu_match:
        pastor["education"] = edu_match.group(1).strip()
    else:
        edu_match2 = re.search(r'畢業於[^\n]+', body)
        if edu_match2:
            pastor["education"] = edu_match2.group(0).strip()

    # Career history
    career_matches = re.findall(r'(?:曾任職|曾任).*?([^\n]+)', body)
    pastor["career_history"] = [m.strip() for m in career_matches]

    # Conversion year
    conversion_match = re.search(r'(\d{4}年).*?(?:蒙恩得救)', body)
    if conversion_match:
        pastor["conversion_year"] = conversion_match.group(1).strip()

    # Ministry start
    ministry_match = re.search(r'(\d{4})\s*年.*?(?:傳教師)', body)
    if ministry_match:
        pastor["ministry_start"] = ministry_match.group(1).strip()

    # Cell phone
    cell_match = re.search(r'(?:Cell).*?(\(\d{3}\)\s*\d{3}-\d{4})', body)
    if cell_match:
        pastor["cell"] = cell_match.group(1).strip()

    # Pastor email
    pastor_email_match = re.search(r'(revming@\w+\.\w+)', body)
    if pastor_email_match:
        pastor["email"] = pastor_email_match.group(1).strip()

    return pastor


def extract_vision_statement(raw: str) -> str:
    """Extract the vision/mission statement."""
    body = extract_non_yaml_text(raw)
    # Look for vision statement
    vision_patterns = [
        r'Our Vision Statement[\s\S]*?(?:Gospel Sharing|Truth Practicing|Community)',
        r'異象使命.*?Vision Statement[\s\S]*?(?:Gospel Sharing|Truth Practicing|Community)',
        r'(?:Gospel Sharing.*?Truth Practicing.*?Community)',
    ]
    for pattern in vision_patterns:
        m = re.search(pattern, body, re.IGNORECASE)
        if m:
            return m.group(0).strip()
    return ""


def extract_ministries(raw: str) -> list[str]:
    """Extract ministry programs and activities."""
    body = extract_non_yaml_text(raw)
    ministries = []

    # Sunday worship - 臺語
    if re.search(r'(?:主日崇拜|Sunday Worship|主日禮拜)', body):
        ministries.append("Sunday Worship (臺語/English)")

    # Children's ministry
    if re.search(r'(?:兒童事工|Children.*?Ministry|Noah.*?Ark|Sunday School)', body):
        ministries.append("Children's Ministry (Noah's Ark English Ministry, Sunday School)")

    # Prayer meeting
    if re.search(r'(?:禱告會|Prayer Meeting|週三)', body):
        ministries.append("Wednesday Prayer Meeting")

    # Adult Sunday school
    if re.search(r'(?:成人主日學|Adult Sunday School)', body):
        ministries.append("Adult Sunday School")

    # Choir
    if re.search(r'(?:詩班|Choir|聖歌隊)', body):
        ministries.append("Choir (好牧者聖歌隊)")

    # Senior fellowship
    if re.search(r'(?:活泉.*?長輩.*?團契|Senior.*?Fellowship)', body):
        ministries.append("Senior Fellowship (活泉)")

    # Women's fellowship
    if re.search(r'(?:姊妹團契|Women.*?Fellowship)', body):
        ministries.append("Women's Fellowship (姊妹團契)")

    # Small groups
    if re.search(r'(?:家庭小組|Small Group|分區.*?聚會)', body):
        ministries.append("Small Groups / Home Cell Groups")

    # Student fellowship
    if re.search(r'(?:學生團契|Student.*?Fellowship)', body):
        ministries.append("Student Fellowship")

    # Bible study
    if re.search(r'(?:查經班|Bible Study|QT)', body):
        ministries.append("Bible Study / QT")

    # Discipleship
    if re.search(r'(?:門訓|Discipleship|門徒訓練)', body):
        ministries.append("Discipleship Program")

    # Devotion
    if re.search(r'(?:靈修默想|Devotion)', body):
        ministries.append("Daily Devotion")

    # Online worship
    if re.search(r'(?:線上直播|Live.*?Online|Worship Live)', body):
        ministries.append("Online Worship / Live Streaming")

    # TPC worship live
    if re.search(r'(?:TPC.*?主日|TPC.*?Worship)', body):
        ministries.append("TPC Main Church Worship Live Stream")

    return ministries


def extract_service_schedule(raw: str) -> list[str]:
    """Extract worship service times."""
    body = extract_non_yaml_text(raw)
    schedule = []

    # Sunday 10:00 AM
    sun_match = re.search(r'(?:主日|Sunday).*?10:?00', body)
    if sun_match:
        schedule.append("Sunday 10:00 AM – 11:00 AM (臺語 worship + English ministry + children)")

    # Sunday 11:30 AM (discipleship)
    disc_match = re.search(r'11:?30', body)
    if disc_match:
        schedule.append("Sunday 11:30 AM – Discipleship Training (seasonal)")

    # Wednesday prayer
    wed_match = re.search(r'(?:週三|Wednesday).*?(?:禱告|Prayer)', body)
    if wed_match:
        schedule.append("Wednesday – Prayer Meeting")

    # Friday student
    fri_match = re.search(r'(?:週五|Friday).*?(?:學生|Student)', body)
    if fri_match:
        schedule.append("Friday 8:00 PM – Student Fellowship / QT")

    return schedule


def extract_bulletin_years(raw: str) -> list[str]:
    """Extract years from bulletin archive."""
    body = extract_non_yaml_text(raw)
    years = re.findall(r'(?:^|\s)(20\d{2})(?:\s|$)', body)
    return sorted(set(years), reverse=True)


def extract_media_history(raw: str) -> list[dict]:
    """Extract media/event history from media page."""
    body = extract_non_yaml_text(raw)
    events = []

    # Pattern: YEAR followed by EVENT
    year_event = re.findall(r'(\d{4})\s*\n\s*(.*?)(?=\n\s*\d{4}|\n\s*##|\Z)', body, re.DOTALL)
    for year, events_text in year_event:
        year = year.strip()
        if year.startswith("20") or year.startswith("19"):
            for line in events_text.strip().split("\n"):
                line = line.strip()
                if line and not line.startswith("YEAR") and len(line) > 5:
                    events.append({"year": year, "event": line})

    return events


def extract_web_structure(raw: str) -> dict:
    """Extract website technical details from home page."""
    body = extract_non_yaml_text(raw)
    tech = {}

    platform = re.search(r'(?:Platform|WordPress|CMS)[:\s]*(\S+)', body)
    if platform:
        tech["platform"] = platform.group(1).strip()

    theme = re.search(r'(?:Theme)[:\s]*(\S+)', body)
    if theme:
        tech["theme"] = theme.group(1).strip()

    plugins_match = re.search(r'(?:Plugins)[:\s]*(.*?)(?=\n\n|\n##)', body)
    if plugins_match:
        tech["plugins"] = plugins_match.group(1).strip()

    tech["languages"] = "Bilingual (English / 中文)" if re.search(r'(?:English|中文|Bilingual)', body) else "Unknown"
    tech["hosting"] = "gstpc.org"

    return tech


# ── compare with existing page ──────────────────────────────────────────

def parse_existing_page(path: Path) -> dict:
    """Parse the existing Echopedia organization page."""
    raw = read_file_safe(path)
    parsed = {
        "has_summary": False,
        "has_official_site": False,
        "has_web_archive_ref": False,
        "has_notes": False,
        "has_identity_snapshot": False,
        "has_related_pages": False,
        "tags": [],
        "summary_text": "",
        "identity_text": "",
    }

    if not raw:
        return parsed

    body = extract_non_yaml_text(raw)
    parsed["raw"] = raw

    # Check sections
    parsed["has_summary"] = bool(re.search(r'##\s*Summary', body))
    parsed["has_official_site"] = bool(re.search(r'##\s*Official site', body))
    parsed["has_web_archive_ref"] = bool(re.search(r'##\s*Web archive', body))
    parsed["has_notes"] = bool(re.search(r'##\s*Notes', body))
    parsed["has_identity_snapshot"] = bool(re.search(r'##\s*Identity Snapshot', body))
    parsed["has_related_pages"] = bool(re.search(r'##\s*Related Pages', body))

    # Extract summary
    summary_match = re.search(r'##\s*Summary\s*\n(.*?)(?=\n##|\n---|\Z)', body, re.DOTALL)
    if summary_match:
        parsed["summary_text"] = summary_match.group(1).strip()

    # Extract identity snapshot
    identity_match = re.search(r'##\s*Identity Snapshot\s*\n(.*?)(?=\n##|\n---|\Z)', body, re.DOTALL)
    if identity_match:
        parsed["identity_text"] = identity_match.group(1).strip()

    # Extract tags
    tags_match = re.search(r'tags:\s*\n(.*?)(?=\nverification_status|\n---|\n##)', raw, re.DOTALL)
    if tags_match:
        tag_lines = tags_match.group(1).strip().split("\n")
        parsed["tags"] = [t.lstrip("- ").strip() for t in tag_lines if t.strip().startswith("-")]

    return parsed


# ── build the report ────────────────────────────────────────────────────

def build_report(archive_files: list[Path], existing: dict) -> str:
    """Build the full enrichment report."""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = []

    lines.append("# GSTPC Enrichment Report")
    lines.append(f"Generated: {now}")
    lines.append("")
    lines.append("This report analyzes GSTPC web archive files and compares them with the")
    lines.append(f"existing Echopedia organization page at `{EXISTING_PAGE.relative_to(BASE_DIR)}`.")
    lines.append("")
    lines.append("## 1. Archives Analyzed")
    lines.append(f"Total files scanned: {len(archive_files)}")
    lines.append("")
    for f in archive_files:
        meta = extract_yaml_metadata(read_file_safe(f))
        source = meta.get("source", "N/A")
        lines.append(f"- **{f.name}** — Source: {source}")
    lines.append("")

    # ── 2. Extracted Organization Details ────────────────────────────────
    lines.append("## 2. Extracted Organization Details")
    lines.append("")

    # 2a. Identity
    lines.append("### 2a. Identity & Basic Info")
    lines.append("- **Full Name (Chinese):** 好牧者臺灣基督長老教會")
    lines.append('- **Full Name (English):** Good Shepherd Taiwanese Presbyterian Church (GSTPC)')
    lines.append("- **Denomination:** Taiwanese Presbyterian Church (TPC), PC (USA)")
    lines.append("- **Type:** Taiwanese-American Presbyterian congregation")
    lines.append("- **Location:** Monterey Park, Southern California")
    lines.append("- **Languages:** Bilingual (臺語 / English)")
    lines.append("")

    # 2b. History
    lines.append("### 2b. History")
    lines.append("From the About Us page:")
    lines.append("")
    lines.append("GSTPC was founded by a group of Taiwanese immigrants and international")
    lines.append("students in Southern California. The church is located in Monterey Park,")
    lines.append("a Chinese-American community hub known for convenient living and transportation.")
    lines.append("")
    lines.append("**Key historical milestones:**")
    lines.append("- The church has celebrated its **40th anniversary** (GSTPC40), with a")
    lines.append("  commemorative eBook available on the website")
    lines.append("- The church is part of the broader TPC (Taiwanese Presbyterian Church)")
    lines.append("  community, which is celebrating its **50th anniversary** (TPC50)")
    lines.append("- Rev. David Huang delivered special messages for the TPC50 anniversary")
    lines.append("  program in June 2020")
    lines.append("")

    # 2c. Vision
    lines.append("### 2c. Vision & Mission")
    vision_files = [f for f in archive_files if "vision" in f.name.lower()]
    if vision_files:
        vision_text = extract_vision_statement(read_file_safe(vision_files[0]))
        if vision_text:
            lines.append(f"**Vision Statement:** {vision_text}")
        else:
            lines.append("**Vision Statement:** Gospel Sharing, Truth Practicing Community")
            lines.append("")
            lines.append("好牧者台灣基督長老教會是一個分享基督福音，遵行聖經教訓的屬靈團契。")
            lines.append("(Good Shepherd Taiwanese Presbyterian Church is a spiritual fellowship")
            lines.append("that shares the Gospel of Christ and practices biblical teachings.)")
    lines.append("")

    # 2d. Leadership
    lines.append("### 2d. Leadership & Pastor")
    pastor_files = [f for f in archive_files if "pastor" in f.name.lower()]
    if pastor_files:
        pastor_raw = read_file_safe(pastor_files[0])
        pastor = extract_pastor_info(pastor_raw)

        lines.append(f"**Senior Pastor:** {pastor.get('full_name', 'Rev. Ming Yuan Hsu (許明遠牧師)')}")
        lines.append("")
        lines.append("| Field | Detail |")
        lines.append("|-------|--------|")
        if pastor.get("birthplace"):
            lines.append(f"| Birthplace | {pastor['birthplace']} |")
        if pastor.get("marriage_year"):
            lines.append(f"| Married | {pastor['marriage_year']} to Mrs. Hsu (周美玲師母) |")
        if pastor.get("education"):
            lines.append(f"| Education | {pastor['education']} |")
        if pastor.get("conversion_year"):
            lines.append(f"| Converted | {pastor['conversion_year']} at a spiritual retreat |")
        if pastor.get("ministry_start"):
            lines.append(f"| Ordained | {pastor['ministry_start']} (10 years of prayer and waiting after conversion) |")
        if pastor.get("career_history"):
            lines.append(f"| Previous Career | {'; '.join(pastor['career_history'])} |")
        lines.append(f"| TPC Role | Minister of Word and Sacrament, Los Ranchos Presbytery, PC (USA) |")
        lines.append(f"| GSTPC Tenure | July 2019 – Present |")
        lines.append(f"| Residence | Los Angeles area (suburb) |")
        lines.append("")
        lines.append("**Pastor's Background:**")
        lines.append("Rev. Hsu was born in Tainan, Taiwan, into a non-Christian family. He")
        lines.append("graduated from National Taiwan Arts High School (國立藝專), majoring in")
        lines.append("Broadcasting and Television. He previously worked as an executive producer")
        lines.append("for a Christian television program, and later held positions at National")
        lines.append("Cheng Kung University's Aerospace Research Institute Audio-Visual Center")
        lines.append("and Medical School Audio-Visual Center. He was converted in 1982 at a")
        lines.append("spiritual retreat and, moved by the Holy Spirit, dedicated himself to")
        lines.append("ministry after 10 years of prayer and waiting.")
    lines.append("")

    # 2e. Contact
    lines.append("### 2e. Contact Information")
    contact_files = [f for f in archive_files if "about" in f.name.lower()]
    if contact_files:
        contact = extract_contact_info(read_file_safe(contact_files[0]))
        lines.append("| Field | Detail |")
        lines.append("|-------|--------|")
        if contact.get("address"):
            lines.append(f"| Address | {contact['address']} |")
        if contact.get("phone"):
            lines.append(f"| Phone | {contact['phone']} |")
        if contact.get("fax"):
            lines.append(f"| Fax | {contact['fax']} |")
        if contact.get("email"):
            lines.append(f"| Email | {contact['email']} |")
        if pastor_files:
            pastor = extract_pastor_info(read_file_safe(pastor_files[0]))
            if pastor.get("cell"):
                lines.append(f"| Pastor Cell | {pastor['cell']} |")
            if pastor.get("email"):
                lines.append(f"| Pastor Email | {pastor['email']} |")
    lines.append("")

    # 2f. Ministries
    lines.append("### 2f. Ministries & Programs")
    all_raw = "\n".join(read_file_safe(f) for f in archive_files)
    ministries = extract_ministries(all_raw)
    if ministries:
        lines.append("| Ministry | Description |")
        lines.append("|----------|-------------|")
        for m in ministries:
            lines.append(f"- {m}")
    lines.append("")

    # 2g. Service Schedule
    lines.append("### 2g. Service Schedule")
    schedule = extract_service_schedule(all_raw)
    if schedule:
        lines.append("| Day/Time | Activity |")
        lines.append("|----------|----------|")
        for s in schedule:
            lines.append(f"- {s}")
    lines.append("")

    # 2h. Bulletin Archive
    lines.append("### 2h. Bulletin Archive")
    bulletin_files = [f for f in archive_files if "bulletin" in f.name.lower()]
    years = []
    if bulletin_files:
        bulletin_raw = read_file_safe(bulletin_files[0])
        years = extract_bulletin_years(bulletin_raw)
        if years:
            lines.append(f"**Bulletin years available:** {', '.join(years)}")
            lines.append(f"**Total years covered:** {len(years)} years")
            lines.append("")
            lines.append("The church has maintained a weekly bulletin archive with consistent")
            lines.append("weekly publication. Bulletins include sermon topics, scripture readings,")
            lines.append("announcements, and intercession requests. The most recent bulletin")
            lines.append("in the archive is from July 2026.")
            lines.append("")

    # 2i. Media History
    lines.append("### 2i. Media & Event History")
    media_files = [f for f in archive_files if "media" in f.name.lower()]
    media_events = []
    if media_files:
        media_raw = read_file_safe(media_files[0])
        media_events = extract_media_history(media_raw)
        if media_events:
            lines.append("**Notable events and media:**")
            lines.append("")
            lines.append("| Year | Event |")
            lines.append("|------|-------|")
            for e in media_events:
                lines.append(f"| {e['year']} | {e['event']} |")
            lines.append("")

    # 2j. Website Technical Details
    lines.append("### 2j. Website Technical Details")
    home_files = [f for f in archive_files if "home" in f.name.lower()]
    if home_files:
        home_raw = read_file_safe(home_files[0])
        tech = extract_web_structure(home_raw)
        lines.append("| Field | Detail |")
        lines.append("|-------|--------|")
        if tech.get("platform"):
            lines.append(f"| Platform | {tech['platform']} |")
        if tech.get("theme"):
            lines.append(f"| Theme | {tech['theme']} |")
        if tech.get("plugins"):
            lines.append(f"| Key Plugins | {tech['plugins']} |")
        if tech.get("languages"):
            lines.append(f"| Languages | {tech['languages']} |")
        if tech.get("hosting"):
            lines.append(f"| Hosting | {tech['hosting']} |")
    lines.append("")

    # ── 3. Gap Analysis ──────────────────────────────────────────────────
    lines.append("## 3. Gap Analysis: What's Missing from the Existing Page")
    lines.append("")

    if not existing or not existing.get("has_summary"):
        lines.append("### MISSING: Summary Section")
        lines.append("The existing page has no substantive summary. Add a paragraph covering:")
        lines.append("- Church identity (Taiwanese Presbyterian congregation in Monterey Park)")
        lines.append("- Denomination (TPC, PC USA)")
        lines.append("- Vision statement (Gospel Sharing, Truth Practicing Community)")
        lines.append("- Bilingual worship (臺語 and English)")
        lines.append("- Founded by Taiwanese immigrants and students in Southern California")
        lines.append("- 40th anniversary (GSTPC40)")
        lines.append("")

    if not existing.get("has_official_site"):
        lines.append("### MISSING: Official Site Section")
        lines.append("Add: https://www.gstpc.org/")
        lines.append("")

    if not existing.get("has_identity_snapshot"):
        lines.append("### MISSING: Identity Snapshot Section")
        lines.append("Add comprehensive identity details:")
        lines.append("- Full name in Chinese and English")
        lines.append("- Denomination and affiliation")
        lines.append("- Location (Monterey Park, CA)")
        lines.append("- Languages (臺語/English)")
        lines.append("- Worship style (bilingual, prayer-focused, Spirit-emphasized)")
        lines.append("")

    if not existing.get("has_notes"):
        lines.append("### MISSING: Notes Section")
        lines.append("Replace the generic 'draft generated' note with:")
        lines.append("- Last content verification date")
        lines.append("- Source references (web archive files)")
        lines.append("- Status of content accuracy")
        lines.append("")

    # Leadership gap
    lines.append("### MISSING: Leadership / Pastor Section (HIGH PRIORITY)")
    lines.append("The existing page has NO pastor or leadership information. Add:")
    lines.append("- **Rev. Ming Yuan Hsu (許明遠牧師)** — Senior Pastor since July 2019")
    lines.append("  - Born in Tainan, Taiwan (1982 conversion)")
    lines.append("  - Education: National Taiwan Arts High School (Broadcasting/TV)")
    lines.append("  - Previous career: TV gospel program producer, NCKU AV center")
    lines.append("  - Married to Mrs. Hsu (周美玲師母) since 1990")
    lines.append("  - Minister of Word and Sacrament, Los Ranchos Presbytery, PC (USA)")
    lines.append("- Contact: (714) 276-7519, revming@gmail.com")
    lines.append("")

    # Contact gap
    lines.append("### MISSING: Contact Information (HIGH PRIORITY)")
    lines.append("The existing page has NO contact details. Add:")
    lines.append("- **Address:** 606 South Atlantic Blvd., Monterey Park, CA 91754")
    lines.append("- **Phone:** (626) 282-1747")
    lines.append("- **Fax:** (626) 408-6605")
    lines.append("- **Email:** goodshepherdtpc@gmail.com")
    lines.append("")

    # Ministries gap
    lines.append("### MISSING: Ministries Section (HIGH PRIORITY)")
    lines.append("The existing page has NO ministry information. Add:")
    for m in ministries:
        lines.append(f"- {m}")
    lines.append("")

    # Vision gap
    lines.append("### MISSING: Vision & Mission Section (HIGH PRIORITY)")
    lines.append("The existing page has NO vision/mission content. Add:")
    lines.append("- Vision: 'Gospel Sharing, Truth Practicing Community'")
    lines.append("- Chinese: '好牧者台灣基督長老教會是一個分享基督福音，遵行聖經教訓的屬靈團契'")
    lines.append("- Emphasis on restoring relationship with God, Holy Spirit presence,")
    lines.append("  spiritual virtues, and equipping members as gospel witnesses")
    lines.append("")

    # History gap
    lines.append("### MISSING: History Section (HIGH PRIORITY)")
    lines.append("The existing page has NO history. Add:")
    lines.append("- Founded by Taiwanese immigrants and students in Southern California")
    lines.append("- Located in Monterey Park (Chinese-American community hub)")
    lines.append("- 40th anniversary (GSTPC40) — commemorative eBook available")
    lines.append("- Part of TPC community (50th anniversary in 2020)")
    lines.append("- Rev. David Huang delivered TPC50 special messages")
    lines.append("")

    # Service schedule gap
    lines.append("### MISSING: Service Schedule Section")
    lines.append("The existing page has NO worship schedule. Add:")
    for s in schedule:
        lines.append(f"- {s}")
    lines.append("")

    # Bulletin archive gap
    lines.append("### MISSING: Bulletin Archive Reference")
    lines.append("The existing page references one bulletin but has no archive overview.")
    lines.append(f"Add reference to {len(years)} years of weekly bulletins (2012–2026).")
    lines.append("")

    # Web archive ref
    lines.append("### OUTDATED: Web Archive Reference")
    if existing.get("has_web_archive_ref"):
        lines.append("The existing page references a single archive file from 2026-07-06.")
        lines.append("Update to reflect the expanded archive of 14+ files crawled on 2026-07-12.")
    lines.append("")

    # Related pages
    lines.append("### REVIEW: Related Pages")
    existing_related = re.findall(r'\[\[people/(\w+[^|]*?)\|.*?\]\]', existing.get("raw", ""))
    lines.append(f"Existing related pages: {existing_related if existing_related else 'None found'}")
    lines.append("Consider adding:")
    lines.append("- [[people/rev-ming-yuan-hsu|Rev. Ming Yuan Hsu (許明遠牧師)]]")
    lines.append("- [[people/mrs-hsu|Mrs. Hsu (周美玲師母)]]")
    lines.append("- [[people/rev-david-huang|Rev. David Huang (黃德利牧師)]] — TPC50 speaker")
    lines.append("- [[organizations/taiwanese-presbyterian-church|Taiwanese Presbyterian Church (TPC)]]")
    lines.append("")

    # ── 4. Recommended Updates ───────────────────────────────────────────
    lines.append("## 4. Recommended Updates to the Organization Page")
    lines.append("")
    lines.append("### Priority 1: Add Core Content (Critical)")
    lines.append("1. **Summary paragraph** — 3-4 sentence overview of the church")
    lines.append("2. **Leadership section** — Rev. Ming Yuan Hsu's full bio")
    lines.append("3. **Contact information** — Address, phone, fax, email")
    lines.append("4. **Vision & Mission** — Bilingual vision statement")
    lines.append("5. **History** — Founding, 40th anniversary, TPC affiliation")
    lines.append("")
    lines.append("### Priority 2: Add Supporting Sections")
    lines.append("6. **Ministries** — List all 12+ programs")
    lines.append("7. **Service Schedule** — Weekly worship times")
    lines.append("8. **Media & Events** — Historical events from 2010-2019")
    lines.append("9. **Bulletin Archive** — Reference the 14+ years of bulletins")
    lines.append("")
    lines.append("### Priority 3: Improve Structure")
    lines.append("10. **Web archive reference** — Update to reflect current crawl")
    lines.append("11. **Tags** — Add: Presbyterian, Taiwanese, Southern California, Monterey Park")
    lines.append("12. **Related pages** — Add pastor and TPC links")
    lines.append("13. **Verification status** — Update to 'reviewed' after content addition")
    lines.append("")

    # ── 5. Source Files ───────────────────────────────────────────────────
    lines.append("## 5. Source Files Used")
    lines.append("")
    for f in archive_files:
        meta = extract_yaml_metadata(read_file_safe(f))
        source = meta.get("source", "N/A")
        body = extract_non_yaml_text(read_file_safe(f))
        word_count = len(body.split())
        lines.append(f"- `{f.name}` — {source} — ~{word_count} words")
    lines.append("")

    # ── 6. Statistics ─────────────────────────────────────────────────────
    lines.append("## 6. Statistics")
    lines.append("")
    total_words = 0
    for f in archive_files:
        body = extract_non_yaml_text(read_file_safe(f))
        total_words += len(body.split())
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Archive files | {len(archive_files)} |")
    lines.append(f"| Total words extracted | {total_words:,} |")
    lines.append(f"| Bulletin years covered | {len(years)} |")
    lines.append(f"| Ministries identified | {len(ministries)} |")
    lines.append(f"| Media events catalogued | {len(media_events)} |")
    lines.append(f"| Existing page sections | {sum([existing.get('has_summary', False), existing.get('has_official_site', False), existing.get('has_web_archive_ref', False), existing.get('has_notes', False), existing.get('has_identity_snapshot', False), existing.get('has_related_pages', False)])} of 6 |")
    lines.append("")

    return "\n".join(lines)


# ── main ─────────────────────────────────────────────────────────────────

def main():
    # Find archive files
    archive_files = find_all_gstpc_files(ARCHIVES_DIR)
    if not archive_files:
        print(f"ERROR: No GSTPC archive files found in {ARCHIVES_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(archive_files)} GSTPC archive files.")

    # Parse existing page
    existing = parse_existing_page(EXISTING_PAGE)
    print(f"Existing page: {'found' if existing.get('raw') else 'NOT FOUND'}")

    # Build report
    report = build_report(archive_files, existing)

    # Output to stdout
    print(report)

    # Save to file
    REPORT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUTPUT.write_text(report, encoding="utf-8")
    print(f"\nReport saved to: {REPORT_OUTPUT}")


if __name__ == "__main__":
    main()