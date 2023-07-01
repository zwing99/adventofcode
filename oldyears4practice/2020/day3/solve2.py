#!/usr/bin/env python

import sys
import functools
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

trees = [0,0,0,0,0]
px = [0,0,0,0,0]
move = [1,3,5,7,1]
maxx = len(lines[0])
for py in range(1, len(lines)):
    for i in range(len(trees)):
        if i == 4 and py % 2 == 0:
            px[i] += move[i]
            trees[i] += lines[py][px[i]%maxx] == '#'
        elif i < 4:
            px[i] += move[i]
            trees[i] += lines[py][px[i]%maxx] == '#'

print(trees)
print(functools.reduce(lambda a, b: a*b, trees))
    
