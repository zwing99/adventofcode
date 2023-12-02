#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]

s = sorted(lines)
a = {1:1, 3:1}
for i in range(1, len(s)):
    diff = s[i] - s[i-1]
    a[diff] += 1

print(a)

