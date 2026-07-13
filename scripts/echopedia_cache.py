#!/usr/bin/env python3
"""
Echopedia Caching Layer

Provides semantic caching, response caching, and tool call caching
for Echopedia operations. Uses SQLite for persistence.

Usage:
  # Initialize cache
  python3 echopedia_cache.py init
  
  # Cache a response
  python3 echopedia_cache.py cache "query" "response"
  
  # Search cache
  python3 echopedia_cache.py search "query"
  
  # Clear cache
  python3 echopedia_cache.py clear
"""

import os
import sys
import json
import hashlib
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

CACHE_DIR = Path(os.environ.get("ECHOPEDIA_CACHE", "/home/leedt/echo-system/cache"))
CACHE_DB = CACHE_DIR / "cache.db"


class EchopediaCache:
    """Semantic and response caching for Echopedia."""
    
    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or CACHE_DB
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()
    
    def _init_db(self):
        """Initialize the cache database."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Semantic cache: stores embeddings and cached responses
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS semantic_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query_hash TEXT UNIQUE NOT NULL,
                query TEXT NOT NULL,
                response TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT 'general',
                confidence REAL NOT NULL DEFAULT 0.0,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                hit_count INTEGER NOT NULL DEFAULT 0
            )
        """)
        
        # Response cache: stores generated content
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS response_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_hash TEXT UNIQUE NOT NULL,
                request TEXT NOT NULL,
                response TEXT NOT NULL,
                response_type TEXT NOT NULL DEFAULT 'text',
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL
            )
        """)
        
        # Tool call cache: stores API/web search results
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tool_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tool_name TEXT NOT NULL,
                params_hash TEXT NOT NULL,
                params TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                hit_count INTEGER NOT NULL DEFAULT 0
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_semantic_query ON semantic_cache(query_hash)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_response_request ON response_cache(request_hash)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_tool_params ON tool_cache(params_hash)")
        
        conn.commit()
        conn.close()
    
    def _hash(self, text: str) -> str:
        """Create a hash of text for caching."""
        return hashlib.sha256(text.encode()).hexdigest()
    
    def _now(self) -> str:
        """Get current ISO timestamp."""
        return datetime.now().isoformat()
    
    def _expires(self, hours: int = 24) -> str:
        """Get expiration timestamp."""
        return (datetime.now() + timedelta(hours=hours)).isoformat()
    
    # Semantic Cache
    def cache_response(self, query: str, response: str, category: str = "general", confidence: float = 0.0, hours: int = 24) -> bool:
        """Cache a query-response pair."""
        query_hash = self._hash(query)
        expires = self._expires(hours)
        now = self._now()
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO semantic_cache 
                (query_hash, query, response, category, confidence, created_at, expires_at, hit_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, 0)
            """, (query_hash, query, response, category, confidence, now, expires))
            conn.commit()
            return True
        except Exception as e:
            print(f"Cache error: {e}", file=sys.stderr)
            return False
        finally:
            conn.close()
    
    def search_cache(self, query: str, threshold: float = 0.8) -> Optional[dict]:  # type: ignore[return-value]
        """Search the semantic cache for matching queries."""
        query_hash = self._hash(query)
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            # Exact match first
            cursor.execute("""
                SELECT query, response, category, confidence, created_at, hit_count
                FROM semantic_cache
                WHERE query_hash = ? AND expires_at > ?
                ORDER BY hit_count DESC
                LIMIT 1
            """, (query_hash, self._now()))
            
            row = cursor.fetchone()
            if row:
                # Increment hit count
                cursor.execute("""
                    UPDATE semantic_cache SET hit_count = hit_count + 1
                    WHERE query_hash = ?
                """, (query_hash,))
                conn.commit()
                
                return {
                    "query": row[0],
                    "response": row[1],
                    "category": row[2],
                    "confidence": row[3],
                    "created_at": row[4],
                    "hit_count": row[5],
                    "match_type": "exact"
                }
            
            # Fuzzy match (simple keyword overlap)
            query_words = set(query.lower().split())
            best_match = None
            best_score = 0
            
            cursor.execute("""
                SELECT query, response, category, confidence, created_at, hit_count
                FROM semantic_cache
                WHERE expires_at > ?
            """, (self._now(),))
            
            for row in cursor.fetchall():
                cached_words = set(row[0].lower().split())
                overlap = len(query_words & cached_words) / max(len(query_words | cached_words), 1)
                
                if overlap > best_score and overlap >= threshold:
                    best_score = overlap
                    best_match = row
            
            if best_match:
                # Increment hit count
                best_hash = self._hash(best_match[0])
                cursor.execute("""
                    UPDATE semantic_cache SET hit_count = hit_count + 1
                    WHERE query_hash = ?
                """, (best_hash,))
                conn.commit()
                
                return {
                    "query": best_match[0],
                    "response": best_match[1],
                    "category": best_match[2],
                    "confidence": best_match[3],
                    "created_at": best_match[4],
                    "hit_count": best_match[5],
                    "match_type": "fuzzy",
                    "similarity": best_score
                }
            
            return None
        finally:
            conn.close()
    
    # Response Cache
    def cache_response_type(self, request: str, response: str, response_type: str = "text", hours: int = 24) -> bool:
        """Cache a response by request type."""
        request_hash = self._hash(request)
        expires = self._expires(hours)
        now = self._now()
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO response_cache
                (request_hash, request, response, response_type, created_at, expires_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (request_hash, request, response, response_type, now, expires))
            conn.commit()
            return True
        except Exception as e:
            print(f"Cache error: {e}", file=sys.stderr)
            return False
        finally:
            conn.close()
    
    def get_cached_response(self, request: str) -> Optional[dict]:  # type: ignore[return-value]
        """Get a cached response by request."""
        request_hash = self._hash(request)
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT response, response_type, created_at
                FROM response_cache
                WHERE request_hash = ? AND expires_at > ?
                LIMIT 1
            """, (request_hash, self._now()))
            
            row = cursor.fetchone()
            if row:
                return {
                    "response": row[0],
                    "response_type": row[1],
                    "created_at": row[2]
                }
            return None
        finally:
            conn.close()
    
    # Tool Cache
    def cache_tool_result(self, tool_name: str, params: dict, result: str, hours: int = 24) -> bool:
        """Cache a tool call result."""
        params_hash = self._hash(json.dumps(params, sort_keys=True))
        expires = self._expires(hours)
        now = self._now()
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO tool_cache
                (tool_name, params_hash, params, result, created_at, expires_at, hit_count)
                VALUES (?, ?, ?, ?, ?, ?, 0)
            """, (tool_name, params_hash, json.dumps(params), result, now, expires))
            conn.commit()
            return True
        except Exception as e:
            print(f"Cache error: {e}", file=sys.stderr)
            return False
        finally:
            conn.close()
    
    def get_cached_tool_result(self, tool_name: str, params: dict) -> Optional[dict]:  # type: ignore[return-value]
        """Get a cached tool result."""
        params_hash = self._hash(json.dumps(params, sort_keys=True))
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT result, created_at, hit_count
                FROM tool_cache
                WHERE tool_name = ? AND params_hash = ? AND expires_at > ?
                LIMIT 1
            """, (tool_name, params_hash, self._now()))
            
            row = cursor.fetchone()
            if row:
                # Increment hit count
                cursor.execute("""
                    UPDATE tool_cache SET hit_count = hit_count + 1
                    WHERE tool_name = ? AND params_hash = ?
                """, (tool_name, params_hash))
                conn.commit()
                
                return {
                    "result": row[0],
                    "created_at": row[1],
                    "hit_count": row[2]
                }
            return None
        finally:
            conn.close()
    
    # Cache Management
    def clear_expired(self) -> int:
        """Remove expired cache entries."""
        now = self._now()
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("DELETE FROM semantic_cache WHERE expires_at < ?", (now,))
            semantic_count = cursor.rowcount
            
            cursor.execute("DELETE FROM response_cache WHERE expires_at < ?", (now,))
            response_count = cursor.rowcount
            
            cursor.execute("DELETE FROM tool_cache WHERE expires_at < ?", (now,))
            tool_count = cursor.rowcount
            
            conn.commit()
            
            total = semantic_count + response_count + tool_count
            return total
        finally:
            conn.close()
    
    def clear_all(self) -> int:
        """Clear all cache entries."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("DELETE FROM semantic_cache")
            semantic_count = cursor.rowcount
            
            cursor.execute("DELETE FROM response_cache")
            response_count = cursor.rowcount
            
            cursor.execute("DELETE FROM tool_cache")
            tool_count = cursor.rowcount
            
            conn.commit()
            
            total = semantic_count + response_count + tool_count
            return total
        finally:
            conn.close()
    
    def stats(self) -> dict:
        """Get cache statistics."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT COUNT(*) FROM semantic_cache")
            semantic_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM response_cache")
            response_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM tool_cache")
            tool_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT SUM(hit_count) FROM semantic_cache")
            semantic_hits = cursor.fetchone()[0] or 0
            
            cursor.execute("SELECT SUM(hit_count) FROM tool_cache")
            tool_hits = cursor.fetchone()[0] or 0
            
            return {
                "semantic_cache": {
                    "entries": semantic_count,
                    "hits": semantic_hits
                },
                "response_cache": {
                    "entries": response_count
                },
                "tool_cache": {
                    "entries": tool_count,
                    "hits": tool_hits
                },
                "total_entries": semantic_count + response_count + tool_count,
                "total_hits": semantic_hits + tool_hits
            }
        finally:
            conn.close()


def main():
    """CLI interface for the cache."""
    cache = EchopediaCache()
    
    if len(sys.argv) < 2:
        print("Usage: python3 echopedia_cache.py <command> [args]")
        print()
        print("Commands:")
        print("  init                    Initialize cache database")
        print("  cache <query> <response>  Cache a query-response pair")
        print("  search <query>          Search cache for a query")
        print("  clear                   Clear all cache entries")
        print("  clear-expired           Remove expired entries")
        print("  stats                   Show cache statistics")
        return
    
    command = sys.argv[1]
    
    if command == "init":
        print("✅ Cache database initialized")
    
    elif command == "cache":
        if len(sys.argv) < 4:
            print("Usage: python3 echopedia_cache.py cache <query> <response>")
            return
        
        query = sys.argv[2]
        response = sys.argv[3]
        
        if cache.cache_response(query, response):
            print(f"✅ Cached response for: {query[:50]}...")
        else:
            print("❌ Failed to cache response", file=sys.stderr)
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: python3 echopedia_cache.py search <query>")
            return
        
        query = " ".join(sys.argv[2:])
        result = cache.search_cache(query)
        
        if result:
            print(f"✅ Cache hit! ({result['match_type']})")
            print(f"   Query: {result['query']}")
            print(f"   Response: {result['response'][:200]}...")
            print(f"   Hits: {result['hit_count']}")
        else:
            print("❌ No cache hit")
    
    elif command == "clear":
        count = cache.clear_all()
        print(f"✅ Cleared {count} cache entries")
    
    elif command == "clear-expired":
        count = cache.clear_expired()
        print(f"✅ Removed {count} expired entries")
    
    elif command == "stats":
        stats = cache.stats()
        print("📊 Cache Statistics:")
        print(f"   Semantic cache: {stats['semantic_cache']['entries']} entries, {stats['semantic_cache']['hits']} hits")
        print(f"   Response cache: {stats['response_cache']['entries']} entries")
        print(f"   Tool cache: {stats['tool_cache']['entries']} entries, {stats['tool_cache']['hits']} hits")
        print(f"   Total: {stats['total_entries']} entries, {stats['total_hits']} hits")
    
    else:
        print(f"❌ Unknown command: {command}")


if __name__ == "__main__":
    main()