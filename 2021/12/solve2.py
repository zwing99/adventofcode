#!/usr/bin/env python

from collections import defaultdict, Counter
import sys

sys.setrecursionlimit(10000)

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
    if node == "start" and path:
        return None
    if node.islower():
        c = Counter([x for x in path if x.islower()])
        if c and c.most_common(1)[0][1] > 1 and node in path:
            return None
        elif c:
            pass
    paths = []
    for neighbor in graph[node]:
        if x := dfs(neighbor, path + [node]):
            paths.extend(x)
    return paths


paths = dfs("start", [])
for p in paths:
    print(",".join(p))
print(len(paths))
