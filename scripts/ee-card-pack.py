#!/usr/bin/env python3
"""CLI alias for ee_card_pack (plan name ee-card-pack.py)."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ee_card_pack import main

if __name__ == "__main__":
    raise SystemExit(main())
