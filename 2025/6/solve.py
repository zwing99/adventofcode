#!/usr/bin/env python

import enum
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

nums = []
for line in lines[:-1]:
    nums.append([int(x) for x in line.split()])
ops = [x.strip() for x in lines[-1].split()]


total = 0
for i, op in enumerate(ops):
    t = 0 if op == "+" else 1
    for num in nums:
        if op == "+":
            t += num[i]
        else:
            t *= num[i]
    # print(t)
    total += t
print(total)
