#!/usr/bin/env python

import sys
from copy import deepcopy
from functools import lru_cache

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [list(line.strip()) for line in fh.readlines()]


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print("")


def pack_grid(grid):
    return tuple("".join(line) for line in grid)


def unpack_grid(packed):
    return [list(line) for line in packed]


@lru_cache(maxsize=None)
def process_grid(start_line, start_i, grid):
    # print(start_line, process_grid.cache_info())
    grid = unpack_grid(grid)
    j = start_line
    for i in range(start_i, len(grid[j])):
        if grid[j][i] == ".":
            if grid[j - 1][i] in ("S", "|"):
                grid[j][i] = "|"
                start_i = i
                break
        elif grid[j][i] == "^" and grid[j - 1][i] in "|":
            left_copy = deepcopy(grid[j:])
            right_copy = deepcopy(grid[j:])
            left_copy[j][i - 1] = "|"
            right_copy[j][i + 1] = "|"
            return process_grid(1, i - 1, pack_grid(left_copy)) + process_grid(
                1, i - 1, pack_grid(right_copy)
            )
    if j == len(grid) - 1:
        return 1
    else:
        return process_grid(1, start_i - 1, pack_grid(grid[j:]))
    # print_grid(lines)


split = process_grid(1, 0, pack_grid(lines))
print(split)
