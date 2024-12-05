#!/usr/bin/env python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

mul = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")

with open(filename) as fh:
    txt = fh.read()

total = 0
active = True
for m in mul.findall(txt):
    if m[0] == "do()":
        active = True
    elif m[0] == "don't()":
        active = False
    elif active:
        total += int(m[1]) * int(m[2])

print(total)
