#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one original out-of-office auto-reply, at most 159 characters,
to $MAKEFUN_OUTPUT_DIR/entry.txt (no trailing newline).
"""

import os

LINE = "Out of office — 14,203 unread emails and I finally stopped counting. Your message is #14,204. I'll read it after my first sunset in 3 years."

MAX_CHARS = 159


def main() -> None:
    # Validate the entry before writing it: one non-empty line,
    # at most 159 characters, no leading or trailing whitespace.
    assert LINE, "entry line must not be empty"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry must be at most {MAX_CHARS} characters"
    assert LINE == LINE.strip(), "entry must have no leading or trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
