#!/usr/bin/env python

from functools import lru_cache
import re
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

r = re.compile(r"\((\d+)x(\d+)\)")


@lru_cache(None)
def get_length(st):
    pos = 0
    v = 0
    while pos < len(st):
        m = r.search(st, pos)
        if m:
            a, b = [int(x) for x in m.groups()]
            v += m.start() - pos
            for _ in range(b):
                v += get_length(st[m.end() : m.end() + a])
            pos = m.end() + a
        else:
            v += len(st) - pos
            break
    return v


for line in lines:
    print(get_length(line))
