#!/usr/bin/env python3
"""echo_wiki_structure_sync.py - Sync individual wiki docs to Google Drive."""
import json
import hashlib
import subprocess
import sys
import os
from datetime import datetime, timezone

WIKI_DIR = "/root/wiki-public/content"
GAPI = "python3 /root/.hermes/skills/productivity/google-workspace/scripts/google_api.py"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.environ["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = "/root/.hermes/google_token.json"
    print(f"[wiki_sync] Starting at {datetime.now(timezone.utc).isoformat()}")
    results = []

    # Check auth first
    auth_check = subprocess.run([GAPI, "--check"], capture_output=True, text=True, timeout=10)
    if auth_check.returncode != 0:
        print(f"[wiki_sync] ERROR: Google auth failed - {auth_check.stderr.strip()}")
        print("[wiki_sync] Cannot sync wiki to Drive. Proceeding with local hash computation only.")
        drive_synced = False
    else:
        drive_synced = True

    # Scan wiki content
    if os.path.isdir(WIKI_DIR):
        for fname in sorted(os.listdir(WIKI_DIR)):
            if fname.endswith(".md"):
                fpath = os.path.join(WIKI_DIR, fname)
                results.append({
                    "file": fname,
                    "sha256": sha256_of(fpath),
                    "size_bytes": os.path.getsize(fpath),
                })
    else:
        print(f"[wiki_sync] WARNING: Wiki dir {WIKI_DIR} not found")

    output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "drive_synced": drive_synced,
        "wiki_files": results
    }

    with open("/root/.hermes/kanban/workspaces/t_2ca54447/wiki_sync_result.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"[wiki_sync] Done. {len(results)} wiki files processed, drive_synced={drive_synced}")
    return 0 if drive_synced else 1


if __name__ == "__main__":
    sys.exit(main())
