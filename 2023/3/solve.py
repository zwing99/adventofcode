#!/usr/bin/env python

import sys
import re
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

for line in lines:
    print(line)

total = 0
max_row = len(lines)
max_col = len(lines[0])
for r, line in enumerate(lines):
    for m in re.finditer("(\d+)", line):
        v = int(m.group(1))
        s = m.start()
        e = m.end() - 1
        #print(v, s, e)
        is_good = False
        if s > 0: 
            if lines[r][s-1] != '.':
                is_good = True
            s = s - 1
        if e < max_col - 1:
            if lines[r][e+1] != '.':
                is_good = True
            e = e + 1
        if r > 0:
            for i in range(s, e+1):
                if lines[r-1][i] != '.':
                    is_good = True
        if r < max_row - 1:
            for i in range(s, e+1):
                if lines[r+1][i] != '.':
                    is_good = True
        if is_good:
            total += v

print(total)

