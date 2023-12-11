#!/usr/bin/env python

import sys
import itertools
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [[x for x in line.strip()] for line in fh.readlines()]

def print_lines():
    for line in lines:
        print("".join(line))

#print_lines()

columns_to_expand = []
for i in range(len(lines[0])):
    all_dot = True
    for j in range(len(lines)):
        if lines[j][i] != ".":
            all_dot = False
        if not all_dot:
            break
    if all_dot:
        columns_to_expand.append(i)

rows_to_expand = []
for j in range(len(lines)):
    all_dot = True
    for i in range(len(lines[0])):
        if lines[j][i] != ".":
            all_dot = False
        if not all_dot:
            break
    if all_dot:
        rows_to_expand.append(j)

#print(columns_to_expand)
#print(rows_to_expand)
        
#print_lines()

galaxies = []
for j in range(len(lines)):
    for i in range(len(lines[0])):
        if lines[j][i] == "#":
            galaxies.append((i, j))

total = 0
expansion_contant = 1000000 - 1
for g1, g2 in itertools.combinations(galaxies, 2):
    range_x = sorted([g1[0], g2[0]])
    distance = 0
    for i in columns_to_expand:
        if range_x[0] <= i <= range_x[1]:
            distance += expansion_contant
    range_y = sorted([g1[1], g2[1]])
    for j in rows_to_expand:
        if range_y[0] <= j <= range_y[1]:
            distance += expansion_contant
    distance += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    total += distance

print(total)
