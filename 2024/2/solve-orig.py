#!/usr/bin/env python

from enum import Enum
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


class Direction(Enum):
    UP = 1
    DOWN = 2


safe_count = 0
for line in lines:
    li = [int(x) for x in line.split()]
    direction: Direction
    is_safe = True
    if 3 >= li[0] - li[1] > 0:
        direction = Direction.DOWN
        # print("down")
    elif -3 <= li[0] - li[1] < 0:
        direction = Direction.UP
        # print("up")
    else:
        is_safe = False
        print("same first 2")
    if is_safe:
        for i in range(1, len(li) - 1):
            if direction == Direction.DOWN:
                diff = li[i] - li[i + 1]
                if diff <= 0:  # going up
                    is_safe = False
                    break
                elif diff > 3:
                    is_safe = False
                    break
            elif direction == Direction.UP:
                diff = li[i] - li[i + 1]
                if diff >= 0:  # going down
                    is_safe = False
                    break
                elif diff < -3:
                    is_safe = False
                    break
    if is_safe:
        print(line)
        safe_count += 1
    else:
        print("not safe", line)

print(safe_count)

# 453
