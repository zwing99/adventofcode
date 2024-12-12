#!/usr/bin/env python

import sys
import shapely
import dataclasses

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

x_range = len(lines[0])
y_range = len(lines)


@dataclasses.dataclass
class Plot:
    geometry: shapely.Polygon
    name: str
    origin: tuple[int, int]


plots: dict[tuple[int, int], Plot] = {}
for y in range(y_range):
    for x in range(x_range):
        shape = shapely.Polygon(([x, y], [x + 1, y], [x + 1, y - 1], [x, y - 1]))
        plots[(x, y)] = Plot(shape, lines[y][x], (x, y))

visited: set[tuple[int, int]] = set()
final_shapes: list[Plot] = list()
for p in plots.values():
    x, y = p.origin
    if (x, y) in visited:
        continue
    visited.add((x, y))
    hunt = [(x, y)]
    while hunt:
        hunt_x, hunt_y = hunt.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = hunt_x + dx, hunt_y + dy
            if (nx, ny) not in visited and (nx, ny) in plots:
                if plots[(nx, ny)].name == p.name:
                    p.geometry = p.geometry.union(plots[(nx, ny)].geometry)
                    visited.add((nx, ny))
                    hunt.append((nx, ny))
    final_shapes.append(p)

total_cost = 0
for f in final_shapes:
    cost = int(round(f.geometry.area, 0)) * int(round(f.geometry.length, 0))
    print(f"{f.name}: {cost}")
    total_cost += cost

print(f"Total cost: {total_cost}")
