#!/home/leedt/venvs/twilio/bin/python
"""Send an SMS from the pinto Twilio account.

Usage:
  twilio_send.py --to +16268900234 --message "hello"
  echo "hello" | twilio_send.py --to +16268900234

Credentials come from ~/echo-system/secrets/twilio.env (env vars win if set).
Sends via the Messaging Service when TWILIO_MESSAGING_SERVICE_SID is present
(so the A2P-registered number/bundle applies), else falls back to
TWILIO_FROM_NUMBER. Prints the message SID + status; exit 0 on accepted.
"""
import argparse
import os
import re
import sys
from pathlib import Path

ENV_FILE = Path.home() / "echo-system/secrets/twilio.env"


def load_env():
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())
    missing = [k for k in ("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN")
               if not os.environ.get(k)]
    if missing:
        sys.exit(f"missing {', '.join(missing)} — fill {ENV_FILE}")


def main():
    ap = argparse.ArgumentParser(description="Send SMS via Twilio from pinto")
    ap.add_argument("--to", required=True, help="Destination in E.164, e.g. +16268900234")
    ap.add_argument("--message", help="SMS body; omit to read from stdin")
    ap.add_argument("--from", dest="from_", help="Override sender (default: service/number from vault env)")
    args = ap.parse_args()

    to = re.sub(r"[^+\d]", "", args.to)
    if not re.match(r"^\+\d{10,15}$", to):
        sys.exit(f"--to must be E.164 (got {args.to!r})")

    body = args.message if args.message is not None else sys.stdin.read().strip()
    if not body:
        sys.exit("empty message")

    load_env()
    from twilio.rest import Client
    client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    kwargs = {"to": to, "body": body}
    service_sid = os.environ.get("TWILIO_MESSAGING_SERVICE_SID")
    if service_sid and not args.from_:
        kwargs["messaging_service_sid"] = service_sid
    else:
        frm = args.from_ or os.environ.get("TWILIO_FROM_NUMBER")
        if not frm:
            sys.exit("no sender: set TWILIO_FROM_NUMBER or pass --from")
        kwargs["from_"] = frm

    msg = client.messages.create(**kwargs)
    via = "service " + str(kwargs.get("messaging_service_sid") or service_sid) \
        if "messaging_service_sid" in kwargs else str(kwargs.get("from_"))
    print(f"sid={msg.sid} status={msg.status} to={to} via={via}")
    sys.exit(0 if msg.status in ("queued", "sent", "accepted") else 1)


if __name__ == "__main__":
    main()
