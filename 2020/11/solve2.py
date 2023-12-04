#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip().replace('L', '#') for line in fh.readlines()]

def count_occupied():
    occupied = 0
    for line in lines:
        occupied += line.count('#')
    return occupied

def count_ajacent_extended(i, j):
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        x, y = i + dx, j + dy
        while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
            if lines[x][y] == '#':
                count += 1
                break
            elif lines[x][y] == 'L':
                break
            x += dx
            y += dy
    return count

last_occupied = count_occupied()
print("last_occupied", last_occupied)

steps = 0
while True:
    last_occupied = count_occupied()
    new_lines = []
    for i, line in enumerate(lines):
        new_line = ''
        for j, seat in enumerate(line):
            if seat == '#':
                if count_ajacent_extended(i, j) >= 5:
                    new_line += 'L'
                else:
                    new_line += '#'
            elif seat == 'L':
                if count_ajacent_extended(i, j) == 0:
                    new_line += '#'
                else:
                    new_line += 'L'
            else:
                new_line += '.'
        new_lines.append(new_line)
    lines = new_lines
    steps += 1
    print ("step", steps, "occupied", count_occupied(), "last_occupied", last_occupied)
    if last_occupied == count_occupied():
        break


print(count_occupied())