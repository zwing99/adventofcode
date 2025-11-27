#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

line = lines[0]

for i in range(40):
    j = 0
    cnt = 1
    c = ""
    while j < len(line) - 1:
        if line[j] == line[j + 1]:
            cnt += 1
        else:
            c += str(cnt) + line[j]
            cnt = 1
        j += 1
    c += str(cnt) + line[j]
    print(i)
    print(len(c))
    line = c
