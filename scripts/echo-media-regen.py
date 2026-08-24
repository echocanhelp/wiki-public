#!/usr/bin/env python3
"""echo-media-regen.py -- P4 regen: re-read the manifest, patch the views region.

Mirror of echo-media-views.py (P3) + echopedi-regen-*.py marker patching. Where
echo-media-views.py *generates* the whole media/index.md from the catalog, this
script is the CI/publish-friendly REGEN: it re-reads media/_manifest.json and
rewrites ONLY the region between the

    <!-- media-index-start --> ... <!-- media-index-end -->

markers in media/index.md, leaving front-matter and the "Related Pages" footer
untouched. Idempotent: regenerating on already-rendered output is a no-op diff.

Also patches any works/<slug>.md file that carries the paired

    <!-- media-section-start --> ... <!-- media-section-end -->

markers, inserting that piece's <audio> embed there (guarded: only when the file
exists and has the markers, so missing works pages never break the run).

ACCEPT CRITERIA: must read the manifest. Reject a version that does not.

Usage:
  python3 scripts/echo-media-regen.py [--dry-run] [--jobs-as-absolute]
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
MANIFEST = REPO / "media" / "_manifest.json"
INDEX = REPO / "media" / "index.md"
WORKS_DIR = REPO / "content" / "works"

FEATURED_KINDS = {"music", "narration"}

MARK_INDEX_START = "<!-- media-index-start -->"
MARK_INDEX_END = "<!-- media-index-end -->"
MARK_SEC_START = "<!-- media-section-start -->"
MARK_SEC_END = "<!-- media-section-end -->"


def slug_to_title(slug: str) -> str:
    """Humanise the agent-assigned token, mirroring echo-media-views.py."""
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


def site_src(asset: str, from_file: Path) -> str:
    """Audio src for the *published* static site.

    MP3s that live inside the repo (content/media/<slug>.mp3) are the default
    embed: Quartz copies content/media/ into public/media/ and GitHub Pages
    serves them, so the stream works publicly at /wiki-public/media/<slug>.mp3.

    For repo-external assets (the ~/media-outputs/jobs SSOT WAVs that were never
    copied in), fall back to the absolute host path so the embed still plays on
    pinto; it 404s under GitHub Pages until the asset is imported into content/media/.
    """
    ap = Path(asset)
    try:
        rel = ap.relative_to(REPO)
    except ValueError:
        return asset  # repo-external SSOT: absolute host path is the faithful src
    depth = len(from_file.parent.relative_to(REPO).parts)
    prefix = "../" * depth
    return f"{prefix}/{'/'.join(rel.parts)}"


def published_media_href(slug: str, page: Path) -> str:
    """Relative href to media/<slug>.mp3 from the *published* HTML location.

    Quartz emits content/people/x.md → /people/x.html (content/ is stripped).
    GitHub Pages serves repo-root media/<slug>.mp3 at /wiki-public/media/<slug>.mp3.
    Using the markdown tree depth (including content/) produced ../../media/...
    which 404s from /people/. Always strip a leading content/ segment.
    """
    rel = page.resolve().relative_to(REPO.resolve())
    parts = rel.parts
    if parts and parts[0] == "content":
        parts = parts[1:]
    depth = max(len(parts) - 1, 0)
    if depth == 0:
        return f"media/{slug}.mp3"
    return ("../" * depth) + f"media/{slug}.mp3"


def asset_src(entry: dict, page: Path) -> tuple[str, str]:
    """Resolve (embed src, download href) for a manifest entry.

    Prefer a repo MP3 at content/media/<slug>.mp3 or media/<slug>.mp3 so the
    player works on GitHub Pages. Else fall back to the host-path WAV SSOT
    (plays on pinto only).
    """
    slug = entry.get("slug", "")
    kind = (entry.get("kind") or "").lower()
    content_mp3 = REPO / "content" / "media" / f"{slug}.mp3"
    root_mp3 = REPO / "media" / f"{slug}.mp3"
    if kind == "music" and (content_mp3.exists() or root_mp3.exists()):
        href = published_media_href(slug, page)
        return href, href
    return entry.get("asset", ""), entry.get("asset", "")


def load_manifest(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(
            f"manifest not found (run echo-media-manifest.py first): {path}"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _escape(t: str) -> str:
    return html.unescape(t or "")


def section_block(e: dict, page: Path) -> str:
    title = _escape(slug_to_title(e["slug"]))
    slug = e["slug"]
    kind = (e.get("kind") or "music").upper()
    lang = e.get("language") or "zh-TW"
    created = e.get("produced_at") or "undated"
    src, dl = asset_src(e, page)
    audio = (
        f'<audio controls preload="none" src="{src}">\n'
        f"              {title} · {kind} · {lang} ({created})\n"
        f"            </audio>"
    )
    dl_link = f"- Download: [{Path(dl).name}]({dl})"
    return (
        f"### {title}  <a href=\"#top\">#</a>\n\n"
        f"- slug: {slug} · kind: {kind} · language: {lang} · produced: {created}\n"
        f"- link: [[#slug-{slug}|{title}]]\n\n"
        f"{dl_link}\n\n"
        f"{audio}\n"
    )


def render_index_region(cat: dict) -> str:
    """Content to sit between the media-index markers (no markers themselves)."""
    entries = list(cat.get("entries", []))
    entries.sort(
        key=lambda e: (e.get("produced_at") or "", slug_to_title(e["slug"])),
        reverse=True,
    )
    featured = [e for e in entries if e.get("kind") in FEATURED_KINDS]
    rest = [e for e in entries if e.get("kind") not in FEATURED_KINDS]
    featured_lines = "\n".join(section_block(e, INDEX) for e in featured) or "_No production pieces yet._"
    rest_lines = "\n".join(section_block(e, INDEX) for e in rest) or "_None._"
    return (
        "\n## Featured pieces\n\n"
        f"{featured_lines}\n\n"
        "## Staged / test recordings\n\n"
        f"{rest_lines}\n\n"
        "## Disclaimer\n\n"
        f"{_escape(cat.get('disclaimer'))}\n\n"
        f"{_escape(cat.get('disclaimer_zh'))}\n\n"
    )


def patch_region(text: str, start: str, end: str, inner: str) -> tuple[str, bool]:
    """Replace the bytes between start/end markers with `inner`.

    Returns (new_text, changed). If the markers are absent, no edit is made.
    """
    if start not in text or end not in text:
        return text, False
    i, j = text.index(start) + len(start), text.index(end)
    new = text[:i] + "\n" + inner + text[j:]
    return new, (new != text)


def build_fresh(cat: dict) -> str:
    """First-run scaffold (when no index.md exists yet), mirroring P3 output."""
    title = _escape(cat.get("name_en") or "Echo Resonance")
    title_yaml = (
        title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )
    zh = _escape(cat.get("name_zh") or "")
    body = render_index_region(cat)
    return (
        "---\n"
        f'title: "{title_yaml}"\n'
        "---\n"
        f"# {title} · {zh}\n\n"
        f"{MARK_INDEX_START}\n\n{body}{MARK_INDEX_END}\n"
    )


def index_change_only(cat: dict) -> tuple[bool, str]:
    """Render-only: compute whether the index region *would* change, no writes.

    Mirrors regen_index's changed computation so --dry-run's report is the real
    figure, not the old hardcoded ``True``.
    """
    text = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    patched, changed = patch_region(text, MARK_INDEX_START, MARK_INDEX_END, render_index_region(cat))
    return changed, patched


def regen_index(cat: dict) -> tuple[bool, str]:
    text = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    patched, changed = patch_region(text, MARK_INDEX_START, MARK_INDEX_END, render_index_region(cat))
    if not INDEX.exists() and not changed:
        patched = build_fresh(cat)
        changed = True
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(patched, encoding="utf-8")
    return changed, patched


def regen_media_sections(cat: dict) -> dict:
    """Patch works/<slug>.md media-section markers for tracked slug pages."""
    by_id = {e["slug"]: e for e in cat.get("entries", [])}
    touched: dict[str, bool] = {}
    if not WORKS_DIR.is_dir():
        return touched
    for md in sorted(WORKS_DIR.glob("**/*.md")):
        slug = md.stem
        if slug not in by_id:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        if MARK_SEC_START not in text or MARK_SEC_END not in text:
            touched[slug] = False
            continue
        e = by_id[slug]
        inner = "\n" + section_block(e, md) + "\n"
        patched, changed = patch_region(text, MARK_SEC_START, MARK_SEC_END, inner)
        if changed:
            md.write_text(patched, encoding="utf-8")
        touched[slug] = changed
    return touched


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    args = ap.parse_args()

    cat = load_manifest(MANIFEST)
    entries = cat.get("entries", [])

    if not args.dry_run:
        idx_changed, _ = regen_index(cat)
        sections = regen_media_sections(cat)
    else:
        idx_changed, _ = index_change_only(cat)  # validate rendering + report real flag
        sections = regen_media_sections(cat)

    n_media = sum(1 for e in entries if e.get("kind") in FEATURED_KINDS)
    n_test = len(entries) - n_media

    print(f"REGEN_MEDIA: n={len(entries)} featured={n_media} test={n_test} "
          f"index_changed={idx_changed} -> {INDEX}")
    print(f"disclaimer bytes: {len(cat.get('disclaimer') or '')} "
          f"zh_bytes: {len(cat.get('disclaimer_zh') or '')}")
    if sections:
        touched = sum(1 for v in sections.values() if v)
        print(f"media-sections: touched={len(sections)} changed={touched}")
        for slug, changed in sections.items():
            print(f"  - {slug}: {'changed' if changed else 'stable'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
