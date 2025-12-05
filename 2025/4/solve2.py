#!/usr/bin/env python

import itertools
from re import L
from statistics import LinearRegression
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [list(line.strip()) for line in fh.readlines()]


def print_grid():
    for line in lines:
        print("".join(line))
    print("---")


x_min = 0
x_max = len(lines[0])
y_min = 0
y_max = len(lines)
dirs: set[tuple[int, int]] = set(itertools.product([-1, 0, 1], [-1, 0, 1]))
dirs.remove((0, 0))


count = 0
last_count = -1
while count != last_count:
    removes: list[tuple[int, int]] = []
    for y in range(y_max):
        for x in range(x_max):
            if lines[y][x] == "@":
                total = 0
                for d in dirs:
                    xn, yn = x + d[0], y + d[1]
                    if xn >= x_min and xn < x_max and yn >= y_min and yn < y_max:
                        # print(yn, xn)
                        if lines[yn][xn] == "@":
                            total += 1
                if total < 4:
                    count += 1
                    removes.append((x, y))
    # for rx, ry in removes:
    #     lines[ry][rx] = "X"
    # print_grid()
    for rx, ry in removes:
        lines[ry][rx] = "."
    if len(removes) < 1:
        break


print(count)
