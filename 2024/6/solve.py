#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines: list[str] = [line.strip() for line in fh.readlines()]

visited: set[tuple[int, int]] = set()
direction: tuple[int, int] = (0, 1)
position = list[int]
x_range = len(lines[0])
y_range = len(lines)
directions_index: int
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for x in range(x_range):
    for y in range(y_range):
        if lines[y][x] in ("^", "v", "<", ">"):
            visited.add((x, y))
            position = [x, y]
            if lines[y][x] == "^":
                directions_index = 0
            elif lines[y][x] == ">":
                directions_index = 1
            elif lines[y][x] == "v":
                directions_index = 2
            elif lines[y][x] == "<":
                directions_index = 3
            break
    
print (x_range, y_range)
print (position)
visited.add(tuple(position))
while True:
    direction = directions[directions_index]
    next_x, next_y = position[0] + direction[0], position[1] + direction[1]
    print(next_x, next_y)
    if next_x < 0 or next_x >= x_range or next_y < 0 or next_y >= y_range:
        break
    if lines[next_y][next_x] == "#":
        directions_index = (directions_index + 1) % 4
    else:
        position = [next_x, next_y]
        visited.add(tuple(position))

print(len(visited))
