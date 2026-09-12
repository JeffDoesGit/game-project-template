#!/usr/bin/env python3
"""Tier 1 check: PROVISIONAL marker <-> docs/provisional.md parity (CLAUDE.md 1.7).

Every `PROVISIONAL(<id>)` marker in code or config must be covered by a row in
the register, and every row that names code/config files must point at a file
that actually carries a marker. Asset entries are exempt on the marker side —
binary assets are marked in the editor's description field (CLAUDE.md 7.8) and
cannot be grepped.

Scope of the marker scan is Source/, Config/ and Plugins/ — the places 1.7
means. Docs and memos describe the marker format and are not scanned.
"""
import re, subprocess, sys, pathlib

REGISTER = pathlib.Path("docs/provisional.md")
SCAN_ROOTS = ("Source/", "Config/", "Plugins/", "scenes/", "scripts/", "data/", "addons/")
CODE_EXT = {".h", ".cpp", ".cs", ".ini", ".py", ".json", ".gd", ".tscn", ".tres", ".cfg"}

def tracked():
    return subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split()

def markers():
    found = {}
    for f in tracked():
        if not f.startswith(SCAN_ROOTS) or f.startswith("scripts/") or pathlib.Path(f).suffix not in CODE_EXT:
            continue  # scripts/ holds the checker itself, which names the marker without carrying one
        try:
            text = pathlib.Path(f).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        n = len(re.findall(r"PROVISIONAL\(", text))
        if n:
            found[f] = n
    return found

def rows():
    if not REGISTER.exists():
        sys.exit(f"FAIL: {REGISTER} missing (CLAUDE.md 1.7)")
    out = []
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or cells[0] == "Decision" or set(cells[0]) <= {"-", " "}:
            continue
        out.append((cells[0], cells[3]))
    return out

def resolve(shorthand, files):
    """Registry paths may be full, or shorthand relative to a directory named
    earlier in the same cell (`UI/InventoryScreen.cpp`, `SoulComponent.cpp`)."""
    if shorthand in files:
        return [shorthand]
    return [f for f in files if f.endswith("/" + shorthand)]

def main():
    found, table = markers(), rows()
    files = set(tracked())
    if not table and not found:
        print("OK: no PROVISIONAL markers and an empty register — nothing to reconcile.")
        return 0
    errors, covered = [], set()

    for decision, cell in table:
        named = [p for p in re.findall(r"`([^`]+)`", cell) if pathlib.Path(p).suffix in CODE_EXT]
        if not named:
            continue  # asset row: the row is the marker (CLAUDE.md 1.6)
        hit = False
        for p in named:
            for real in resolve(p, files):
                covered.add(real)
                if real in found:
                    hit = True
        if not hit:
            errors.append(f"row '{decision}' names {', '.join(named)} but none of them carries a PROVISIONAL( marker")

    for f in sorted(found):
        if f not in covered:
            errors.append(f"{f} has {found[f]} PROVISIONAL( marker(s) but no register row names it")

    if errors:
        print("Provisional register out of sync (CLAUDE.md 1.7):\n")
        for e in errors:
            print(f"  - {e}")
        print(f"\n{len(errors)} problem(s).")
        return 1
    print(f"OK: {sum(found.values())} marker(s) in {len(found)} file(s), {len(table)} register row(s), all matched.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
