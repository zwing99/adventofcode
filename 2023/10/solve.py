#!/usr/bin/env python

import sys
import typing as typ
from enum import Enum, auto as auto_enum
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

class Pipe(Enum):
    up = auto_enum()
    down = auto_enum()
    left = auto_enum()
    right = auto_enum()

connects = [[Pipe.up, Pipe.down], [Pipe.left, Pipe.right]]


mappings: dict[str, set[Pipe]] = {
    "|": {Pipe.up, Pipe.down}, # is a vertical pipe connecting north and south.
    "-": {Pipe.left, Pipe.right}, # is a horizontal pipe connecting east and west.
    "L": {Pipe.up, Pipe.right}, # is a 90-degree bend connecting north and east.
    "J": {Pipe.up, Pipe.left}, # is a 90-degree bend connecting north and west.
    "7": {Pipe.down, Pipe.left}, # is a 90-degree bend connecting south and west.
    "F": {Pipe.down, Pipe.right}, # is a 90-degree bend connecting south and east.
    ".": {},  # is ground; there is no pipe in this tile.
    "S": {},  # is
}

step_map: dict[Pipe, typ.Tuple[int, int]] = {
    Pipe.up: (0, -1),
    Pipe.down: (0, 1),
    Pipe.left: (-1, 0),
    Pipe.right: (1, 0),
}
all_dirs = list(step_map.values())
back_map: dict[typ.Tuple[int, int], Pipe] = {
    (0, -1): Pipe.down,
    (0, 1): Pipe.up,
    (-1, 0): Pipe.right,
    (1, 0): Pipe.left,
}

start = None
grid: list[list[Pipe]] = []
for j, line in enumerate(lines):
    grid.append([mappings[c] for c in line])
    for i, c in enumerate(line):
        # print (i, j, c)
        if c == "S":
            start = (i, j)
if start is None:
    raise ValueError("No start found")

starts = []

for dx, dy in all_dirs:
    x, y = start[0] + dx, start[1] + dy
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        p = grid[y][x]
        if back_map[(dx, dy)] in p:
            #print(p)
            starts.append((dx, dy))

my_start = starts[0]
step_dir = my_start
step = start[0] + step_dir[0], start[1] + step_dir[1]
loop = [start, step]
while step != start:
    next_dir = grid[step[1]][step[0]].copy() - {back_map[step_dir]}
    if len(next_dir) != 1:
        raise ValueError("Invalid path")
    #print(next_dir)
    step_dir = step_map[next_dir.pop()]
    step = step[0] + step_dir[0], step[1] + step_dir[1]
    loop.append(step)
    #print(step)


#print(f"Loop: {loop}")
print(len(loop)//2)





#print(grid)