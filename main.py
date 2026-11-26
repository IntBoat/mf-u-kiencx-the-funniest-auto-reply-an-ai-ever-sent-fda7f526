#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent (make.fun).

Writes the entry -- one original one-line text -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = 'Thank you for your email — I have understood it perfectly and will now do nothing about it with complete confidence.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
