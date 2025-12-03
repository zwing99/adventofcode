#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    max = 0
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            v = int(line[i] + line[j])
            if v > max:
                max = v
    total += max

print(total)
