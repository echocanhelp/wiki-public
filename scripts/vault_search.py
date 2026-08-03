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
def index_vault(rebuild=False):
    """Build or update the vector + graph index for all vault pages."""
    conn = get_db()
    c = conn.cursor()

    embedder = get_embedder()
    if embedder is False:
        print("  [info] No embedding model available — indexing graph only")

    # Collect all pages
    pages = []

    # Tier 1: content/ (exclude Tier2 archive under content/articles/)
    for md_file in CONTENT_DIR.rglob("*.md"):
        rel = md_file.relative_to(CONTENT_DIR)
        rel_s = str(rel).replace("\\", "/")
        if rel.name.startswith(".") or "index" in rel_s:
            continue
        if rel_s.startswith("articles/") or "/articles/" in rel_s:
            continue
        if "*" in rel.name or not md_file.is_file():
            continue
        try:
            content = md_file.read_text(errors="replace")
        except OSError as e:
            print(f"  [warn] skip {rel_s}: {e}", file=sys.stderr)
            continue
        fm = extract_frontmatter(content)
        body = extract_body(content)
        pages.append({
            "path": str(rel),
            "tier": 1,
            "content": content,
            "body": body,
            "fm": fm,
        })

    # Tier 2: knowledge/ (skip web-archives bulk if present)
    for md_file in KNOWLEDGE_DIR.rglob("*.md"):
        rel = md_file.relative_to(ECHOPEDIA_DIR)
        rel_s = str(rel).replace("\\", "/")
        if rel.name.startswith("."):
            continue
        if "web-archives/" in rel_s or "/articles/" in rel_s:
            continue
        if "*" in rel.name or not md_file.is_file():
            continue
        try:
            content = md_file.read_text(errors="replace")
        except OSError as e:
            print(f"  [warn] skip {rel_s}: {e}", file=sys.stderr)
            continue
        fm = extract_frontmatter(content)
        body = extract_body(content)
        pages.append({
            "path": str(rel),
            "tier": 2,
            "content": content,
            "body": body,
            "fm": fm,
        })

    print(f"  [info] Found {len(pages)} pages to index")

    # Clear old graph if rebuilding
    if rebuild:
        c.execute("DELETE FROM vault_embeddings")
        c.execute("DELETE FROM vault_graph_links")
        c.execute("DELETE FROM vault_graph_tags")
        conn.commit()

    # Index each page
    for page in pages:
        path = page["path"]
        ch = content_hash(page["content"])

        # Skip if already indexed and unchanged
        if not rebuild:
            c.execute("SELECT content_hash FROM vault_embeddings WHERE path = ?", (path,))
            row = c.fetchone()
            if row and row["content_hash"] == ch:
                continue

        fm = page["fm"]
        title = fm.get("title", Path(path).stem)
        page_type = fm.get("type", "unknown")
        tags = extract_tags(fm)

        # Generate embedding
        if embedder:
            # Use title + first 500 chars of body for embedding
            embed_text = f"{title}\n{page['body'][:500]}"
            import numpy as np
            emb = embedder.encode(embed_text)
            embedding = np.asarray(emb, dtype=np.float32).tobytes()
        else:
            embedding = b"\x00" * 384  # placeholder

        # Store embedding
        c.execute("""
            INSERT OR REPLACE INTO vault_embeddings
            (path, tier, title, page_type, tags, embedding, content_hash, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (path, page["tier"], title, page_type, ",".join(tags),
              embedding, ch, datetime.now().isoformat()))

        # Store wikilinks
        for link in extract_wikilinks(page["body"]):
            # Normalize link to path
            target = link.replace("|", "").strip()
            # Try to resolve to a known path
            target_path = _resolve_wikilink(target, pages)
            if target_path:
                c.execute("""
                    INSERT OR IGNORE INTO vault_graph_links
                    (source, target, link_type) VALUES (?, ?, 'wikilink')
                """, (path, target_path))

        # Store tags
        for tag in tags:
            c.execute("""
                INSERT OR IGNORE INTO vault_graph_tags (tag, path) VALUES (?, ?)
            """, (tag, path))

    conn.commit()
    print(f"  [info] Indexed {len(pages)} pages")
    return len(pages)


def _resolve_wikilink(link, pages):
    """Resolve a wikilink to a known page path."""
    # Build a lookup from title/slug to path
    lookup = {}
    for p in pages:
        fm = p["fm"]
        title = fm.get("title", Path(p["path"]).stem)
        slug = Path(p["path"]).stem
        lookup[title.lower()] = p["path"]
        lookup[slug.lower()] = p["path"]
        # Also try content/people/slug format
        lookup[f"people/{slug}"] = p["path"]
        lookup[f"organizations/{slug}"] = p["path"]

    # Try direct match
    if link.lower() in lookup:
        return lookup[link.lower()]

    # Try with people/ prefix
    if f"people/{link.lower()}" in lookup:
        return lookup[f"people/{link.lower()}"]

    # Try with organizations/ prefix
    if f"organizations/{link.lower()}" in lookup:
        return lookup[f"organizations/{link.lower()}"]

    return None


# ─── Vector search ──────────────────────────────────────────────────────
def vector_search(query, top_k=10):
    """Semantic search using embeddings."""
    embedder = get_embedder()
    if not embedder:
        return []

    conn = get_db()
    c = conn.cursor()

    # Get all embeddings
    c.execute("SELECT path, tier, title, page_type, embedding FROM vault_embeddings")
    rows = c.fetchall()

    if not rows:
        return []

    # Encode query
    query_emb = embedder.encode(query)

    # Compute cosine similarity
    import numpy as np
    results = []
    for row in rows:
        emb = np.frombuffer(row["embedding"], dtype=np.float32)
        if emb.shape[0] != query_emb.shape[0]:
            continue
        # Cosine similarity
        sim = float(np.dot(query_emb, emb) / (np.linalg.norm(query_emb) * np.linalg.norm(emb) + 1e-8))
        results.append({
            "path": row["path"],
            "tier": row["tier"],
            "title": row["title"],
            "type": row["page_type"],
            "score": sim,
            "source": "vector",
        })

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_k]


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

    # 2. Vector search
    vector_results = vector_search(query, top_k * 3)

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
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_k]


def _keyword_search(query, top_k=10):
    """Existing keyword search logic from knowledge_qa.py."""
    query_lower = query.lower()
    query_words = set(query_lower.split())

    results = []

    # Tier 1: content/
    for md_file in CONTENT_DIR.rglob("*.md"):
        rel = md_file.relative_to(CONTENT_DIR)
        if rel.name.startswith(".") or "index" in str(rel):
            continue
        content = md_file.read_text()
        fm = extract_frontmatter(content)
        body = extract_body(content)
        page_type = fm.get("type", "")
        if page_type not in ("person", "organization"):
            continue
        title = fm.get("title", md_file.stem)
        score = 0
        for word in query_words:
            if word in title.lower():
                score += 10
            if word in body.lower():
                score += 1
        wikilinks = extract_wikilinks(body)
        for link in wikilinks:
            for word in query_words:
                if word in link.lower():
                    score += 3
        if score > 0:
            results.append({
                "title": title, "path": str(rel), "type": f"wiki/{page_type}",
                "tier": 1, "score": score,
                "verification": fm.get("verification_status", "unknown"),
                "source": "public_wiki",
            })

    # Tier 2: knowledge/ (skip web-archives bulk if present)
    for md_file in KNOWLEDGE_DIR.rglob("*.md"):
        rel = md_file.relative_to(ECHOPEDIA_DIR)
        rel_s = str(rel).replace("\\", "/")
        if rel.name.startswith("."):
            continue
        if "web-archives/" in rel_s or "/articles/" in rel_s:
            continue
        if "*" in rel.name or not md_file.is_file():
            continue
        try:
            content = md_file.read_text(errors="replace")
        except OSError as e:
            print(f"  [warn] skip {rel_s}: {e}", file=sys.stderr)
            continue
        fm = extract_frontmatter(content)
        body = extract_body(content)
        title = fm.get("title", md_file.stem)
        category = fm.get("category", "knowledge")
        score = 0
        for word in query_words:
            if word in title.lower():
                score += 10
            if word in body.lower():
                score += 1
        if score > 0:
            results.append({
                "title": title, "path": str(rel), "type": f"knowledge/{category}",
                "tier": 2, "score": score,
                "verification": fm.get("verification_status", "raw"),
                "source": category,
            })

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
        count = index_vault(rebuild=True)
        print(f"Indexed {count} pages")
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

    # Hybrid search
    results = hybrid_search(query, top_k=10)

    # LLM rerank
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
