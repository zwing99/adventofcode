#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

input = lines[0]
processed = []
for i in range(len(input)):
    number_of_blocks = int(input[i])
    if i % 2 == 0:  # is file
        v = str(i // 2)
        for j in range(number_of_blocks):
            processed.append(v)
    else:  # is empty
        for j in range(number_of_blocks):
            processed.append(".")

print(processed)
print("".join(processed))

front_index = 0
back_index = len(processed) - 1
while front_index < back_index:
    while processed[front_index] != "." and front_index < back_index:
        front_index += 1
    while processed[back_index] == "." and front_index < back_index:
        back_index -= 1
    print(front_index, back_index)
    if front_index >= back_index:
        break
    #
    a = processed[front_index]
    b = processed[back_index]
    processed[front_index] = b
    processed[back_index] = a

print("".join(processed))

check_sum = 0
for i in range(len(processed)):
    if processed[i] == ".":
        break
    check_sum += int(processed[i]) * i

print(check_sum)

# 91235952521 That's not the right answer; your answer is too low.
# 91235952521
# 91235952521
# 6415184586041
