#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines: list[list[str]] = [[x for x in line.strip()] for line in fh.readlines()]

direction: tuple[int, int] = (0, 1)
position = list[int]
x_range = len(lines[0])
y_range = len(lines)
directions_index: int
start_directions_index: int
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for x in range(x_range):
    for y in range(y_range):
        if lines[y][x] in ("^", "v", "<", ">"):
            position = [x, y]
            start = (x, y)
            if lines[y][x] == "^":
                start_directions_index = 0
            elif lines[y][x] == ">":
                start_directions_index = 1
            elif lines[y][x] == "v":
                start_directions_index = 2
            elif lines[y][x] == "<":
                start_directions_index = 3
            break
    
count = 0
for i in range(x_range):
    for j in range(y_range):
        position = [start[0], start[1]]
        directions_index = start_directions_index
        visited: set[tuple[int, int, int]] = set()
        visited.add((position[0], position[1], directions_index))
        leaves_grid = True
        if (i, j) == start or lines[j][i] == "#":
            continue
        lines[j][i] = "#"
        #print('---------------')
        while True:
            direction = directions[directions_index]
            next_x, next_y = position[0] + direction[0], position[1] + direction[1]
            if next_x < 0 or next_x >= x_range or next_y < 0 or next_y >= y_range:
                #print("leaves grid")
                break
            elif (next_x, next_y, directions_index) in visited:
                #print(next_x, next_y, directions_index)
                leaves_grid = False
                break
            if lines[next_y][next_x] == "#":
                directions_index = (directions_index + 1) % 4
                visited.add((position[0], position[1], directions_index))
            else:
                position = [next_x, next_y]
                visited.add((position[0], position[1], directions_index))
        if not leaves_grid:
            count += 1
        lines[j][i] = "."

print(count)
