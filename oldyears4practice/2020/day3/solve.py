#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

trees = 0
px = 0
maxx = len(lines[0])
for py in range(1, len(lines)):
    px += 3
    trees += lines[py][px%maxx] == '#'

print(trees)
    
