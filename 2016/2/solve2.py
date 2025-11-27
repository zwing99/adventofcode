#!/usr/bin/env python
import sys
import functools

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def clamp(n, min_val, max_val):
    if n < min_val:
        return min_val
    elif n > max_val:
        return max_val
    else:
        return n


keypad_clamp = functools.partial(clamp, min_val=0, max_val=4)
dirs = {
    "U": [0, -1],
    "R": [1, 0],
    "D": [0, 1],
    "L": [-1, 0],
}


keypad = """
* * 1 * *
* 2 3 4 *
5 6 7 8 9
* A B C *
* * D * *
"""
keys = [a.split() for a in keypad.strip().split("\n")]
# print(keys)
pos = [0, 2]
new_pos = pos[:]

pressed = ""
for line in lines:
    for d in line:
        m = dirs[d]
        new_pos[0] = keypad_clamp(pos[0] + m[0])
        new_pos[1] = keypad_clamp(pos[1] + m[1])
        if keys[new_pos[1]][new_pos[0]] != "*":
            pos = new_pos[:]

        # print(d, pos)
    # print(pos)
    pressed += keys[pos[1]][pos[0]]
    # print(pressed)

print(pressed)
