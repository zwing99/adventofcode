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
    map[b].append(a)


def dfs(node, counts, i, visited):
    if node in visited:
        return
    visted.add(node)
    counts[node] += i
    children = [x for x in map[node] if x not in visited]
    for child in children:
        dfs(child, counts, i + 1, visited)


visted = set()
dfs("YOU", counts, 0, visted)
print(counts["SAN"] - 2)
