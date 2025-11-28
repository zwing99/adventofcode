#!/usr/bin/env python

import re
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

r = re.compile(r"\((\d+)x(\d+)\)")

for line in lines:
    pos = 0
    full = ""
    while pos < len(line):
        m = r.search(line, pos)
        if m:
            a, b = [int(x) for x in m.groups()]
            full += line[pos : m.start()]
            for _ in range(b):
                full += line[m.end() : m.end() + a]
            pos = m.end() + a
        else:
            full += line[pos:]
            break
    print(full, len(full))
