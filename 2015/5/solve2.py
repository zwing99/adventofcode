#!/usr/bin/env python

from operator import is_
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

all_letters = "abcdefghijklmnopqrstuvwxyz"
double_letters = [l + l for l in all_letters]


def is_nice(s):
    is_nice = False
    for i in range(len(s) - 2):
        v = s[i : i + 2]
        if v in s[:i] or v in s[i + 2 :]:
            print(v, s[:i], s[i + 2 :])
            is_nice = True
            break
    if not is_nice:
        return is_nice
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            print(s[i : i + 3])
            return True
    return False


a = [line for line in lines if is_nice(line)]
la = len(a)
print(a)
print(la)


# 49
