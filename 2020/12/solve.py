#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


start = [0,0]
direction = [1, 0]

for line in lines:
    action = line[0]
    value = int(line[1:])
    if action == 'N':
        start[1] += value
    elif action == 'S':
        start[1] -= value
    elif action == 'E':
        start[0] += value
    elif action == 'W':
        start[0] -= value
    elif action == 'L':
        for i in range(value // 90):
            direction = [-direction[1], direction[0]]
    elif action == 'R':
        for i in range(value // 90):
            direction = [direction[1], -direction[0]]
    elif action == 'F':
        start[0] += direction[0] * value
        start[1] += direction[1] * value


print(abs(start[0]) + abs(start[1]))
