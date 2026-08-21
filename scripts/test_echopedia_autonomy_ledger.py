#!/usr/bin/env python3
"""Tests for autonomy ledger / catalog (plan 2026-08-21_162843)."""
import importlib.util
import json
import sys
import unittest
from pathlib import Path

MOD_PATH = Path("/home/leedt/echo-system/scripts/echopedia-autonomy-collect.py")


def _load():
    spec = importlib.util.spec_from_file_location("echopedia_autonomy_collect", MOD_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["echopedia_autonomy_collect"] = mod
    spec.loader.exec_module(mod)
    return mod


class LedgerSchemaTests(unittest.TestCase):
    def test_ledger_requires_date_and_nodes(self):
        mod = _load()
        raw = mod.build_ledger(
            jobs={"jobs": []},
            janitor_run={},
            queue={},
            standards={"version": 10},
        )
        self.assertTrue(raw["date"])
        self.assertIn("nodes", raw)
        self.assertIsInstance(raw["telegram_auto_lines"], list)
        self.assertLessEqual(len(raw["telegram_auto_lines"]), 8)
        self.assertTrue(raw["telegram_auto_lines"])

    def test_first_mention_count_becomes_auto_line(self):
        mod = _load()
        ledger = mod.build_ledger(
            jobs={
                "jobs": [
                    {
                        "name": "echopedia-janitor",
                        "enabled": True,
                        "no_agent": True,
                        "last_status": "ok",
                    }
                ]
            },
            janitor_run={"healed_mentions": ["a.md", "b.md"], "healed_related": []},
            queue={
                "total_pages_scanned": 1658,
                "auto_queued": 52,
                "suppressed_findings": 0,
            },
            standards={
                "version": 10,
                "janitor": {
                    "auto_apply_agent": False,
                    "first_mention_apply": {"enabled": True},
                },
            },
            enrichment_today=[],
            kanban_blocked=[],
        )
        text = "\n".join(ledger["telegram_auto_lines"])
        self.assertIn("first-mention", text.lower())
        self.assertIn("2", text)
        self.assertTrue("suppressed 0" in text.lower() or "queued 52" in text)
        self.assertLessEqual(len(ledger["telegram_auto_lines"]), 8)

    def test_catalog_includes_first_mention_and_disabled_b(self):
        mod = _load()
        cat = mod.build_catalog(
            standards={"janitor": {"first_mention_apply": {"enabled": True}}}
        )
        ids = {n["id"] for n in cat["nodes"]}
        self.assertIn("janitor.first_mention", ids)
        b = next(n for n in cat["nodes"] if n["id"] == "kanban.auto_go")
        self.assertIs(b["enabled"], False)

    def test_load_latest_janitor_run_picks_run_at_not_page(self):
        import tempfile
        from pathlib import Path

        mod = _load()
        td = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        td.write(
            json.dumps({"run_at": "2026-08-21T00:00:00+00:00", "healed_mentions": ["x.md"]})
            + "\n"
        )
        td.write(json.dumps({"page": {"path": "p.md"}}) + "\n")
        td.write(
            json.dumps({"run_at": "2026-08-21T01:00:00+00:00", "healed_mentions": ["a.md", "b.md"]})
            + "\n"
        )
        td.close()
        rec = mod.load_latest_janitor_run(Path(td.name))
        self.assertEqual(rec.get("healed_mentions"), ["a.md", "b.md"])


if __name__ == "__main__":
    unittest.main()
