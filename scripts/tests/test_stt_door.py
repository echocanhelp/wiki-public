#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, "/home/leedt/ai-services/media-stack/orchestrator")
from stt import resolve_engine, taigi_ready, write_sidecars  # noqa: E402


def test_zh_aliases():
    assert resolve_engine("zh") == "zh"
    assert resolve_engine("zh-TW") == "zh"
    assert resolve_engine("auto") == "zh"


def test_zh_ready_prefers_25():
    from stt import zh_ready

    assert zh_ready() is True



def test_taigi_falls_back_when_missing():
    got = resolve_engine("taigi")
    assert got in ("taigi", "zh")
    if not taigi_ready():
        assert got == "zh"


def test_sidecar_does_not_touch_tape(tmp_path: Path):
    src = tmp_path / "voice-01.m4a"
    payload = b"tape-bytes"
    src.write_bytes(payload)
    out = write_sidecars(src, {"text": "七點半", "engine": "faster-whisper-base-zh", "lang": "zh"}, None)
    assert src.read_bytes() == payload
    assert out.name == "voice-01.m4a.stt.txt"
    assert out.read_text(encoding="utf-8").strip() == "七點半"
    meta = Path(str(out)[:-4] + ".json")
    assert meta.is_file()
    assert "萌典" in meta.read_text(encoding="utf-8")
