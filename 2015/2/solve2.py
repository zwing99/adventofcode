#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

needed = 0
for line in lines:
    l, w, h = [int(x) for x in line.split("x")]
    v = l * w * h
    a = 2 * l + 2 * w
    b = 2 * w + 2 * h
    c = 2 * h + 2 * l
    needed += min(a, b, c) + v
print(needed)

# 1456684 That's not the right answer; your answer is too low.
