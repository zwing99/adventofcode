#!/usr/bin/env python

from functools import lru_cache
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]
    ranges = [[int(i) for i in p.split("-")] for p in lines[0].split(",")]


# @lru_cache(None)
def string_split(s: str, l: int):
    return [s[i : i + l] for i in range(0, len(s), l)]


# @lru_cache(None)
def is_invalid(i: int):
    s = str(i)
    l = len(s)
    for a in range(l // 2, 0, -1):
        if l % a == 0:
            things = string_split(s, a)
            if len(set(things)) == 1:
                return True
    return False


total = 0
for a, b in ranges:
    nums = range(a, b + 1)
    for i in nums:
        if is_invalid(i):
            total += i

print(total)
