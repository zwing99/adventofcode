#!/usr/bin/env python

import enum
import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.rstrip("\n") for line in fh.readlines()]

num_nums = len(lines) - 1

p = re.compile(r"[+*]\s+")
total = 0
for m in p.finditer(lines[-1]):
    i = m.start()
    j = m.end()
    if j == len(lines[-1]):
        j += 1
    # print(i, j)
    op = m.group().strip()
    t = 0 if op == "+" else 1
    for z in range(j - 2, i - 1, -1):
        v = ""
        for n in range(num_nums):
            # print(n, z, lines[n], lines[n][z])
            v += lines[n][z]
        v = int(v)
        # print(v)
        if op == "+":
            t += v
        else:
            t *= v
    # print(t)
    # print("----")
    total += t

print(total)
