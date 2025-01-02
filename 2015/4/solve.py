#!/usr/bin/env python

from hashlib import md5
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

line = lines[0]


def get_hash(value):
    hash = md5((line + str(value)).encode())
    return hash.hexdigest()


for i in range(1000000):
    if get_hash(i).startswith("00000"):
        print(i)
        break
