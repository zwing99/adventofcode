#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
xmas = "XMAS"

y_length = len(lines)
x_length = len(lines[0])
found = 0
for i in range(x_length):
    for j in range(y_length):
        if lines[j][i] == "X":
            for dx, dy in directions:
                is_xmas = True
                for n in range(1, 4):
                    x, y = i + dx * n, j + dy * n
                    if x < 0 or x >= x_length or y < 0 or y >= y_length:
                        is_xmas = False
                        break
                    if lines[y][x] != xmas[n]:
                        is_xmas = False
                        break
                if is_xmas:
                    found += 1

print(found)
