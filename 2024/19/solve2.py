#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


inps = []
while lines[0]:
    line = lines.pop(0)
    inps.extend([x.strip() for x in line.split(",")])
lines.pop(0)

inps = set(inps)


def dfs(whats_left, vistied: dict):
    if whats_left in vistied:
        return vistied[whats_left]
    total = 0
    for i in inps:
        if i == whats_left:
            total += 1
        if whats_left.startswith(i):
            total += dfs(whats_left[len(i) :], vistied)
    vistied[whats_left] = total
    return total


# for line in lines:
#     print("YES" if dfs(line) else "NO")

full_total = 0
visited = {}
for line in lines:
    print(line)
    full_total += dfs(line, visited)
print(full_total)
