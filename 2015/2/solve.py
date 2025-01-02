#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

needed = 0
for line in lines:
    l, w, h = [int(x) for x in line.split("x")]
    a = l * w
    b = w * h
    c = h * l
    needed += 2 * a + 2 * b + 2 * c + min(a, b, c)
print(needed)

# 1456684 That's not the right answer; your answer is too low.
