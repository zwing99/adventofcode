#!/usr/bin/env python

from collections import defaultdict
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

x_range = len(lines[0])
y_range = len(lines)
grid: list[list[int]] = list()
starts: list[tuple[int, int]] = list()
ends: list[tuple[int, int]] = list()

for y in range(y_range):
    row: list[int] = list()
    for x in range(x_range):
        v = int(lines[y][x])
        row.append(v)
        if v == 0:
            starts.append((x, y))
        elif v == 9:
            ends.append((x, y))
    grid.append(row)

print(starts)
print(ends)

paths: defaultdict[tuple[int, int], int] = defaultdict(int)


def dfs(x: int, y: int, paths: defaultdict[tuple[int, int], int]) -> int:
    # print(x, y)
    if grid[y][x] == 9:
        # print(f"Found end at {x, y}")
        return 1
    ## look up, down, left, right
    total_paths = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= x_range or ny < 0 or ny >= y_range:
            continue
        if grid[ny][nx] != grid[y][x] + 1:
            continue
        if (nx, ny) in paths:
            pass
            # print(f"Found {nx, ny} in paths, value: {paths[(nx, ny)]}")
            # total_paths += paths[(nx, ny)]
        else:
            n_paths = dfs(nx, ny, paths)
            paths[(nx, ny)] += n_paths
            total_paths += n_paths
    return total_paths


total_score = 0
for s in starts:
    paths = defaultdict(int)
    v = dfs(s[0], s[1], paths)
    print(s, v)
    total_score += v

print(total_score)
