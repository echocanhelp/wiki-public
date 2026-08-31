#!/usr/bin/env python3
"""Copy inbound LINE media into the oral-stories vault. No transcode-in-place."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ROOT = Path("/home/leedt/echo-system/knowledge/oral-stories/media")


def ingest_media(
    *,
    src: Path,
    dest_root: Path = DEFAULT_ROOT,
    date: str,
    display_slug: str,
    kind: str = "voice",
    sitting: str = "",
    consent_archive: bool = True,
    consent_voice_bank: bool = False,
    consent_resonance_ref: bool = False,
) -> dict:
    src = Path(src)
    if not src.is_file():
        raise FileNotFoundError(src)
    kind = kind if kind in ("voice", "photo", "video", "file") else "file"
    ext = src.suffix.lower() or { "voice": ".m4a", "photo": ".jpg", "video": ".mp4" }.get(kind, ".bin")
    folder = dest_root / f"{date}-{display_slug}"
    folder.mkdir(parents=True, exist_ok=True)
    n = 1
    while True:
        dest = folder / f"{kind}-{n:02d}{ext}"
        if not dest.exists():
            break
        n += 1
    shutil.copy2(src, dest)
    dest.chmod(0o600)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    meta = {
        "sha256": digest,
        "kind": kind,
        "bytes": dest.stat().st_size,
        "src_name": src.name,
        "sitting": sitting,
        "consent": {
            "archive": consent_archive,
            "voice_bank": consent_voice_bank,
            "resonance_ref": consent_resonance_ref,
        },
        "ingested_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    meta_path = dest.with_name(dest.stem + ".meta.json")
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    meta_path.chmod(0o600)
    return {"path": str(dest), "sha256": digest, "seq": n, "meta": str(meta_path)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--kind", default="voice")
    ap.add_argument("--sitting", default="")
    args = ap.parse_args()
    out = ingest_media(
        src=Path(args.src),
        date=args.date,
        display_slug=args.slug,
        kind=args.kind,
        sitting=args.sitting,
    )
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
