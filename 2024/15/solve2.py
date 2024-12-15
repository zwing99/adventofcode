#!/usr/bin/env python

import sys
import os
import debugpy

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
    new_line = []
    for c in line:
        if c == "#":
            new_line.extend(["#", "#"])
        elif c == "O":
            new_line.extend(["[", "]"])
        elif c == ".":
            new_line.extend([".", "."])
        elif c == "@":
            new_line.extend(["@", "."])
        else:
            new_line.extend(c)
    grid.append(new_line)
    if "@" in new_line:
        x = new_line.index("@")
        start = (x, y)
    y += 1

moves = ""
for line in lines:
    moves += line

directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
current_pos = (start[0], start[1])
x_length = len(grid[0])
y_length = len(grid)

print("\n".join(["".join(x) for x in grid]))
print(moves)
print(start)


def swap_obj(p1, dir):
    new_pos = (p1[0] + dir[0], p1[1] + dir[1])
    v1 = grid[p1[1]][p1[0]]
    v2 = grid[new_pos[1]][new_pos[0]]
    grid[p1[1]][p1[0]] = v2
    grid[new_pos[1]][new_pos[0]] = v1


def is_outside_bounds(pos):
    return pos[0] < 0 or pos[0] >= x_length or pos[1] < 0 or pos[1] >= y_length


for n, m in enumerate(moves):
    d = directions.get(m)
    assert d
    pot_pos = (current_pos[0] + d[0], current_pos[1] + d[1])
    if grid[pot_pos[1]][pot_pos[0]] == "#":
        pass
    elif grid[pot_pos[1]][pot_pos[0]] == ".":
        swap_obj(current_pos, d)
        current_pos = pot_pos
    elif grid[pot_pos[1]][pot_pos[0]] in "[]":  # pushing 'O' object
        # find empty '.' space in the direction
        fcols = set([current_pos[0]])
        if m in "^v":
            if grid[pot_pos[1]][pot_pos[0]] == "[":
                fcols.add(current_pos[0] + 1)
            elif grid[pot_pos[1]][pot_pos[0]] == "]":
                fcols.add(current_pos[0] - 1)
            else:
                assert -1 == 1, "Invalid move"
        to_move = [(1, fcols)]
        found = False
        steps = 2
        while True:
            empty = True
            blocked = False
            new_cols = set()
            look_ahead_y = current_pos[1] + d[1] * steps
            for col in to_move[0][1]:
                look_ahead_x = col + d[0] * steps
                v = grid[look_ahead_y][look_ahead_x]
                if v == "#":
                    blocked = True
                    break
                if v in "[]":
                    new_cols.add(col)
                    empty = False
                    if m in "^v":
                        if v == "[":
                            new_cols.add(look_ahead_x + 1)
                        elif v == "]":
                            new_cols.add(look_ahead_x - 1)
            if blocked:
                break
            if empty:
                found = True
                break
            to_move.insert(0, (steps, new_cols))
            steps += 1
        if found:
            for i, cols in to_move:
                for col in cols:
                    swap_pos = (col + d[0] * i, current_pos[1] + d[1] * i)
                    swap_obj(swap_pos, d)
            swap_obj(current_pos, d)
            current_pos = pot_pos
    else:
        print(grid[pot_pos[1]][pot_pos[0]])
        assert -1 == 1, "Invalid move"

    # print(f"{m}")
    # print("\n".join(["".join(x) for x in grid]))

print("\n".join(["".join(x) for x in grid]))

total = 0
for y in range(y_length):
    for x in range(x_length):
        if grid[y][x] == "[":
            total += 100 * y + x

print(total)
