#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip().split(":")[1].strip().split() for line in fh.readlines()]

total_time = int("".join(lines[0]))
distance_min = int("".join(lines[1]))
print(total_time, distance_min)

def calc_distance(total_time: int, charge_time: int):
    rest_time = total_time - charge_time
    speed = charge_time
    return speed * rest_time

ways = 0
for charge_time in range(1, total_time):
    if calc_distance(total_time, charge_time) > distance_min:
        ways += 1
print(ways)
