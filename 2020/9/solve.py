#!/usr/bin/env python

import sys
from itertools import combinations
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.txt'

l = 5
if filename == 'input.txt':
    l = 25

print(f"preamble: {l}")

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]

#print(lines[:50])
for i in range(l,len(lines)):
    p = lines[i-l:i]
    v = lines[i]
    is_valid = False
    #print('---------------------------------------')
    for x,y in combinations(p, 2):
        #print(x+y, v)
        if v == x + y:
            is_valid = True
        if is_valid:
            break
    if not is_valid:
        print(v)
        break


# You guessed 639.  That's not the right answer; your answer is too low.