#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def print_grid(grid):
    for row in grid:
        print("".join([str(x) for x in row]))


grid = [[0 for x in range(1000)] for y in range(1000)]
# print_grid(grid)
for line in lines:
    line, to_pair = line.split("through")
    cmd, from_pair = line.strip().rsplit(" ", 1)
    to_pair = tuple(map(int, to_pair.strip().split(",")))
    from_pair = tuple(map(int, from_pair.strip().split(",")))
    for x in range(from_pair[0], to_pair[0] + 1):
        for y in range(from_pair[1], to_pair[1] + 1):
            if cmd == "turn on":
                grid[x][y] += 1
            elif cmd == "turn off":
                grid[x][y] = max(0, grid[x][y] - 1)
            elif cmd == "toggle":
                grid[x][y] += 2

print(sum([sum(row) for row in grid]))
