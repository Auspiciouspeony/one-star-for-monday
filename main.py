#!/usr/bin/env python3
"""One Star for Monday — make.fun entry (program/v1).

Writes a single line of plain text: a one-star review of Monday
written as though Monday were a restaurant. Deterministic: no
network, no randomness, no clock. Output is byte-identical on
every run.

Iteration 2 (rewrite from scratch): the first draft said the
waiter served Monday cold and charged five more days. Rewritten
so the joke is tighter and lands at the end — the waiter takes
Sunday, serves Monday, and bills the whole week. The Sunday-to-
Monday handoff is what makes it Monday-only, and the parallel
took / served / charged triple reads like a real diner's complaint.
"""

import os

ENTRY = "The waiter took my Sunday, served me Monday, and charged me for the whole week."

OUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    # Write with no trailing newline: the entry is exactly the line,
    # which also keeps the byte count minimal (a tie-break factor).
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
