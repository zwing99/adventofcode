#!/usr/bin/env python

import math
from statistics import variance
import sys
import dataclasses
from functools import partial

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
if filename == "test.txt":
    x_range, y_range = 11, 7
else:
    x_range, y_range = 101, 103


with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


robots: list[list[tuple[int, int], tuple[int, int]]] = list()
original_robots: set[tuple[tuple[int, int], tuple[int, int]]] = set()
for line in lines:
    p, v = line.split(" ")
    x, y = [int(x) for x in p.split("=")[1].split(",")]
    vx, vy = [int(x) for x in v.split("=")[1].split(",")]
    robots.append([(x, y), (vx, vy)])
    original_robots.add(((x, y), (vx, vy)))


def char_convert(x):
    if x > 0:
        return "#"
    if x < 0:
        return "*"
    return "."


def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    squared_deviations = [(x - mean) ** 2 for x in data]
    variance = sum(squared_deviations) / n
    return variance


v_x = []
v_y = []
vars = []

print(x_range, y_range)
all_grids = set()
for i in range(1, 100000):
    grid = [[0 for _x in range(x_range)] for _y in range(y_range)]
    now_robots = set()
    total_dis = 0
    for robot in robots:
        pos = robot[0]
        vel = robot[1]
        final_pos = [
            pos[0] + vel[0],
            pos[1] + vel[1],
        ]
        if final_pos[0] < 0:
            final_pos[0] = final_pos[0] % x_range
        if final_pos[1] < 0:
            final_pos[1] = final_pos[1] % y_range
        if final_pos[0] >= x_range:
            final_pos[0] = final_pos[0] % x_range
        if final_pos[1] >= y_range:
            final_pos[1] = final_pos[1] % y_range
        robot[0] = tuple(final_pos)
        grid[robot[0][1]][robot[0][0]] += 1
        now_robots.add(tuple(robot))

    if now_robots == original_robots:
        print("Found a loop")
        break
    # print([r[0][0] for r in robots])
    variance_x = calculate_variance([r[0][0] for r in robots])
    # print(variance_x)
    variance_y = calculate_variance([r[0][1] for r in robots])
    v_x.append(variance_x)
    v_y.append(variance_y)
    vars.append(variance_x + variance_y)
    if variance_x + variance_y < 1000:
        print(f"{i}" + "-" * x_range)
        print(variance_x)
        print()
        for row in grid:
            print("".join([char_convert(x) for x in row]))
    # input("")

print(sorted(v_x)[:50])
print(sorted(v_y)[:50])
print(sorted(vars)[:50])

# 5149 That's not the right answer; your answer is too low.
# 10402 That's not the right answer; your answer is too high.
