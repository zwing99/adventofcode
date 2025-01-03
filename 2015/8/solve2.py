#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    a = ""
    for c in line:
        if c == "\\" or c == '"':
            a += "\\"
        a += c
    print(a)
    total += len(a) - len(line) + 2
print(total)

# 2170 That's not the right answer; your answer is too high.
