#!/usr/bin/env python3
"""echo-media-manifest.py — P2 of the Echo Resonance / 歲月有聲 media-integration.

Scan the audio-blob SSOT directory (~/media-outputs/jobs/*.wav) and populate /
merge ~/echo-system/media/_manifest.json (THE catalog — source of truth).

This is a REGISTER step: it reads blobs + sidecars and auto-fills *derivable* fields
(slug, asset, size, mtime, produced_at, engine, kind). It intentionally does **not**
touch entities[] (human/agent-assigned in P3) and does **not** copy blobs — the WAVs
are the single source of truth (SSOT), the manifest only records the relation.

Usage:
  echo-media-manifest.py [--jobs-dir DIR] [--manifest PATH] [--status STAGED]

Re-run anytime; it merges by id (idempotent).
"""
import argparse, json, os, re, datetime

def slugify(fn: str) -> str:
    # Strip .wav; keep the HeartMuLa/agent-assigned token verbatim.
    base = os.path.basename(fn)
    if base.lower().endswith(".wav"):
        base = base[:-4]
    return base.lower().strip().replace(" ", "-")

def engine_for(slug: str) -> str:
    s = slug.lower()
    if s.startswith("whisper") or "smoke" in s:
        return "whisper"
    if s.startswith("tts"):
        return "tts"
    if s.startswith("selftest"):
        return "HeartMuLa"  # test render, still HeartMuLa pipeline
    return "HeartMuLa"

def kind_for(slug: str) -> str:
    # Heuristic; the vast majority here are HeartMuLa music. Nudgers in P3.
    s = slug.lower()
    if s.startswith("whisper") or s.startswith("tts"):
        return "test"  # non-production; P3 can promote/demote
    if "quote" in s or "quote" in (os.path.basename(slug)):
        return "narration"
    return "music"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs-dir", default=os.path.expanduser("~/media-outputs/jobs"))
    ap.add_argument("--manifest", default=os.path.expanduser(
        "~/echo-system/media/_manifest.json"))
    ap.add_argument("--status", default="staged")
    args = ap.parse_args()

    if not os.path.isdir(args.jobs_dir):
        raise SystemExit(f"jobs dir not found: {args.jobs_dir}")

    existing = {}
    if os.path.exists(args.manifest):
        with open(args.manifest, "r", encoding="utf-8") as f:
            existing = {e["id"]: e for e in json.load(f).get("entries", [])}

    out_dir = os.path.dirname(args.manifest)
    os.makedirs(out_dir, exist_ok=True)

    entries, seen = {}, []
    # seed from existing so register only *adds/updates*
    seen = list(existing.keys())
    entries.update(existing)

    for fn in sorted(os.listdir(args.jobs_dir)):
        if not fn.lower().endswith(".wav"):
            continue
        path = os.path.join(args.jobs_dir, fn)
        slug = slugify(fn)
        if slug in seen:
            # already cataloged -> refresh auto fields only
            st = os.stat(path)
            entries[slug]["size_bytes"] = st.st_size
            entries[slug]["mtime"] = datetime.datetime.utcfromtimestamp(
                st.st_mtime).strftime("%Y-%m-%dT%H:%M:%SZ")
            entries[slug]["produced_at"] = datetime.datetime.utcfromtimestamp(
                st.st_mtime).strftime("%Y-%m-%d")
            continue
        seen.append(slug)

        st = os.stat(path)
        entry = {
            "id": slug,
            "slug": slug,
            "kind": kind_for(slug),
            "asset": path,  # blob SSOT path (gitignored, repo-external)
            "size_bytes": st.st_size,
            "language": "zh-TW",  # default; P3 refine (en|zh-TW|bilingual)
            "entities": [],       # human/agent-assigned in P3 (no blind auto-merge)
            "source": "heartmula::job::" + slug,
            "interpretation": True,
            "disclaimer": "",       # inherited from manifest top-level when empty
            "produced_at": datetime.datetime.utcfromtimestamp(
                st.st_mtime).strftime("%Y-%m-%d"),
            "engine": engine_for(slug),
            "status": args.status,
        }
        entries[slug] = entry

    catalog = {
        "version": 1,
        "brand": "echo-resonance",
        "name_en": "Echo Resonance",
        "name_zh": "歲月有聲",
        "disclaimer": (
            "Echopedia records facts. This piece is an AI "
            "interpretation built from those facts — creative, not verified "
            "history. Treat it as a story inspired by truth, not a primary "
            "source."),
        "disclaimer_zh": (
            "Echopedia 記錄事實；本作品則據這些事實以 AI 創作，屬藝術詮釋而非查證之史實。"
            "請視為源於真實的故事，而非第一手史料。"),
        "interpretation": True,
        "updated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "entries": [entries[k] for k in seen],
    }
    with open(args.manifest, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"manifest: {args.manifest}")
    print(f"entries cataloged: {len(seen)}")
    kinds = {}
    for e in catalog["entries"]:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    print("by kind:", kinds)

if __name__ == "__main__":
    main()
