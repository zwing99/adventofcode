#!/usr/bin/env python

import sys
from math import fabs

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]
    steps = [l.strip() for l in lines[0].split(",")]
    steps = [(s[0], int(s[1:])) for s in steps]

pos = [0, 0]
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
di: int = 0

visited = [pos[:]]
found = False
for lr, a in steps:
    print(lr, a)
    if lr == "L":
        di -= 1
    elif lr == "R":
        di += 1
    else:
        print("error")
        exit("-1")
    di = di % 4
    print(di)
    d = dirs[di]
    print(d)
    for i in range(a):
        pos[0] += d[0]
        pos[1] += d[1]
        if pos in visited:
            found = True
            print("visited twice")
            break
        else:
            visited.append(pos[:])
    if found:
        break
    print(pos)

print(int(sum([fabs(j) for j in pos])))
