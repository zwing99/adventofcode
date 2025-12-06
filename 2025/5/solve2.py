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

ranges.sort(key=lambda x: (x[0], x[1]))

total = 0
new_ranges = []
for x, y in ranges:
    pop_out = []
    inside = False
    for i in range(len(new_ranges)):
        r = new_ranges[i]
        if x < r[0] and y > r[1]:
            pop_out.append(i)
        elif x < r[0] and y >= r[0] and y <= r[1]:
            y = r[1]
            pop_out.append(i)
        elif x >= r[0] and x <= r[1] and y > r[1]:
            x = r[0]
            pop_out.append(i)
        elif x >= r[0] and x <= r[1] and y >= r[0] and y <= r[1]:
            inside = True
            # print("inside")
    # if pop_out:
    #     print(pop_out, x, y, inside)
    for i in reversed(pop_out):
        new_ranges.pop(i)
    if not inside:
        new_ranges.append((x, y))

for x, y in new_ranges:
    # print(x, y)
    total += y - x + 1

print(total)
