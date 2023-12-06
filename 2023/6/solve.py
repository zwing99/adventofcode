#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [[int(x) for x in line.strip().split(":")[1].strip().split()] for line in fh.readlines()]
    pairs = list(zip(*lines))

def calc_distance(total_time: int, charge_time: int):
    rest_time = total_time - charge_time
    speed = charge_time
    return speed * rest_time

final = 1
for total_time, distance_min in pairs:
    ways = 0
    for charge_time in range(1, total_time):
        if calc_distance(total_time, charge_time) > distance_min:
            ways += 1
    final *= ways
print(final)
