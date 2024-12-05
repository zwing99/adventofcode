#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

rules = []
line = lines.pop(0)
while line != "":
    a, b = [int(i) for i in line.split("|")]
    rules.append((a, b))
    line = lines.pop(0)

total = 0


def is_good_check(numbers):
    is_good = True
    for a, b in rules:
        if a in numbers and b in numbers:
            if numbers.index(a) > numbers.index(b):
                is_good = False
                break
    return is_good


for line in lines:
    numbers = [int(i) for i in line.split(",")]
    is_good = is_good_check(numbers)
    if not is_good:
        print(numbers)
        while not is_good_check(numbers):
            for a, b in rules:
                if a in numbers and b in numbers:
                    a_idx = numbers.index(a)
                    b_idx = numbers.index(b)
                    if a_idx > b_idx:
                        b = numbers.pop(b_idx)
                        numbers.insert(a_idx, b)
                        print(numbers)
        if not is_good_check(numbers):
            print("Still not good")
            exit()
        total += numbers[len(numbers) // 2]
        print("---")

print(total)

# 4803 That's not the right answer; your answer is too low
