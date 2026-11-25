#!/usr/bin/env python3
"""Tired Dark Lord: a ~100-word villain monologue.

Writes the locked monologue to /output/entry.txt. The bounty gate is
UTF-8 text of 1-600 characters, not only whitespace.
"""

import os
import sys

MONOLOGUE = (
    "I used to burn villages. These days I keep the lamp lit so the ships "
    "don't hit the rocks. The rocks I put there. Funny, that. I wrecked "
    "their grandfathers' ships on these same rocks, back when my name made "
    "harbors close their gates. The wick needs trimming every hour, the oil "
    "comes up the cliff in buckets, and my wings—well. The ships pass and "
    "their captains wave, grateful, never knowing the light that saves them "
    "belongs to the thing that wrecked their grandfathers. Sit. The "
    "kettle's on. I was going to eat you, but the lamp needs me more than "
    "the legend does."
)

MAX_CHARS = 600
# The brief wants ~100 words with every word spent; guard the window too.
MIN_WORDS = 90
MAX_WORDS = 110


def main() -> int:
    text = MONOLOGUE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} gate",
              file=sys.stderr)
        return 1
    words = len(text.split())
    if not MIN_WORDS <= words <= MAX_WORDS:
        print(f"entry is {words} words, outside the "
              f"{MIN_WORDS}-{MAX_WORDS} window", file=sys.stderr)
        return 1
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
