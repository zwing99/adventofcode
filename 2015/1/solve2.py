#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

line = lines[0]
# up = line.count("(")
# down = line.count(")")

i = 1
level = 0
while True:
    c, line = line[0], line[1:]
    if c == "(":
        level += 1
    else:
        level -= 1
    if level == -1:
        print(i)
        break
    i += 1
