#!/usr/bin/env python
from math import fabs

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [[int(i) for i in line.strip().split(",")] for line in fh.readlines()]


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


max_area = 0
for i in range(0, len(lines) - 1):
    for j in range(i + 1, len(lines)):
        if (a := area(lines[i], lines[j])) > max_area:
            max_area = a

print(max_area)
