#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

a, b = [int(x) for x in lines[0].split("-")]

count = 0
for x in range(a, b + 1):
    v = str(x)
    last = v[0]
    double = False
    increasing = True
    for i in range(1, len(v)):
        if v[i] == last:
            double = True
        if int(v[i]) < int(last):
            increasing = False
        last = v[i]
    if increasing and double:
        count += 1

print(count)
