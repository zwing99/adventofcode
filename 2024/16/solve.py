#!/usr/bin/env python

import sys

sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [[x for x in line.strip()] for line in fh.readlines()]

x_range = len(lines[0])
y_range = len(lines)

for y in range(y_range):
    for x in range(x_range):
        if lines[y][x] == "E":
            E = (x, y)
        elif lines[y][x] == "S":
            S = (x, y)

dir = (1, 0)


def turn_cw(dir):
    return (dir[1], -dir[0])


def turn_ccw(dir):
    return (-dir[1], dir[0])


def dfs(
    node: tuple[tuple[int, int], tuple[int, int]], steps, visited: dict, can_turn=True
):
    if node in visited:
        if visited[node] <= steps:
            return
    visited[node] = steps
    # forward step
    x, y = node[0]
    dx, dy = node[1]
    if lines[y + dy][x + dx] in [".", "E"]:
        dfs(((x + dx, y + dy), (dx, dy)), steps + 1, visited)
    # turn cw
    if not can_turn:
        return
    dfs(((x, y), turn_cw((dx, dy))), steps + 1000, visited, False)
    # turn ccw
    dfs(((x, y), turn_ccw((dx, dy))), steps + 1000, visited, False)


visited = {}

dfs((S, dir), 0, visited)

dir = (1, 0)
smallest = 9e99
for i in range(4):
    dir = turn_cw(dir)
    if (E, dir) in visited:
        smallest = min(int(smallest), visited[(E, dir)])
print(smallest)
