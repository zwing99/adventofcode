#!/usr/bin/env python

from calendar import c
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

orig_code = [int(x) for x in lines[0].split(",")]


def test(noun, verb):
    code = orig_code[:]
    code[1] = noun
    code[2] = verb
    i = 0
    while True:
        instruction = code[i]
        if instruction == 1:
            v = code[code[i + 1]] + code[code[i + 2]]
            # print(v)
            code[code[i + 3]] = v
        elif instruction == 2:
            v = code[code[i + 1]] * code[code[i + 2]]
            # print(v)
            code[code[i + 3]] = v
        elif instruction == 99:
            break
        i += 4

    return code[0]


for noun in range(100):
    for verb in range(100):
        if test(noun, verb) == 19690720:
            print(100 * noun + verb)


# 406198 That's not the right answer; your answer is too low.
