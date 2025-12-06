#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

ranges = []
nums = []
isPart2 = False
for line in lines:
    if line == "":
        isPart2 = True
        continue
    if not isPart2:
        x, y = line.split("-")
        ranges.append((int(x), int(y)))
    else:
        nums.append(int(line))

total = 0
for n in nums:
    for x, y in ranges:
        if n >= x and n <= y:
            total += 1
            break

print(total)
