#!/usr/bin/env python

import math
import sys
from collections import defaultdict
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]

s = sorted(lines)
s1 = len(s) - 1

print(s)
t = dict()
r = dict()
paths = 1
def dfs(i):
    global paths
    if i >= s1:
        return
    if i in t: r[i] += 1; return
    t[i] = []
    r[i] = 1
    parts = 0
    v=s[i]
    v1=s[i+1]
    if (v1 - v) <= 3:
        t[i].append(i+1)
        dfs(i+1)
    if (i+2) < s1:
        v2 = s[i+2]
        if (v2 - v) <= 3:
            t[i].append(i+2)
            #print(i, paths)
            dfs(i+2)
    if (i+3) < s1:
        v3 = s[i+3]
        if (v3 - v) <= 3:
            t[i].append(i+3)
            #print(i, paths)
            dfs(i+3)
    return

dfs(0)
print(t)
print(r)
print(paths)


paths = 1

paths = 1
for i in range(s1):
    for v in t[i]:
        if len(v) > 1:


# (You guessed 70368744177664.)  That's not the right answer; your answer is too low.

