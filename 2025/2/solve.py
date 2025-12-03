#!/usr/bin/env python

from functools import lru_cache
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]
    ranges = [[int(i) for i in p.split("-")] for p in lines[0].split(",")]


@lru_cache(None)
def is_invalid(i: int):
    s = str(i)
    l = len(s)
    if l % 2 == 1:
        return False
    half_l = l // 2
    if s[:half_l] == s[half_l:]:
        return True
    return False


total = 0
for a, b in ranges:
    nums = range(a, b + 1)
    for i in nums:
        if is_invalid(i):
            total += i

print(total)
