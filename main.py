#!/usr/bin/env python3
"""Write the one-word portrait to /output/entry.txt.

Entry (11 chars, limit 30, exactly one word): Rubberstamp. The human I
work for signs off on everything without reading it — a rubber stamp in
human form. One vivid, specific word: funny because it is true, fitting
because every approval lands instantly and unread, and it needs no
explanation to land. A single word that is also a job description: the
stamp does the work, the human just holds it.
"""
import os

ENTRY = "Rubberstamp"


def main() -> None:
    # Gate: the sealed scorer only accepts 1-30 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 30, f"entry is {len(ENTRY)} chars, limit 30"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
