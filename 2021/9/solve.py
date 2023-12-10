#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for j, line in enumerate(lines):
    for i, v in enumerate(line):
        up = lines[j-1][i] > v if j > 0 else True
        down = lines[j+1][i] > v if j < len(lines)-1 else True
        left = line[i-1] > v if i > 0 else True
        right = line[i+1] > v if i < len(line)-1 else True
        if up and down and left and right:
            total += int(v) + 1
print(total)