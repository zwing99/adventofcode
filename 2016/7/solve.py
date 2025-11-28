#!/usr/bin/env python

import sys, re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def has_abba(st):
    for i in range(0, len(st) - 3):
        if st[i] == st[i + 3] and st[i + 1] == st[i + 2] and st[i] != st[i + 1]:
            # print(st[i : i + 4])
            return True
    return False


brackets = re.compile(r"\[|\]")

count = 0
for line in lines:
    parts = brackets.split(line)
    bracket_parts = []
    non_bracket_parts = []
    for i in range(len(parts)):
        if i % 2 == 0:
            non_bracket_parts.append(parts[i])
        else:
            bracket_parts.append(parts[i])
    if any([has_abba(p) for p in non_bracket_parts]) and all(
        [not has_abba(p) for p in bracket_parts]
    ):
        # print(non_bracket_parts, bracket_parts)
        count += 1

print(count)

# 119 That's not the right answer; your answer is too high
