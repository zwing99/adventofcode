#!/usr/bin/env python

from hmac import new
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

stones_li = [int(i) for i in lines[0].split()]


def dfs(stone, i, visited):
    if (stone, i) in visited:
        return visited[(stone, i)]
    if i >= 75:
        return 1
    sum = 0
    if stone == 0:
        sum += dfs(1, i + 1, visited)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        ls = int(s[len(s) // 2 :])
        rs = int(s[: len(s) // 2])
        sum += dfs(ls, i + 1, visited)
        sum += dfs(rs, i + 1, visited)
    else:
        sum += dfs(stone * 2024, i + 1, visited)
    visited[(stone, i)] = sum
    return sum


sum = 0
visited = dict()
for stone in stones_li:
    sum += dfs(stone, 0, visited)

print(len(visited))
print(sum)
