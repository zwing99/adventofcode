#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [[int(i) for i in line.strip().split()] for line in fh.readlines()]

cnt = 0
for i in range(len(lines) // 3):
    l1 = lines[3 * i]
    l2 = lines[3 * i + 1]
    l3 = lines[3 * i + 2]
    for j in range(3):
        a, b, c = l1[j], l2[j], l3[j]
        if a + b > c and b + c > a and c + a > b:
            cnt += 1

print(cnt)
