#!/usr/bin/env python

import sys
from collections import deque
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

starts = ['[', '{', '(', '<']
ends = [']', '}', ')', '>']
ends2starts = dict(zip(ends, starts))
starts2ends = dict(zip(starts, ends))

scoring = {
    ")": 1, # point.
    "]": 2, # points.
    "}": 3, # points.
    ">": 4, # points.
}

scores = []
for line in lines:
    stack = deque()
    bad = False
    score = 0
    for c in line:
        if c in starts:
            stack.append(c)
        elif c in ends:
            if len(stack) == 0:
                print("Unbalanced")
            if stack[-1] == ends2starts[c]:
                stack.pop()
            else:
                #print("Bad")
                #print(c)
                bad = True
                break
    if bad:
        continue

    for c in reversed(stack):
        score *= 5
        score += scoring[starts2ends[c]]
    scores.append(score)

scores.sort()
print(scores)
print(scores[len(scores)//2])
        
    

