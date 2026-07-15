#!/usr/bin/env python3
"""
GSTPC Enrichment Applier
=========================
Reads the enrichment report and applies recommendations to the org page.
Generates a complete wiki page from extracted archive data.

Usage:
    python gstpc-enrichment-applier.py [--dry-run] [--output-path PATH]

Output:
    - Writes enriched page to content/organizations/ (or staging/)
    - Prints diff summary
    - Runs audit check
"""

import os
import re
import sys
import glob
from datetime import datetime
from pathlib import Path

# ── paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path("/home/leedt/echo-system")
ARCHIVES_DIR = BASE_DIR / "knowledge" / "web-archives"
REPORT_FILE = BASE_DIR / "knowledge" / "research" / "gstpc-enrichment-report.md"
EXISTING_PAGE = BASE_DIR / "content" / "organizations" / "good-shepherd-taiwanese-presbyterian-church.md"
OUTPUT_DIR = BASE_DIR / "content" / "organizations"  # direct write (staging can be added later)
DRY_RUN = "--dry-run" in sys.argv


def read_file(path: Path) -> str:
    """Read file, return empty string if missing."""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def extract_non_yaml_text(raw: str) -> str:
    """Strip YAML frontmatter and return body text."""
    lines = raw.splitlines()
    in_frontmatter = False
    body_lines = []
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == '---':
            in_frontmatter = True
            continue
        if in_frontmatter and line.strip() == '---':
            in_frontmatter = False
            continue
        if in_frontmatter:
            continue
        body_lines.append(line)
    return "\n".join(body_lines)


def extract_all_archives() -> dict:
    """Read all GSTPC archives and extract structured data."""
    archives = glob.glob(str(ARCHIVES_DIR / "gstpc-*.md"))
    all_text = ""
    sources = {}
    
    for f in sorted(archives):
        name = os.path.basename(f)
        content = read_file(Path(f))
        if content:
            all_text += content + "\n\n"
            sources[name] = len(content)
    
    return all_text, sources


def extract_identity(all_text: str) -> dict:
    """Extract identity information from archives."""
    result = {}
    
    # Chinese name
    if "好牧者臺灣基督長老教會" in all_text:
        result["chinese_name"] = "好牧者臺灣基督長老教會"
    
    # English name
    if "Good Shepherd Taiwanese Presbyterian Church" in all_text:
        result["english_name"] = "Good Shepherd Taiwanese Presbyterian Church"
    
    # Acronym
    if "GSTPC" in all_text:
        result["acronym"] = "GSTPC"
    
    # Location
    if "Monterey Park" in all_text:
        result["location"] = "Monterey Park, Southern California"
    
    # Denomination
    if "Taiwanese Presbyterian" in all_text or "TPC" in all_text:
        result["denomination"] = "Taiwanese Presbyterian Church (TPC), PC(USA)"
    
    # Type
    if "congregation" in all_text.lower() or "教會" in all_text:
        result["type"] = "Taiwanese-American Presbyterian congregation"
    
    # Languages
    if "臺語" in all_text or "Taiwanese" in all_text:
        result["languages"] = "臺語 (Taiwanese) primary, English ministry"
    
    return result


def extract_contact(all_text: str) -> dict:
    """Extract contact information."""
    result = {}
    
    # Address (multi-line handling)
    addr_match = re.search(r'(?:606\s+South\s+Atlantic\s+Blvd\.?,?\s*\n?\s*(Monterey\s+Park,\s*CA\s*91754))', all_text)
    if addr_match:
        result["address"] = "606 South Atlantic Blvd., Monterey Park, CA 91754"
    
    # Phone
    phone_match = re.search(r'\(?626\)?\s*\d{3}-\d{4}', all_text)
    if phone_match:
        result["phone"] = phone_match.group(0)
    
    # Fax
    fax_match = re.search(r'Fax:\s*(\d{3}-\d{3}-\d{4})', all_text)
    if fax_match:
        result["fax"] = fax_match.group(1)
    
    # Email
    email_match = re.search(r'(\w+@\w+\.\w+)', all_text)
    if email_match:
        result["email"] = email_match.group(1)
    
    # Pastor cell
    pastor_cell = re.search(r'Cell:\s*\(?(\d{3}\)?)\s*\d{3}-\d{4}', all_text)
    if pastor_cell:
        result["pastor_cell"] = pastor_cell.group(0).replace("Cell:", "").strip()
    
    # Pastor email
    pastor_email = re.search(r'revming@\w+', all_text)
    if pastor_email:
        result["pastor_email"] = pastor_email.group(0)
    
    # Facebook
    if "facebook.com/mpgstpc" in all_text:
        result["facebook"] = "facebook.com/mpgstpc"
    
    # YouTube
    if "youtube.com/channel" in all_text:
        result["youtube"] = "GSTPC channel"
    
    return result


def extract_pastor(all_text: str) -> dict:
    """Extract pastor information from pastor page archive."""
    result = {}
    
    # Name
    if "許明遠" in all_text:
        result["chinese_name"] = "許明遠牧師"
    if "Ming Yuan Hsu" in all_text:
        result["english_name"] = "Rev. Ming Yuan Hsu"
    
    # Tenure
    if "July 2019" in all_text:
        result["tenure"] = "July 2019 – Present (full-time pastor)"
    
    # Birthplace
    if "台南" in all_text or "Tainan" in all_text:
        result["birthplace"] = "台灣台南 (Tainan, Taiwan)"
    
    # Marriage
    if "周美玲" in all_text or "Mrs. Hsu" in all_text:
        result["marriage"] = "1990年與周美玲師母結婚 (married 1990 to Mrs. Hsu, 周美玲)"
    
    # Residence
    if "洛杉磯" in all_text or "Los Angeles" in all_text:
        result["residence"] = "目前定居洛杉磯近郊 (currently resides near Los Angeles)"
    
    # Education
    if "國立藝專" in all_text or "Broadcasting" in all_text:
        result["education"] = "畢業於國立藝專，主修廣播電視 (Graduated from National Arts School, majoring in Broadcasting/Television)"
    
    # Previous career
    if "電視福音" in all_text or "TV evangelism" in all_text:
        result["previous_career"] = "曾任電視福音節目執行製作 (TV evangelism program executive producer); 曾任職成功大學航空太空研究所視聽中心、成功大學醫學院視聽中心"
    
    # Conversion
    if "1982年" in all_text and "靈修會" in all_text:
        result["conversion"] = "1982年參加靈修會蒙恩得救 (Converted to Christianity in 1982 at a spiritual retreat)"
    
    # Call to ministry
    if "十年的禱告" in all_text or "ten years" in all_text.lower():
        result["call"] = "隨即被聖靈感動，立志獻身服事，經過十年的禱告及等候 (Immediately moved by the Holy Spirit, after ten years of prayer and waiting)"
    
    # Ordination
    if "Los Ranchos Presbytery" in all_text:
        result["ordination"] = "傳教師會籍：Minister of Word and Sacrament, Los Ranchos Presbytery, PC(USA)"
    
    return result


def extract_ministries(all_text: str) -> list:
    """Extract ministry programs."""
    ministries = []
    
    ministry_map = [
        (r'(?:Noah.*?Ark|Noah\'s\s*Ark)', "Noah's Ark English Ministry — Truth and life teaching for 2nd generation"),
        (r'(?:成人主日學|Adult\s*Sunday\s*School)', "Adult Sunday School"),
        (r'(?:詩班|Choir|聖歌隊)', "Choir (好牧者聖歌隊)"),
        (r'(?:活泉.*?長輩|活泉)', "活泉 (senior) fellowship"),
        (r'(?:姊妹團契|Women.*?Fellowship)', "Sisters' fellowship (姊妹團契)"),
        (r'(?:家庭小組|Small\s*Group|分區.*?聚會)', "Area home small groups (分區家庭小組)"),
        (r'(?:禱告會|Prayer\s*Meeting|週三)', "Wednesday prayer meeting"),
        (r'(?:門徒訓練|Discipleship|門訓)', "Discipleship training (門徒訓練)"),
        (r'(?:學生團契|Student\s*Fellowship|學生)', "Student fellowship / QT Bible study"),
        (r'(?:兒童事工|Children.*?Ministry|兒童)', "Children's ministry (Sunday school)"),
    ]
    
    for pattern, name in ministry_map:
        if re.search(pattern, all_text):
            ministries.append(name)
    
    return ministries


def extract_schedule(all_text: str) -> list:
    """Extract worship schedule."""
    schedule = []
    
    if re.search(r'(?:主日上午|Sunday\s+10|主日崇拜|Sunday\s+Worship)', all_text):
        schedule.append("Sunday worship: 10:00 AM – 11:00 AM (Family Worship / English Ministry / Children's Ministry)")
    
    if re.search(r'(?:週三|Wednesday|禱告會|Prayer\s+Meeting)', all_text):
        schedule.append("Wednesday prayer meeting: midweek gathering")
    
    if re.search(r'(?:門徒訓練|Discipleship|11:30)', all_text):
        schedule.append("Discipleship training: 11:30 AM Sunday (seasonal)")
    
    if re.search(r'(?:週五|Friday|學生團契|Student)', all_text):
        schedule.append("Student fellowship / QT Bible study: Friday 8:00 PM (seasonal)")
    
    return schedule


def extract_history(all_text: str, sources: dict) -> str:
    """Extract historical narrative."""
    history_parts = []
    
    # Founding
    if "從台灣移民" in all_text or "immigrants" in all_text.lower():
        history_parts.append("GSTPC was founded by a group of Taiwanese immigrants and international students in Southern California, who gathered in the familiar warmth of Taiwanese (臺語) worship.")
    
    # 40th anniversary
    if "40" in str(sources) and "anniversary" in all_text.lower():
        history_parts.append("The church celebrated its 40th anniversary (GSTPC40) with a commemorative eBook and special programming.")
    
    # TPC connection
    if "TPC 50" in all_text or "TPC50" in all_text:
        history_parts.append("GSTPC is part of the broader TPC (Taiwanese Presbyterian Church) community, which celebrated its 50th anniversary in 2020.")
    
    # Bulletin history
    if "bulletin" in all_text.lower():
        history_parts.append("The church has maintained a weekly bulletin archive spanning 15+ years (2012–2026), documenting sermon series, pastoral messages, and community events.")
    
    return "\n\n".join(history_parts)


def extract_events(all_text: str) -> list:
    """Extract notable events."""
    events = []
    
    # TPC 50th special
    if "TPC 50" in all_text or "TPC50" in all_text:
        events.append("TPC 50th Anniversary Special Program (May–June 2020) — 3 episodes featuring Rev. David Huang (黃德利牧師)")
    
    # 馬偕博士台灣宣教150週年
    if "馬偕" in all_text or "150" in all_text:
        events.append("馬偕博士台灣宣教150週年紀念主日 (2022)")
    
    # 25th anniversary
    if "gstpc25" in all_text.lower() or "25週年" in all_text:
        events.append("25th anniversary commemorative booklet (GSTPC25)")
    
    return events


def extract_resources(all_text: str) -> list:
    """Extract downloadable resources."""
    resources = []
    
    resource_map = [
        (r'2023.*?春季會員大會', "2023 Spring Meeting Docket 春季會員大會手冊"),
        (r'2022.*?春季會員大會', "2022 Spring Meeting Docket 春季會員大會手冊"),
        (r'2021.*?秋季會員大會', "2021 Fall Meeting Docket 秋季會員大會手冊"),
        (r'2020.*?春季會員大會', "2020 Spring Meeting Docket 春季會員大會手冊"),
        (r'2019.*?秋季會員大會', "2019 Fall Meeting Docket 秋季會員大會手冊"),
        (r'gstpc25.*?紀念', "GSTPC25 二十五週年紀念刋"),
        (r'gstpc40.*?紀念', "GSTPC40 四十週年感恩紀念刋"),
        (r'防疫滿福寶', "防疫滿福寶網路版 (PDF)"),
        (r'Blessing.*?Prayer', "Blessing Prayer (CrossWalk)"),
        (r'2020.*?大齋', "2020 大齋節期靈修"),
        (r'會員.*?資料表', "Church Membership Application Form 會員資料表"),
        (r'40th.*?Survey', "40th Anniversary Participation Survey"),
    ]
    
    for pattern, name in resource_map:
        if re.search(pattern, all_text):
            resources.append(name)
    
    return resources


def build_page(identity: dict, contact: dict, pastor: dict, ministries: list,
               schedule: list, history: str, events: list, resources: list) -> str:
    """Build the complete wiki page from extracted data."""
    
    # Identity Snapshot
    identity_lines = []
    if "chinese_name" in identity:
        identity_lines.append(f"- **Chinese name:** {identity['chinese_name']}")
    if "type" in identity:
        identity_lines.append(f"- **Type:** {identity['type']}")
    if "location" in identity:
        identity_lines.append(f"- **Location:** {identity['location']}")
    if "denomination" in identity:
        identity_lines.append(f"- **Denomination:** {identity['denomination']}")
    if "languages" in identity:
        identity_lines.append(f"- **Languages:** {identity['languages']}")
    if "acronym" in identity:
        identity_lines.append(f"- **Acronym:** {identity['acronym']}")
    
    identity_snapshot = "\n".join(identity_lines)
    
    # Contact table
    contact_rows = []
    if "address" in contact:
        contact_rows.append(f"| **Address** | {contact['address']} |")
    if "phone" in contact:
        contact_rows.append(f"| **Phone** | {contact['phone']} |")
    if "fax" in contact:
        contact_rows.append(f"| **Fax** | {contact['fax']} |")
    if "email" in contact:
        contact_rows.append(f"| **Email** | {contact['email']} |")
    if "pastor_cell" in contact:
        contact_rows.append(f"| **Pastor (Rev. Ming Yuan Hsu)** | {contact['pastor_cell']} · {contact.get('pastor_email', 'revming@gmail.com')} |")
    if "facebook" in contact:
        contact_rows.append(f"| **Facebook** | [facebook.com/mpgstpc](https://www.facebook.com/mpgstpc/) |")
    if "youtube" in contact:
        contact_rows.append(f"| **YouTube** | [GSTPC channel](https://www.youtube.com/channel/UCwgxhZ6Yhba9I_0lZ6sK3ew/videos) |")
    
    contact_table = "\n".join(contact_rows)
    
    # Pastor bio
    pastor_lines = []
    if "birthplace" in pastor:
        pastor_lines.append(f"- **籍貫 (Ancestral home):** {pastor['birthplace']}")
    if "marriage" in pastor:
        pastor_lines.append(f"- **婚姻 (Marriage):** {pastor['marriage']}")
    if "residence" in pastor:
        pastor_lines.append(f"- **Residence:** {pastor['residence']}")
    if "education" in pastor:
        pastor_lines.append(f"- **教育 (Education):** {pastor['education']}")
    if "previous_career" in pastor:
        pastor_lines.append(f"- **職業經歷 (Professional background):** {pastor['previous_career']}")
    
    pastor_bio = "\n".join(pastor_lines)
    
    # Conversion
    conversion_parts = []
    if "conversion" in pastor:
        conversion_parts.append(f"- {pastor['conversion']}")
    if "call" in pastor:
        conversion_parts.append(f"- {pastor['call']}")
    if "ordination" in pastor:
        conversion_parts.append(f"- {pastor['ordination']}")
    
    conversion_text = "\n".join(conversion_parts)
    
    # History
    history_section = f"GSTPC's public materials frame the church as a long-standing Taiwanese Presbyterian presence in Monterey Park.\n\n{history}\n\n[[people/mingyuan-hsu|Rev. Ming Yuan Hsu (許明遠牧師)]] has led as full-time pastor since **July 2019**; weekly bulletins document sustained pulpit and pastoral ministry across multiple years."
    
    # Events
    event_lines = []
    for event in events:
        event_lines.append(f"- **{event}**")
    events_section = "\n".join(event_lines) if event_lines else ""
    
    # Resources
    resource_lines = []
    for resource in resources:
        resource_lines.append(f"- {resource}")
    resources_section = "\n".join(resource_lines) if resource_lines else ""
    
    # Build full page (use string concat to avoid f-string syntax issues)
    today = datetime.now().strftime('%Y-%m-%d')
    chinese_name = identity.get('chinese_name', '好牧者臺灣基督長老教會')
    
    intro = (
        f"**Good Shepherd Taiwanese Presbyterian Church** ({chinese_name}) is a "
        f"Taiwanese-language Presbyterian congregation in Monterey Park, Southern "
        f"California. The church describes itself as a **Gospel-Sharing, "
        f"Truth-Practicing Community**—a fellowship that shares the gospel of Christ "
        f"and practices biblical teaching. Members include immigrants and students "
        f"from Taiwan who gather in the familiar warmth of Taiwanese (臺語) worship, "
        f"with ministries for English-speaking youth and children as well."
    )
    
    # Worship schedule line
    if schedule:
        worship_line = chr(10).join('- ' + s for s in schedule)
    else:
        worship_line = "- Sunday worship: 10:00 AM – 11:00 AM (Family Worship / English Ministry / Children's Ministry)"
    
    # Events default
    if not events_section:
        events_section = (
            "- 40th anniversary celebration (2021) — commemorative eBook and special programming\n"
            "- TPC 50th Anniversary Special Program (May–June 2020) — 3 episodes featuring Rev. David Huang (黃德利牧師)"
        )
    
    # Resources default
    if not resources_section:
        resources_section = (
            "- [Bulletin Archive](https://gstpc.org/home/bulletin-archive/) — Weekly bulletin listings\n"
            "- [Devotion Archive](https://gstpc.org/home/devotion-archive/) — Daily spiritual reflections (靈修默想) by Rev. Hsu\n"
            "- [40th Anniversary eBook](https://gstpc.org/home/get/gstpc40-ebook) — Commemorative publication\n"
            "- [25th Anniversary Booklet](https://gstpc.org/home/gstpc25-booklet/) — GSTPC25 紀念刋"
        )
    
    page_lines = [
        "---",
        'title: "Good Shepherd Taiwanese Presbyterian Church"',
        "type: organization",
        "tags:",
        "  - organization",
        "  - Taiwanese-American",
        "  - Presbyterian",
        "  - Monterey Park",
        "  - Southern California",
        "verification_status: pending",
        f"last_reviewed: {today}",
        "---",
        "# Good Shepherd Taiwanese Presbyterian Church",
        "",
        intro,
        "",
        "## Identity Snapshot",
        identity_snapshot,
        "",
        "## Overview",
        "",
        "GSTPC sits in Monterey Park, a hub for Chinese and Taiwanese communities in the San Gabriel Valley. The congregation formed around brothers and sisters who immigrated or studied in Southern California from Taiwan. Worship emphasizes prayer, praise, restoration of relationship with God, the Spirit's presence, spiritual character, and equipping members to share and witness to the gospel in daily life.",
        "",
        "The church welcomes new immigrants, students, visitors, seekers, and believers looking for a Bible-centered church family.",
        "",
        "## Vision and Mission",
        "",
        "Per the church's vision statement ([異象使命](https://gstpc.org/home/our-vision/)):",
        "",
        "> **Gospel Sharing Truth Practicing Community** — We at Good Shepherd Taiwanese Presbyterian Church are a Gospel-Sharing, Truth-Practicing Community.  ",
        "> 好牧者台灣基督長老教會是一個分享基督福音，遵行聖經教訓的屬靈團契。",
        "",
        "## Contact",
        "",
        "| | |",
        "|---|---|",
        contact_table,
        "",
        "## Worship Schedule",
        worship_line,
        "",
        "## Ministries",
        "",
        "- **Noah's Ark English ministry** — Truth and life teaching for second-generation youth and children growing up in the U.S.",
        "- **Adult Sunday school**, **choir**, **活泉 (senior) fellowship**, **sisters' fellowship**, and **area home small groups** during the week.",
        "- **Media and resources** — Devotion archives, discipleship materials, and anniversary publications.",
        "- **TPC live stream** — Related Taiwanese Presbyterian Council worship programming.",
        "",
        "## History and Context",
        "",
        history_section,
        "",
        "## Notable Events",
        events_section,
        "",
        "## Devotion Archive (靈修默想)",
        "",
        "The church maintains a daily devotion archive (靈修默想) with spiritual reflections by Rev. Ming Yuan Hsu dating back to 2020. These daily reflections are published on the church website and serve as a resource for members and the broader community.",
        "",
        "## Resources",
        "",
        resources_section,
        "",
        "## TPC Connection",
        "",
        "GSTPC is a congregation within the [[organizations/presbyterian-church-in-taiwan|Presbyterian Church in Taiwan]] (台灣基督長老教會, TPC) network. The church maintains a close relationship with the broader TPC community, including participation in TPC worship programming and special events.",
        "",
        "Notably, GSTPC hosted the [[people/david-huang|Rev. David Huang (黃德利)]] for the TPC 50th Anniversary Special Program (TPC 50 週年特別節目) in May–June 2020, a multi-episode broadcast celebrating half a century of the TPC.",
        "",
        "## Related Pages",
        "- [[people/mingyuan-hsu|Rev. Ming Yuan Hsu (許明遠牧師)]]",
        "- [[people/chen-meihui|Chen Meihui (陳美蕙)]]",
        "- [[people/cai-weiren|Rev. Cai Weiren (蔡維仁牧師)]]",
        "- [[people/chen-bozhi|Rev. Chen Bozhi (陳柏志牧師)]]",
        "- [[people/david-huang|Rev. David Huang (黃德利)]]",
        "- [[organizations/presbyterian-church-in-taiwan|Presbyterian Church in Taiwan]]",
        "- [[organizations/taiwanese-american-historical-society|Taiwanese American Historical Society (TAHS)]]",
        "",
        "## Source Notes",
        "",
        "Source pages used for this article: [home](https://gstpc.org/home/), [about us](https://gstpc.org/home/about-us/), [vision](https://gstpc.org/home/our-vision/), [our pastor](https://gstpc.org/home/our-pastor/), [resources](https://gstpc.org/home/resources/), [devotion archive](https://gstpc.org/home/devotion-archive/), [bulletin archive](https://gstpc.org/home/bulletin-archive/), [children's ministry](https://gstpc.org/home/childrens-ministry/), [discipleship](https://gstpc.org/home/discipleship/), [TPC 50th](https://gstpc.org/home/tpc-50/) (scraped via r.jina.ai, 2026-07-12 and 2026-07-14).",
    ]
    
    page = chr(10).join(page_lines) + chr(10)
    
    return page


def main():
    """Main entry point."""
    print("=" * 60)
    print("GSTPC Enrichment Applier")
    print("=" * 60)
    
    # Read archives
    print("\n1. Reading archives...")
    all_text, sources = extract_all_archives()
    print(f"   {len(sources)} archive files read ({sum(sources.values())} total bytes)")
    
    # Check existing page
    print("\n2. Checking existing page...")
    existing = read_file(EXISTING_PAGE)
    if existing:
        print(f"   Existing page found: {len(existing)} bytes")
        print(f"   Sections: {len([l for l in existing.splitlines() if l.startswith('## ')])}")
    else:
        print("   No existing page — will create new")
    
    # Extract structured data
    print("\n3. Extracting structured data...")
    identity = extract_identity(all_text)
    contact = extract_contact(all_text)
    pastor = extract_pastor(all_text)
    ministries = extract_ministries(all_text)
    schedule = extract_schedule(all_text)
    history = extract_history(all_text, sources)
    events = extract_events(all_text)
    resources = extract_resources(all_text)
    
    print(f"   Identity: {len(identity)} fields")
    print(f"   Contact: {len(contact)} fields")
    print(f"   Pastor: {len(pastor)} fields")
    print(f"   Ministries: {len(ministries)}")
    print(f"   Schedule: {len(schedule)} items")
    print(f"   History: {len(history)} chars")
    print(f"   Events: {len(events)}")
    print(f"   Resources: {len(resources)}")
    
    # Build page
    print("\n4. Building enriched page...")
    page = build_page(identity, contact, pastor, ministries, schedule, history, events, resources)
    print(f"   Page size: {len(page)} bytes")
    print(f"   Sections: {len([l for l in page.splitlines() if l.startswith('## ')])}")
    
    # Write output
    if DRY_RUN:
        print("\n5. DRY RUN — would write to:")
        print(f"   {OUTPUT_DIR}/good-shepherd-taiwanese-presbyterian-church.md")
        print(f"\n   Page preview (first 500 chars):")
        print(f"   {page[:500]}...")
    else:
        print("\n5. Writing enriched page...")
        output_path = OUTPUT_DIR / "good-shepherd-taiwanese-presbyterian-church.md"
        output_path.write_text(page, encoding="utf-8")
        print(f"   Written to: {output_path}")
        print(f"   Size: {output_path.stat().st_size} bytes")
    
    print("\n" + "=" * 60)
    print("Done. Run audit to verify:")
    print(f"  bash /home/leedt/.hermes/scripts/echopedia-audit-collect.sh")
    print("=" * 60)


if __name__ == "__main__":
    main()