#!/usr/bin/env python

from hashlib import md5
import sys
from webbrowser import get

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

line = lines[0]


def get_hash(value):
    hash = md5((line + str(value)).encode())
    return hash.hexdigest()


# print(get_hash(6742839))
# exit()

for i in range(10000000):
    h = get_hash(i)
    if h.startswith("000000") and h[6] != "0":
        print(i)
        break

# 6742839 That's not the right answer; your answer is too low.
