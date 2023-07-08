#!/usr/bin/env python

import sys
from collections import defaultdict
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

groups = []
d = defaultdict(lambda: 0)
p = 0
for l in lines:
    if l == '': 
        groups.append((dict(d), p))
        d = defaultdict(lambda: 0)
        p = 0
        continue
    for c in l:
        d[c] += 1
    p += 1

groups.append((dict(d),p))
print(groups)

total = 0
for d, p in groups:
    for v in d.values():
        if v == p:
            total += 1

print(total)