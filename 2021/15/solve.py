#!/usr/bin/env python

from collections import deque
import sys
from typing import Deque

sys.setrecursionlimit(100000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

grid = [[int(c) for c in line] for line in lines]
range_x = len(grid)
range_y = len(grid[0])

directions = [(0, 1), (1, 0)]  # , (-1, 0), (0, -1)]


def dfs(x, y, path, score, visited: dict[str, int]):
    if (x, y) in path:
        return
    if (x, y) in visited and score >= visited[(x, y)]:
        return
    visited[(x, y)] = score
    # print(x, y, score)
    if x == range_x - 1 and y == range_y - 1:
        print(score)
        return
    options = []
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if nx < 0 or nx >= range_x or ny < 0 or ny >= range_y:
            continue
        options.append((nx, ny, grid[nx][ny]))
    options.sort(key=lambda x: x[2], reverse=True)
    for nx, ny, v in options:
        dfs(nx, ny, path | {(x, y)}, score + v, visited)


visited = {}
dfs(0, 0, set(), 0, visited)

print(visited[(range_x - 1, range_y - 1)])


# scores = dict()
# Q = deque()
# Q.append((0, 0, 0))
# while Q:
#     x, y, score = Q.popleft()
#     if (x, y) in scores and score >= scores[(x, y)]:
#         continue
#     scores[(x, y)] = score
#     if (x, y) == (range_x - 1, range_y - 1):
#         print(score)
#         continue
#     for d in directions:
#         nx, ny = x + d[0], y + d[1]
#         if nx < 0 or nx >= range_x or ny < 0 or ny >= range_y:
#             continue
#         Q.append((nx, ny, score + grid[nx][ny]))
#
