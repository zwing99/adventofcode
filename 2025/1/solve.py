#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

numbers = list(range(100))
pos = 50
# print(numbers[pos])

count = 0
for line in lines:
    dir = line[0]
    amount = int(line[1:])
    if dir == "L":
        pos = (pos - amount) % 100
    elif dir == "R":
        pos = (pos + amount) % 100
    else:
        assert False, "fail"
    # print(pos)
    if numbers[pos] == 0:
        count += 1

print(count)
