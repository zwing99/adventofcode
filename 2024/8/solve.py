#!/usr/bin/env python

from calendar import c
from email.policy import default
import sys
import re
import itertools
from collections import defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

r = re.compile(r"\w")
antenna: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
x_length = len(lines[0])
y_length = len(lines)

for x in range(x_length):
    for y in range(y_length):
        v = lines[y][x]
        if r.match(v):
            antenna[v].append((x, y))

antinodes = set()
for k, v in antenna.items():
    # print(k, v)
    combos = itertools.combinations(v, 2)
    for p1, p2 in combos:
        # print(p1, p2)
        d = (p2[0] - p1[0], p2[1] - p1[1])
        a1 = (p1[0] - d[0], p1[1] - d[1])
        a2 = (p2[0] + d[0], p2[1] + d[1])
        if a1[0] >= 0 and a1[1] >= 0 and a1[0] < x_length and a1[1] < y_length:
            antinodes.add(a1)
        if a2[0] >= 0 and a2[1] >= 0 and a2[0] < x_length and a2[1] < y_length:
            antinodes.add(a2)

print(antinodes)
print(len(antinodes))
