#!/usr/bin/env python3
"""Harvest penghu.info: sitemap URLs + the 3 Tier1-anchored articles,
via jina reader, producing vault markdown + a MANIFEST.json.

Crawl scope is deliberately bounded (the platform has ~8,946 articles;
the 3 cited are the historically-anchored subset). A separate larger
harvest of the full corpus is out of scope here.
"""
from __future__ import annotations
import json, re, sys, time, hashlib
from pathlib import Path
import urllib.request, urllib.error

SITE = "https://penghu.info"
REPO = Path("/home/leedt/echo-system")
VAULT = REPO / "knowledge/web-archives/penghu-info"
VAULT.mkdir(parents=True, exist_ok=True)

# The 3 articles directly cited on Tier1 content:
CITED = {
    "OB08DF845E664F47451E": "許凌雲秀才紀念館",
    "OB8D7D9C164FCF102ED7": "許凌雲",
    "OB9B088F09F89D8B7F9E": "瓦硐許姓",
}
# 10 canonical sitemap anchor URLs (2017-era):
SITEMAP = {
    "OB1F10AF08C936E984B5": "馬公市",
    "OB3EA09D40C6E9BC3602": None,
    "OB0CB9D97C7D16435617": None,
    "OB78143B240A367EE7F3": None,
    "OB838BA9677DFF314042": "白沙鄉",
    "OB8566DA837B0C048C40": None,
    "OB23C512046DFE3D988E": "文化 (category, 2181 則)",
    "OB3BAC46B986E5DBC51B": None,
    "OB2C73E27C74756946C9": None,
    "OBC70EF284CBE5C8FB3C": None,
}

def slugify(url: str) -> str:
    p = url.rstrip("/").split("/")[-1]
    return p.lower()

def slug_zh(url: str, zh: str | None) -> str:
    p = url.rstrip("/").split("/")[-1]
    base = re.sub(r"[^0-9A-Za-z]+", "-", p)
    return f"penghu-info-{base}" + (f"-{zh}" if zh else "")

def fetch_reader(url: str) -> str:
    """jina reader text (stripped to visible text + title)."""
    req = urllib.request.Request(
        f"https://r.jina.ai/{url}",
        headers={"User-Agent": "Echopedia-harvest/1.0", "Accept-Language": "zh-Hant"},
    )
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read().decode("utf-8", "replace")
    return raw

def meta_and_body(raw: str) -> tuple[str, str, str, str]:
    """Extract <title>, og:title, and body markdown from jina text."""
    title = ""
    m = re.search(r"Title:\s*(.+)", raw, re.I)
    if m:
        title = m.group(1).strip()
    m = re.search(r"OG_TITLE:\s*(.+)", raw, re.I)
    if m:
        title = m.group(1).strip()
    # body: strip front meta lines jina adds
    lines = [l for l in raw.splitlines() if l.strip()]
    body = "\n".join(lines)
    return title, body, title

def vault_md(url: str, zh: str | None, raw: str) -> str:
    title = ""
    m = re.search(r"^Title:\s*(.+)$", raw, re.M | re.I)
    if m:
        title = m.group(1).strip()
    og = re.search(r"^OG_TITLE:\s*(.+)$", raw, re.M | re.I)
    if og:
        title = og.group(1).strip() or title
    ogd = re.search(r"OG_DESCRIPTION:\s*(.+)$", raw, re.M | re.I)
    return (
        f"# {title or url}  「{url}」\n\n"
        f"- Source: {url}\n"
        f"- Type: penghu.info 知識条目\n"
        f"- Cached: 2026-08-22 via r.jina.ai\n"
        f"- Archival note: platform-wide 8,946 則知識; this URL is "
        f"{('a cited Tier1 anchor' if url in CITED else 'a sitemap anchor')}\n\n"
        f"## Cached body\n\n"
        f"<!-- strip frontmatter by reader -->\n"
        f"{raw.replace(f'Title: {title}', '').replace(f'OG_TITLE: {title}', '')}\n"
    )

def main() -> int:
    manifest = {
        "version": 1,
        "domain": "penghu.info",
        "generated": "2026-08-22",
        "note": (
            "Partial, historically-anchored harvest. Platform totals ~8,946 "
            "則知識 across 8 categories / 7 time periods; full corpus is a "
            "separate large ingest. Captured: 3 Tier1-anchored articles + "
            "10 sitemap anchor pages."
        ),
        "total_platform_knowledge": 8946,
        "count_html": 0,
        "entries": [],
    }
    urls = list(CITED.keys()) + list(SITEMAP.keys())
    for i, uid in enumerate(urls):
        url = f"{SITE}/{uid}"
        zh = CITED.get(uid) or SITEMAP.get(uid)
        fn = slug_zh(uid, zh) + ".md"
        out = VAULT / fn
        try:
            raw = fetch_reader(url)
        except Exception as e:
            print(f"FAIL {uid}: {e}", file=sys.stderr)
            manifest["entries"].append({"url": url, "status": "fail", "error": str(e)})
            continue
        text = vault_md(url, zh, raw)
        out.write_text(text, encoding="utf-8")
        b = len(text.encode("utf-8"))
        manifest["count_html"] += 1
        manifest["entries"].append({
            "url": url, "file": str(out.relative_to(REPO)),
            "bytes": b, "status": "ok", "source": "jina",
            "http": 200, "title": re.search(r"^Title:\s*(.+)$", raw, re.M).group(1) if re.search(r"^Title:", raw, re.M) else "",
        })
        print(f"OK  {uid} -> {fn} ({b} bytes)" + (f"  [{zh}]" if zh else ""))
        time.sleep(0.35)

    man_path = VAULT / "penghu-info-MANIFEST.json"
    man_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nMANIFEST: {man_path} ({manifest['count_html']} ok)")
    print(f"VAULT: {VAULT} ({len(list(VAULT.glob('*.md')))} md, "
          f"{sum(s.stat().st_size for s in VAULT.glob('*.md'))} bytes)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
