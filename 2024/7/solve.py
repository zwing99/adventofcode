#!/usr/bin/env python

import sys
from aoc2024_7 import bfs_rust, Part


filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


total = 0
for i, line in enumerate(lines):
    target_str, nums_str = line.split(":")
    target = int(target_str)
    nums = list(map(int, nums_str.split()))
    total = bfs_rust(total, target, nums, Part.Part1)

    print(i)

print(total)

# 932137733500 That's not the right answer; your answer is too high.
# 932137732557 <-- winner
# 929059481129 That's not the right answer; your answer is too low.
# 929059480186 That's not the right answer; your answer is too low.
