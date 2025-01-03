#!/usr/bin/env python

from itertools import permutations
import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

to_from = re.compile("(\w+) to (\w+) = (\d+)")

distances = {}
for line in lines:
    m = to_from.match(line)
    assert m
    t, f, d = m.groups()
    print(t, f, d)
    distances[(t, f)] = int(d)
    distances[(f, t)] = int(d)

locations = set([t for t, f in distances.keys()] + [f for t, f in distances.keys()])
len_locations = len(locations)

min_distance = 999999999
long_distance = 0
for perm in permutations(locations):
    total = sum([distances[(perm[i], perm[i + 1])] for i in range(len_locations - 1)])
    if total < min_distance:
        min_distance = total
        best = perm
    if total > long_distance:
        long_distance = total
        worst = perm
    print(perm, total)

print(f"Best: {best} {min_distance}")
print(f"Worst: {worst} {long_distance}")
