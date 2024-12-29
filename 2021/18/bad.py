#!/usr/bin/env python

from hmac import new
from math import exp
import sys
from typing import Union

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


def find_depth(li):
    if type(li) == int:
        return 0
    else:
        max_depth = 0
        for i in li:
            max_depth = max(max_depth, find_depth(i))
        return max_depth + 1


def red(item):
    print(item)


for line in lines:
    li = eval(line)
    red(line)
