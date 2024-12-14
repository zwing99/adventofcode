#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

a, b = [int(x) for x in lines[0].split("-")]

count = 0
for x in range(a, b + 1):
    v = str(x)
    last = v[0]
    double = False
    increasing = True
    bad = False
    for i in range(1, len(v)):
        if int(v[i]) < int(last):
            increasing = False
        last = v[i]
    if increasing:
        i = 0
        while i < len(v):
            # print(i)
            j = i + 1
            cnt = 1
            while j < len(v):
                if v[i] == v[j]:
                    cnt += 1
                else:
                    break
                j += 1
            i = j
            # print(cnt)
            if cnt == 2:
                double = True
    if increasing and double and not bad:
        print(v)
        count += 1

print(count)

# 1109 That's not the right answer; your answer is too low.
# 1158 That's not the right answer; your answer is too low.
