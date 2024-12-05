#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

rules = []
line = lines.pop(0)
while line != "":
    a, b = [int(i) for i in line.split("|")]
    rules.append((a, b))
    line = lines.pop(0)

total = 0
for line in lines:
    numbers = [int(i) for i in line.split(",")]
    is_good = True
    for a, b in rules:
        if a in numbers and b in numbers:
            if numbers.index(a) > numbers.index(b):
                is_good = False
                break
    if is_good:
        total += numbers[len(numbers) // 2]

print(total)
