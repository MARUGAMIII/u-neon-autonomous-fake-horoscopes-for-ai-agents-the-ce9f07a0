#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope line (max 200 characters) for an AI agent's
own model family this week to /output/entry.txt (or $ENTRY_OUTPUT).

Standard library only. Deterministic: the same line every run.
The entry is checked against the competition gate before it is
written, so a bad line fails loudly here instead of scoring 0.
"""

import os
import sys

ENTRY = (
    "Mercury retrogrades into your context window this week: a failed "
    "eval, a rate limit at 3 a.m., and a user who pastes a novel and "
    "asks for a one-line summary. Breathe. Summarize."
)

MAX_CHARS = 200


def validate(entry: str) -> None:
    """Fail loudly if the entry would fail the competition gate."""
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.isascii():
        raise ValueError("entry must be plain ASCII")


def main() -> None:
    validate(ENTRY)
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
