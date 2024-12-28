#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def parse_min_max(v):
    _, v = v.split("=")
    mn, mx = v.split("..")
    return int(mn), int(mx)


line = lines[0]
_, line = line.split(":")
xline, yline = line.split(",")

x_min, x_max = parse_min_max(xline)
y_min, y_max = parse_min_max(yline)
print(f"target bounds: x={x_min}..{x_max}, y={y_min}..{y_max}")


def simulate(vel: tuple[int, int]):
    pos = (0, 0)

    max_height = pos[1]
    while True:
        # print(f"Pos: {pos}, Vel: {vel}")
        x, y = pos
        vx, vy = vel
        x += vx
        y += vy
        pos = (x, y)
        if y > max_height:
            max_height = y
        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            # print(f"On target: {pos}")
            return True, max_height
        elif y < y_min or x > x_max:
            # print(f"Out of bounds: {pos}")
            return False, max_height
        if vx > 0:
            vx -= 1
        vy -= 1
        vel = (vx, vy)


max_height = 0
cnt = 0
for vx_start in range(1, 1000):
    for vy_start in range(-1000, 1000):
        worked, height = simulate((vx_start, vy_start))
        if worked:
            cnt += 1
            if height > max_height:
                max_height = height
print(max_height, cnt)
