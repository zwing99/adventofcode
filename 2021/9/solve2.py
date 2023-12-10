#!/usr/bin/env python

import sys
import math
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [[int(x) for x in line.strip()] for line in fh.readlines()]

bowls = []
for j, line in enumerate(lines):
    for i, v in enumerate(line):
        up = lines[j-1][i] > v if j > 0 else True
        down = lines[j+1][i] > v if j < len(lines)-1 else True
        left = line[i-1] > v if i > 0 else True
        right = line[i+1] > v if i < len(line)-1 else True
        if up and down and left and right:
            to_check = set()
            more = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for m in more:
                x, y = m
                if x >= 0 and x < len(line) and y >= 0 and y < len(lines):
                    to_check.add(m)
            total = 0
            checked = set()
            #print(f"Checking {j},{i}")
            #print(f"to_check: {to_check}")
            steps = 0
            while len(to_check) > 0:
                m = to_check.pop()
                if m in checked:
                    print("Already checked")
                    continue
                    #exit(1)
                #print (f"Checking {m}")
                steps += 1
                #print(f"Step: {steps}")
                #print("-----------------------------------")
                checked.add(m)
                x, y = m
                try:
                    if lines[y][x] == 9:
                        #print(f"Stop at {x},{y}")
                        continue
                except IndexError:
                    print(f"IndexError: {x},{y}")
                    print(f"IndexError: {lines[y]}")
                    raise
                more = set([(x+1,y), (x-1,y), (x,y-1), (x,y+1)]) - checked
                for n in more:
                    a, b = n
                    if a >= 0 and a < len(line) and b >= 0 and b < len(lines):
                        #print(f"Adding {n}")
                        to_check.add(n)
                #print(m)
                total += 1
            bowls.append(total)

bowls.sort(reverse=True)
print(bowls[:3])
print(math.prod(bowls[:3]))