"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene — a builder
watching something she built alone for years finally land with a
real stranger on the other side of it.
"""

import os
import sys

# The line. One read, pride arriving with the last words.
LINE = (
    "Three years of stolen weekends ended at 2 a.m.: she pressed deploy, "
    "and a stranger \u2014 her first real user \u2014 signed up before her "
    "coffee went cold."
)


def main() -> int:
    """Validate the line and write it to /output/entry.txt."""
    text = LINE.strip()
    if not text or len(text) > 240:
        print(f"entry must be 1-240 characters, got {len(text)}", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
