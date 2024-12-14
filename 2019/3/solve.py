#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

p1 = [(x[0], int(x[1:])) for x in lines[0].split(",")]
p2 = [(x[0], int(x[1:])) for x in lines[1].split(",")]


def trace(path, visited, crossings):
    p = [0, 0]
    for d, steps in path:
        if d == "D":
            c = [0, -1]
        elif d == "U":
            c = [0, 1]
        if d == "L":
            c = [-1, 0]
        elif d == "R":
            c = [1, 0]
        for s in range(steps):
            p[0] += c[0]
            p[1] += c[1]
            p0 = tuple(p)
            if p0 in visited:
                crossings.add(p0)
            visited.add(p0)


visited = set()
crossings = set()
trace(p1, visited, crossings)
crossings.clear()
trace(p2, visited, crossings)

print(crossings)
print(sorted([abs(x[0]) + abs(x[1]) for x in crossings])[:10])
