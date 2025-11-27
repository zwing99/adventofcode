#!/usr/bin/env python

from collections import Counter, defaultdict
from itertools import chain
import sys
from tabnanny import check

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

letters = "abcdefghijklmnopqrstuvwxyz"


def shift_it(l, amount):
    ix = letters.index(l)
    ix = (ix + amount) % len(letters)
    return letters[ix]


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
        new_parts = []
        for p in parts:
            n = ""
            for l in p:
                n += shift_it(l, sector_id)
            new_parts.append(n)
        dec = " ".join(new_parts)
        if dec.count("north"):
            print(dec, sector_id)
