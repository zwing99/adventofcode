#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [[int(i) for i in line.strip().split()] for line in fh.readlines()]

cnt = 0
for a, b, c in lines:
    if a + b > c and b + c > a and c + a > b:
        cnt += 1

print(cnt)
