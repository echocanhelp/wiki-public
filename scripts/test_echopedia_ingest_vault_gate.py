#!/usr/bin/env python3
"""Vault coverage gate: high-value units without a body are PARTIAL."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MOD = Path("/home/leedt/echo-system/scripts/echopedia-ingest-complete.py")
spec = importlib.util.spec_from_file_location("ingest_complete", MOD)
mod = importlib.util.module_from_spec(spec)
sys.modules["ingest_complete"] = mod
spec.loader.exec_module(mod)

CLS = Path("/home/leedt/echo-system/scripts/echopedia-source-class.py")
cspec = importlib.util.spec_from_file_location("source_class", CLS)
cmod = importlib.util.module_from_spec(cspec)
sys.modules["source_class"] = cmod
cspec.loader.exec_module(cmod)


class VaultGateTests(unittest.TestCase):
    def test_missing_body_is_gap(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            sid = "tah-test"
            units = repo / "knowledge" / "research" / sid / "units.jsonl"
            vault = repo / "knowledge" / "web-archives" / sid / "posts"
            units.parent.mkdir(parents=True)
            vault.mkdir(parents=True)
            units.write_text(
                json.dumps(
                    {
                        "unit_id": "1",
                        "url": "https://example.org/our-journey-1",
                        "value_band": "A",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            gaps = mod.vault_gaps(repo, sid)
            self.assertTrue(gaps)
            self.assertIn("missing 1/1", gaps[0])

    def test_body_on_disk_clears_gap(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            sid = "tah-test"
            units = repo / "knowledge" / "research" / sid / "units.jsonl"
            vault = repo / "knowledge" / "web-archives" / sid / "posts"
            units.parent.mkdir(parents=True)
            vault.mkdir(parents=True)
            units.write_text(
                json.dumps(
                    {
                        "unit_id": "1",
                        "url": "https://example.org/our-journey-1",
                        "value_band": "A",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            (vault / "our-journey-1.md").write_text("# x\n" + ("body line of historical text\n" * 40), encoding="utf-8")
            self.assertEqual(mod.vault_gaps(repo, sid), [])

    def test_tah_host_is_directory_corpus(self):
        self.assertEqual(
            cmod.classify(
                {
                    "posts_total": 9739,
                    "pages_total": 128,
                    "cms": "wordpress",
                    "host": "www.taiwaneseamericanhistory.org",
                }
            ),
            "directory-corpus",
        )


if __name__ == "__main__":
    unittest.main()
