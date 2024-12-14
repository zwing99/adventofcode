#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

code = [int(x) for x in lines[0].split(",")]
code[1] = 12
code[2] = 2
print(code)

i = 0
while True:
    instruction = code[i]
    if instruction == 1:
        v = code[code[i + 1]] + code[code[i + 2]]
        print(v)
        code[code[i + 3]] = v
    elif instruction == 2:
        v = code[code[i + 1]] * code[code[i + 2]]
        print(v)
        code[code[i + 3]] = v
    elif instruction == 99:
        break
    i += 4

print(",".join([str(x) for x in code]))

# 406198 That's not the right answer; your answer is too low.
