#!/usr/bin/env python3
"""Tests for vault_search incremental index (temp vault, no network)."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path("/home/leedt/echo-system/scripts")))
import vault_search as vs  # noqa: E402


class IncrementalIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.content = root / "content"
        (self.content / "people").mkdir(parents=True)
        (self.content / "articles").mkdir(parents=True)
        (root / "knowledge" / "web-archives").mkdir(parents=True)
        (root / "knowledge" / "research").mkdir(parents=True)
        self.cache = root / "cache" / "cache.db"
        vs.ECHOPEDIA_DIR = root
        vs.CONTENT_DIR = self.content
        vs.KNOWLEDGE_DIR = root / "knowledge"
        vs.CACHE_DB = self.cache
        vs._embedder = False  # skip sentence-transformers in unit test

        (self.content / "people" / "alice.md").write_text(
            "---\ntitle: Alice\ntype: person\n---\nHello [[Bob]]\n"
        )
        (self.content / "articles" / "firehose.md").write_text("# should not index\n")
        (root / "knowledge" / "web-archives" / "scraped.md").write_text("# skip\n")
        (root / "knowledge" / "research" / "note.md").write_text("# tier2 note\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_collect_skips_articles_and_archives(self):
        pages = vs.collect_pages(tier1_only=True)
        paths = {p["path"] for p in pages}
        self.assertIn("people/alice.md", paths)
        self.assertNotIn("articles/firehose.md", paths)
        full = vs.collect_pages(tier1_only=False)
        fpaths = {p["path"] for p in full}
        self.assertTrue(any("research/note.md" in p for p in fpaths))
        self.assertFalse(any("web-archives" in p for p in fpaths))

    def test_incremental_hash_skip_and_update(self):
        s1 = vs.index_vault(rebuild=False, tier1_only=True, with_embeddings=False)
        self.assertEqual(s1["updated"], 1)
        s2 = vs.index_vault(rebuild=False, tier1_only=True, with_embeddings=False)
        self.assertEqual(s2["updated"], 0)
        self.assertEqual(s2["skipped"], 1)
        (self.content / "people" / "alice.md").write_text(
            "---\ntitle: Alice\ntype: person\n---\nChanged\n"
        )
        s3 = vs.index_vault(rebuild=False, tier1_only=True, with_embeddings=False)
        self.assertEqual(s3["updated"], 1)
        (self.content / "people" / "alice.md").unlink()
        s4 = vs.index_vault(rebuild=False, tier1_only=True, with_embeddings=False)
        self.assertGreaterEqual(s4["pruned"], 1)


if __name__ == "__main__":
    unittest.main()
