#!/usr/bin/env python
import sys

import shapely

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [[int(i) for i in line.strip().split(",")] for line in fh.readlines()]


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


shp = shapely.geometry.polygon.Polygon(lines)

max_area = 0
for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        box = shapely.geometry.box(lines[i][0], lines[i][1], lines[j][0], lines[j][1])
        if shp.contains(box):
            if (a := area(lines[i], lines[j])) > max_area:
                max_area = a

print(max_area)
