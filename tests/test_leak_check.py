"""New archive lines must show up on a page or under ## Skipped."""
from __future__ import annotations

import importlib.util
import os
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path("/home/leedt/echo-system/scripts/leak-check.py")


def load():
    spec = importlib.util.spec_from_file_location("leak_check", ROOT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class LeakCheck(unittest.TestCase):
    def test_reports_unplaced_line_and_ignores_skipped(self):
        mod = load()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            content = tmp / "content" / "people"
            content.mkdir(parents=True)
            kept = "Acme Hall opened in 1999 on Main Street with a named donor."
            skipped = "Beta Hall opened in 2001 on Oak Street beside the old chapel."
            leaked = "Gamma Hall opened in 2004 on Pine Street after the parish vote."
            (content / "acme.md").write_text(
                "---\ntitle: Acme\ntype: person\n---\n\n" + kept + "\n\n## Skipped\n\n" + skipped + "\n"
            )
            archives = tmp / "archives"
            archives.mkdir()
            arch = archives / "new.md"
            arch.write_text("\n".join([kept, skipped, leaked]) + "\n")
            now = time.time() + 5
            os.utime(arch, (now, now))
            state = tmp / "state.json"
            buf = StringIO()
            with redirect_stdout(buf):
                rc = mod.main([
                    "--archives", str(archives),
                    "--content", str(tmp / "content"),
                    "--state", str(state),
                    "--since", "0",
                ])
            out = buf.getvalue()
            self.assertEqual(rc, 0, out)
            self.assertIn("leaks=1", out)
            self.assertIn("Gamma Hall", out)
            self.assertNotIn("Beta Hall", out)
            self.assertNotIn("Acme Hall", out)
            self.assertTrue(state.is_file())


if __name__ == "__main__":
    unittest.main()
