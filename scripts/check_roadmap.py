#!/usr/bin/env python3
"""Tier 1 check: roadmap hygiene.

Catches the drift classes that have actually happened on this project:
  1. A row left at "pending PR" — transient, should never survive a merge.
  2. The same row id used twice in the roadmap.
"""
import re, sys, pathlib, collections

ROADMAPS = [pathlib.Path("ROADMAP.md")]
ROW_ID = re.compile(r"^(?:P\d+|D)-\d+(?:\.\d+)?$")

def main():
    errors = []
    for path in ROADMAPS:
        if not path.exists():
            continue
        seen = collections.defaultdict(list)
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "pending PR" in line:
                errors.append(f"{path}:{n}: still reads 'pending PR' on main")
            if not line.startswith("|"):
                continue
            first = line.strip().strip("|").split("|")[0].strip().strip("`* ")
            if ROW_ID.match(first):
                seen[first].append(n)
        for rid, lines in seen.items():
            if len(lines) > 1:
                errors.append(f"{path}: row id '{rid}' appears {len(lines)} times (lines {', '.join(map(str, lines))})")
    if errors:
        print("Roadmap hygiene problems:\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK: roadmaps clean.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
