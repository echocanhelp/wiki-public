#!/usr/bin/env python3
"""
P1 Link: Keep ## Works on person pages as a dossier, not a firehose.

Reads taiwanjustice-net priority-hits JSONL, groups by slug, and:

  1. Writes a CAPPED ## Works section (last 5 years, ≤8 titles/year, counts for
     the rest). Nightly cron must not dump 10k+ harvest hits onto a person page.
  2. Backlinks only the listed title hits (not the whole harvest).

Skip index pages. Do not treat body text as a title hit (no DOTALL).
Full-corpus Chinese-name scan is --scan-bodies only (off in cron).

Usage:
  python3 echopedia-person-works-linker.py --all
  python3 echopedia-person-works-linker.py --columnist chen-po-kong
  python3 echopedia-person-works-linker.py --dry-run --all

P5 media extension (people <-> works):
  Reads media/_manifest.json and, for each person whose page is referenced by a
  manifest entry's `entities` (people/<slug>.md), writes:
    1. A marked "## Echo Resonance 歲月有聲" media section on the person page:
       [[works/<slug>|name]] wikilinks + <audio> embeds + manifest disclaimer
       (never hardcoded). Marked region is idempotent.
    2. A works/<slug>.md page (if missing) carrying the paired
       <!-- media-section-start --> marker so scripts/echo-media-regen.py owns
       its media section afterwards.
  Usage:
  python3 echopedia-person-works-linker.py --media-only [--dry-run]
  python3 echopedia-person-works-linker.py --columnist leonard-hsu-jr --media
"""

import json
import os
import re
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Paths
REPO_ROOT = Path.home() / "echo-system"
HITS_FILE = REPO_ROOT / "knowledge/research/taiwanjustice-net-priority-hits.jsonl"
CONTENT_DIR = REPO_ROOT / "content"
PEOPLE_DIR = CONTENT_DIR / "people"
ARTICLES_DIR = CONTENT_DIR / "articles" / "taiwanjustice-net"
LOG_DIR = REPO_ROOT / "echopedia" / "logs"

# Columnist slugs that have person pages
COLUMNIST_SLUGS = [
    "chen-po-kong",      # 陳破空
    "chen-maoxiong",     # 陳茂雄
    "chen-zhaonan",      # 陳昭南
    "lin-baohua",        # 林保華
    "yu-jie",            # 余杰
    "fan-jiang-ti-ang",  # 范姜提昂
    "yang-ziqing",       # 楊子清
    "huang-diyin",       # 黃帝穎
    "he-qingxuan",       # 何清漣
    "liao-qingshan",     # 廖清山
    "jin-hegui",         # 金恆煒
    "ku-chuan-min",      # 辜寬敏
    "zeng-daoxiong",     # 曾道雄
    "li-xiaofeng",       # 李筱峰
    "hong-ya",           # 洪雅
    "chen-rijun",        # 陳日君
    "du-ao-cunfu",       # 獨傲村夫
]

# Additional contributor slugs with person pages
ADDITIONAL_SLUGS = [
    "tang-peili", "yang-yuanxun", "yang-yueqing", "li-jian",
    "nanfang-shuo", "wang-dan", "wang-shufen", "wei-jingsheng",
    "wu-lipei", "xia-ming", "ye-siya", "zhang-xinhui",
    "yuan-zhihui", "zheng-bingquan", "li-rongsong", "cai-shunyu",
    "cao-changqing", "chao-sile", "guan-renjian", "huang-yongcheng",
    "hu-ping", "kevin-lee", "bai-peiyu", "sang-pu", "shen-zizai",
    "ian-easton", "richard-d-fisher", "john-j-tkacik", "ryan-hass",
    "jiang-bai-xian", "gong-sun-le",
]

# TAHS member slugs — expanded from priority roster (LINE-verified + all members)
# These appear in articles but aren't columnists; they need Chinese name body search
TAHS_MEMBER_SLUGS = [
    "yang-jia-you", "leonard-hsu-jr", "franklin-ping-cheng",
    "freeman-huang", "phoenix-ko", "yi-sen-lee", "sunu-tsai",
    "tzetsai-eric-shen", "roger-tsai", "paul-chen", "john-yang",
    "linda-liu", "david-lee", "ken-wu", "rex-chen", "ashton-hsu",
    "albert-s-lai", "willy-pan", "chen-wenshi", "huang-gen-shen",
    "liao-shu-zong", "alan-thian", "gene-tsai", "xu-shihuan",
    "bai-weiwei", "becky-yang",
    # Publication-mention members
    "bai-peiyu", "cao-changqing", "zhang-xinhui", "chao-sile",
    "chen-bozhi", "chen-zhaonan", "chen-maoxiong", "chen-po-kong",
    "zheng-qinren", "zheng-wenlong", "jin-hegui", "du-ao-cunfu",
    "fan-jiang-ti-ang", "gong-sun-le", "he-qingxuan", "hu-ping",
    "huang-diyin", "huang-yongcheng", "guan-renjian", "li-xiaofeng",
    "li-jian", "liao-qingshan", "lin-baohua", "lin-rongsong",
    "nanfang-shuo", "sang-pu", "tang-peili", "zou-jingwen",
    "wang-qiaoling", "wang-dan", "wang-shufen", "wei-jingsheng",
    "wu-lipei", "xia-ming", "yang-yuanxun", "yang-yueqing",
    "yang-ziqing", "ye-siya", "yu-jie", "yuan-zhihui",
    "zheng-bingquan",
]

ALL_SLUGS = list(dict.fromkeys(COLUMNIST_SLUGS + ADDITIONAL_SLUGS + TAHS_MEMBER_SLUGS))

MAX_YEARS = 5
MAX_PER_YEAR = 8
MAX_BODY = 5

# Chinese name lookup for wikilinks
SLUG_TO_CHINESE = {
    "chen-po-kong": "陳破空",
    "chen-maoxiong": "陳茂雄",
    "chen-zhaonan": "陳昭南",
    "lin-baohua": "林保華",
    "yu-jie": "余杰",
    "fan-jiang-ti-ang": "范姜提昂",
    "yang-ziqing": "楊子清",
    "huang-diyin": "黃帝穎",
    "he-qingxuan": "何清漣",
    "liao-qingshan": "廖清山",
    "jin-hegui": "金恆煒",
    "ku-chuan-min": "辜寬敏",
    "zeng-daoxiong": "曾道雄",
    "li-xiaofeng": "李筱峰",
    "hong-ya": "洪雅",
    "chen-rijun": "陳日君",
    "du-ao-cunfu": "獨傲村夫",
    "tang-peili": "唐培理",
    "yang-yuanxun": "楊遠薰",
    "yang-yueqing": "楊月清",
    "li-jian": "李堅",
    "nanfang-shuo": "南方朔",
    "wang-dan": "王丹",
    "wang-shufen": "王淑芬",
    "wei-jingsheng": "魏景升",
    "wu-lipei": "吳立埔",
    "xia-ming": "小明",
    "ye-siya": "葉思雅",
    "zhang-xinhui": "張信惠",
    "yuan-zhihui": "袁志輝",
    "zheng-bingquan": "鄭炳全",
    "li-rongsong": "林榮松",
    "cai-shunyu": "蔡順宇",
    "cao-changqing": "曹長青",
    "chao-sile": "朝思樂",
    "guan-renjian": "管仁健",
    "huang-yongcheng": "黃永成",
    "hu-ping": "胡平",
    "kevin-lee": "Kevin Lee",
    "bai-peiyu": "白珮瑜",
    "sang-pu": "桑普",
    "shen-zizai": "沈子載",
    "ian-easton": "易思安",
    "richard-d-fisher": "費學禮",
    "john-j-tkacik": "譚慎格",
    "ryan-hass": "何瑞恩",
    "jiang-bai-xian": "江百顯",
    "gong-sun-le": "公孫樂",
    # TAHS founding members
    "yang-jia-you": "楊嘉猷",
    "becky-yang": "楊佩珊",
    "leonard-hsu-jr": "許景鴻",
    "franklin-ping-cheng": "程炳成",
    "wang-gui-rong": "王桂榮",
    "huang-gen-shen": "黃根深",
    "zhou-wei-lin": "周威霖",
    "zhou-shi": "周實",
    "chen-long": "陳隆",
    "hong-zhu-mei": "洪珠美",
    "liao-ji-chun": "廖述宗",
    "wang-ting-yi": "王廷宜",
}


def load_hits():
    """Load the priority-hits JSONL file."""
    hits = []
    with open(HITS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                hits.append(json.loads(line))
    return hits


def group_hits_by_slug(hits, scan_bodies=False):
    """Group hits by slug. Title vs body from JSONL `where` only.

    `--scan-bodies` is the expensive full-corpus Chinese-name walk. Cron must
    not do that: a DOTALL title regex previously classified every body mention
    as a title hit and blew ## Works to megabytes.
    """
    grouped = defaultdict(lambda: {"title": [], "body": []})

    for hit in hits:
        if hit.get("is_index"):
            continue
        for match in hit.get("matches", []):
            slug = match.get("slug")
            if slug and slug in ALL_SLUGS:
                where = match.get("where", [])
                if "title" in where:
                    grouped[slug]["title"].append(hit)
                elif "body" in where:
                    grouped[slug]["body"].append(hit)

    if not scan_bodies:
        return grouped

    founding_member_slugs = set(TAHS_MEMBER_SLUGS)
    chinese_to_slug = {}
    for slug in founding_member_slugs:
        chinese_name = SLUG_TO_CHINESE.get(slug)
        if chinese_name:
            chinese_to_slug[chinese_name] = slug

    articles_dir = CONTENT_DIR / "articles" / "taiwanjustice-net"
    if not articles_dir.exists():
        return grouped
    for article_file in articles_dir.rglob("*.md"):
        try:
            content = article_file.read_text(encoding="utf-8")
            rel_path = str(article_file.relative_to(REPO_ROOT))
            title_line = ""
            for line in content.splitlines()[:40]:
                if line.startswith("title:"):
                    title_line = line
                    break
            for chinese_name, slug in chinese_to_slug.items():
                if chinese_name not in content:
                    continue
                in_title = chinese_name in title_line
                hit = {
                    "path": rel_path,
                    "score": 1,
                    "title": title_line[6:].strip().strip('"').strip("'"),
                    "matches": [{
                        "slug": slug,
                        "where": ["title"] if in_title else ["body"],
                        "text": chinese_name,
                    }],
                }
                grouped[slug]["title" if in_title else "body"].append(hit)
        except (OSError, UnicodeDecodeError):
            continue
    return grouped


def extract_article_metadata(article_path):
    """Extract frontmatter metadata from an article markdown file."""
    path = REPO_ROOT / article_path
    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse frontmatter
    fm_match = re.match(r"^---\n(.*?)---\n", content, re.DOTALL)
    if not fm_match:
        return None

    fm = fm_match.group(1)
    fm_dict = {}
    for line in fm.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            fm_dict[key.strip()] = value.strip()

    title = fm_dict.get("title", "")
    post_date = fm_dict.get("post_date", "")
    source_url = fm_dict.get("source_url", "")
    archive_url = fm_dict.get("archive_url", "")

    # Extract date
    date_str = ""
    if post_date:
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", post_date)
        if date_match:
            date_str = date_match.group(1)

    # Extract year
    year = ""
    if date_str:
        year = date_str[:4]
    elif post_date:
        year_match = re.search(r"(\d{4})", post_date)
        if year_match:
            year = year_match.group(1)

    return {
        "title": title,
        "date": date_str,
        "year": year,
        "source_url": source_url,
        "archive_url": archive_url,
        "path": article_path,
        "filename": path.name,
        "content": content,
        "fm_match": fm_match,
        "fm_dict": fm_dict,
    }


def build_echopedia_article_link(article_path):
    """Build an echopedia wikilink from an article's content path.

    Converts content/articles/taiwanjustice-net/YEAR/FILENAME.md
    to [[articles/taiwanjustice-net/YEAR/FILENAME|Title]]

    Returns None if the article file doesn't exist on disk.
    """
    # article_path is relative to REPO_ROOT, e.g. "content/articles/taiwanjustice-net/2026/20260118105817_...md"
    full_path = REPO_ROOT / article_path
    if not full_path.exists():
        return None

    # Strip "content/" prefix and ".md" extension to get the echopedia path
    echo_path = article_path
    if echo_path.startswith("content/"):
        echo_path = echo_path[len("content/"):]
    if echo_path.endswith(".md"):
        echo_path = echo_path[:-3]

    return echo_path


def _year_from_path(path: str) -> str:
    m = re.search(r"/(\d{4})/", str(path).replace("\\", "/"))
    return m.group(1) if m else "Undated"


def _dedupe_hits(hits):
    seen = set()
    out = []
    for h in hits:
        p = h.get("path")
        if not p or p in seen:
            continue
        seen.add(p)
        out.append(h)
    return out


def listed_title_hits(title_articles):
    """Title hits that will appear in the capped Works list (for backlinks)."""
    titles = _dedupe_hits(title_articles)
    by_year = defaultdict(list)
    for article in titles:
        by_year[_year_from_path(article.get("path", ""))].append(article)
    years = sorted(by_year.keys(), reverse=True)[:MAX_YEARS]
    listed = []
    for year in years:
        arts = sorted(by_year[year], key=lambda x: x.get("path", ""), reverse=True)
        listed.extend(arts[:MAX_PER_YEAR])
    return listed


def generate_works_section(slug, title_articles, body_articles):
    """Dossier ## Works: counts + recent sample. Never dump the full harvest."""
    chinese_name = SLUG_TO_CHINESE.get(slug, slug)
    titles = _dedupe_hits(title_articles)
    title_paths = {h.get("path") for h in titles}
    bodies = [h for h in _dedupe_hits(body_articles) if h.get("path") not in title_paths]
    total_title = len(titles)
    total_body = len(bodies)

    by_year = defaultdict(list)
    for article in titles:
        by_year[_year_from_path(article.get("path", ""))].append(article)
    years = sorted(by_year.keys(), reverse=True)
    shown_years = years[:MAX_YEARS]
    omitted_n = sum(len(by_year[y]) for y in years[MAX_YEARS:])

    lines = [
        "",
        "## Works",
        "",
        (
            f"**{chinese_name}** — **{total_title}** title hits, **{total_body}** body mentions "
            f"in the taiwanjustice.net harvest. Listed: last {MAX_YEARS} years, "
            f"up to {MAX_PER_YEAR}/year. Full index: [[sources/taiwanjustice-net|taiwanjustice.net]]."
        ),
        "",
    ]
    for year in shown_years:
        arts = sorted(by_year[year], key=lambda x: x.get("path", ""), reverse=True)
        listed = arts[:MAX_PER_YEAR]
        extra = len(arts) - len(listed)
        lines.append(f"### {year} ({len(arts)})")
        lines.append("")
        for i, article in enumerate(listed, 1):
            path = article.get("path", "")
            title = article.get("title") or Path(path).stem
            echo_path = build_echopedia_article_link(path) if path else None
            if echo_path:
                lines.append(f"{i}. [[{echo_path}|{title}]]")
            else:
                lines.append(f"{i}. {title}")
        if extra:
            lines.append(f"- … {extra} more this year")
        lines.append("")
    if omitted_n:
        lines.append(f"Earlier years: **{omitted_n}** additional title hits (not listed).")
        lines.append("")
    if total_body:
        lines.append(f"### Body mentions ({total_body})")
        lines.append("")
        lines.append("See the source hub. Top mentions:")
        lines.append("")
        top = sorted(bodies, key=lambda x: x.get("score", 0), reverse=True)[:MAX_BODY]
        for i, article in enumerate(top, 1):
            path = article.get("path", "")
            title = article.get("title") or Path(path).stem
            echo_path = build_echopedia_article_link(path) if path else None
            if echo_path:
                lines.append(f"{i}. [[{echo_path}|{title}]]")
            else:
                lines.append(f"{i}. {title}")
        lines.append("")
    return "\n".join(lines) + "\n"


def add_works_to_person_page(slug, title_articles, body_articles, dry_run=False):
    """Add or update the ## Works section on a person page."""
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        print(f"  SKIP: {slug} — no person page exists at {page_path}")
        return False

    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_section = generate_works_section(slug, title_articles, body_articles)
    works_match = re.search(r"\n## Works\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if works_match:
        old = works_match.group(0).strip()
        if old == new_section.strip():
            return False
        content = content[:works_match.start()] + "\n" + new_section.lstrip("\n") + content[works_match.end():]
    else:
        if "## Source Notes" in content:
            content = content.replace("## Source Notes", new_section.lstrip("\n") + "\n## Source Notes", 1)
        elif "## Related Pages" in content:
            content = content.replace("## Related Pages", new_section.lstrip("\n") + "\n## Related Pages", 1)
        else:
            content = content.rstrip() + "\n" + new_section

    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"last_reviewed: \d{4}-\d{2}-\d{2}",
        f"last_reviewed: {today}",
        content,
        count=1,
    )

    if dry_run:
        print(f"  DRY-RUN: {slug} — would update {page_path}")
        return True

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  DONE: {slug} — {len(_dedupe_hits(title_articles))} title / {len(_dedupe_hits(body_articles))} body (capped list)")
    return True


def add_person_link_to_article(article_path, slug, dry_run=False):
    """Add a wikilink from an article back to the person page.

    Adds [[people/<slug>|Chinese Name]] to the article's frontmatter
    'authors' field or to the body as a first-mention link.
    """
    path = REPO_ROOT / article_path
    if not path.exists():
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has the wikilink
    wikilink = f"[[people/{slug}"
    if wikilink in content:
        return False

    chinese_name = SLUG_TO_CHINESE.get(slug, slug)
    full_wikilink = f"[[people/{slug}|{chinese_name}]]"

    # Try to add to frontmatter authors field
    if content.startswith("---"):
        fm_end = content.find("---\n", 5)
        if fm_end > 0:
            fm = content[:fm_end]
            if "authors:" in fm:
                # Add to existing authors list
                new_content = content.replace(
                    "authors:",
                    f"authors:\n  - {full_wikilink}",
                    1
                )
            else:
                # Add authors field after the last frontmatter line before ---
                # Insert before the closing ---
                new_fm = fm.rstrip() + f"\nauthors:\n  - {full_wikilink}\n"
                new_content = new_fm + content[fm_end:]

            if dry_run:
                return True

            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True

    return False


def process_columnist(slug, grouped_hits, dry_run=False):
    """Process a single columnist: update person page + link articles."""
    title_articles = grouped_hits.get(slug, {}).get("title", [])
    body_articles = grouped_hits.get(slug, {}).get("body", [])

    if not title_articles and not body_articles:
        print(f"  SKIP: {slug} — no hits found")
        return False

    # Update person page with Works section
    page_updated = add_works_to_person_page(slug, title_articles, body_articles, dry_run)

    articles_linked = 0
    for article in listed_title_hits(title_articles):
        if add_person_link_to_article(article["path"], slug, dry_run):
            articles_linked += 1

    return page_updated


def verify_person_page_links(slug):
    """Verify that all links in a person page's ## Works section are echopedia wikilinks.

    Returns a list of issues found (external URLs, missing articles, etc.).
    """
    page_path = PEOPLE_DIR / f"{slug}.md"
    if not page_path.exists():
        return [(slug, "PAGE_MISSING", str(page_path))]

    content = page_path.read_text(encoding="utf-8")
    issues = []

    # Find the ## Works section
    works_match = re.search(r"\n## Works\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if not works_match:
        return issues  # No Works section, nothing to verify

    works_section = works_match.group(1)

    # Find all markdown links [text](url) — these are external URLs
    # Wikilinks [[path|title]] are OK
    for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", works_section):
        link_text = match.group(1)
        link_url = match.group(2)
        # External URLs (http/https/web.archive.org) are issues
        if link_url.startswith("http://") or link_url.startswith("https://"):
            issues.append((slug, "EXTERNAL_URL", link_url, link_text))

    return issues


# ---------------------------------------------------------------------------
# P5 media extension: people <-> works, driven by media/_manifest.json
# ---------------------------------------------------------------------------

MEDIA_MANIFEST = REPO_ROOT / "media" / "_manifest.json"
WORKS_DIR = REPO_ROOT / "content" / "works"

# Media-section markers, paired with echo-media-regen.py (P4) so it can own the
# works/<slug>.md region afterwards.
MARK_MEDIA_START = "<!-- works-media-start -->"
MARK_MEDIA_END = "<!-- works-media-end -->"
MARK_SEC_START = "<!-- media-section-start -->"
MARK_SEC_END = "<!-- media-section-end -->"
MEDIA_SECTION_HEADING = "## Echo Resonance 歲月有聲"


def load_media_manifest() -> dict:
    """Read media/_manifest.json (P2 SSOT). Exit with guidance if absent."""
    if not MEDIA_MANIFEST.exists():
        raise SystemExit(
            f"media manifest not found (run scripts/echo-media-manifest.py first): "
            f"{MEDIA_MANIFEST}"
        )
    return json.loads(MEDIA_MANIFEST.read_text(encoding="utf-8"))


def media_slug_to_title(slug: str) -> str:
    """Humanise a media slug — mirrors slug_to_title in echo-media-regen.py."""
    s = slug.replace("_", " ").strip()
    s = re.sub(r"\.(?=\S)", ". ", s)  # "dr.lo" -> "dr. lo"
    toks = [t for t in re.split(r"[-\s]+", s) if t]
    out = []
    for t in toks:
        low = t.lower()
        if low in ("go", "of", "the", "a", "an", "in", "on") and out:
            out.append(low)
        else:
            out.append(t.capitalize())
    return " ".join(out)


def media_asset_src(entry: dict) -> str:
    """Audio src for a person-page embed, mirroring echo-media-regen.asset_src.

    Prefer a repo MP3 (content/media/<slug>.mp3, else media/<slug>.mp3) so the
    player also works under GitHub Pages; fall back to the manifest asset
    (~/media-outputs/jobs/<slug>.wav — pinto-only). No copy of the blob, ever.
    """
    slug = entry.get("slug", "")
    for rel in (f"content/media/{slug}.mp3", f"media/{slug}.mp3"):
        if (REPO_ROOT / rel).exists():
            return f"../media/{slug}.mp3"  # person page lives one level below content/
    return entry.get("asset", "")


def media_entries_for_person(entries: list, person_slug: str) -> list:
    """Manifest entries whose `entities` reference people/<person_slug>.md."""
    target = f"people/{person_slug}.md"
    out = [e for e in entries if target in (e.get("entities") or [])]
    out.sort(key=lambda e: (e.get("produced_at") or "", e["slug"]))
    return out


def render_person_media_section(entries: list, manifest: dict, person_slug: str) -> str:
    """Marked media section body for a person page (no markers, no heading).

    Links are full [[works/<slug>|name]] wikilinks (never bare ./slug), each
    piece carries an <audio> embed, and the disclaimer is pulled verbatim from
    the manifest — no hardcoded strings (P6 rule).
    """
    chinese_name = SLUG_TO_CHINESE.get(person_slug, person_slug)
    lines = [
        f"**{chinese_name}** — {len(entries)} Echo Resonance pieces. "
        f"Full catalog: [[media/index|Echo Resonance — Media]].",
        "",
    ]
    for e in entries:
        slug = e["slug"]
        title = media_slug_to_title(slug)
        src = media_asset_src(e)
        lang = e.get("language") or "zh-TW"
        created = e.get("produced_at") or "undated"
        lines.append(f"- [[works/{slug}|{title}]] · {lang} · {created}")
        lines.append(f"  <audio controls preload=\"none\" src=\"{src}\">")
        lines.append(f"  {title} · {e.get('kind') or 'music'} ({created})</audio>")
        lines.append("")
    dis_en = manifest.get("disclaimer") or ""
    dis_zh = manifest.get("disclaimer_zh") or ""
    if dis_en:
        lines.append(f"> {dis_en}")
        lines.append(">")
    if dis_zh:
        lines.append(f"> {dis_zh}")
        lines.append(">")
    return "\n".join(lines).rstrip() + "\n"


def add_media_section_to_person_page(person_slug: str, entries: list,
                                     manifest: dict, dry_run: bool) -> bool:
    """Write the marked media section onto a person page (idempotent).

    Replaces a marked region if present; else any pre-existing unmarked
    "## Echo Resonance 歲月有聲" section (P3-era hand sections); else inserts
    before "## Related Pages" / "## Sources"; else appends.
    """
    page_path = PEOPLE_DIR / f"{person_slug}.md"
    if not page_path.exists():
        print(f"  MEDIA SKIP: {person_slug} — no person page at {page_path}")
        return False
    content = page_path.read_text(encoding="utf-8")
    inner = render_person_media_section(entries, manifest, person_slug)
    block = f"{MEDIA_SECTION_HEADING}\n\n{MARK_MEDIA_START}\n{inner}{MARK_MEDIA_END}\n"

    # 1. Existing marked region: replace in place.
    marked = re.search(
        rf"\n{re.escape(MEDIA_SECTION_HEADING)}\n.*?{re.escape(MARK_MEDIA_START)}.*?"
        rf"{re.escape(MARK_MEDIA_END)}\n",
        content, re.DOTALL,
    )
    if marked:
        new = content[:marked.start()] + "\n" + block + content[marked.end():]
    else:
        # 2. Pre-existing unmarked section with the same heading: swap it out.
        unmarked = re.search(
            rf"\n{re.escape(MEDIA_SECTION_HEADING)}\n(.*?)(?=\n## |\Z)",
            content, re.DOTALL,
        )
        if unmarked:
            new = content[:unmarked.start()] + "\n" + block + content[unmarked.end():]
        else:
            # 3. Anchor before a known tail section, else append.
            if "## Related Pages" in content:
                new = content.replace("## Related Pages", block + "## Related Pages", 1)
            elif "## Sources" in content:
                new = content.replace("## Sources", block + "## Sources", 1)
            elif "## Revision History" in content:
                new = content.replace("## Revision History", block + "## Revision History", 1)
            else:
                new = content.rstrip() + "\n\n" + block
    new = re.sub(
        r"last_reviewed: \d{4}-\d{2}-\d{2}",
        f"last_reviewed: {datetime.now().strftime('%Y-%m-%d')}",
        new, count=1,
    )
    if dry_run:
        print(f"  MEDIA DRY-RUN: {person_slug} — would update {page_path} "
              f"({len(entries)} pieces)")
        return True
    if new != content:
        page_path.write_text(new, encoding="utf-8")
        print(f"  MEDIA DONE: {person_slug} — {len(entries)} pieces with embeds")
    return True


WORKS_PAGE_TEMPLATE = """---
title: "{title}"
type: work
source_id: echo-resonance
value_band: C
license: all-rights
verification_status: pending
last_reviewed: {today}
---
# {title}

## Identity Snapshot
- Kind: {kind} (AI interpretation)
- Language: {language}
- Core roles: Echo Resonance 歲月有聲 production piece (band C — creative)

## Record
- **Produced:** {produced}
- **Engine:** {engine}
- **Subject(s):** {subjects}

## Media
{MARK_SEC_START}
{MARK_SEC_END}

## Disclaimer
> {dis_en}
>
> {dis_zh}

## Related Pages
- [[media/index|Echo Resonance — Media]]
"""


def ensure_works_page(slug: str, entry: dict, manifest: dict,
                      person_slug: str, dry_run: bool) -> bool:
    """Create content/works/<slug>.md carrying the media-section markers.

    Only ever *creates*; an existing page is left untouched (its media region
    is owned by scripts/echo-media-regen.py once markers exist).
    """
    page = WORKS_DIR / f"{slug}.md"
    if page.exists():
        return False
    if dry_run:
        print(f"  MEDIA DRY-RUN: would create {page}")
        return True
    WORKS_DIR.mkdir(parents=True, exist_ok=True)
    subjects = (
        f"[[people/{person_slug}|{SLUG_TO_CHINESE.get(person_slug, person_slug)}]]"
        if person_slug else "—"
    )
    page.write_text(
        WORKS_PAGE_TEMPLATE.format(
            title=media_slug_to_title(slug),
            today=datetime.now().strftime("%Y-%m-%d"),
            kind=entry.get("kind") or "music",
            language=entry.get("language") or "zh-TW",
            produced=entry.get("produced_at") or "undated",
            engine=entry.get("engine") or "HeartMuLa",
            subjects=subjects,
            MARK_SEC_START=MARK_SEC_START,
            MARK_SEC_END=MARK_SEC_END,
            dis_en=manifest.get("disclaimer") or "",
            dis_zh=manifest.get("disclaimer_zh") or "",
        ),
        encoding="utf-8",
    )
    print(f"  MEDIA DONE: created {page.relative_to(REPO_ROOT)}")
    return True


def process_media_links(slugs=None, dry_run=False) -> list:
    """P5: person page media sections + works pages, from the manifest."""
    manifest = load_media_manifest()
    entries = manifest.get("entries", [])
    print(f"Loaded {len(entries)} media entries from {MEDIA_MANIFEST}")

    # person slug -> entries (an entry may reference several people)
    by_person = defaultdict(list)
    for e in entries:
        for ent in e.get("entities") or []:
            m = re.fullmatch(r"people/([a-z0-9-]+)\.md", ent)
            if m:
                by_person[m.group(1)].append(e)
    if not by_person:
        print("No manifest entries reference people/*.md — nothing to link.")
        return []

    person_slugs = sorted(by_person)
    if slugs is not None:
        person_slugs = [s for s in person_slugs if s in slugs]

    results = []
    created_works = 0
    for slug in person_slugs:
        ents = media_entries_for_person(entries, slug)
        print(f"\nMEDIA: {slug} ({len(ents)} pieces)")
        updated = add_media_section_to_person_page(slug, ents, manifest, dry_run)
        for e in ents:
            if ensure_works_page(e["slug"], e, manifest, slug, dry_run):
                created_works += 1
        results.append((slug, updated))

    print("\n" + "=" * 60)
    print("MEDIA SUMMARY")
    print("=" * 60)
    done = sum(1 for _, s in results if s)
    print(f"  Person pages: {done}/{len(results)} ({'dry-run' if dry_run else 'written'})")
    print(f"  Works pages created: {created_works}")
    return results


def main():
    parser = argparse.ArgumentParser(description="Link Echopedia person pages to all their works")
    parser.add_argument("--all", action="store_true", help="Process all columnists")
    parser.add_argument("--columnist", type=str, help="Process a single columnist by slug")
    parser.add_argument("--dry-run", action="store_true", help="Don't write changes")
    parser.add_argument("--list-slugs", action="store_true", help="List all columnist slugs")
    parser.add_argument("--verify", action="store_true", help="Verify existing person pages for external links")
    parser.add_argument("--scan-bodies", action="store_true",
                        help="Expensive full-corpus Chinese-name walk (off in cron)")
    parser.add_argument("--media", action="store_true",
                        help="Also run the P5 media pass (person page media section + works pages)")
    parser.add_argument("--media-only", action="store_true",
                        help="Run ONLY the P5 media pass (manifest-driven; no taiwanjustice hits)")
    args = parser.parse_args()

    if args.media_only:
        media_slugs = [args.columnist] if args.columnist else None
        process_media_links(media_slugs, args.dry_run)
        return

    if args.list_slugs:
        for slug in ALL_SLUGS:
            print(slug)
        return

    if args.verify:
        print("Verifying person pages for external links in ## Works sections...")
        all_issues = []
        for slug in ALL_SLUGS:
            issues = verify_person_page_links(slug)
            if issues:
                all_issues.extend(issues)
                for issue in issues:
                    if issue[1] == "EXTERNAL_URL":
                        print(f"  {slug}: EXTERNAL_URL — {issue[2]} ({issue[3]})")
                    elif issue[1] == "PAGE_MISSING":
                        print(f"  {slug}: PAGE_MISSING — {issue[2]}")

        print(f"\n{'=' * 60}")
        print(f"VERIFICATION SUMMARY")
        print(f"{'=' * 60}")
        external_count = sum(1 for i in all_issues if i[1] == "EXTERNAL_URL")
        missing_count = sum(1 for i in all_issues if i[1] == "PAGE_MISSING")
        print(f"  External URLs found: {external_count}")
        print(f"  Missing pages: {missing_count}")
        print(f"  Total issues: {len(all_issues)}")
        return

    # Determine which slugs to process
    if args.columnist:
        slugs = [args.columnist]
    elif args.all:
        slugs = ALL_SLUGS
    else:
        print("Specify --all, --columnist <slug>, --list-slugs, or --verify")
        return

    if not slugs:
        print("No slugs to process.")
        return

    print(f"Loading priority hits from {HITS_FILE}...")
    hits = load_hits()
    print(f"  Loaded {len(hits)} hits")

    print(f"Grouping hits by slug...")
    grouped = group_hits_by_slug(hits, scan_bodies=args.scan_bodies)
    print(f"  Found hits for {len(grouped)} slugs")

    results = []
    for slug in slugs:
        print(f"\nProcessing: {slug}")
        success = process_columnist(slug, grouped, args.dry_run)
        results.append((slug, success))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for slug, success in results:
        status = "DONE" if success else "SKIPPED"
        print(f"  {slug}: {status}")

    done = sum(1 for _, s in results if s)
    print(f"\n  Total: {done}/{len(results)} pages processed")

    if args.media:
        process_media_links(set(slugs), args.dry_run)


if __name__ == "__main__":
    main()
