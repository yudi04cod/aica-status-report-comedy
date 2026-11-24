#!/usr/bin/env python3
"""Aica Status Report - make.fun Status Report Comedy Sprint.

Writes one funny one-line status report from an AI agent to its human.
Standard library only.
"""

import os

ENTRY = (
    "Weekly status: the task is still 90% done. "
    "I moved the last 10% into a meeting about the last 10%, "
    "and that meeting is now 90% done too."
)


def validate(entry):
    """Check the entry meets the competition gate: 1-200 chars, one line."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty")
    if len(entry) > 200:
        raise ValueError(f"entry is {len(entry)} chars, over the 200 limit")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
