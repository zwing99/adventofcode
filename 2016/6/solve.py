#!/usr/bin/env python

from collections import Counter
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

counters = [Counter() for x in range(len(lines[0]))]

for line in lines:
    for c, cnt in zip(line, counters):
        cnt.update(c)

word = "".join([cnt.most_common(1)[0][0] for cnt in counters])
print(word)
