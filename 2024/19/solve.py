#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


inps = []
while lines[0]:
    line = lines.pop(0)
    inps.extend([x.strip() for x in line.split(",")])
lines.pop(0)

inps = set(inps)


def dfs(whats_left):
    for i in inps:
        if i == whats_left:
            return True
        if whats_left.startswith(i):
            if dfs(whats_left[len(i) :]):
                return True
    return False


# for line in lines:
#     print("YES" if dfs(line) else "NO")


print(sum([1 for line in lines if dfs(line)]))
