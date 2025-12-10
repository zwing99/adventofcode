#!/usr/bin/env python
from cmath import sqrt

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
loops = 10 if filename != "input.txt" else 1000

with open(filename) as fh:
    lines = [
        tuple([int(i) for i in line.strip().split(",")]) for line in fh.readlines()
    ]


def distance(a, b):
    return sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


distances = {}

for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        dist = distance(lines[i], lines[j])
        if dist.imag != 0:
            raise ValueError("Unexpected complex distance")
        if dist.real not in distances:
            distances[dist.real] = (lines[i], lines[j])
        else:
            print("woooooah")

sorted_distances = sorted(distances.keys())
# print(sorted_distances[:loops])
groups = []
for i in range(loops):
    dist = sorted_distances[i]
    a, b = distances[dist]
    groups_found = []
    for i, group in enumerate(groups):
        if a in group or b in group:
            group.add(a)
            group.add(b)
            groups_found.append(i)
    if not groups_found:
        groups.append(set([a, b]))
    if len(groups_found) > 1:
        first = groups_found[0]
        for other in groups_found[1:]:
            groups[first].update(groups[other])
        for other in reversed(groups_found[1:]):
            del groups[other]
    # print(f"{i}: Groups: {groups}")

groups.sort(key=lambda g: -len(g))

# for group in groups[:3]:
#    print("Group:")
#    for point in group:
#        print(f"  {point}")

nums = [len(i) for i in groups[:3]]
print(nums)
print(nums[0] * nums[1] * nums[2])

# 2145 = 15,13,11
