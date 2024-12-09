#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

input = lines[0]
processed = ""
for i in range(len(input)):
    number_of_blocks = int(input[i])
    if i % 2 == 0:  # is file
        v = str(i // 2)
        processed += v * number_of_blocks
    else:  # is empty
        processed += "." * number_of_blocks

print(processed)

processed_li = list(processed)

front_index = 0
back_index = len(processed_li) - 1
while front_index < back_index:
    while processed_li[front_index] != "." and front_index < back_index:
        front_index += 1
    while processed_li[back_index] == "." and front_index < back_index:
        back_index -= 1
    print(front_index, back_index)
    if front_index >= back_index:
        break
    #
    a = processed_li[front_index]
    b = processed_li[back_index]
    processed_li[front_index] = b
    processed_li[back_index] = a

print("".join(processed_li))

check_sum = 0
for i in range(len(processed_li)):
    if processed_li[i] == ".":
        break
    check_sum += int(processed_li[i]) * i

print(check_sum)

# 91235952521 That's not the right answer; your answer is too low.
# 91235952521
