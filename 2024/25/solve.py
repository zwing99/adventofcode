#!/usr/bin/env python

from itertools import product
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


keys = []
locks = []
height = 0


def process(s):
    global height
    height = len(s) - 2
    if all([x == "#" for x in s[0]]):
        v = [0 for x in range(len(s[0]))]
        for i in range(1, len(s)):
            for j in range(len(s[i])):
                if s[i][j] == "#":
                    v[j] += 1
        keys.append(v)
    if all([x == "#" for x in s[-1]]):
        v = [0 for x in range(len(s[0]))]
        for i in range(len(s) - 2, 0, -1):
            for j in range(len(s[i])):
                if s[i][j] == "#":
                    v[j] += 1
        locks.append(v)


s = []
while True:
    try:
        l = lines.pop(0)
    except IndexError:
        break
    if l == "":
        process(s)
        s = []
    else:
        s.append(l)
process(s)

print(keys)
print(locks)
print(height)

total = 0
for k, l in product(keys, locks):
    if all([x + y <= height for x, y in zip(k, l)]):
        total += 1
print(total)
