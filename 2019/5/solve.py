#!/usr/bin/env python

from enum import IntEnum
from dataclasses import dataclass
import functools
import sys
import typing as typ

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

orig_code = [int(x) for x in lines[0].split(",")]


class PositionMode(IntEnum):
    position = 0
    immediate = 1


def get_vals(arr: list[int], i: int, p1: PositionMode, p2: PositionMode):
    # print(p1, p2)
    if p1 == PositionMode.position:
        a = arr[arr[i + 1]]
    else:
        a = arr[i + 1]
    if p2 == PositionMode.position:
        b = arr[arr[i + 2]]
    else:
        b = arr[i + 2]
    return a, b


def resolve(arr: list[int], i: int, v: int, p3: PositionMode):
    assert p3 == PositionMode.position
    arr[arr[i + 3]] = v


def mul(arr: list[int], i: int, p1: PositionMode, p2: PositionMode, p3: PositionMode):
    a, b = get_vals(arr, i, p1, p2)
    v = a * b
    print("mul", arr[i : i + 4], p1, p2, p3, v)
    resolve(arr, i, v, p3)


def add(arr: list[int], i: int, p1: PositionMode, p2: PositionMode, p3: PositionMode):
    a, b = get_vals(arr, i, p1, p2)
    v = a + b
    print("add", arr[i : i + 4], p1, p2, p3, v)
    resolve(arr, i, v, p3)


def inputf(arr: list[int], i: int, inp: int, p1: PositionMode):
    print("input", arr[i : i + 2], i, p1, inp)
    assert p1 == PositionMode.position
    arr[arr[i + 1]] = inp


def outputf(arr: list[int], i: int, p1: PositionMode):
    a = arr[arr[i + 1]] if p1 == PositionMode.position else arr[i + 1]
    print("print:", a)


@dataclass
class Operation:
    func: typ.Callable
    skips: int
    end: bool = False


def opcode_parse(x: int, inp: int):
    """
    ABCDE
     1002

    DE - two-digit opcode,      02 == opcode 2
    C - mode of 1st parameter,  0 == position mode
    B - mode of 2nd parameter,  1 == immediate mode
    A - mode of 3rd parameter,  0 == position mode,
                                     omitted due to being a leading zero
    """
    v = str(x)
    v = (5 - len(v)) * "0" + v
    print(v)
    p3 = PositionMode(int(v[0]))
    p2 = PositionMode(int(v[1]))
    p1 = PositionMode(int(v[2]))
    # print(p1, p2, p3)
    skips: int
    f: typ.Callable
    end = False
    inst_i = int(v[3:])
    if inst_i == 1:
        f = functools.partial(add, p1=p1, p2=p2, p3=p3)
        skips = 4
    elif inst_i == 2:
        f = functools.partial(mul, p1=p1, p2=p2, p3=p3)
        skips = 4
    elif inst_i == 3:
        f = functools.partial(inputf, p1=p1, inp=inp)
        skips = 2
    elif inst_i == 4:
        f = functools.partial(outputf, p1=p1)
        skips = 2
    elif inst_i == 99:
        f = print
        skips = 0
        end = True
    return Operation(f, skips, end)


def run(code: list[int], inp: int):
    i = 0
    while True:
        op: Operation = opcode_parse(code[i], inp)
        if op.end:
            print("end")
            break
        v = op.func(code, i)
        if v:
            return v
        i += op.skips


code = orig_code[:]
if filename == "test.txt":
    code[1] = 12
    code[2] = 2

run(code, 1)
print(code[0])
