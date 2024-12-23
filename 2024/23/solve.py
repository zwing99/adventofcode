#!/usr/bin/env python

from collections import deque
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


mappings: dict[str, str] = {}
starts: set[str] = set()
for line in lines:
    a, b = line.split("-")
    if a not in mappings:
        mappings[a] = []
    if b not in mappings:
        mappings[b] = []
    mappings[a].append(b)
    mappings[b].append(a)
    starts.add(a)
    starts.add(b)

# print(mappings)
# print(starts)

rings = set()


def dfs(node: str, depth: int, visited: str, path: list[str]):
    if node in visited:
        return
    if path[0] in mappings[node]:
        rings.add(tuple(sorted(path)))
    visited.add(node)
    for c in mappings[node]:
        dfs(c, depth + 1, visited, path + [c])


for start in starts:
    # print(start)
    dfs(start, 1, set(), [start])

# print(rings)

max_size = 0
max_ring = None
rings = list(rings)
rings.sort(key=lambda x: len(x), reverse=True)
for r in rings:
    # print(r)
    all_connections = True
    for i in r:
        rest = set(r) - {i}
        if set(mappings[i]).intersection(rest) != rest:
            all_connections = False
            break
    if all_connections and len(r) > max_size:
        max_size = len(r)
        max_ring = r
        break

print("-------------")
print(",".join(max_ring))
