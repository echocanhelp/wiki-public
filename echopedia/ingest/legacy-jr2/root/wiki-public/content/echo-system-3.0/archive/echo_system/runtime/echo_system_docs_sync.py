#!/usr/bin/env python3
"""echo_system_docs_sync.py - Sync all canonical docs to Google Drive."""
import json
import hashlib
import subprocess
import sys
import os
from datetime import datetime, timezone

DOCS_DIR = "/root/echo_system/docs"
CANONICAL_DOCS = [
    {"doc_id": "master_index", "file": "Echo_System_Master_Index.md", "owner": "Archivist"},
    {"doc_id": "vision_architecture", "file": "Echo_System_Vision_Architecture.md", "owner": "Orchestrator"},
    {"doc_id": "agent_prompts", "file": "Echo_System_Agent_Prompts.md", "owner": "Orchestrator"},
    {"doc_id": "knowledge_core", "file": "Echo_System_Knowledge_Core.md", "owner": "Archivist + Historian"},
    {"doc_id": "runtime_self_management", "file": "Echo_System_Runtime_and_Self_Management.md", "owner": "Orchestrator + Sentinel"},
    {"doc_id": "operations_guide", "file": "Echo_System_Operations_Guide.md", "owner": "ToolGateway + Orchestrator"},
]

ORACLE_PATH = "/root/echo_system/environment/EnvironmentOracle.json"
GAPI = "python3 /root/.hermes/skills/productivity/google-workspace/scripts/google_api.py"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sync_doc_to_drive(doc):
    """Upload/update a single doc to Google Drive."""
    local_path = os.path.join(DOCS_DIR, doc["file"])
    result = subprocess.run(
        [GAPI, "drive", "upload", "--file", local_path],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        return {"status": "failed", "error": result.stderr.strip()}
    return json.loads(result.stdout)


def main():
    os.environ["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = "/root/.hermes/google_token.json"
    print(f"[docs_sync] Starting at {datetime.now(timezone.utc).isoformat()}")
    results = []

    # Check auth first
    auth_check = subprocess.run([GAPI, "--check"], capture_output=True, text=True, timeout=10)
    if auth_check.returncode != 0:
        print(f"[docs_sync] ERROR: Google auth failed - {auth_check.stderr.strip()}")
        print("[docs_sync] Cannot sync to Drive. Proceeding with local hash computation only.")
        drive_synced = False
    else:
        drive_synced = True

    # Compute hashes
    for doc in CANONICAL_DOCS:
        local_path = os.path.join(DOCS_DIR, doc["file"])
        doc["sha256"] = sha256_of(local_path)
        doc["size_bytes"] = os.path.getsize(local_path)
        doc["local_path"] = local_path
        print(f"  {doc['doc_id']}: sha256={doc['sha256'][:16]}... size={doc['size_bytes']}")
        results.append(doc)

    # Sync to Drive if auth available
    if drive_synced:
        for doc in results:
            print(f"[docs_sync] Uploading {doc['file']} to Drive...")
            upload_result = sync_doc_to_drive(doc)
            doc["drive_result"] = upload_result
            print(f"  Result: {upload_result.get('status', 'unknown')}")

    # Save results
    output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "drive_synced": drive_synced,
        "docs": results
    }

    with open("/root/.hermes/kanban/workspaces/t_2ca54447/docs_sync_result.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"[docs_sync] Done. {len(results)} docs processed, drive_synced={drive_synced}")
    return 0 if drive_synced else 1


if __name__ == "__main__":
    sys.exit(main())
