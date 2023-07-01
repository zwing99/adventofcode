#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [[x.strip() for x in line.strip().split(':')] for line in fh.readlines()]

good_count = 0
for rule, password in lines:
    rng, char = rule.split(' ')
    mn, mx = [int(x) for x in rng.split("-")]
    if (password[mn-1] == char) ^ (password[mx-1] == char):
        good_count+=1

print(good_count)

