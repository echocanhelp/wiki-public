#!/usr/bin/env python3
"""echo_control_plane_sync.py - Sync control-plane truth bundle to Google Drive."""
import json
import hashlib
import subprocess
import sys
import os
from datetime import datetime, timezone

ORACLE_PATH = "/root/echo_system/environment/EnvironmentOracle.json"
PULSE_PATH = "/root/echo_system/system_pulse/SystemPulse.json"
EVOLUTION_LOG = "/root/echo_system/system_pulse/System_Evolution_Log.md"
GAPI = "python3 /root/.hermes/skills/productivity/google-workspace/scripts/google_api.py"


def sha256_of(path):
    if not os.path.exists(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.environ["GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE"] = "/root/.hermes/google_token.json"
    print(f"[control_plane_sync] Starting at {datetime.now(timezone.utc).isoformat()}")

    # Check auth first
    auth_check = subprocess.run([GAPI, "--check"], capture_output=True, text=True, timeout=10)
    if auth_check.returncode != 0:
        print(f"[control_plane_sync] ERROR: Google auth failed - {auth_check.stderr.strip()}")
        print("[control_plane_sync] Cannot sync control plane to Drive. Local verification only.")
        drive_synced = False
    else:
        drive_synced = True

    # Build truth bundle
    bundle = {
        "environment_oracle": {
            "path": ORACLE_PATH,
            "sha256": sha256_of(ORACLE_PATH),
            "exists": os.path.exists(ORACLE_PATH),
        },
        "system_pulse": {
            "path": PULSE_PATH,
            "sha256": sha256_of(PULSE_PATH),
            "exists": os.path.exists(PULSE_PATH),
        },
        "evolution_log": {
            "path": EVOLUTION_LOG,
            "sha256": sha256_of(EVOLUTION_LOG),
            "exists": os.path.exists(EVOLUTION_LOG),
        },
    }

    # Upload if auth available
    if drive_synced:
        for name, info in bundle.items():
            if info["exists"]:
                print(f"[control_plane_sync] Uploading {name} to Drive...")
                result = subprocess.run(
                    [GAPI, "drive", "upload", "--file", info["path"]],
                    capture_output=True, text=True, timeout=30
                )
                info["drive_result"] = result.stdout.strip() if result.returncode == 0 else result.stderr.strip()

    output = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "drive_synced": drive_synced,
        "bundle": bundle
    }

    with open("/root/.hermes/kanban/workspaces/t_2ca54447/control_plane_sync_result.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"[control_plane_sync] Done. bundle components={len(bundle)}, drive_synced={drive_synced}")
    return 0 if drive_synced else 1


if __name__ == "__main__":
    sys.exit(main())
