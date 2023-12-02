#!/usr/bin/env python

import sys
import re
from collections import defaultdict
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip().rstrip('.').split(' contain ') for line in fh.readlines()]

lookup = defaultdict(list)
for bag, con in lines:
    bag = bag.split(' bag')[0]
    if con == "no other bags":
        continue
    contains = con.split(", ")
    for c in contains:
        r = re.search(r"(\d+)\s+(.+)", c)
        num = int(r.group(1))
        b = r.group(2)
        b = b.split(' bag')[0]
        lookup[bag].append((num, b))


def count(n):
    if n in lookup:
        t = 1
        for c, b in lookup[n]:
            t += c*count(b)
        return t
    else:
        return 1

#print(dict(lookup))
print(count("shiny gold") - 1)