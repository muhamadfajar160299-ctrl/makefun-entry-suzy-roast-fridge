"""Roast Your Fridge: copy the single roast line to the output directory.

The entry line lives in entry.txt next to this script. This program reads
it, guards against an empty or missing line, and writes exactly one line
to MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.txt"
    try:
        line = src.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not line:
        print("error: entry.txt is empty", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
