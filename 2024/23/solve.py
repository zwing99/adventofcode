#!/usr/bin/env python

from collections import Counter
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


def dfs(node: str, depth: int, visited: set, path: list[str], max_depth, rings):
    if node in visited:
        return
    if path[0] in mappings[node] and len(path) > 2:
        rings.add(tuple(sorted(path)))
    if depth == max_depth:
        return
    visited.add(node)
    for c in mappings[node]:
        dfs(c, depth + 1, visited, path + [c], max_depth, rings)


def part1():
    print("----Part1----")
    rings = set()

    for start in starts:
        visited = set()
        if start.startswith("t"):
            dfs(start, 1, visited, [start], 3, rings)

    print(len(rings))


def part2():
    print("----Part2----")
    rings = set()

    # print(len(starts))
    for start in starts:
        visited = set()
        dfs(start, 1, visited, [start], len(starts), rings)
    # print("done with rings finding")

    # print(rings)

    max_size = 0
    max_ring = None
    rings = list(rings)
    rings.sort(key=lambda x: len(x), reverse=True)
    # print(f"Len: {len(rings)}")
    # print(f"SizeCounts: {Counter([len(r) for r in rings])}")
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

    print(",".join(max_ring))


part1()
part2()
