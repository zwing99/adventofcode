#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]

sum = 0
for line in lines:
    v = line
    while True:
        v = int(v / 3) - 2
        if v <= 0:
            break
        sum += v

print(sum)
