#!/usr/bin/env python3
"""
Interactions Calendar Logger
Logs LINE/Bridge interactions as ICS for calendar integration.
"""
import json
from datetime import datetime
from pathlib import Path

ECHOPEDIA_DIR = Path("/home/leedt/echo-system")
INTERACTIONS_DIR = ECHOPEDIA_DIR / "knowledge" / "interactions"
INTERACTIONS_DIR.mkdir(parents=True, exist_ok=True)

ICS_PATH = INTERACTIONS_DIR / "linebot-interactions.ics"

def log_interaction(source: str, message: str, user: str = "unknown"):
    """Log an interaction as ICS event."""
    now = datetime.now()
    dt = now.strftime("%Y%m%dT%H%M%S")
    
    event = f"""BEGIN:VEVENT
DTSTART:{dt}
DTEND:{dt}
SUMMARY:{source} - {message[:50]}
DESCRIPTION:{message}
UID:{source}-{user}-{int(now.timestamp())}@tahs.org
END:VEVENT"""
    
    # Append to ICS file
    existing = ICS_PATH.read_text() if ICS_PATH.exists() else "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//TAHS//ES//EN\n"
    
    if ICS_PATH.exists():
        content = ICS_PATH.read_text().rstrip()
        # Remove trailing VCALENDAR, add event, close
        if content.endswith("END:VCALENDAR"):
            content = content[:content.rfind("END:VCALENDAR")]
    
    result = content.rstrip() + "\n" + event + "\nEND:VCALENDAR\n"
    ICS_PATH.write_text(result)
    print(f"Logged: {source} - {message[:50]}")

if __name__ == "__main__":
    log_interaction("LINE", "Test interaction")
