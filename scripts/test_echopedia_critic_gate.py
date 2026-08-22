#!/usr/bin/env python3
"""Tests for echopedia-critic-gate (no LLM)."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

GATE_PATH = Path("/home/leedt/echo-system/scripts/echopedia-critic-gate.py")
spec = importlib.util.spec_from_file_location("echopedia_critic_gate", GATE_PATH)
gate = importlib.util.module_from_spec(spec)
sys.modules["echopedia_critic_gate"] = gate
spec.loader.exec_module(gate)


class CriticGateTests(unittest.TestCase):
    def test_reject_planted_year(self):
        proposed = """# Test Person

Born in 1492 in nowhere.

## Sources
- https://example.com/real
"""
        sources = ["Albert S. Lai was born in 1934 in Taiwan."]
        r = gate.evaluate(proposed, sources)
        self.assertEqual(r["decision"], "reject")
        self.assertTrue(any("unsupported_years" in x and "1492" in x for x in r["reasons"]))

    def test_accept_cited_year(self):
        proposed = """# Albert S. Lai

Born in 1934 in Taiwan.

## Sources
- https://example.com/lai
"""
        sources = ["Albert S. Lai was born in 1934 in Taiwan. He later served FPCLA."]
        r = gate.evaluate(proposed, sources)
        self.assertEqual(r["decision"], "accept", r)

    def test_reject_missing_sources_section(self):
        r = gate.evaluate("Born in 1934.\n", ["born 1934"])
        self.assertEqual(r["decision"], "reject")
        self.assertIn("missing_sources_section", r["reasons"])

    def test_reject_birth_conflict(self):
        proposed = """# X

He was born in 1910.

## Sources
- https://example.com/x
"""
        sources = ["He was born in 1911 according to the legal record."]
        r = gate.evaluate(proposed, sources)
        self.assertEqual(r["decision"], "reject")
        self.assertTrue(any("birth_conflict" in x for x in r["reasons"]))

    def test_cli_accept_files(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            prop = td / "p.md"
            src = td / "s.txt"
            prop.write_text("# A\n\nBorn in 1934.\n\n## Sources\n- https://ex.com\n")
            src.write_text("Born in 1934 in Taiwan.")
            rc = gate.main(["--proposed", str(prop), "--source", str(src)])
            self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
