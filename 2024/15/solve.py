#!/usr/bin/env python

import enum
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

grid = []
y = 0
start = (0, 0)
while True:
    line = str(lines.pop(0))
    if line == "":
        break
    if (x := line.find("@")) != -1:
        start = (x, y)
    grid.append([x for x in line])
    y += 1

moves = ""
for line in lines:
    moves += line

directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
current_pos = (start[0], start[1])
x_length = len(grid[0])
y_length = len(grid)


def swap_obj(p1, dir):
    new_pos = (p1[0] + dir[0], p1[1] + dir[1])
    v1 = grid[p1[1]][p1[0]]
    v2 = grid[new_pos[1]][new_pos[0]]
    grid[p1[1]][p1[0]] = v2
    grid[new_pos[1]][new_pos[0]] = v1


def is_outside_bounds(pos):
    return pos[0] < 0 or pos[0] >= x_length or pos[1] < 0 or pos[1] >= y_length


# print("\n".join(["".join(x) for x in grid]))


for n, m in enumerate(moves):
    d = directions.get(m)
    assert d
    pot_pos = (current_pos[0] + d[0], current_pos[1] + d[1])
    if grid[pot_pos[1]][pot_pos[0]] == "#":
        pass
    elif grid[pot_pos[1]][pot_pos[0]] == ".":
        swap_obj(current_pos, d)
        current_pos = pot_pos
    elif grid[pot_pos[1]][pot_pos[0]] == "O":  # pushing 'O' object
        # find empty '.' space in the direction
        found = False
        look_ahead = pot_pos
        while True:
            look_ahead = (look_ahead[0] + d[0], look_ahead[1] + d[1])
            if (
                is_outside_bounds(look_ahead)
                or grid[look_ahead[1]][look_ahead[0]] == "#"
            ):
                break
            if grid[look_ahead[1]][look_ahead[0]] == ".":
                found = True
                grid[look_ahead[1]][look_ahead[0]] = "O"
                break
        if found:
            grid[pot_pos[1]][pot_pos[0]] = "."
            swap_obj(current_pos, d)
            current_pos = pot_pos
    else:
        assert -1 == 1, "Invalid move"

    # print(f"{m}")
    # print("\n".join(["".join(x) for x in grid]))

print("\n".join(["".join(x) for x in grid]))

total = 0
for y in range(y_length):
    for x in range(x_length):
        if grid[y][x] == "O":
            total += 100 * y + x

print(total)
