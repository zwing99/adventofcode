#!/usr/bin/env python

from functools import cache
from itertools import pairwise
import sys
from collections import Counter, defaultdict

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

initial = lines.pop(0)
lines.pop(0)

m = {}
for line in lines:
    a, _, b = line.split()
    m[a] = b


@cache
def dfs(s, depth, max_depth):
    # print(s, depth)
    if depth == max_depth:
        return dict(Counter(s[:-1]))
    else:
        c = Counter()
        for a, b in pairwise(s):
            # print(depth, a, b)
            c.update(dfs(a + m[a + b] + b, depth + 1, max_depth))
        if depth == 0:
            # print(s[-1])
            c.update({s[-1]: 1})
        return c


c = dfs(initial, 0, 40)
# print(c)
d = c.most_common()
print(d[0][1] - d[-1][1])
