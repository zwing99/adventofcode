#!/usr/bin/env python

import sys
from collections import deque
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

starts = ['[', '{', '(', '<']
ends = [']', '}', ')', '>']
ends2starts = dict(zip(ends, starts))

scoring = {
    ")": 3, #points.
    "]": 57, #points.
    "}": 1197, #points.
    ">": 25137, #points.
}

total = 0
for line in lines:
    stack = deque()
    for c in line:
        if c in starts:
            stack.append(c)
        elif c in ends:
            if len(stack) == 0:
                print("Unbalanced")
            if stack[-1] == ends2starts[c]:
                stack.pop()
            else:
                print("Bad")
                print(c)
                total += scoring[c]
                break

print(total)
