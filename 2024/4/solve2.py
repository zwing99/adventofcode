#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
xmas = "MAS"

y_length = len(lines)
x_length = len(lines[0])
found = 0
pairs_diag = []
pairs_updown = []
for i in range(x_length):
    for j in range(y_length):
        if lines[j][i] == "M":
            for m, (dx, dy) in enumerate(directions):
                is_xmas = True
                for n in range(1, 3):
                    x, y = i + dx * n, j + dy * n
                    if x < 0 or x >= x_length or y < 0 or y >= y_length:
                        is_xmas = False
                        break
                    if lines[y][x] != xmas[n]:
                        is_xmas = False
                        break
                if is_xmas:
                    if m < 4:
                        pairs_updown += [(i + dx, j + dy)]
                    else:
                        pairs_diag += [(i + dx, j + dy)]

from collections import Counter

c1 = Counter(pairs_updown)
print(c1)
c2 = Counter(pairs_diag)
print(c2)

print(len(list(filter(lambda x: x[1] == 2, c2.items()))))
