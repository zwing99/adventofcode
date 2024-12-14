#!/usr/bin/env python

import sys
import dataclasses
from typing import final

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
if filename == "test.txt":
    x_range, y_range = 11, 7
else:
    x_range, y_range = 101, 103


with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


@dataclasses.dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]


robots: list[Robot] = []
for line in lines:
    p, v = line.split(" ")
    x, y = [int(x) for x in p.split("=")[1].split(",")]
    vx, vy = [int(x) for x in v.split("=")[1].split(",")]
    robots.append(Robot((x, y), (vx, vy)))


TIME_STEPS = 100
for robot in robots:
    final_pos = [
        robot.position[0] + TIME_STEPS * robot.velocity[0],
        robot.position[1] + TIME_STEPS * robot.velocity[1],
    ]
    if final_pos[0] < 0:
        final_pos[0] = final_pos[0] % x_range
    if final_pos[1] < 0:
        final_pos[1] = final_pos[1] % y_range
    if final_pos[0] > x_range:
        final_pos[0] = final_pos[0] % x_range
    if final_pos[1] > y_range:
        final_pos[1] = final_pos[1] % y_range
    robot.position = tuple(final_pos)

quadrants = {1: 0, 2: 0, 3: 0, 4: 0}
middle_x = (x_range - 1) // 2
middle_y = (y_range - 1) // 2
for robot in robots:
    # print(robot.position)
    if robot.position[0] < middle_x:
        if robot.position[1] < middle_y:
            quadrants[1] += 1
        elif robot.position[1] > middle_y:
            quadrants[3] += 1
    elif robot.position[0] > middle_x:
        if robot.position[1] < middle_y:
            quadrants[2] += 1
        elif robot.position[1] > middle_y:
            quadrants[4] += 1

total = 1
for q in quadrants.values():
    total *= q

print(total)
