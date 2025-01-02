#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

all_letters = "abcdefghijklmnopqrstuvwxyz"
double_letters = [l + l for l in all_letters]


def is_nice(s):
    vowel_count = 0
    for v in "aeiou":
        vowel_count += s.count(v)
    if vowel_count < 3:
        return False
    if not any(dl in s for dl in double_letters):
        return False
    if any(bad in s for bad in ["ab", "cd", "pq", "xy"]):
        return False
    return True


a = [line for line in lines if is_nice(line)]
la = len(a)
print(la)

# 165 That's not the right answer; your answer is too low.
