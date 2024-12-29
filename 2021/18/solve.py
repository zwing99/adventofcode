#!/usr/bin/env python

from dataclasses import dataclass
from hmac import new
from math import exp
from operator import add
import sys
from typing import Union

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def full_parse(item: str):
    arr = []
    while item:
        if item[0] == "[":
            item = item[1:]
            arr += ["["]
        elif item[0] == "]":
            item = item[1:]
            arr += ["]"]
        elif item[0] == ",":
            item = item[1:]
            arr += [","]
        else:
            v = ""
            while item[0].isdigit():
                v += item[0]
                item = item[1:]
            v = int(v)
            arr += [v]
    return arr


def test_arr(arr):
    v = "".join([str(x) for x in arr])
    print(v)
    li = eval(v)
    return li


def explode(arr):
    depth = 0
    for i in range(len(arr)):
        if arr[i] == "[":
            depth += 1
        elif arr[i] == "]":
            depth += -1
        if depth >= 5:
            vl = arr[i + 1]
            vr = arr[i + 3]
            if not isinstance(vl, int) or not isinstance(vr, int):
                continue
            print("exploding")
            print(arr)
            print(vl, vr)
            assert isinstance(vl, int)
            assert isinstance(vr, int)
            lhs = arr[:i]
            rhs = arr[i + 5 :]
            # print(lhs)
            # print(rhs)
            # print(vl, vr)
            for j in range(len(lhs) - 1, -1, -1):
                if isinstance(lhs[j], int):
                    # print("added left")
                    lhs[j] += vl
                    break
            for j in range(len(rhs)):
                if isinstance(rhs[j], int):
                    # print("added right")
                    rhs[j] += vr
                    break
            arr = lhs + [0] + rhs
            test_arr(arr)
            return arr, True

    return arr, False


def split(arr):
    for i in range(len(arr)):
        if isinstance(arr[i], int):
            if arr[i] >= 10:
                print("splitting")
                vl = arr[i] // 2
                vr = arr[i] // 2
                if arr[i] % 2 == 1:
                    vr += 1
                arr = arr[:i] + ["[", vl, ",", vr, "]"] + arr[i + 1 :]
                # print(arr)
                test_arr(arr)
                return arr, True
    return arr, False


def red(arr):
    while True:
        arr, did_explode = explode(arr)
        if did_explode:
            continue
        arr, did_split = split(arr)
        if did_split:
            continue
        break
    return arr


def magnitude(arr):
    l, r = arr
    if isinstance(l, list):
        l = magnitude(l)
    if isinstance(r, list):
        r = magnitude(r)
    return 3 * l + 2 * r


arr = full_parse(lines.pop(0))
for line in lines:
    print(arr, line)
    arr = ["["] + arr + [","] + full_parse(line) + ["]"]
    arr = red(arr)
    test_arr(arr)

li = test_arr(arr)
v = magnitude(li)
print(v)
