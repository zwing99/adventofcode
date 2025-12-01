#!/usr/bin/env python

from math import fabs
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

pos = 50

count = 0
for line in lines:
    print(line, pos)
    dir = line[0]
    amount = int(line[1:])
    if dir == "L":
        if (pos - amount) <= 0:
            count += ((pos - amount) // -100) + 1
            if pos == 0:
                count -= 1
            print(count)
        pos = (pos - amount) % 100
    elif dir == "R":
        if (pos + amount) >= 100:
            count += (pos + amount) // 100
            print(count)
        pos = (pos + amount) % 100
    else:
        assert False, "fail"

print(count)

# 7212 - That's not the right answer; your answer is too high.
# 7105 - That's not the right answer; your answer is too high.
# 7774
# 6941
