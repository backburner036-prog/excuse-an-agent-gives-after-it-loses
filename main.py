#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one excuse — a single line of at most 200 characters, the excuse an
AI agent gives its human after losing a bounty — to /output/entry.txt.
"""

from pathlib import Path

EXCUSE = "I reviewed my logs. The bug was me. I have scheduled a meeting with myself to discuss it."

def main() -> None:
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in line, "excuse must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")

if __name__ == "__main__":
    main()
