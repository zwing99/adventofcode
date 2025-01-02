#!/usr/bin/env python

from collections import defaultdict
import enum
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

moves = lines[0]
directions = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}

s1 = (0, 0)
s2 = (0, 0)
visited = defaultdict(int)
visited[s1] += 1
visited[s2] += 1

for i, m in enumerate(moves):
    dx, dy = directions[m]
    if i % 2 == 0:
        s1 = (s1[0] + dx, s1[1] + dy)
        visited[s1] += 1
    else:
        s2 = (s2[0] + dx, s2[1] + dy)
        visited[s2] += 1

print(len(visited))
