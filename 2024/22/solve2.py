#!/usr/bin/env python

import sys
import aoc_2024_22

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]

v = aoc_2024_22.do_it(lines)
print(v)
exit()

## below is original python code


a: list[list[int]] = []
for sn in lines:
    seq = []
    for i in range(2000):
        sn = ((sn * 64) ^ sn) % 16777216
        sn = ((sn // 32) ^ sn) % 16777216
        sn = ((sn * 2048) ^ sn) % 16777216
        seq.append(sn % 10)
    a.append(seq)

# print(a[0][:10])
# exit()

patterns: set[tuple[int, int, int, int]] = set()

b = []
for v in a:
    b_map = {}
    x = 0
    while x < len(v) - 4:
        new_pattern = (
            v[x + 1] - v[x],
            v[x + 2] - v[x + 1],
            v[x + 3] - v[x + 2],
            v[x + 4] - v[x + 3],
        )
        if sum(new_pattern) > 0:
            patterns.add(new_pattern)
        if new_pattern not in b_map:
            b_map[new_pattern] = v[x + 4]
        x += 1
    b.append(b_map)
    # print(v[:10])

# patterns = {(-2, 1, -1, 3)}
best = 0
for n, p in enumerate(patterns):
    total = 0
    for v in b:
        if p in v:
            total += v[p]
    # print(p, total)
    # print(f"---------------{n+1}/{len(patterns)}-------")
    if total > best:
        best = total
print(best)
# print((-2, 1, -1, 3) in patterns)

# for v in a:
#    print(v)

# 1458
