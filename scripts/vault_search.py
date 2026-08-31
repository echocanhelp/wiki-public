#!/usr/bin/env python3
"""
Vault Search v2 — Enhanced recall for the Echo Vault second brain.

Adds three capabilities on top of the existing keyword search:
  1. Vector embeddings (semantic search) via sentence-transformers
  2. Obsidian-style graph traversal (wikilink graph, co-citation, shared tags)
  3. LLM-reranked results (relevance scoring via auxiliary model)

Usage:
  python3 vault_search.py "Who are the theologians?"
  python3 vault_search.py --related people/albert-s-lai.md
  python3 vault_search.py --rebuild-index
  python3 vault_search.py --stats

Design:
  - Embeddings stored as BLOB in SQLite (cache.db) — no external vector DB needed
  - Graph stored as adjacency list in SQLite (wikilinks + co-citation + tags)
  - LLM reranking uses the local NVFP4 model via vLLM (:8888) or Grok fallback
  - Falls back to keyword-only search if sentence-transformers is unavailable
"""

import os
import re
import sys
import json
import sqlite3
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional

# ─── Paths ──────────────────────────────────────────────────────────────
ECHOPEDIA_DIR = Path(os.environ.get("ECHOPEDIA_DIR", "/home/leedt/echo-system"))
CONTENT_DIR = ECHOPEDIA_DIR / "content"
KNOWLEDGE_DIR = ECHOPEDIA_DIR / "knowledge"
CACHE_DB = ECHOPEDIA_DIR / "cache" / "cache.db"

# ─── Embedding model ────────────────────────────────────────────────────
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
_embedder = None

def get_embedder():
    """Lazy-load the embedding model."""
    global _embedder
    if _embedder is not None:
        return _embedder
    try:
        from sentence_transformers import SentenceTransformer
        _embedder = SentenceTransformer(EMBEDDING_MODEL)
        return _embedder
    except Exception as e:
        print(f"  [warn] sentence-transformers unavailable: {e}", file=sys.stderr)
        _embedder = False
        return None


# ─── Database ───────────────────────────────────────────────────────────
def get_db():
    """Get SQLite connection with vector and graph tables."""
    CACHE_DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(CACHE_DB))
    conn.row_factory = sqlite3.Row
    _init_tables(conn)
    return conn


def _init_tables(conn):
    """Create tables for embeddings, graph, and search history."""
    c = conn.cursor()

    # Vector embeddings table
    c.execute("""
        CREATE TABLE IF NOT EXISTS vault_embeddings (
            path TEXT PRIMARY KEY,
            tier INTEGER NOT NULL,
            title TEXT,
            page_type TEXT,
            tags TEXT,
            embedding BLOB NOT NULL,
            content_hash TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)

    # Wikilink graph (adjacency list)
    c.execute("""
        CREATE TABLE IF NOT EXISTS vault_graph_links (
            source TEXT NOT NULL,
            target TEXT NOT NULL,
            link_type TEXT NOT NULL DEFAULT 'wikilink',
            PRIMARY KEY (source, target, link_type)
        )
    """)

    # Tag co-occurrence graph
    c.execute("""
        CREATE TABLE IF NOT EXISTS vault_graph_tags (
            tag TEXT NOT NULL,
            path TEXT NOT NULL,
            PRIMARY KEY (tag, path)
        )
    """)

    # Search history (for learning)
    c.execute("""
        CREATE TABLE IF NOT EXISTS vault_search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            results_json TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()


# ─── Content extraction ─────────────────────────────────────────────────
def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def extract_body(content):
    """Extract body text (after frontmatter)."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return content


def extract_wikilinks(content):
    """Extract [[wikilinks]] from content."""
    return re.findall(r'\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]', content)


def extract_tags(fm):
    """Extract tags from frontmatter."""
    tags_str = fm.get("tags", "")
    if not tags_str:
        return []
    # Handle both space-separated and comma-separated
    return [t.strip() for t in re.split(r'[,\s]+', tags_str) if t.strip()]


def content_hash(text):
    """Fast hash of content for change detection."""
    return hashlib.md5(text.encode()).hexdigest()[:16]


# ─── Indexing ───────────────────────────────────────────────────────────
# Never rglob content/articles (Tier2 firehose) or knowledge/web-archives.
TIER1_INDEX_DIRS = ("people", "organizations", "sources", "works", "events", "media")


def _read_page(md_file: Path, rel: str, tier: int):
    try:
        content = md_file.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"  [warn] skip unreadable {md_file}: {e}", file=sys.stderr)
        return None
    return {
        "path": rel,
        "tier": tier,
        "content": content,
        "body": extract_body(content),
        "fm": extract_frontmatter(content),
    }


def collect_pages(tier1_only=False):
    """Collect indexable markdown. Skips articles/, web-archives/, broken symlinks."""
    pages = []

    for sub in TIER1_INDEX_DIRS:
        d = CONTENT_DIR / sub
        if not d.is_dir():
            continue
        for md_file in d.rglob("*.md"):
            if not md_file.is_file() or "*" in md_file.name or md_file.name.startswith("."):
                continue
            rel = md_file.relative_to(CONTENT_DIR)
            if "index" in str(rel):
                continue
            page = _read_page(md_file, str(rel), 1)
            if page:
                pages.append(page)

    if not tier1_only and KNOWLEDGE_DIR.is_dir():
        for child in KNOWLEDGE_DIR.iterdir():
            if child.name in ("web-archives",) or child.name.startswith("."):
                continue
            files = []
            if child.is_file() and child.suffix == ".md":
                files = [child]
            elif child.is_dir():
                files = [p for p in child.rglob("*.md")]
            for md_file in files:
                if not md_file.is_file() or "*" in md_file.name or md_file.name.startswith("."):
                    continue
                rel = md_file.relative_to(ECHOPEDIA_DIR)
                if "web-archives" in rel.parts:
                    continue
                page = _read_page(md_file, str(rel), 2)
                if page:
                    pages.append(page)

    return pages


def index_vault(rebuild=False, tier1_only=False, with_embeddings=None):
    """Build or update the vector + graph index.

    rebuild=True wipes tables then reindexes.
    rebuild=False is incremental: hash-skip unchanged, prune missing, re-embed dirty.
    with_embeddings=None → embeddings only when not tier1_only (weekly speed).
    Incremental after ci-heal should pass with_embeddings=True.
    """
    conn = get_db()
    c = conn.cursor()

    if with_embeddings is None:
        with_embeddings = not tier1_only

    embedder_state = "lazy" if with_embeddings else None

    def _get_embedder_lazy():
        nonlocal embedder_state
        if embedder_state != "lazy":
            return embedder_state
        loaded = get_embedder()
        if loaded and loaded is not False:
            embedder_state = loaded
        else:
            print("  [info] No embedding model available — indexing graph only")
            embedder_state = None
        return embedder_state

    pages = collect_pages(tier1_only=tier1_only)
    print(f"  [info] Found {len(pages)} pages to consider")

    if rebuild:
        if tier1_only:
            c.execute("DELETE FROM vault_graph_links WHERE source IN (SELECT path FROM vault_embeddings WHERE tier = 1)")
            c.execute("DELETE FROM vault_graph_tags WHERE path IN (SELECT path FROM vault_embeddings WHERE tier = 1)")
            c.execute("DELETE FROM vault_embeddings WHERE tier = 1")
        else:
            c.execute("DELETE FROM vault_embeddings")
            c.execute("DELETE FROM vault_graph_links")
            c.execute("DELETE FROM vault_graph_tags")
        conn.commit()

    updated = 0
    skipped = 0
    wikilink_lookup = None

    for page in pages:
        path = page["path"]
        ch = content_hash(page["content"])

        if not rebuild:
            c.execute("SELECT content_hash FROM vault_embeddings WHERE path = ?", (path,))
            row = c.fetchone()
            if row and row["content_hash"] == ch:
                skipped += 1
                continue
            c.execute("DELETE FROM vault_graph_links WHERE source = ?", (path,))
            c.execute("DELETE FROM vault_graph_tags WHERE path = ?", (path,))

        fm = page["fm"]
        title = fm.get("title", Path(path).stem)
        page_type = fm.get("type", "unknown")
        tags = extract_tags(fm)

        if with_embeddings:
            model = _get_embedder_lazy()
            if model:
                embed_text = f"{title}\n{page['body'][:500]}"
                import numpy as np
                emb = model.encode(embed_text)
                embedding = np.asarray(emb, dtype=np.float32).tobytes()
            else:
                embedding = b"\x00" * 384
        else:
            embedding = b"\x00" * 384

        c.execute("""
            INSERT OR REPLACE INTO vault_embeddings
            (path, tier, title, page_type, tags, embedding, content_hash, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (path, page["tier"], title, page_type, ",".join(tags),
              embedding, ch, datetime.now().isoformat()))

        for link in extract_wikilinks(page["body"]):
            target = link.replace("|", "").strip()
            target_path, wikilink_lookup = _resolve_wikilink(target, pages, wikilink_lookup)
            if target_path:
                c.execute("""
                    INSERT OR IGNORE INTO vault_graph_links
                    (source, target, link_type) VALUES (?, ?, 'wikilink')
                """, (path, target_path))

        for tag in tags:
            c.execute("""
                INSERT OR IGNORE INTO vault_graph_tags (tag, path) VALUES (?, ?)
            """, (tag, path))
        updated += 1

    pruned = 0
    live_paths = {p["path"] for p in pages}
    if tier1_only:
        c.execute("SELECT path FROM vault_embeddings WHERE tier = 1")
    else:
        c.execute("SELECT path FROM vault_embeddings")
    stale = [row["path"] for row in c.fetchall() if row["path"] not in live_paths]
    for sp in stale:
        c.execute("DELETE FROM vault_embeddings WHERE path = ?", (sp,))
        c.execute("DELETE FROM vault_graph_links WHERE source = ? OR target = ?", (sp, sp))
        c.execute("DELETE FROM vault_graph_tags WHERE path = ?", (sp,))
        pruned += 1

    conn.commit()
    print(f"  [info] updated={updated} skipped={skipped} pruned={pruned} considered={len(pages)}")
    return {"pages": len(pages), "updated": updated, "skipped": skipped, "pruned": pruned}


def _resolve_wikilink(link, pages, _lookup=None):
    """Resolve a wikilink to a known page path."""
    # Build a lookup from title/slug to path (cache to avoid O(n²) rebuild)
    if _lookup is None:
        _lookup = {}
        for p in pages:
            fm = p["fm"]
            title = fm.get("title", Path(p["path"]).stem)
            slug = Path(p["path"]).stem
            _lookup[title.lower()] = p["path"]
            _lookup[slug.lower()] = p["path"]
            # Also try content/people/slug format
            _lookup[f"people/{slug}"] = p["path"]
            _lookup[f"organizations/{slug}"] = p["path"]

    # Try direct match
    if link.lower() in _lookup:
        return _lookup[link.lower()], _lookup

    # Try with people/ prefix
    if f"people/{link.lower()}" in _lookup:
        return _lookup[f"people/{link.lower()}"], _lookup

    # Try with organizations/ prefix
    if f"organizations/{link.lower()}" in _lookup:
        return _lookup[f"organizations/{link.lower()}"], _lookup

    return None, _lookup


# ─── Vector search ──────────────────────────────────────────────────────
_VEC_CACHE = None  # (paths, tiers, titles, types, matrix, norms)


def _vec_cache():
    """Load embeddings once — 5k rows; do not reread SQLite every query."""
    global _VEC_CACHE
    if _VEC_CACHE is not None:
        return _VEC_CACHE
    import numpy as np

    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT path, tier, title, page_type, embedding FROM vault_embeddings")
    rows = c.fetchall()
    if not rows:
        _VEC_CACHE = []
        return _VEC_CACHE
    paths, tiers, titles, types, vecs = [], [], [], [], []
    buckets: dict[int, list] = {}
    for row in rows:
        emb = np.frombuffer(row["embedding"], dtype=np.float32).copy()
        buckets.setdefault(emb.shape[0], []).append((row, emb))
    # Prefer the MiniLM-L6 dim (384); else the largest bucket.
    dim = 384 if 384 in buckets else max(buckets, key=lambda d: len(buckets[d]))
    for row, emb in buckets[dim]:
        paths.append(row["path"])
        tiers.append(row["tier"])
        titles.append(row["title"])
        types.append(row["page_type"])
        vecs.append(emb)
    mat = np.vstack(vecs)
    norms = np.linalg.norm(mat, axis=1) + 1e-8
    _VEC_CACHE = (paths, tiers, titles, types, mat, norms)
    return _VEC_CACHE


def vector_search(query, top_k=10):
    """Semantic search using embeddings."""
    embedder = get_embedder()
    if not embedder:
        return []
    cache = _vec_cache()
    if not cache:
        return []
    import numpy as np

    paths, tiers, titles, types, mat, norms = cache
    q = np.asarray(embedder.encode(query), dtype=np.float32).reshape(-1)
    if q.shape[0] != mat.shape[1]:
        return []
    qn = float(np.linalg.norm(q) + 1e-8)
    sims = (mat @ q) / (norms * qn)
    idx = np.argpartition(-sims, min(top_k, len(sims) - 1))[:top_k]
    idx = idx[np.argsort(-sims[idx])]
    return [
        {
            "path": paths[i],
            "tier": tiers[i],
            "title": titles[i],
            "type": types[i],
            "score": float(sims[i]),
            "source": "vector",
        }
        for i in idx
    ]


# ─── Graph traversal ────────────────────────────────────────────────────
def find_related(path, top_k=10):
    """Find pages related to the given path via graph traversal.

    Uses three signals:
    1. Wikilink graph (direct links)
    2. Co-citation (pages that link to the same targets)
    3. Shared tags
    """
    conn = get_db()
    c = conn.cursor()

    results = []

    # 1. Direct wikilinks (pages this page links to)
    c.execute("""
        SELECT target as path FROM vault_graph_links
        WHERE source = ? AND link_type = 'wikilink'
    """, (path,))
    for row in c.fetchall():
        results.append({"path": row["path"], "relation": "links_to", "weight": 3.0})

    # 2. Reverse wikilinks (pages that link to this page)
    c.execute("""
        SELECT source as path FROM vault_graph_links
        WHERE target = ? AND link_type = 'wikilink'
    """, (path,))
    for row in c.fetchall():
        results.append({"path": row["path"], "relation": "linked_from", "weight": 3.0})

    # 3. Co-citation (pages that link to the same targets)
    c.execute("""
        SELECT DISTINCT gl.source as path, COUNT(*) as co_count
        FROM vault_graph_links gl
        JOIN vault_graph_links gl2 ON gl.target = gl2.target
        WHERE gl2.source = ? AND gl.source != ?
        GROUP BY gl.source
        ORDER BY co_count DESC
        LIMIT ?
    """, (path, path, top_k))
    for row in c.fetchall():
        results.append({"path": row["path"], "relation": "co_cited", "weight": float(row["co_count"])})

    # 4. Shared tags
    c.execute("""
        SELECT DISTINCT vg.path, COUNT(DISTINCT vg.tag) as shared_tags
        FROM vault_graph_tags vg
        JOIN vault_graph_tags vg2 ON vg.tag = vg2.tag
        WHERE vg2.path = ? AND vg.path != ?
        GROUP BY vg.path
        ORDER BY shared_tags DESC
        LIMIT ?
    """, (path, path, top_k))
    for row in c.fetchall():
        results.append({"path": row["path"], "relation": "shared_tag", "weight": float(row["shared_tags"])})

    # Merge and dedupe by path, keeping highest weight
    merged = {}
    for r in results:
        p = r["path"]
        if p not in merged or r["weight"] > merged[p]["weight"]:
            merged[p] = r

    # Get metadata for each result
    final = []
    for p, r in merged.items():
        c.execute("SELECT tier, title, page_type FROM vault_embeddings WHERE path = ?", (p,))
        row = c.fetchone()
        if row:
            final.append({
                "path": p,
                "tier": row["tier"],
                "title": row["title"],
                "type": row["page_type"],
                "relation": r["relation"],
                "weight": r["weight"],
            })

    final.sort(key=lambda r: r["weight"], reverse=True)
    return final[:top_k]


# ─── Hybrid search ──────────────────────────────────────────────────────
def hybrid_search(query, top_k=10):
    """Combine keyword, vector, and graph signals for ranked results."""
    # 1. Keyword search (existing logic)
    keyword_results = _keyword_search(query, top_k * 3)

    # 2. Vector search (skip if embed dim mismatch)
    try:
        vector_results = vector_search(query, top_k * 3)
    except Exception:
        vector_results = []

    # 3. Graph expansion: for top keyword results, find related pages
    graph_results = {}
    for r in keyword_results[:5]:
        related = find_related(r["path"], top_k=5)
        for rel in related:
            if rel["path"] not in graph_results:
                graph_results[rel["path"]] = rel

    # Merge all results
    merged = {}

    # Keyword scores (normalized to 0-1)
    max_kw = max((r["score"] for r in keyword_results), default=1)
    for r in keyword_results:
        p = r["path"]
        merged[p] = {
            "path": p, "tier": r["tier"], "title": r["title"],
            "type": r["type"], "score": r["score"] / max(max_kw, 1),
            "source": "keyword", "kw_score": r["score"] / max(max_kw, 1),
            "vec_score": 0, "graph_weight": 0,
        }

    # Vector scores
    for r in vector_results:
        p = r["path"]
        if p in merged:
            merged[p]["vec_score"] = r["score"]
            merged[p]["score"] = merged[p]["kw_score"] * 0.3 + r["score"] * 0.7
        else:
            merged[p] = {
                "path": p, "tier": r["tier"], "title": r["title"],
                "type": r["type"], "score": r["score"],
                "source": "vector", "kw_score": 0,
                "vec_score": r["score"], "graph_weight": 0,
            }

    # Graph results
    for p, rel in graph_results.items():
        if p in merged:
            merged[p]["graph_weight"] = rel["weight"]
            # Boost score slightly for graph-connected pages
            merged[p]["score"] *= 1.1
        else:
            merged[p] = {
                "path": p, "tier": rel["tier"], "title": rel["title"],
                "type": rel["type"], "score": rel["weight"] / 10,
                "source": "graph", "kw_score": 0,
                "vec_score": 0, "graph_weight": rel["weight"],
            }

    # Sort and return
    results = list(merged.values())
    for r in results:
        path = r.get("path") or ""
        ptype = r.get("type") or ""
        if path.startswith("organizations/") or ptype == "organization":
            r["score"] *= 1.3
        elif path.startswith("people/") or ptype == "person":
            r["score"] *= 1.15
        elif path.startswith("sources/"):
            r["score"] *= 0.65
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_k]


_REG_ALIAS = None
_REG_PATH = ECHOPEDIA_DIR / "echopedia" / "identity" / "identity_registry.json"


def registry_slug_aliases() -> dict:
    """LINE display names → person slugs. Never includes U-ids."""
    global _REG_ALIAS
    if _REG_ALIAS is not None:
        return _REG_ALIAS
    out: dict[str, str] = {}
    try:
        data = json.loads(_REG_PATH.read_text(encoding="utf-8"))
    except Exception:
        _REG_ALIAS = {}
        return _REG_ALIAS
    for link in data.get("links") or []:
        if link.get("state") not in ("verified", "owner_verified"):
            continue
        slug = (link.get("person_slug") or "").strip()
        if not slug:
            continue
        names = [
            link.get("display_name_en") or "",
            link.get("display_name_zh") or "",
            slug.replace("-", " "),
        ]
        extra = []
        for n in names:
            n = (n or "").strip()
            if not n:
                continue
            extra.append(n)
            extra.append(re.sub(r"\bjr\.?\b", "junior", n, flags=re.I))
            extra.append(re.sub(r"\bjunior\b", "jr", n, flags=re.I))
        for n in extra:
            key = n.strip()
            if len(key) < 2:
                continue
            out[key.lower()] = slug
            out[key] = slug
    _REG_ALIAS = out
    return out


_STOP = {
    "the", "me", "my", "a", "an", "in", "on", "of", "to", "for", "and", "or",
    "tell", "about", "who", "is", "what", "info", "please", "this", "that",
    "with", "from", "you", "your", "are", "was", "were", "be", "been", "it",
    "its", "at", "by", "as", "not", "no", "i", "we", "they", "he", "she",
}

_PLACE_CACHE = None


def _place_cache() -> dict:
    """City/place → org paths. Built once from org pages; no query-time rglob."""
    global _PLACE_CACHE
    if _PLACE_CACHE is not None:
        return _PLACE_CACHE
    cache_path = ECHOPEDIA_DIR / "cache" / "org_places.json"
    orgs = CONTENT_DIR / "organizations"
    mtime = orgs.stat().st_mtime if orgs.is_dir() else 0.0
    if cache_path.is_file():
        try:
            data = json.loads(cache_path.read_text(encoding="utf-8"))
            if abs(float(data.get("mtime") or 0) - mtime) < 1:
                _PLACE_CACHE = data.get("places") or {
                    k: v for k, v in data.items() if k != "mtime" and isinstance(v, list)
                }
                return _PLACE_CACHE
        except Exception:
            pass
    mapping: dict[str, list[str]] = {}
    loc_line = re.compile(r"(?im)^(?:\*\*location:\*\*|location:|地址[:：]).+$")
    city_rx = re.compile(
        r"\b([A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+)+),?\s*"
        r"(?:CA|California|NY|TX|NJ|MD|VA|WA|IL|PA|GA|FL)\b"
    )
    yaml_item = re.compile(r"(?m)^  - ([A-Z][A-Za-z .'-]{3,40})$")
    if orgs.is_dir():
        for p in orgs.glob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")[:3000]
            except OSError:
                continue
            rel = f"organizations/{p.name}"
            cities: set[str] = set()
            for line in loc_line.findall(text):
                cities.update(city_rx.findall(line))
            cities.update(city_rx.findall(text[:1500]))
            for item in yaml_item.findall(text[:600]):
                if 1 <= item.strip().count(" ") <= 3:
                    cities.add(item.strip())
            for city in cities:
                key = city.lower().strip()
                if len(key) < 5:
                    continue
                mapping.setdefault(key, []).append(rel)
    try:
        payload = {"mtime": mtime, "places": mapping}
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    except OSError:
        pass
    _PLACE_CACHE = mapping
    return mapping


def _keyword_tokens(query: str) -> list[str]:
    words = []
    for w in _expand_query_tokens(query):
        wl = w.lower().strip()
        if not wl:
            continue
        if " " in wl:
            words.append(w)
            continue
        if wl in _STOP or len(wl) < 3:
            continue
        words.append(w)
    return words


def _expand_query_tokens(query: str) -> list[str]:
    """Add alias expansions (GSTPC → church slug/title) without disk walk."""
    tokens = [w for w in re.split(r"\s+", (query or "").strip()) if len(w) >= 2]
    q_l = (query or "").lower()
    q_raw = query or ""
    try:
        alias_path = Path(__file__).resolve().parent / "ee_card_aliases.json"
        aliases = json.loads(alias_path.read_text(encoding="utf-8"))
        slugs = aliases.get("slug_aliases") or {}
        key = q_l.strip()
        if key in slugs:
            slug = slugs[key]
            tokens.append(slug.replace("-", " "))
            tokens.extend(slug.split("-"))
        for k, slug in slugs.items():
            if k and (k in q_l or k in q_raw):
                tokens.append(slug.replace("-", " "))
    except Exception:
        pass
    try:
        for k, slug in registry_slug_aliases().items():
            if not k or len(k) < 3:
                continue
            if k in q_l or k in q_raw:
                tokens.append(slug.replace("-", " "))
                tokens.extend([p for p in slug.split("-") if len(p) >= 3])
    except Exception:
        pass
    seen = set()
    out = []
    for t in tokens:
        tl = t.lower()
        if tl not in seen:
            seen.add(tl)
            out.append(t)
    return out


def _keyword_search(query, top_k=10):
    """Title/path/place keyword search over the SQLite index (no rglob)."""
    words = _keyword_tokens(query)
    if not words:
        return []
    conn = get_db()
    c = conn.cursor()
    clauses, params = [], []
    for w in words[:12]:
        clauses.append("(lower(title) LIKE ? OR lower(path) LIKE ? OR lower(ifnull(tags,'')) LIKE ?)")
        pat = f"%{w.lower()}%"
        params.extend([pat, pat, pat])
    sql = (
        "SELECT path, tier, title, page_type FROM vault_embeddings WHERE "
        + " OR ".join(clauses)
    )
    try:
        rows = c.execute(sql, params).fetchall()
    except Exception:
        return []
    by_path = {}
    q_l = (query or "").lower()
    for row in rows:
        path = row["path"] or ""
        title = row["title"] or ""
        ptype = row["page_type"] or ""
        title_l = title.lower()
        path_l = path.lower().replace("-", " ")
        score = 0
        for w in words:
            wl = w.lower()
            if " " in wl:
                if wl in title_l or wl in path_l:
                    score += 22
                continue
            if wl == title_l or title_l.startswith(wl + " "):
                score += 12
            elif re.search(rf"\b{re.escape(wl)}\b", title_l):
                score += 8
            elif wl in title_l:
                score += 2
            if re.search(rf"\b{re.escape(wl)}\b", path_l):
                score += 4
        if ptype in ("person", "organization") or path.startswith(
            ("people/", "organizations/")
        ):
            score += 8
        if path.startswith(("knowledge/", "works/", "articles/", "sources/", "events/")):
            score -= 6
        if q_l and q_l in title_l:
            score += 10
        if score > 0:
            by_path[path] = {
                "path": path,
                "tier": row["tier"],
                "title": title,
                "type": ptype,
                "score": score,
                "source": "keyword",
            }
    try:
        for place, paths in _place_cache().items():
            if place not in q_l:
                continue
            for path in paths:
                rec = by_path.get(path)
                if rec:
                    rec["score"] += 18
                    continue
                by_path[path] = {
                    "path": path,
                    "tier": 1,
                    "title": Path(path).stem.replace("-", " "),
                    "type": "organization",
                    "score": 18,
                    "source": "place",
                }
    except Exception:
        pass
    results = list(by_path.values())
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_k]


# ─── LLM reranking ──────────────────────────────────────────────────────
def llm_rerank(query, results, top_k=10):
    """Rerank search results using LLM for relevance scoring.

    Uses the local NVFP4 model via vLLM (:8888) or Grok fallback.
    Falls back to hybrid scores if LLM is unavailable.
    """
    if not results:
        return results

    # Build a prompt for the LLM
    candidates = "\n".join(
        f"{i+1}. [{r['type']}] {r['title']} — {r['path']}"
        for i, r in enumerate(results[:20])
    )

    prompt = f"""Rank these search results for the query: "{query}"

Rate each result's relevance to the query on a scale of 0-10.
Return ONLY a JSON array of objects with "index" and "score" keys.
Sort by score descending.

Results:
{candidates}

JSON:"""

    # Try to get LLM response
    llm_results = _call_llm(prompt)

    if llm_results:
        # Apply LLM scores
        for r in results:
            r["llm_score"] = 0
        for item in llm_results:
            idx = item.get("index", 0) - 1
            if 0 <= idx < len(results):
                results[idx]["llm_score"] = item.get("score", 0)

        # Combine: 40% keyword/vector, 60% LLM
        for r in results:
            r["score"] = r.get("score", 0) * 0.4 + r.get("llm_score", 0) / 10 * 0.6

        results.sort(key=lambda r: r["score"], reverse=True)
        return results[:top_k]

    # Fallback: return hybrid results as-is
    return results[:top_k]


def _call_llm(prompt):
    """Call the local NVFP4 model or Grok for LLM reranking."""
    import json
    import urllib.request

    # Try local vLLM first
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:8888/v1/chat/completions",
            data=json.dumps({
                "model": "poolside/Laguna-S-2.1-NVFP4",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1024,
                "temperature": 0.1,
            }).encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            text = data["choices"][0]["message"]["content"]
            # Parse JSON from response
            text = text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text)
    except Exception as e:
        print(f"  [warn] Local LLM failed: {e}", file=sys.stderr)

    # Fallback: Grok via /model (would need to be called from Hermes context)
    # For now, return None to use hybrid scores
    return None


# ─── Stats ──────────────────────────────────────────────────────────────
def get_stats():
    """Show vault search statistics."""
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM vault_embeddings")
    total = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM vault_embeddings WHERE tier = 1")
    tier1 = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM vault_embeddings WHERE tier = 2")
    tier2 = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM vault_graph_links")
    links = c.fetchone()[0]

    c.execute("SELECT COUNT(DISTINCT tag) FROM vault_graph_tags")
    tags = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM vault_search_history")
    searches = c.fetchone()[0]

    print(f"## Vault Search Statistics")
    print(f"")
    print(f"| Metric | Count |")
    print(f"|--------|-------|")
    print(f"| Total indexed pages | {total} |")
    print(f"| Tier 1 (public wiki) | {tier1} |")
    print(f"| Tier 2 (raw knowledge) | {tier2} |")
    print(f"| Wikilink graph edges | {links} |")
    print(f"| Unique tags | {tags} |")
    print(f"| Search history entries | {searches} |")
    print(f"")

    embedder = get_embedder()
    if embedder:
        print(f"| Embedding model | {EMBEDDING_MODEL} (384-dim) |")
    else:
        print(f"| Embedding model | not available |")


# ─── Main ───────────────────────────────────────────────────────────────
def main():
    args = sys.argv[1:]

    if "--rebuild-index" in args:
        print("Rebuilding vault index...")
        stats = index_vault(rebuild=True)
        print(f"Indexed {stats['pages']} pages (updated={stats['updated']})")
        return

    if "--rebuild-index-tier1" in args:
        print("Rebuilding vault index (Tier1 only, no embeddings)...")
        stats = index_vault(rebuild=True, tier1_only=True, with_embeddings=False)
        print(f"Indexed {stats['pages']} pages (updated={stats['updated']})")
        return

    if "--incremental-tier1" in args:
        print("Incremental vault index (Tier1, embed dirty)...")
        stats = index_vault(rebuild=False, tier1_only=True, with_embeddings=True)
        print(
            f"incremental-tier1 considered={stats['pages']} "
            f"updated={stats['updated']} skipped={stats['skipped']} pruned={stats['pruned']}"
        )
        return

    if "--stats" in args:
        get_stats()
        return

    if "--related" in args:
        idx = args.index("--related")
        if idx + 1 < len(args):
            path = args[idx + 1]
            results = find_related(path, top_k=10)
            print(f"## Related to: {path}")
            print(f"")
            for i, r in enumerate(results, 1):
                print(f"{i}. [{r['type']}] **{r['title']}**")
                print(f"   - Path: `{r['path']}`")
                print(f"   - Relation: {r['relation']} (weight: {r['weight']})")
                print(f"")
            return
        else:
            print("Usage: vault_search.py --related <path>")
            return

    if not args or "-h" in args or "--help" in args:
        print("Usage: python3 vault_search.py <query>")
        print("       python3 vault_search.py --related <path>")
        print("       python3 vault_search.py --rebuild-index")
        print("       python3 vault_search.py --rebuild-index-tier1")
        print("       python3 vault_search.py --incremental-tier1")
        print("       python3 vault_search.py --stats")
        print()
        print("Examples:")
        print('  python3 vault_search.py "Who are the theologians?"')
        print('  python3 vault_search.py "Tell me about Dr. Albert Lai"')
        print('  python3 vault_search.py --related people/albert-s-lai.md')
        return

    query = " ".join(args)

    # Ensure index exists
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM vault_embeddings")
    if c.fetchone()[0] == 0:
        print("  [info] No index found, building...")
        index_vault()

    # Hybrid search (SQL keyword + cached vectors). LLM rerank is opt-in —
    # default path must stay <1s so the 2nd brain can run on every turn.
    results = hybrid_search(query, top_k=10)
    if "--rerank" in args:
        results = llm_rerank(query, results, top_k=10)

    # Format output
    print(f"## Vault Search: \"{query}\"")
    print(f"")
    print(f"Found {len(results)} result(s) across {len(set(r['tier'] for r in results))} tier(s):")
    print(f"")

    for i, r in enumerate(results, 1):
        tier_badge = "📖" if r["tier"] == 1 else "📚"
        icon = "👤" if "person" in r.get("type", "") else "🏢" if "organization" in r.get("type", "") else "📄"

        print(f"{i}. {tier_badge} **{r['title']}** ({r.get('type', 'unknown')})")
        print(f"   - Path: `{r['path']}`")
        print(f"   - Relevance: {r['score']:.3f}")

        if r["tier"] == 1:
            badge = "✅" if r.get("verification") == "verified" else "⏳"
            print(f"   - Status: {badge} {r.get('verification', 'unknown')}")
            print(f"   - Live URL: https://echocanhelp.github.io/wiki-public/{r['path'].replace('.md', '')}")

        if "relation" in r:
            print(f"   - Related via: {r['relation']}")

        print(f"")

    # Log to search history
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        INSERT INTO vault_search_history (query, results_json, timestamp)
        VALUES (?, ?, ?)
    """, (query, json.dumps([{k: v for k, v in r.items() if k != 'source'} for r in results]),
          datetime.now().isoformat()))
    conn.commit()


if __name__ == "__main__":
    main()
