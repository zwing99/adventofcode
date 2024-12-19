#!/usr/bin/env python

from re import L, S
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

if filename != "input.txt":
    max_x = 6
    max_y = 6
    START_BYTES = 12
else:
    max_x = 70
    max_y = 70
    START_BYTES = 1024

all_bytes = list()
for i, line in enumerate(lines):
    all_bytes.append(tuple([int(x) for x in line.split(",")]))

print(max_x, max_y)

start = (0, 0)
end = (max_x, max_y)

INT_MAX = 2**63 - 1


def dfs(visited: dict, node: tuple[int, int], blocked: set, steps=0):
    # print(node, steps)
    prior_steps = visited.get(node, INT_MAX)
    if steps >= prior_steps:
        # print("returning")
        return
    visited[node] = steps
    if node == end:
        return
    x, y = node
    if x + 1 <= max_x and (x + 1, y) not in blocked:
        # print("right")
        dfs(visited, (x + 1, y), blocked, steps + 1)
    if x - 1 >= 0 and (x - 1, y) not in blocked:
        # print("left")
        dfs(visited, (x - 1, y), blocked, steps + 1)
    if y + 1 <= max_y and (x, y + 1) not in blocked:
        # print("down")
        dfs(visited, (x, y + 1), blocked, steps + 1)
    if y - 1 >= 0 and (x, y - 1) not in blocked:
        # print("up")
        dfs(visited, (x, y - 1), blocked, steps + 1)


last_bad = (-1, -1)
for i in range(len(all_bytes), START_BYTES, -1):
    visited = {}
    s = set(all_bytes[:i])
    dfs(visited, start, s)
    if end not in visited:
        # print(i, all_bytes[i - 1], "bad")
        last_bad = (i, all_bytes[i - 1])
    else:
        print(i, all_bytes[i - 1], "good")
        print(*last_bad, "bad")
        break
