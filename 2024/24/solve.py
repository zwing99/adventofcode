#!/usr/bin/env python

from collections import deque
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

vals: dict[str, int] = {}
while True:
    line = lines.pop(0)
    if line == "":
        break
    key, val = line.split(":")
    vals[key.strip()] = int(val)


def andfun(a: int, b: int) -> int:
    return 1 if a and b else 0


def orfun(a: int, b: int) -> int:
    return 1 if a or b else 0


def xorfun(a: int, b: int) -> int:
    return 1 if a ^ b else 0


# print(xorfun(1, 1))
# print(xorfun(1, 0))
# print(xorfun(0, 1))
# print(xorfun(0, 0))
# exit()

equations = deque()
for line in lines:
    v1, o, v2, _, out = line.split(" ")
    if o == "AND":
        op = andfun
    elif o == "OR":
        op = orfun
    elif o == "XOR":
        op = xorfun
    else:
        print("Unknown operator", o)
        exit()
    equations.append((op, v1, v2, out))

# print(equations)
# exit()

while equations:
    eq = equations.popleft()
    op, v1, v2, out = eq
    if v1 in vals and v2 in vals:
        vals[out] = op(vals[v1], vals[v2])
    else:
        equations.append(eq)

# keys = sorted(
#     [x for x in vals.keys() if not x.startswith("x") and not x.startswith("y")]
# )
# for key in keys:
#     print(f"{key}: {vals[key]}")
#

keys = sorted([x for x in vals.keys() if x.startswith("z")], reverse=True)

num = "".join([str(vals[key]) for key in keys])
print(num)
print(eval(f"0b{num}"))
