#!/usr/bin/env python

from collections import defaultdict
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

graph = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    graph[a].append(b)
    graph[b].append(a)


def dfs(node: str, path: list[str]):
    if node == "end":
        return [path + ["end"]]
    if (node.islower() or node == "start") and node in path:
        return None
    paths = []
    for neighbor in graph[node]:
        if x := dfs(neighbor, path + [node]):
            paths.extend(x)
    return paths


paths = dfs("start", [])
for p in paths:
    print(p)
print(len(paths))
