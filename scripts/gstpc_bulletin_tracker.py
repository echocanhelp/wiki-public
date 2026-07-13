#!/usr/bin/env python3
"""
GSTPC Bulletin Tracker - Spark-based analysis of bulletin content.

Processes GSTPC web archive markdown files to extract:
- Weekly sermon topics
- Speaker/pastor information
- Timeline of ministry activities
- Cross-reference with Echopedia person pages

Usage:
    python3 gstpc_bulletin_tracker.py [--output-dir PATH]
"""

import os
import sys
import re
import json
from pathlib import Path
from datetime import datetime

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, regexp_extract, regexp_replace, lower, trim, count, when, lit
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType
    SPARK_AVAILABLE = True
except ImportError:
    print("ERROR: PySpark not available. Install with: pip3 install pyspark")
    sys.exit(1)

# Configuration
ECHOPEDIA_DIR = Path("/home/leedt/echo-system")
WEB_ARCHIVES_DIR = ECHOPEDIA_DIR / "knowledge" / "web-archives"
PEOPLE_DIR = ECHOPEDIA_DIR / "content" / "people"
ORGANIZATIONS_DIR = ECHOPEDIA_DIR / "content" / "organizations"
OUTPUT_DIR = ECHOPEDIA_DIR / "knowledge" / "research" / "gstpc-bulletin-tracker"

# Person name patterns
PERSON_PATTERNS = {
    "pastors": [
        r"Rev\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
        r"許明遠牧師",
        r"David\s+Huang",
        r"Min\s+Yuan\s+Hsu",
        r"Ming\s+Yuan\s+Hsu",
    ],
    "elders": [
        r"Elder\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
        r"長老\s+([A-Z][a-z]+)",
        r"Deng\s+Shuzhen",
        r"Shuzhen\s+Deng",
        r"Chen\s+Xialian",
        r"Xialian\s+Chen",
    ],
    "generic": [
        r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:牧師|Pastor|Rev\.)",
        r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:長老|Elder)",
    ]
}

def create_spark_session():
    """Create a Spark session with GPU support."""
    spark = SparkSession.builder \
        .appName("GSTPC-Bulletin-Tracker") \
        .config("spark.executor.memory", "4g") \
        .config("spark.driver.memory", "2g") \
        .config("spark.sql.shuffle.partitions", "4") \
        .config("spark.executor.cores", "2") \
        .config("spark.executor.instances", "2") \
        .getOrCreate()
    
    print(f"✅ Spark session created")
    print(f"   Version: {spark.version}")
    print(f"   Executors: {spark.sparkContext.getConf().get('spark.executor.instances', '1')}")
    print(f"   Memory: {spark.sparkContext.getConf().get('spark.executor.memory', '1g')}")
    
    return spark

def load_markdown_files(spark):
    """Load markdown files from web-archives/ as a DataFrame."""
    files = list(WEB_ARCHIVES_DIR.glob("gstpc-*.md"))
    if not files:
        print("No GSTPC markdown files found in web-archives/")
        return None
    
    print(f"\n📄 Loading {len(files)} GSTPC files...")
    
    # Create a list of (filename, content) tuples
    data = []
    for f in files:
        content = f.read_text()
        # Extract title from frontmatter
        title_match = re.search(r'title:\s*["\']?([^"\']+)["\']?', content)
        title = title_match.group(1) if title_match else f.name
        data.append((f.name, title, content, f.stat().st_size))
    
    # Create DataFrame
    schema = StructType([
        StructField("filename", StringType(), True),
        StructField("title", StringType(), True),
        StructField("content", StringType(), True),
        StructField("size", IntegerType(), True),
    ])
    
    df = spark.createDataFrame(data, schema)
    print(f"   ✅ Loaded {df.count()} files")
    return df

def extract_person_names(df):
    """Extract person names from bulletin content."""
    print("\n🔍 Extracting person names...")
    
    # For each file, extract names using regex patterns
    results = []
    for row in df.collect():
        filename = row["filename"]
        content = row["content"]
        
        # Extract pastor names
        pastors = []
        for pattern in PERSON_PATTERNS["pastors"]:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for m in matches:
                if m not in pastors:
                    pastors.append(m)
        
        # Extract elder names
        elders = []
        for pattern in PERSON_PATTERNS["elders"]:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for m in matches:
                if m not in elders:
                    elders.append(m)
        
        results.append({
            "filename": filename,
            "title": row["title"],
            "pastors": pastors,
            "elders": elders,
            "total_names": len(pastors) + len(elders),
        })
    
    # Create DataFrame
    results_df = spark.createDataFrame(results)
    print(f"   ✅ Extracted names from {results_df.count()} files")
    return results_df

def cross_reference_with_echopedia(df):
    """Cross-reference extracted names with Echopedia person pages."""
    print("\n📚 Cross-referencing with Echopedia...")
    
    # Load existing person page slugs
    if PEOPLE_DIR.exists():
        person_slugs = [f.stem for f in PEOPLE_DIR.glob("*.md")]
    else:
        person_slugs = []
    
    print(f"   📄 Found {len(person_slugs)} person pages in Echopedia")
    
    # Check which extracted names match existing pages
    matches = []
    for row in df.collect():
        filename = row["filename"]
        pastors = row["pastors"]
        elders = row["elders"]
        
        for name in pastors + elders:
            # Check if name matches any person page slug
            for slug in person_slugs:
                if name.lower() in slug.lower() or slug.lower() in name.lower():
                    matches.append({
                        "filename": filename,
                        "name": name,
                        "matched_slug": slug,
                        "type": "pastor" if name in pastors else "elder",
                    })
    
    if matches:
        matches_df = spark.createDataFrame(matches)
        print(f"   ✅ Found {matches_df.count()} matches between bulletin names and Echopedia pages")
        return matches_df
    else:
        print("   ⚠️ No matches found")
        return None

def generate_timeline(df):
    """Generate a timeline of bulletin activities."""
    print("\n📅 Generating timeline...")
    
    # Extract dates from filenames and content
    timeline = []
    for row in df.collect():
        filename = row["filename"]
        content = row["content"]
        
        # Try to extract date from filename (e.g., gstpc-bulletin-archive.md)
        date_match = re.search(r'(\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4})', filename)
        if date_match:
            date_str = date_match.group(1)
            timeline.append({
                "date": date_str,
                "filename": filename,
                "title": row["title"],
            })
    
    # If no dates in filenames, try content
    if not timeline:
        for row in df.collect():
            content = row["content"]
            date_matches = re.findall(r'(\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4})', content)
            if date_matches:
                timeline.append({
                    "date": date_matches[0],
                    "filename": row["filename"],
                    "title": row["title"],
                })
    
    if timeline:
        timeline_df = spark.createDataFrame(timeline)
        print(f"   ✅ Generated timeline with {timeline_df.count()} entries")
        return timeline_df
    else:
        print("   ⚠️ No dates found in files")
        return None

def generate_report(df, names_df, matches_df, timeline_df):
    """Generate a comprehensive report."""
    print("\n📊 Generating report...")
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    report_path = OUTPUT_DIR / "gstpc-bulletin-tracker-report.md"
    
    with open(report_path, "w") as f:
        f.write("# GSTPC Bulletin Tracker Report\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- Total files analyzed: {df.count()}\n")
        f.write(f"- Total person names extracted: {names_df.agg({'total_names': 'sum'}).collect()[0][0]}\n")
        if matches_df:
            f.write(f"- Matches with Echopedia: {matches_df.count()}\n")
        if timeline_df:
            f.write(f"- Timeline entries: {timeline_df.count()}\n")
        
        f.write("\n## Person Names Extracted\n\n")
        for row in names_df.collect():
            f.write(f"### {row['title']}\n\n")
            f.write(f"- **Pastors:** {', '.join(row['pastors']) if row['pastors'] else 'None'}\n")
            f.write(f"- **Elders:** {', '.join(row['elders']) if row['elders'] else 'None'}\n\n")
        
        if matches_df:
            f.write("## Matches with Echopedia\n\n")
            for row in matches_df.collect():
                f.write(f"- **{row['name']}** → `{row['matched_slug']}` (from {row['filename']})\n")
            f.write("\n")
        
        if timeline_df:
            f.write("## Timeline\n\n")
            for row in timeline_df.collect():
                f.write(f"- {row['date']}: {row['title']} ({row['filename']})\n")
            f.write("\n")
    
    print(f"   ✅ Report saved to {report_path}")
    return report_path

def main():
    """Main entry point."""
    print("=== GSTPC Bulletin Tracker ===\n")
    
    # Create Spark session
    spark = create_spark_session()
    
    try:
        # Load markdown files
        df = load_markdown_files(spark)
        if not df:
            return
        
        # Extract person names
        names_df = extract_person_names(df)
        
        # Cross-reference with Echopedia
        matches_df = cross_reference_with_echopedia(df)
        
        # Generate timeline
        timeline_df = generate_timeline(df)
        
        # Generate report
        report_path = generate_report(df, names_df, matches_df, timeline_df)
        
        print(f"\n✅ Complete! Report saved to {report_path}")
        
    finally:
        spark.stop()
        print("✅ Spark session stopped")

if __name__ == "__main__":
    main()