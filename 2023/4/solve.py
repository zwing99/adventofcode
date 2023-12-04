#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    winners, numbers = line.split(":")[1].split("|")
    winners = set([int(i) for i in winners.strip().split()])
    numbers = set([int(i) for i in numbers.strip().split()])
    matching = len(winners & numbers)
    total += int(2 ** (matching - 1))

print(total)