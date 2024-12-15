#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

map: dict[str, []] = {}
counts: dict[str, int] = dict()

for line in lines:
    a, b = line.split(")")
    if a not in map:
        counts[a] = 0
        map[a] = []
    if b not in map:
        counts[b] = 0
        map[b] = []
    map[a].append(b)


def dfs(node, counts, i):
    counts[node] += i
    for child in map[node]:
        dfs(child, counts, i + 1)


dfs("COM", counts, 0)
print(counts)
print(sum(counts.values()))
