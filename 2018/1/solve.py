#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]
    numbers = lines[:]

frequency = 0
for num in numbers:
    frequency = frequency + num

print(frequency)
