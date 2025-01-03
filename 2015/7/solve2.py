#!/usr/bin/env python

from operator import lshift, rshift
import sys
import re

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
target = "h"
if filename == "input.txt":
    target = "a"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

assignre = re.compile(r"(\d+) -> (\w+)")
assignre2 = re.compile(r"(\w+) -> (\w+)")
andre = re.compile(r"(\w+) AND (\w+) -> (\w+)")
orre = re.compile(r"(\w+) OR (\w+) -> (\w+)")
lshiftre = re.compile(r"(\w+) LSHIFT (\d+) -> (\w+)")
rshiftre = re.compile(r"(\w+) RSHIFT (\d+) -> (\w+)")
notre = re.compile(r"NOT (\w+) -> (\w+)")
all_res = [assignre, andre, orre, lshiftre, rshiftre, notre]

values = {}
while lines:
    line = lines.pop(0)
    if x := assignre.match(line):
        if x.group(2) == "b":
            values[x.group(2)] = 46065
            continue
        values[x.group(2)] = int(x.group(1))
        continue
    elif x := assignre2.match(line):
        if x.group(1) in values:
            values[x.group(2)] = values[x.group(1)]
            continue
        elif x.group(1).isdigit():
            values[x.group(2)] = int(x.group(1))
            continue
    elif x := andre.match(line):
        if x.group(1) in values and x.group(2) in values:
            values[x.group(3)] = values[x.group(1)] & values[x.group(2)]
            continue
        elif x.group(1).isdigit() and x.group(2) in values:
            values[x.group(3)] = int(x.group(1)) & values[x.group(2)]
            continue
        elif x.group(2).isdigit() and x.group(1) in values:
            values[x.group(3)] = values[x.group(1)] & int(x.group(2))
            continue
    elif x := orre.match(line):
        if x.group(1) in values and x.group(2) in values:
            values[x.group(3)] = values[x.group(1)] | values[x.group(2)]
            continue
        elif x.group(1).isdigit() and x.group(2) in values:
            values[x.group(3)] = int(x.group(1)) | values[x.group(2)]
            continue
        elif x.group(2).isdigit() and x.group(1) in values:
            values[x.group(3)] = values[x.group(1)] | int(x.group(2))
            continue
    elif x := lshiftre.match(line):
        if x.group(1) in values:
            values[x.group(3)] = lshift(values[x.group(1)], int(x.group(2)))
            continue
        elif x.group(1).isdigit():
            values[x.group(3)] = lshift(int(x.group(1)), int(x.group(2)))
            continue
    elif x := rshiftre.match(line):
        if x.group(1) in values:
            values[x.group(3)] = rshift(values[x.group(1)], int(x.group(2)))
            continue
        elif x.group(1).isdigit():
            values[x.group(3)] = rshift(int(x.group(1)), int(x.group(2)))
            continue
    elif x := notre.match(line):
        if x.group(1) in values:
            values[x.group(2)] = ~values[x.group(1)] & 0xFFFF
            continue
        elif x.group(1).isdigit():
            values[x.group(2)] = ~int(x.group(1)) & 0xFFFF
            continue
    else:
        print(f"Error: {line}")
    lines.append(line)


for k, v in values.items():
    print(f"{k}: {v}")
print(values[target])
