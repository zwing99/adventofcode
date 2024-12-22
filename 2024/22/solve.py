#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [int(line.strip()) for line in fh.readlines()]


total = 0
for sn in lines:
    for i in range(2000):
        sn = ((sn * 64) ^ sn) % 16777216
        sn = ((sn // 32) ^ sn) % 16777216
        sn = ((sn * 2048) ^ sn) % 16777216
    print(sn)
    total += sn

print("---------------")
print(f"Total: {total}")
