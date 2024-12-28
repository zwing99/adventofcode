#!/usr/bin/env python

from re import M
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

grid = set()
x_max = 0
y_max = 0
while True:
    line = lines.pop(0)
    if line == "":
        break
    x, y = line.split(",")
    x, y = int(x), int(y)
    if x > x_max:
        x_max = x
    if y > y_max:
        y_max = y
    grid.add((x, y))

for y in range(y_max + 1):
    for x in range(x_max + 1):
        if (x, y) in grid:
            print("#", end="")
        else:
            print(".", end="")
    print()
print(len(grid))

for fold in lines:
    fold = fold.split(" ")[2]
    axis, val = fold.split("=")
    val = int(val)
    print(axis, val)

    if axis == "x":
        max_axis = 2 * val
        x_max = max_axis
    else:
        max_axis = 2 * val
        y_max = max_axis

    new_grid = set()
    for item in grid:
        x, y = item
        if axis == "x" and x >= val:
            if x == val:
                continue
            x = max_axis - x
            x_max = val - 1
        elif axis == "y" and y >= val:
            if y == val:
                continue
            y = max_axis - y
            y_max = val - 1
        new_grid.add((x, y))
    grid = new_grid
    break

for y in range(y_max + 1):
    for x in range(x_max + 1):
        if (x, y) in grid:
            print("#", end="")
        else:
            print(".", end="")
    print()
print(len(grid))

# 722 That's not the right answer; your answer is too high.
