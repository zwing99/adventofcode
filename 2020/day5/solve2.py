#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def parseit(seat: str):
    rows = list(range(128))
    cols = list(range(8))
    for i in seat[:7]:
        if i == 'F': rows = rows[:len(rows)//2]
        elif i == 'B': rows = rows[len(rows)//2:]
        else: print('fail:', i, seat); exit(1)
    for i in seat[7:]:
        if i == 'L': cols = cols[:len(cols)//2]
        elif i == 'R': cols = cols[len(cols)//2:]
        else: print('fail:', i, seat); exit(1)
    row, col = rows[0], cols[0]
    #print(row, col)
    return row * 8 + col

seat_ids = sorted([parseit(l) for l in lines])
for i, s in enumerate(seat_ids[:-1]):
    if s + 1 != seat_ids[i+1]:
        print(s+1)