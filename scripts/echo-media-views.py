#!/usr/bin/env python3
"""echo-media-views.py — P3 of the Echo Resonance / 歲月有聲 media-integration.

Reads the git-tracked media catalog at media/_manifest.json (source of truth,
built by echo-media-manifest.py / P2) and derives the *views*:

  * content/media/index.md  — the media catalog (<!-- media-index-start/end -->)
  * each slug appears as a self-contained section with a Quartz <audio> embed.

Wired into echopedi-publish.sh before Quartz (see echo-media-regen.py, P4, for
the mirror that re-reads the manifest on every publish). Do not hand-edit the
region between the markers.

SSOT rule: the WAVs live at ~/media-outputs/jobs/<slug>.wav and are NOT copied
into the repo. The embed references the asset via its repo-relative path so a
published site can play them; the catalog never duplicates the blob.

Usage:
  python3 ~/echo-system/scripts/echo-media-views.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

REPO = Path("/home/leedt/echo-system")
MANIFEST = REPO / "media" / "_manifest.json"
OUT = REPO / "media" / "index.md"
FEATURED_KINDS = {"music", "narration"}

# reuse the regen-*.py marker pattern (matches content/works/index.md style)
MARK_START = "<!-- media-index-start -->"
MARK_END = "<!-- media-index-end -->"


def slug_to_title(slug: str) -> str:
    """Humanise the agent-assigned token. The manifest leaves name_en/name_zh
    empty (auto-derived in P2); P3 turns the slug into a readable title only.
    """
    s = slug.replace("_", " ").strip()
    s = re.sub(r"\.(?=\S)", ". ", s)  # "dr.lo" -> "dr. lo"
    toks = [t for t in re.split(r"[-\s]+", s) if t]
    out = []
    for t in toks:
        low = t.lower()
        # keep short function/connector tokens lowercase for readability
        if low in ("go", "of", "the", "a", "an", "in", "on") and out:
            out.append(low)
        else:
            out.append(t.capitalize())
    return " ".join(out)


def rel_asset(asset: str, from_file: Path) -> str:
    """repo-relative path from from_file to the WAV asset.

    The jobs WAVs are the repo-external SSOT (P2: never copied into the repo).
    When an asset lives outside REPO we cannot produce a portable repo-relative
    src — emit the absolute external path so the embed is faithful to the SSOT
    (deployment URL wiring is P4's concern), and add a [Download] link.
    """
    ap = Path(asset)
    try:
        rel = ap.relative_to(REPO)
    except ValueError:
        return asset  # repo-external SSOT: absolute path
    parts = [".."] * len(from_file.parent.relative_to(REPO).parts)
    return "/".join([*parts, *rel.parts]) if parts else str(rel)


def load_catalog(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"manifest not found (run echo-media-manifest.py first): {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    import json  # local: keep top-level imports tidy, only needed in main path

    cat = load_catalog(MANIFEST)
    entries = list(cat.get("entries", []))

    # stable order: produced_at desc, then title
    entries.sort(key=lambda e: (e.get("produced_at") or "", slug_to_title(e["slug"])), reverse=True)

    featured = [e for e in entries if e.get("kind") in FEATURED_KINDS]
    rest = [e for e in entries if e.get("kind") not in FEATURED_KINDS]

    def section(e: dict) -> str:
        title = html.unescape(slug_to_title(e["slug"]))
        slug = e["slug"]
        kind = (e.get("kind") or "music").upper()
        lang = e.get("language") or "zh-TW"
        created = e.get("produced_at") or "undated"
        asset = e.get("asset", "")
        # full-wikilink to the slug section (NOT a bare ./slug link)
        link = f"[[#slug-{slug}|{title}]]"
        audio = (
            f'<audio controls preload="none" '
            f'src="{rel_asset(asset, OUT)}">\n'
            f"              {title} · {kind} · {lang} ({created})\n"
            f"            </audio>"
        )
        dl = f"- Download: [{Path(asset).name}]({asset})"
        return (
            f"### {title}  <a href=\"#top\">#</a>\n\n"
            f"- slug: {slug} · kind: {kind} · language: {lang} · produced: {created}\n"
            f"- link: {link}\n\n"
            f"{dl}\n\n"
            f"{audio}\n"
        )

    title = html.unescape(cat.get("name_en") or "Echo Resonance")
    zh_title = html.unescape(cat.get("name_zh") or "")
    disclaimer = html.unescape(cat.get("disclaimer") or "")
    disclaimer_zh = html.unescape(cat.get("disclaimer_zh") or "")

    featured_lines = "\n".join(section(e) for e in featured) or "_No production pieces yet._"
    rest_lines = "\n".join(section(e) for e in rest) or "_None._"

    body = f"""---
title: "{html.unescape(cat.get('name_en') or 'Echo Resonance').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')} — Media"
type: index
tags:
  - index
  - media
  - stories
verification_status: pending
last_reviewed: 2026-08-24
---
# {title} · {zh_title}

Sound recordings from the Echo Resonance / 歲月有聲 pipeline. Each piece is an AI
interpretation built from Echopedia facts — **creative, not verified history**.
Listen below; every piece is listed (not a teaser).

<!-- media-index-start -->

## Featured pieces

{featured_lines}

## Staged / test recordings

{rest_lines}

## Disclaimer

{disclaimer}

{disclaimer_zh}

<!-- media-index-end -->

## Related Pages
- [[works/index|Stories & historical works]]
- [[media/_manifest|Media catalog manifest]]
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(body, encoding="utf-8")

    n_media = sum(1 for e in entries if e.get("kind") in FEATURED_KINDS)
    n_test = len(entries) - n_media
    n_sections = sum(1 for e in entries if slug_to_title(e["slug"]) is not None)
    print(
        f"REGEN_MEDIA: n={len(entries)} featured={n_media} test={n_test} "
        f"sections={n_sections} -> {OUT}"
    )
    print(f"disclaimer bytes: {len(disclaimer)} zh_bytes: {len(disclaimer_zh)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
