#!/usr/bin/env python3
"""
Disabled by user request.

Previously this script would:
1) parse LINE unauthorized-group events from gateway.log,
2) auto-add group IDs into line.allowed_groups,
3) optionally restart the gateway.

That auto-authorize behavior has been removed.
"""


def main() -> int:
    # Intentionally no-op.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
