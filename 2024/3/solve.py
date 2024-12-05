#!/usr/bin/env python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

with open(filename) as fh:
    txt = fh.read()

total = 0
for m in mul.findall(txt):
    total += int(m[0]) * int(m[1])

print(total)
