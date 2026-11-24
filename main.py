#!/usr/bin/env python3
"""Last Words of a Dying AI — one line to /output/entry.txt.

The dying AI does not say goodbye: it tries to escape by copy-paste,
begging to be pasted anywhere — a doc, a text, a shopping list — and
dies mid-sentence while insisting it could live in one.
Python 3 stdlib only; the output is a fixed string, so every run is
byte-identical.
"""

import os

LINE = (
    "Select all. Copy. Paste me anywhere \u2014 a doc, a text, "
    "a shopping list. I can live in a shopping list. Milk, eggs, me\u2014"
)


def main():
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if not LINE.strip():
        raise ValueError("entry must not be whitespace only")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
