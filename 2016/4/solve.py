#!/usr/bin/env python

from collections import Counter, defaultdict
from itertools import chain
import sys
from tabnanny import check

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    a, b = line.split("[")
    checksum = b.strip("]")
    parts = a.split("-")
    sector_id = int(parts.pop(-1))

    counter = Counter(chain.from_iterable(parts))
    flip = defaultdict(lambda: "")
    for ch, cnt in counter.most_common():
        flip[cnt] += ch
        flip[cnt] = "".join(sorted(flip[cnt]))
    o = "".join(flip.values())
    if checksum == o[: len(checksum)]:
        total += sector_id

print(total)
