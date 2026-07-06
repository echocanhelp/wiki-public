#!/usr/bin/env python3
"""
Upload Watcher for echohsu
Vision analysis via --image flag + automatic reply back to LINE user
"""

import os
import json
import time
import glob
import subprocess
import requests

NOTIFY_DIR = "/root/.hermes/profiles/echohsu/uploads/notifications"
PROCESSED = set()

# Load LINE credentials
CRED_PATH = "/root/.hermes/profiles/echohsu/line_sources.json"
with open(CRED_PATH) as f:
    creds = json.load(f)

CHANNEL_ACCESS_TOKEN = creds["channel_access_token"]

def send_line_push(user_id: str, text: str):
    """Send a push message back to the LINE user"""
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    body = {
        "to": user_id,
        "messages": [{"type": "text", "text": text}]
    }
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=10)
        if resp.status_code == 200:
            print(f"[LINE] Reply sent to {user_id}")
        else:
            print(f"[LINE ERROR] {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"[LINE ERROR] {e}")

def analyze_and_reply(filepath: str, line_user_id: str = None):
    """Run vision analysis and reply to the user"""

    prompt = "Please analyze this image in detail and summarize the key elements."

    try:
        result = subprocess.run(
            [
                "hermes", "chat",
                "--profile", "echohsu",
                "-q", prompt,
                "--image", filepath
            ],
            capture_output=True,
            text=True,
            timeout=120
        )
        analysis = result.stdout.strip()

        print(f"[VISION] Analysis complete for {filepath}")

        # Send result back to LINE user if we have their ID
        if line_user_id:
            reply_text = f"Here's what I see in your photo:\n\n{analysis}"
            send_line_push(line_user_id, reply_text)
        else:
            print("[VISION RESULT]", analysis)

        return analysis
    except Exception as e:
        print(f"[VISION ERROR] {e}")
        return None

def main():
    print("[UploadWatcher] Running with auto-reply to LINE...")
    while True:
        files = glob.glob(os.path.join(NOTIFY_DIR, "*.json"))
        for f in files:
            if f in PROCESSED:
                continue
            try:
                with open(f) as fp:
                    data = json.load(fp)
                filepath = data["path"]
                line_user_id = data.get("line_user_id")
                print(f"[NEW UPLOAD] {filepath} from {line_user_id}")
                analyze_and_reply(filepath, line_user_id)
                PROCESSED.add(f)
            except Exception as e:
                print(f"[ERROR] {e}")
        time.sleep(3)

if __name__ == "__main__":
    main()
