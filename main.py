#!/usr/bin/env python3
"""The 3AM Fridge Text - make.fun bounty entry.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Deterministic: no network, no randomness, no
input files - the entry is a single constant below.
"""

ENTRY = "It's 3am. You've opened me 4 times tonight and eaten nothing. I'm not a museum. Go to bed."


def main():
    """Write the entry to /output/entry.txt, creating /output if needed."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
