#!/usr/bin/env python

import sys
import re
from collections import defaultdict
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

#for line in lines:
#    print(line)

max_row = len(lines)
max_col = len(lines[0])
numbers = defaultdict(list)
for r, line in enumerate(lines):
    for m in re.finditer("(\d+)", line):
        v = int(m.group(1))
        s = m.start()
        e = m.end() - 1
        numbers[r].append((s, e, v))

total = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "*":
            #print(r,c)
            vals = []
            if r > 0:
                nums = numbers[r-1]
                for (s, e, v) in nums:
                    if s <= c + 1 and c - 1 <= e:
                        vals.append(v)
            if r < max_row - 1:
                nums = numbers[r+1]
                for (s, e, v) in nums:
                    if s <= c + 1 and c - 1 <= e:
                        vals.append(v)
            nums = numbers[r]
            for (s, e, v) in nums:
                if e == c - 1:
                    vals.append(v)
                if s == c + 1:
                    vals.append(v)
            if len (vals) == 2:
                total += vals[0] * vals[1]
            if len (vals) > 2:
                print('error')
                exit(1)




print(total)

