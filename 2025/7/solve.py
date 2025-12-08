#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [list(line.strip()) for line in fh.readlines()]


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print("")


split = 0
for j in range(1, len(lines)):
    for i in range(len(lines[j])):
        if lines[j][i] == ".":
            if lines[j - 1][i] in ("S", "|"):
                lines[j][i] = "|"
        elif lines[j][i] == "^" and lines[j - 1][i] in "|":
            lines[j][i - 1] = "|"
            lines[j][i + 1] = "|"
            split += 1
    # print_grid(lines)

print(split)
