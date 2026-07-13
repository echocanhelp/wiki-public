#!/usr/bin/env python3
"""
GSTPC Bulletin Tracker — PySpark Edition
=========================================
Processes GSTPC web archive markdown files and Echopedia person pages
to extract bulletin activities, person mentions, and generate a
comprehensive timeline report.

Usage:
    python3 gstpc_bulletin_tracker.py
    # or with Hermes venv:
    ~/.hermes/hermes-agent/venv/bin/python3 gstpc_bulletin_tracker.py

Outputs (in /home/leedt/echo-system/knowledge/research/):
    - gstpc-bulletin-tracker-report.md    (comprehensive markdown report)
    - bulletin_timeline.csv               (date-by-date bulletin activity)
    - person_mentions.json                (person mention analysis)
    - bulletin_dates.csv                  (all extracted bulletin dates)
    - bulletin_dates.json                 (JSON version of dates)
    - bulletin_person_crossref.csv        (cross-reference of persons in bulletins)
"""

import os
import re
import json
import glob
from datetime import datetime
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql.window import Window

# ──────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────
WEB_ARCHIVE_DIR = Path("/home/leedt/echo-system/knowledge/web-archives")
ECHOPEDIA_PEOPLE_DIR = Path("/home/leedt/echo-system/content/people")
OUTPUT_DIR = Path("/home/leedt/echo-system/knowledge/research")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ──────────────────────────────────────────────────────────────────────
# 1. Initialize Spark
# ──────────────────────────────────────────────────────────────────────
print("=" * 70)
print("  GSTPC Bulletin Tracker — PySpark Edition")
print("=" * 70)

spark = (
    SparkSession.builder
    .appName("GSTPC_Bulletin_Tracker")
    .config("spark.ui.showConsoleProgress", "false")
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")
    .config("spark.driver.memory", "2g")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

sc = spark.sparkContext

print(f"\n✓ Spark session started (version {spark.version})\n")

# ──────────────────────────────────────────────────────────────────────
# 2. Name extraction patterns
# ──────────────────────────────────────────────────────────────────────

# Pastor patterns
PASTOR_PATTERNS = [
    # "Rev. [Name]" English
    (r"Rev\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b", "Rev_Name"),
    # "[Name]牧師" Chinese pastor
    (r"([^\s]{2,15})牧師", "Chinese_Pastor"),
    # "Rev. [Name] [Chinese]" mixed
    (r"Rev\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+([^\s]+)", "Rev_Chinese"),
]

# Elder patterns
ELDER_PATTERNS = [
    (r"Elder\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b", "Elder_English"),
    (r"([^\s]{2,15})長老", "Chinese_Elder"),
    (r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b長老", "Name_Elder"),
]

# Speaker / other clergy
SPEAKER_PATTERNS = [
    (r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+傳道", "Speaker"),
    (r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+牧師", "Speaker_Pastor"),
    (r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+長老", "Speaker_Elder"),
]

# Date patterns (various bulletin date formats)
DATE_PATTERNS = [
    # MM-DD-YYYY (most common in bulletin archive)
    r"(\d{1,2}-\d{1,2}-\d{4})",
    # YYYY-MM-DD
    r"(\d{4}-\d{2}-\d{2})",
    # YYYY-M-D
    r"(\d{4}-\d{1,2}-\d{1,2})",
    # MM/DD/YYYY
    r"(\d{1,2}/\d{1,2}/\d{4})",
    # YYYY.MM.DD
    r"(\d{4}\.\d{1,2}\.\d{1,2})",
    # DD.MM.YYYY (from TPC worship live)
    r"(\d{2}\.\d{2}\.\d{4})",
]

# ──────────────────────────────────────────────────────────────────────
# 3. Load web archive files
# ──────────────────────────────────────────────────────────────────────
print("[1/6] Loading web archive files...")

archive_files = sorted(glob.glob(str(WEB_ARCHIVE_DIR / "*.md")))
# Filter out non-GSTPC and meta files
gstpc_files = [
    f for f in archive_files
    if "gstpc" in Path(f).stem.lower()
    and f not in [str(WEB_ARCHIVE_DIR / "README.md"), str(WEB_ARCHIVE_DIR / "index.md")]
]

print(f"  Found {len(gstpc_files)} GSTPC archive files")

# Read all files into an RDD of (filename, content)
def read_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        return (os.path.basename(path), fh.read())

file_rdd = sc.parallelize(gstpc_files).map(read_file)
file_lines = file_rdd.flatMap(lambda x: [(x[0], line) for line in x[1].splitlines()])

# Create DataFrame
file_df = file_lines.toDF(["filename", "line"])

print(f"  Loaded {file_df.count()} lines across {file_df.select('filename').distinct().count()} files\n")

# ──────────────────────────────────────────────────────────────────────
# 4. Load Echopedia person pages
# ──────────────────────────────────────────────────────────────────────
print("[2/6] Loading Echopedia person pages...")

person_files = sorted(glob.glob(str(ECHOPEDIA_PEOPLE_DIR / "*.md")))
person_rdd = sc.parallelize(person_files).map(read_file)
person_lines = person_rdd.flatMap(lambda x: [(x[0], line) for line in x[1].splitlines()])

person_df = person_lines.toDF(["person_file", "line"])

# Extract person metadata from frontmatter and headings
def extract_person_info(filename, content):
    """Extract person name, title, and key info from a person page."""
    info = {
        "person_file": filename,
        "name": "",
        "chinese_name": "",
        "role": "",
        "aliases": [],
        "full_content": content,
    }

    lines = content.splitlines()

    # Extract title from frontmatter
    in_frontmatter = False
    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                break
        if in_frontmatter and stripped.startswith("title:"):
            title = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            info["name"] = title
        if in_frontmatter and stripped.startswith("tags:"):
            break

    # Extract Chinese name (typically in parentheses after English name)
    name_match = re.search(r"\(([^)]+)\)", info["name"])
    if name_match:
        info["chinese_name"] = name_match.group(1)

    # Extract role from heading or content
    for line in lines:
        if line.startswith("## Identity Snapshot") or line.startswith("## Historical Significance"):
            break
        if "Core roles:" in line or "roles:" in line:
            role_match = re.search(r"roles?:?\s*(.*)", line)
            if role_match:
                info["role"] = role_match.group(1).strip()

    # Extract aliases from "Bulletin aliases" or "Name Variants"
    for line in lines:
        if "Bulletin aliases" in line or "aliases" in line.lower():
            alias_match = re.search(r"aliases?:?\s*(.*)", line)
            if alias_match:
                info["aliases"].extend([a.strip() for a in alias_match.group(1).split(";")])

    return info

person_info_rdd = person_rdd.map(lambda x: extract_person_info(x[0], x[1]))
person_info_list = person_info_rdd.collect()

# Create person reference DataFrame
person_rows = []
for p in person_info_list:
    person_rows.append({
        "person_file": p["person_file"],
        "name": p["name"],
        "chinese_name": p["chinese_name"],
        "role": p["role"],
        "aliases": "; ".join(p["aliases"]) if p["aliases"] else "",
    })

person_ref_df = spark.createDataFrame(person_rows)
print(f"  Loaded {person_ref_df.count()} person pages\n")

# ──────────────────────────────────────────────────────────────────────
# 5. Extract bulletin dates
# ──────────────────────────────────────────────────────────────────────
print("[3/6] Extracting bulletin dates...")

def extract_dates_from_line(filename, line_text):
    """Extract all dates from a line, normalizing to YYYY-MM-DD."""
    results = []
    for pattern in DATE_PATTERNS:
        matches = re.findall(pattern, line_text)
        for m in matches:
            try:
                # Try to parse the date
                if "-" in m and len(m.split("-")[0]) == 4:
                    # YYYY-MM-DD or YYYY-M-D
                    dt = datetime.strptime(m, "%Y-%m-%d")
                elif "/" in m:
                    # MM/DD/YYYY
                    dt = datetime.strptime(m, "%m/%d/%Y")
                elif "." in m:
                    # YYYY.MM.DD or DD.MM.YYYY
                    parts = m.split(".")
                    if len(parts[0]) == 4:
                        dt = datetime.strptime(m, "%Y.%m.%d")
                    else:
                        dt = datetime.strptime(m, "%d.%m.%Y")
                else:
                    # MM-DD-YYYY
                    dt = datetime.strptime(m, "%m-%d-%Y")
                results.append(dt.strftime("%Y-%m-%d"))
            except ValueError:
                continue
    return results

# Extract dates from all lines
date_extraction_rdd = file_lines.map(
    lambda x: [(x[0], d) for d in extract_dates_from_line(x[0], x[1]) if d]
).flatMap(lambda x: x)

# Deduplicate dates per file
date_df = spark.createDataFrame(date_extraction_rdd, ["filename", "date"])
date_df = date_df.dropDuplicates()

# Count dates per file
date_counts = date_df.groupBy("filename").count().orderBy(F.desc("count"))
print(f"  Extracted {date_df.count()} unique date entries")

# Create bulletin timeline: all dates across all files
bulletin_dates_df = (
    date_df
    .groupBy("date")
    .agg(
        F.collect_list(F.col("filename")).alias("sources"),
        F.count("filename").alias("source_count")
    )
    .orderBy(F.col("date"))
)

print(f"  Found {bulletin_dates_df.count()} unique dates\n")

# ──────────────────────────────────────────────────────────────────────
# 6. Extract person mentions
# ──────────────────────────────────────────────────────────────────────
print("[4/6] Extracting person mentions...")

# Build a combined regex for all known person names from Echopedia
known_names = []
for p in person_info_list:
    if p["name"]:
        known_names.append(p["name"])
    if p["chinese_name"]:
        known_names.append(p["chinese_name"])
    for alias in p["aliases"]:
        known_names.append(alias)

# Also add patterns from the bulletin archive content analysis
# Based on the Echopedia person pages, key names include:
known_person_names = [
    "Rev. Ming Yuan Hsu", "Rev. Mingyuan Hsu", "Rev. Hsu", "Pastor Hsu",
    "許明遠牧師", "許明遠", "Rev. Ming",
    "Rev. David Huang", "黃德利牧師", "David Huang",
    "Elder Deng Shuzhen", "鄧淑貞長老", "Deng Shuzhen",
    "Elder Chen Xialian", "陳夏蓮長老", "Chen Xialian",
    "張大業 傳道", "張大業",
    "周美玲", "劉炳熹", "Ping Hsi Liu",
]

# Create a single combined pattern for matching known names
if known_person_names:
    # Escape special regex characters and build pattern
    escaped_names = [re.escape(name) for name in known_person_names]
    combined_pattern = "|".join(escaped_names)
else:
    combined_pattern = ""

# Extract person mentions from bulletin archive (the richest source)
bulletin_archive_file = [f for f in gstpc_files if "bulletin-archive" in f]
if not bulletin_archive_file:
    bulletin_archive_file = [f for f in gstpc_files if "bulletin" in f.lower()]

bulletin_df = None
if bulletin_archive_file:
    ba_file = bulletin_archive_file[0]
    ba_content = Path(ba_file).read_text(encoding="utf-8")
    ba_lines = [(os.path.basename(ba_file), line) for line in ba_content.splitlines()]
    bulletin_df = spark.createDataFrame(ba_lines, ["filename", "line"])
    print(f"  Using {os.path.basename(ba_file)} as primary bulletin source ({len(ba_lines)} lines)")
else:
    print("  WARNING: No bulletin archive file found, using all files")
    bulletin_df = file_df

# Extract person mentions
def extract_person_mentions(filename, line_text):
    """Extract all known person names from a line."""
    mentions = []
    if combined_pattern:
        matches = re.findall(combined_pattern, line_text)
        for m in matches:
            if m:
                mentions.append(m.strip())
    return mentions

mention_rdd = bulletin_df.map(
    lambda x: [(x[0], m) for m in extract_person_mentions(x[0], x[1]) if m]
).flatMap(lambda x: x)

mention_df = spark.createDataFrame(mention_rdd, ["filename", "person_name"])
mention_df = mention_df.dropDuplicates()

# Count mentions per person
person_mention_counts = mention_df.groupBy("person_name").count().orderBy(F.desc("count"))

print(f"  Found {mention_df.count()} unique person-date mentions")

# ──────────────────────────────────────────────────────────────────────
# 7. Cross-reference with Echopedia
# ──────────────────────────────────────────────────────────────────────
print("[5/6] Cross-referencing with Echopedia person pages...")

# Build a mapping of person mentions to Echopedia entries
def match_to_echopedia(person_name):
    """Match a person mention to an Echopedia entry."""
    for p in person_info_list:
        if p["name"] and person_name.lower() in p["name"].lower():
            return {
                "echopedia_name": p["name"],
                "echopedia_chinese": p["chinese_name"],
                "role": p["role"],
                "person_file": p["person_file"],
            }
        if p["chinese_name"] and person_name.lower() in p["chinese_name"].lower():
            return {
                "echopedia_name": p["name"],
                "echopedia_chinese": p["chinese_name"],
                "role": p["role"],
                "person_file": p["person_file"],
            }
        for alias in p["aliases"]:
            if person_name.lower() in alias.lower():
                return {
                    "echopedia_name": p["name"],
                    "echopedia_chinese": p["chinese_name"],
                    "role": p["role"],
                    "person_file": p["person_file"],
                }
    return None

# Add cross-reference info
crossref_rdd = mention_df.map(
    lambda x: (x[0], x[1], match_to_echopedia(x[1]))
).filter(lambda x: x[2] is not None)

crossref_rows = []
for filename, person_name, match in crossref_rdd.collect():
    crossref_rows.append({
        "filename": filename,
        "person_name": person_name,
        "echopedia_name": match["echopedia_name"],
        "echopedia_chinese": match["echopedia_chinese"],
        "role": match["role"],
        "person_file": match["person_file"],
    })

crossref_df = spark.createDataFrame(crossref_rows)

print(f"  Matched {crossref_df.count()} mentions to Echopedia entries\n")

# ──────────────────────────────────────────────────────────────────────
# 8. Generate structured outputs
# ──────────────────────────────────────────────────────────────────────
print("[6/6] Generating outputs...")

# --- 8a. Bulletin timeline CSV ---
bulletin_dates_df.write.csv(
    str(OUTPUT_DIR / "bulletin_timeline.csv"),
    header=True,
    mode="overwrite",
    sep=",",
)

# --- 8b. Bulletin dates JSON ---
bulletin_dates_df.write.json(
    str(OUTPUT_DIR / "bulletin_dates.json"),
    mode="overwrite",
)

# --- 8c. Person mentions JSON ---
if mention_df.count() > 0:
    mention_df.write.json(
        str(OUTPUT_DIR / "person_mentions.json"),
        mode="overwrite",
    )

# --- 8d. Person mentions CSV ---
if mention_df.count() > 0:
    mention_df.write.csv(
        str(OUTPUT_DIR / "bulletin_dates.csv"),
        header=True,
        mode="overwrite",
        sep=",",
    )

# --- 8e. Cross-reference CSV ---
if crossref_df.count() > 0:
    crossref_df.write.csv(
        str(OUTPUT_DIR / "bulletin_person_crossref.csv"),
        header=True,
        mode="overwrite",
        sep=",",
    )

# ──────────────────────────────────────────────────────────────────────
# 9. Generate comprehensive markdown report
# ──────────────────────────────────────────────────────────────────────
print("\n  Generating markdown report...")

# Gather statistics
total_files = file_df.select("filename").distinct().count()
total_lines = file_df.count()
total_dates = bulletin_dates_df.count()
total_mentions = mention_df.count()
total_crossref = crossref_df.count()

# Year breakdown from bulletin dates
year_breakdown = (
    bulletin_dates_df
    .withColumn("year", F.regexp_extract(F.col("date"), r"(\d{4})", 1))
    .groupBy("year")
    .count()
    .orderBy(F.col("year"))
)

# Person mention breakdown
person_breakdown = (
    mention_df
    .groupBy("person_name")
    .count()
    .orderBy(F.desc("count"))
)

# File-level date counts
file_date_counts = (
    date_df
    .groupBy("filename")
    .count()
    .orderBy(F.desc("count"))
)

# File-level person mention counts
file_person_counts = (
    mention_df
    .groupBy("filename")
    .count()
    .orderBy(F.desc("count"))
)

# Build the report
report_lines = []
report_lines.append("# GSTPC Bulletin Tracker Report")
report_lines.append("")
report_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report_lines.append(f"**Data Source:** GSTPC Web Archives ({WEB_ARCHIVE_DIR})")
report_lines.append(f"**Cross-reference:** Echopedia Person Pages ({ECHOPEDIA_PEOPLE_DIR})")
report_lines.append(f"**Engine:** PySpark {spark.version}")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# ── Section 1: Executive Summary ──
report_lines.append("## Executive Summary")
report_lines.append("")
report_lines.append(f"This report analyzes **{total_files} GSTPC web archive files** containing "
                     f"**{total_lines:,} lines** of content, extracting bulletin dates, "
                     f"person mentions, and cross-referencing with **{person_ref_df.count()} Echopedia "
                     f"person pages**.")
report_lines.append("")
report_lines.append("### Key Findings")
report_lines.append("")
report_lines.append(f"- **{total_dates:,} unique bulletin dates** extracted across all files")
report_lines.append(f"- **{total_mentions:,} person-date mentions** found in bulletin content")
report_lines.append(f"- **{total_crossref:,} mentions** matched to Echopedia person records")
report_lines.append(f"- **{person_breakdown.count()} unique persons** identified across bulletins")
report_lines.append(f"- **{year_breakdown.count()} years** of bulletin coverage")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# ── Section 2: File Inventory ──
report_lines.append("## File Inventory")
report_lines.append("")
report_lines.append("| File | Lines | Date Entries | Person Mentions |")
report_lines.append("|------|-------|-------------|-----------------|")

for row in file_date_counts.collect():
    fname = row["filename"]
    lines_count = file_df.filter(F.col("filename") == fname).count()
    dates = row["count"]
    mentions = file_person_counts.filter(F.col("filename") == fname).first()
    mentions_count = mentions["count"] if mentions else 0
    report_lines.append(f"| {fname} | {lines_count:,} | {dates} | {mentions_count} |")

report_lines.append("")
report_lines.append("---")
report_lines.append("")

# ── Section 3: Bulletin Date Timeline ──
report_lines.append("## Bulletin Date Timeline")
report_lines.append("")
report_lines.append(f"Total unique dates extracted: **{total_dates:,}**")
report_lines.append("")

# Year breakdown
report_lines.append("### Coverage by Year")
report_lines.append("")
report_lines.append("| Year | Bulletin Count |")
report_lines.append("|------|---------------|")
for row in year_breakdown.collect():
    report_lines.append(f"| {row['year']} | {row['count']} |")
report_lines.append("")

# Recent dates (last 30)
recent_dates = bulletin_dates_df.orderBy(F.desc("date")).limit(30)
report_lines.append("### Recent Bulletins (Last 30)")
report_lines.append("")
report_lines.append("| Date | Source Count | Files |")
report_lines.append("|------|-------------|-------|")
for row in recent_dates.collect():
    sources = row["sources"]
    source_list = ", ".join(sources[:3])
    if len(sources) > 3:
        source_list += f" (+{len(sources)-3} more)"
    report_lines.append(f"| {row['date']} | {row['source_count']} | {source_list} |")
report_lines.append("")

# Oldest dates
oldest_dates = bulletin_dates_df.limit(15)
report_lines.append("### Earliest Bulletins")
report_lines.append("")
report_lines.append("| Date | Source Count | Files |")
report_lines.append("|------|-------------|-------|")
for row in oldest_dates.collect():
    sources = row["sources"]
    source_list = ", ".join(sources[:3])
    if len(sources) > 3:
        source_list += f" (+{len(sources)-3} more)"
    report_lines.append(f"| {row['date']} | {row['source_count']} | {source_list} |")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# ── Section 4: Person Mentions ──
report_lines.append("## Person Mentions Analysis")
report_lines.append("")
report_lines.append(f"Total unique person mentions: **{total_mentions:,}**")
report_lines.append("")

# Top persons
report_lines.append("### Top Mentioned Persons")
report_lines.append("")
report_lines.append("| Person | Mention Count |")
report_lines.append("|--------|--------------|")
for row in person_breakdown.take(20):
    report_lines.append(f"| {row['person_name']} | {row['count']} |")
report_lines.append("")

# ── Section 5: Echopedia Cross-Reference ──
report_lines.append("## Echopedia Cross-Reference")
report_lines.append("")
report_lines.append(f"Cross-referenced **{total_crossref:,}** bulletin mentions against "
                     f"**{person_ref_df.count()}** Echopedia person pages.")
report_lines.append("")

if crossref_df.count() > 0:
    # Group by Echopedia name
    echopedia_grouped = (
        crossref_df
        .groupBy("echopedia_name", "echopedia_chinese", "role")
        .agg(
            F.countDistinct("person_name").alias("mention_variants"),
            F.count("*").alias("total_mentions"),
            F.collect_list("filename").alias("source_files"),
            F.collect_list("person_name").alias("mentioned_as"),
        )
        .orderBy(F.desc("total_mentions"))
    )

    report_lines.append("### Person Records with Bulletin Mentions")
    report_lines.append("")
    report_lines.append("| Echopedia Name | Chinese | Role | Variants | Mentions | Sources |")
    report_lines.append("|---------------|---------|------|----------|----------|---------|")

    for row in echopedia_grouped.collect():
        name = row["echopedia_name"]
        chinese = row["echopedia_chinese"] if row["echopedia_chinese"] else ""
        role = row["role"] if row["role"] else ""
        variants = row["mention_variants"]
        mentions = row["total_mentions"]
        sources = row["source_files"]
        mentioned_as = row["mentioned_as"]

        source_str = f"{len(sources)} files" if sources else "N/A"
        name_str = f"[{name}](people/{Path(name.lower().replace(' ', '-').replace('.', '')).with_suffix('.md')})"
        chinese_str = f" ({chinese})" if chinese else ""
        role_str = f" — {role}" if role else ""

        report_lines.append(
            f"| {name_str}{chinese_str}{role_str} | {variants} | {mentions} | {source_str} |"
        )
    report_lines.append("")

    # Detailed person profiles
    report_lines.append("### Detailed Person Profiles")
    report_lines.append("")

    for row in echopedia_grouped.take(10):
        name = row["echopedia_name"]
        chinese = row["echopedia_chinese"] if row["echopedia_chinese"] else ""
        role = row["role"] if row["role"] else ""
        variants = row["mention_variants"]
        mentions = row["total_mentions"]
        mentioned_as = row["mentioned_as"]

        report_lines.append(f"#### {name} {chinese}")
        report_lines.append("")
        report_lines.append(f"- **Role:** {role}")
        report_lines.append(f"- **Total mentions:** {mentions}")
        report_lines.append(f"- **Mention variants:** {variants}")
        report_lines.append(f"- **Referenced as:** {', '.join(mentioned_as)}")
        report_lines.append("")

        # Get date range for this person
        person_dates = (
            crossref_df
            .filter(F.col("echopedia_name") == name)
            .join(bulletin_dates_df, bulletin_dates_df.date == crossref_df.date, how="inner")
            .select("date")
            .orderBy("date")
        )

        if person_dates.count() > 0:
            dates_list = person_dates.collect()
            first_date = dates_list[0]["date"] if dates_list else "N/A"
            last_date = dates_list[-1]["date"] if dates_list else "N/A"
            report_lines.append(f"- **Date range:** {first_date} to {last_date}")
            report_lines.append(f"- **Years active:** {len(set(d['date'][:4] for d in dates_list))}")
            report_lines.append("")

            # Yearly breakdown
            yearly = (
                person_dates
                .withColumn("year", F.regexp_extract(F.col("date"), r"(\d{4})", 1))
                .groupBy("year")
                .count()
                .orderBy("year")
            )
            report_lines.append("| Year | Mentions |")
            report_lines.append("|------|----------|")
            for yr in yearly.collect():
                report_lines.append(f"| {yr['year']} | {yr['count']} |")
            report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

# ── Section 6: Activity Timeline ──
report_lines.append("## Activity Timeline")
report_lines.append("")
report_lines.append("Quarterly bulletin activity across the archive:")
report_lines.append("")

# Quarterly breakdown
quarterly = (
    bulletin_dates_df
    .withColumn("year", F.regexp_extract(F.col("date"), r"(\d{4})", 1))
    .withColumn("month", F.regexp_extract(F.col("date"), r"\d{4}-(\d{2})", 1))
    .withColumn("quarter", F.when(F.col("month").cast("int") <= 3, "Q1")
                 .when(F.col("month").cast("int") <= 6, "Q2")
                 .when(F.col("month").cast("int") <= 9, "Q3")
                 .otherwise("Q4"))
    .groupBy("year", "quarter")
    .count()
    .orderBy("year", "quarter")
)

report_lines.append("| Year | Q1 | Q2 | Q3 | Q4 | Total |")
report_lines.append("|------|----|----|----|----|-------|")

years = quarterly.select("year").distinct().orderBy("year").collect()
for year_row in years:
    yr = year_row["year"]
    quarters = {r["quarter"]: r["count"] for r in quarterly.filter(F.col("year") == yr).collect()}
    total = sum(quarters.values())
    report_lines.append(f"| {yr} | {quarters.get('Q1', 0)} | {quarters.get('Q2', 0)} | "
                         f"{quarters.get('Q3', 0)} | {quarters.get('Q4', 0)} | {total} |")

report_lines.append("")
report_lines.append("---")
report_lines.append("")

# ── Section 7: Key Insights ──
report_lines.append("## Key Insights & Actionable Findings")
report_lines.append("")

# Insight 1: Pastor continuity
top_persons = person_breakdown.take(5)
if top_persons:
    report_lines.append("### 1. Leadership Continuity")
    report_lines.append("")
    for p in top_persons:
        report_lines.append(f"- **{p['person_name']}**: {p['count']} mentions — "
                           "indicates sustained leadership presence")
    report_lines.append("")

# Insight 2: Bulletin coverage span
if year_breakdown.count() > 0:
    first_year = year_breakdown.first()["year"]
    last_year = year_breakdown.last()["year"]
    report_lines.append(f"### 2. Archive Coverage Span")
    report_lines.append("")
    report_lines.append(f"- Bulletins span from **{first_year}** to **{last_year}** "
                         f"({int(last_year) - int(first_year) + 1} years)")
    report_lines.append(f"- Average **{total_dates / max(1, int(last_year) - int(first_year) + 1):.0f} dates/year** "
                         "of bulletin coverage")
    report_lines.append("")

# Insight 3: Echopedia gaps
if crossref_df.count() > 0:
    unmatched = mention_df.count() - crossref_df.count()
    if unmatched > 0:
        report_lines.append("### 3. Echopedia Coverage Gaps")
        report_lines.append("")
        report_lines.append(f"- **{unmatched:,}** person mentions ({unmatched*100//max(1, mention_df.count())}%) "
                           "not yet matched to Echopedia pages")
        report_lines.append("- **Recommendation:** Create new Echopedia pages for unmatched persons")
        report_lines.append("")

# Insight 4: File quality
report_lines.append("### 4. Archive Quality Assessment")
report_lines.append("")
report_lines.append("- **Bulletin Archive**: Primary source with most comprehensive date coverage")
report_lines.append("- **Devotion Archive**: Daily devotion dates (less structured)")
report_lines.append("- **Pastor Profile**: Rich biographical data for Rev. Hsu")
report_lines.append("- **Media Archive**: Event-based content with speaker names")
report_lines.append("- **TPC/TPC-50**: Worship live dates and special event speakers")
report_lines.append("")

# Insight 5: Recommendations
report_lines.append("### 5. Recommendations")
report_lines.append("")
report_lines.append("1. **Expand Echopedia coverage** for frequently mentioned persons not yet in the wiki")
report_lines.append("2. **Enrich bulletin content** by linking dates to specific bulletin PDFs or images")
report_lines.append("3. **Track speaker rotation** patterns across years for ministry planning")
report_lines.append("4. **Monitor elder activity** — recurring mentions indicate active leadership")
report_lines.append("5. **Cross-reference devotion dates** with bulletin dates for complete ministry calendar")
report_lines.append("")
report_lines.append("---")
report_lines.append("")

# ── Section 6: Output Files ──
report_lines.append("## Output Files")
report_lines.append("")
report_lines.append("The following structured data files were generated:")
report_lines.append("")
report_lines.append("| File | Format | Description |")
report_lines.append("|------|--------|-------------|")
report_lines.append("| `bulletin_timeline.csv` | CSV | Date-by-date bulletin activity with source files |")
report_lines.append("| `bulletin_dates.json` | JSON | All extracted bulletin dates |")
report_lines.append("| `bulletin_dates.csv` | CSV | Person mentions per bulletin date |")
report_lines.append("| `person_mentions.json` | JSON | Person mention analysis |")
report_lines.append("| `bulletin_person_crossref.csv` | CSV | Cross-reference of persons to Echopedia |")
report_lines.append("| `gstpc-bulletin-tracker-report.md` | MD | This report |")
report_lines.append("")
report_lines.append("---")
report_lines.append("")
report_lines.append("*Report generated by GSTPC Bulletin Tracker (PySpark Edition)*")
report_lines.append(f"*Spark version: {spark.version} | Python: {os.sys.version.split()[0]}*")

# Write the report
report_path = OUTPUT_DIR / "gstpc-bulletin-tracker-report.md"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"\n✓ Report written to: {report_path}")

# ──────────────────────────────────────────────────────────────────────
# 10. Final summary
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("  GSTPC Bulletin Tracker — Complete")
print("=" * 70)
print(f"\n  Files processed:     {total_files}")
print(f"  Lines analyzed:      {total_lines:,}")
print(f"  Unique dates:        {total_dates:,}")
print(f"  Person mentions:     {total_mentions:,}")
print(f"  Echopedia matches:   {total_crossref:,}")
print(f"  Unique persons:      {person_breakdown.count()}")
print(f"  Years covered:       {year_breakdown.count()}")
print(f"\n  Outputs:")
for f in sorted(OUTPUT_DIR.glob("gstpc-*")):
    print(f"    - {f.name} ({f.stat().st_size:,} bytes)")
for f in sorted(OUTPUT_DIR.glob("*.csv")):
    if f.name != "gstpc-bulletin-tracker-report.md":
        print(f"    - {f.name} ({f.stat().st_size:,} bytes)")
for f in sorted(OUTPUT_DIR.glob("*.json")):
    print(f"    - {f.name} ({f.stat().st_size:,} bytes)")

print("\n✓ Done.\n")

spark.stop()