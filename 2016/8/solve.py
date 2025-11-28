#!/usr/bin/env python

import sys
from copy import deepcopy

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

if filename == "test.txt":
    size = 7, 3
    char = "*"
else:
    size = 50, 6
    char = " "

grid = []
for i in range(size[1]):
    grid.append([char] * size[0])


def print_grid():
    print("\n".join(["".join(g) for g in grid]))
    print("")


# print_grid()

for line in lines:
    if "rect" in line:
        x, y = [int(v) for v in line.split(" ")[1].split("x")]
        for i in range(x):
            for j in range(y):
                grid[j][i] = "#"
        # print_grid()

    elif "row" in line:
        _, _, a, _, b = line.split(" ")
        r, n = int(a.split("=")[1]), int(b)
        new_grid = deepcopy(grid)
        for i in range(size[0]):
            new_grid[r][(i + n) % size[0]] = grid[r][i]
        grid = new_grid
        # print_grid()
    elif "column" in line:
        _, _, a, _, b = line.split(" ")
        c, n = int(a.split("=")[1]), int(b)
        new_grid = deepcopy(grid)
        for j in range(size[1]):
            new_grid[(j + n) % size[1]][c] = grid[j][c]
        grid = new_grid
        # print_grid()

print_grid()

print(sum([r.count("#") for r in grid]))
