#!/usr/bin/env python

import sys, re
from typing import ChainMap
import itertools

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def has_abba(st):
    for i in range(0, len(st) - 3):
        if st[i] == st[i + 3] and st[i + 1] == st[i + 2] and st[i] != st[i + 1]:
            # print(st[i : i + 4])
            return True
    return False


def find_abas(st):
    for i in range(0, len(st) - 2):
        if st[i] == st[i + 2] and st[i] != st[i + 1]:
            yield st[i : i + 3]


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
    abas = list(
        itertools.chain.from_iterable(
            itertools.starmap(find_abas, [(b,) for b in bracket_parts])
        )
    )
    if abas:
        found = False
        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            found = any([nb.count(bab) for nb in non_bracket_parts])
            if found:
                break
        if found:
            count += 1


print(count)

# 119 That's not the right answer; your answer is too high
