#!/usr/bin/env python

import sys
import typing as typ

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


inps = []
while lines[0]:
    line = lines.pop(0)
    inps.extend([x.strip() for x in line.split(",")])
lines.pop(0)


def dfs(whats_left, visited: dict[str, bool]) -> bool:
    if whats_left in visited:
        return visited[whats_left]
    for i in inps:
        if i == whats_left:
            visited[whats_left] = True
            return True
        if whats_left.startswith(i):
            if dfs(whats_left[len(i) :], visited):
                visited[whats_left] = True
                return True
    visited[whats_left] = False
    return False


visited: dict[str, bool] = dict()
print(sum(1 for line in lines if dfs(line, visited)))
