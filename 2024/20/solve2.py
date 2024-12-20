#!/usr/bin/env python

from collections import defaultdict
import dis
from email.policy import default
from re import S
import sys

sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    grid = [[x for x in line.strip()] for line in fh.readlines()]

range_x = len(grid[0])
range_y = len(grid[0])

for x in range(range_x):
    for y in range(range_y):
        if grid[y][x] == "S":
            S = (x, y)
        elif grid[y][x] == "E":
            E = (x, y)

INT_MAX = 2**63 - 1
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(
    node: tuple[int, int],
    steps: int,
    current_path: list[tuple[int, int]],
    visited: dict[tuple[int, int], int],
    paths: dict,
):
    best = visited.get(node, INT_MAX)
    if steps >= best:
        if steps == best:
            pass
            # todo add me
            # paths[node].append(node)
        return
    visited[node] = steps
    paths[node] = current_path
    if node == E:
        return
    x, y = node
    for d in directions:
        new_x, new_y = x + d[0], y + d[1]
        if new_x < 0 or new_x >= range_x or new_y < 0 or new_y >= range_y:
            continue
        if grid[new_y][new_x] == "#":
            continue
        dfs((new_x, new_y), steps + 1, current_path + [(new_x, new_y)], visited, paths)


visited: dict[tuple[int, int], int] = {}
paths: dict = {}
dfs = dfs(S, 0, [S], visited, paths)
best_path = paths[E]


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


CHEAT_THRESHOLD = 50 if filename == "test.txt" else 100
cheats = defaultdict(lambda: 0)
for i in range(len(best_path) - 3):
    x, y = best_path[i]
    options = []
    for j in range(i + 3, len(best_path)):
        d = distance(best_path[i], best_path[j])
        if d <= 20:
            v = j - i - d
            if v >= CHEAT_THRESHOLD:
                cheats[v] += 1

if filename == "test.txt":
    keys = sorted(cheats.keys())
    ordered_cheaats = {k: cheats[k] for k in keys}
    print(ordered_cheaats)
print(sum(cheats.values()))


# print(32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3)
