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
        processed.append((number_of_blocks, v))
    else:  # is empty
        processed.append((number_of_blocks, "."))

print(processed)
processed_str = ""
for i in range(len(processed)):
    processed_str += processed[i][0] * processed[i][1]
print(processed_str)

back_index = len(processed) - 1
while back_index >= 0:
    if processed[back_index][1] == ".":
        back_index -= 1
        continue
    front_index = 0
    found_spot = False
    while front_index < back_index:
        if (
            processed[front_index][1] == "."
            and processed[front_index][0] >= processed[back_index][0]
        ):
            found_spot = True
            break
        front_index += 1
    if found_spot:
        new_back = (processed[back_index][0], ".")
        new_front_1 = processed[back_index]
        new_front_2 = (processed[front_index][0] - processed[back_index][0], ".")
        processed[back_index] = new_back
        processed[front_index] = new_front_1
        processed.insert(front_index + 1, new_front_2)
    back_index -= 1

processed_str = ""
for i in range(len(processed)):
    processed_str += processed[i][0] * processed[i][1]
print(processed_str)

processed_li = []
for i in range(len(processed)):
    for j in range(processed[i][0]):
        processed_li.append(processed[i][1])
print(processed_li)
print("".join(processed_li))

check_sum = 0
for i in range(len(processed_li)):
    if processed_li[i] == ".":
        continue
    check_sum += int(processed_li[i]) * i

print(check_sum)

# 91235952521 That's not the right answer; your answer is too low.
# 91235952521
# 91235952521
# 6415184586041
