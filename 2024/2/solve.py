#!/usr/bin/env python

from enum import Enum
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


class Direction(Enum):
    UP = 1
    DOWN = 2


safe_count = 0
for line in lines:
    li = [int(x) for x in line.split()]
    diffs = [li[i] - li[i + 1] for i in range(len(li) - 1)]
    if all(3 >= diff > 0 for diff in diffs):
        safe_count += 1
    elif all(-3 <= diff < 0 for diff in diffs):
        safe_count += 1


print(safe_count)

# 453
