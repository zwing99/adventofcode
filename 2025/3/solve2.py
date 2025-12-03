#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    digits = ""
    last_digit_index = 0
    for i in range(11, -1, -1):
        max = 0
        for j in range(last_digit_index, len(line) - i):
            jv = int(line[j])
            if jv > max:
                max = jv
                last_digit_index = j + 1
        digits += str(max)

    print(digits)
    total += int(digits)

print(total)
