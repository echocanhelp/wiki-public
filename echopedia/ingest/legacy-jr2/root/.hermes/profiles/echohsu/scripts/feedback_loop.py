#!/usr/bin/env python3
"""
Feedback Loop Automation for Echopedia / TAHS
Auto-generates proposals from Community Intake Queue and tracks lifecycle.
Integrates with Google Sheets (intake queue), identity links, and notifications.
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Add skill paths
sys.path.insert(0, '/root/.hermes/profiles/echohsu/skills/productivity/google-workspace/scripts')

try:
    from google_api import main as gapi_main  # Reuse if possible, but we'll call directly
except:
    pass

import subprocess

SHEET_ID = "1O9y-fFX8YVBPiMJqHut6WS6X3pRAVwGubBuQ_xiMhgU"
RANGE = "Form Responses 1!A:Z"

def run_gapi(command_args):
    """Run google_api.py commands."""
    cmd = ["python3", "/root/.hermes/profiles/echohsu/skills/productivity/google-workspace/scripts/google_api.py"] + command_args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout

def get_intake_data():
    """Read intake queue data."""
    output = run_gapi(["sheets", "get", SHEET_ID, RANGE])
    if not output:
        return []
    try:
        data = json.loads(output)
        return data
    except:
        print("Failed to parse sheet data")
        return []

def generate_proposal(row):
    """Generate a structured proposal from an intake row."""
    if not row or len(row) < 3:
        return None
    
    timestamp = row[0] if len(row) > 0 else ""
    person_page = row[1] if len(row) > 1 else ""
    relationship = row[2] if len(row) > 2 else ""
    memory_quote = row[3] if len(row) > 3 else ""
    date_period = row[4] if len(row) > 4 else ""
    source_type = row[5] if len(row) > 5 else ""
    file_link = row[6] if len(row) > 6 else ""
    permission = row[7] if len(row) > 7 else ""
    privacy_notes = row[8] if len(row) > 8 else ""
    
    proposal = {
        "id": f"prop_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "timestamp": timestamp,
        "type": "community_intake",
        "target": person_page,
        "summary": f"Proposal for Echopedia page on {person_page}. Relationship: {relationship}. Key memory/quote: {memory_quote[:100]}... Date: {date_period}. Source: {source_type}. Permission: {permission}.",
        "lifecycle": "proposed",
        "created_at": datetime.now().isoformat(),
        "source_channel": "form",
        "details": {
            "relationship": relationship,
            "memory": memory_quote,
            "date": date_period,
            "link": file_link,
            "privacy": privacy_notes
        },
        "status_history": [
            {"status": "proposed", "at": datetime.now().isoformat(), "note": "Auto-generated from intake form"}
        ]
    }
    return proposal

def track_lifecycle(proposal, new_status="reviewed"):
    """Update proposal lifecycle (simulated; extend to sheet update)."""
    proposal["lifecycle"] = new_status
    proposal["status_history"].append({
        "status": new_status,
        "at": datetime.now().isoformat(),
        "note": "Automated review step"
    })
    return proposal

def main():
    print("=== Echopedia Feedback Loop Automation ===")
    print(f"Started at: {datetime.now().isoformat()}")
    
    intake_rows = get_intake_data()
    if not intake_rows:
        print("No data or error reading sheet.")
        return
    
    print(f"Found {len(intake_rows)} rows in intake queue.")
    
    proposals = []
    for i, row in enumerate(intake_rows[1:]):  # Skip header
        if row and row[0]:  # Has timestamp
            prop = generate_proposal(row)
            if prop:
                # Simulate lifecycle progression
                prop = track_lifecycle(prop, "proposed")
                proposals.append(prop)
                print(f"\n--- Proposal {i+1} ---")
                print(json.dumps(prop, indent=2, ensure_ascii=False))
    
    # Save proposals to a tracking file (working artifact output)
    output_path = Path("/root/.hermes/profiles/echohsu/cron/output/feedback_proposals.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump({"generated_at": datetime.now().isoformat(), "proposals": proposals}, f, indent=2)
    
    print(f"\n=== Summary ===")
    print(f"Generated {len(proposals)} proposals.")
    print(f"Saved to: {output_path}")
    print("Feedback loop exercised successfully. Extend with sheet updates, webhooks, or cron for full automation.")

if __name__ == "__main__":
    main()