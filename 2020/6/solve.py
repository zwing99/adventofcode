#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

groups = []
s = set()
for l in lines:
    if l == '': 
        groups.append(s)
        s = set()
        continue
    for c in l:
        s.add(c)

groups.append(s)
# print(groups)
print(sum([len(g) for g in groups]))