#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip().split() for line in fh.readlines()]

li1 = sorted([int(l[0]) for l in lines])
li2 = sorted([int(l[1]) for l in lines])

print(sum(map(lambda x: abs(x[0] - x[1]), zip(li1, li2))))
