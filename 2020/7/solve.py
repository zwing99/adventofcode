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
        lookup[b].append(bag)


def count(n):
    if n in lookup:
        s = set()
        s.add(n)
        for v in lookup[n]:
            a = count(v)
            #print(a)
            if isinstance(a, str):
                s.add(a)
            else:
                s = s.union(a)
        print((n, s))
        return s
    else:
        print((n, n))
        return n

s = count("shiny gold")
print(s)
print(len(s)-1)
# You guessed 83.