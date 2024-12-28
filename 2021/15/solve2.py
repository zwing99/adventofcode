#!/usr/bin/env python

from gettext import find
import heapq
import sys

sys.setrecursionlimit(1000000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

grid = [[int(c) for c in line] for line in lines]
orig_range_x = len(grid)
orig_range_y = len(grid[0])
range_x = len(grid) * 5
range_y = len(grid[0]) * 5


def get_score(x, y):
    mul_x = x // orig_range_x
    mod_x = x % orig_range_x
    mul_y = y // orig_range_y
    mod_y = y % orig_range_y
    v = grid[mod_x][mod_y] + 1 * mul_x + 1 * mul_y
    while v > 9:
        v -= 9
    return v


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_best():
    seen = set()
    q = [(0, (0, 0), [(0, 0)])]
    mins = {(0, 0): 0}

    while q:
        # print(q[:5])
        score, (x, y), path = heapq.heappop(q)
        if (x, y) not in seen:
            # print(x, y, score)
            seen.add((x, y))
            if x == range_x - 1 and y == range_y - 1:
                return path, score

            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if nx < 0 or nx >= range_x or ny < 0 or ny >= range_y:
                    continue
                if (nx, ny) in seen:
                    continue
                prev = mins.get((nx, ny), None)
                next = score + get_score(nx, ny)
                if prev is None or next < prev:
                    mins[(nx, ny)] = next
                    heapq.heappush(q, (next, (nx, ny), path + [(nx, ny)]))


path, score = find_best()


class style:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"


for x in range(range_x):
    for y in range(range_y):
        if (x, y) in path:
            print(f"{style.RED}{get_score(x,y)}{style.RESET}", end="")
        else:
            print(get_score(x, y), end="")
    print()

print(score)
