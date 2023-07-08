#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip().split() for line in fh.readlines()]
    lines = [(inst, int(v)) for inst, v in lines]

print(lines)

accum = 0
i = 0
visited = set()

while True:
    if i in visited:
        break
    visited.add(i)
    inst, v = lines[i]
    #print(inst, v, visited)
    if inst == 'nop':
        i += 1
    elif inst == 'acc':
        i += 1
        accum += v
    elif inst == 'jmp':
        i += v

print(i, accum)
