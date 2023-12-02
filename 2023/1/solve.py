#!/usr/bin/env python

import sys
import re
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    m1 = re.match(r"\D*(\d)", line).group(1)
    m2 = re.match(r".*(\d)\D*", line).group(1)
    v = int(m1+m2)
    total += v

print(total)