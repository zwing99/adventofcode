#!/usr/bin/env python

from hashlib import md5
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

start = lines[0].strip()

codes = {}
i = 0
while len(codes) < 8:
    i += 1
    # print(i)
    md = md5((start + str(i)).encode("ascii"))
    dig = str(md.hexdigest())
    if "00000" == dig[:5]:
        pos = dig[5]
        if pos in "01234567" and pos not in codes:
            print()
            codes[pos] = dig[6]

code = "".join(codes[str(i)] for i in range(8))
print(code)
