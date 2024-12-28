#!/usr/bin/env python

import sys
from collections import Counter
from itertools import pairwise

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

initial = lines.pop(0)
lines.pop(0)

m = {}
for line in lines:
    a, _, b = line.split()
    m[a] = b

for i in range(10):
    new = ""
    for a, b in pairwise(initial):
        new += a + m[a + b]
    new += b
    initial = new

c = Counter(initial)
d = c.most_common()
print(d[0][1] - d[-1][1])
