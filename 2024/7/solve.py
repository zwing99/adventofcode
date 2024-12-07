#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


total = 0
for line in lines:
    target_str, nums_str = line.split(":")
    target = int(target_str)
    nums = list(map(int, nums_str.split()))
    visited = []
    queue = []
    node_index = 0
    start = nums[node_index]
    queue.append((start, node_index))
    visited.append((start, node_index))
    found = False
    print("target:", target)
    while queue:
        v, i = queue.pop(0)
        next_i = i + 1
        # print(next_i)
        n = nums[next_i]
        for op in (mul, add):
            next_v = op(v, n)
            if next_i + 1 == len(nums) and next_v == target:
                print((next_v, next_i))
                found = True
                break
            if (
                ((next_v, next_i) not in visited)
                and (next_i + 1 < len(nums))
                and (next_v <= target)
            ):
                print((next_v, next_i))
                visited.append((next_v, next_i))
                queue.append((next_v, next_i))

    if found:
        total += target
        print("found")

    print("-----")
    # break

print(total)

# 932137733500 That's not the right answer; your answer is too high.
# 932137732557 <-- winner
# 929059481129 That's not the right answer; your answer is too low.
# 929059480186 That's not the right answer; your answer is too low.
