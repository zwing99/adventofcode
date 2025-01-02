#!/usr/bin/env python

from hmac import new
from itertools import combinations, permutations, product
from math import dist
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

scanners = []
scan = []
while lines:
    line = lines.pop(0)
    if not line:
        scanners.append(scan[:])
        scan = []
        continue
    if line.count("scanner"):
        continue
    scan.append(tuple(map(int, line.split(","))))

# add the last scan
if scan:
    scanners.append(scan)


rotations_3x3 = [
    [
        [1, 0, 0],  # Rotate 90° counterclockwise around Z-axis
        [0, 1, 0],
        [0, 0, 1],
    ],
    [
        [0, 0, 1],  # Rotate 90° counterclockwise around Z-axis
        [0, 1, 0],
        [-1, 0, 0],
    ],
    [
        [0, 0, -1],  # Rotate 90° clockwise around Z-axis
        [0, 1, 0],
        [1, 0, 0],
    ],
    [
        [0, -1, 0],  # Rotate 90° counterclockwise around Y-axis
        [1, 0, 0],
        [0, 0, 1],
    ],
    [
        [0, 1, 0],  # Rotate 90° clockwise around Y-axis
        [-1, 0, 0],
        [0, 0, 1],
    ],
    [
        [-1, 0, 0],  # Rotate 180° around Y-axis
        [0, -1, 0],
        [0, 0, 1],
    ],
]


def multiply_matrix_vector(matrix, vector):
    # Ensure the dimensions are compatible
    result = [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]
    return tuple(result)


distances = []

for scan in scanners:
    d_scan = []
    for a, b in permutations(scan, 2):
        # calculated squared distance between two points
        d = sum((a[i] - b[i]) ** 2 for i in range(3))
        d_scan.append(d)
    set_d_scan = set(d_scan)
    distances.append(set_d_scan)

print(distances[0] & distances[1])
