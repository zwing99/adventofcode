#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

stones = [int(i) for i in lines[0].split()]

sum = 0
for st in stones:
    stones_li = [st]
    for i in range(25):
        new_stones = []
        for stone in stones_li:
            print(stones_li)
            new_stones = []
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                ls = int(s[len(s) // 2 :])
                rs = int(s[: len(s) // 2])
                new_stones.extend([ls, rs])
            else:
                new_stones.append(stone * 2024)
        stones_li = new_stones[:]
        print(i, stones_li)
    sum += len(stones_li)

print(sum)
