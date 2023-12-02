#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

expected = {
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",# "cid",
}

pps = []
p = {}
for line in lines:
    if line == '':
        pps.append(p)
        p = {}
    else:
        p.update(dict([z.split(':') for z in line.split(' ')]))

pps.append(p)


valid = 0
for p in pps:
    #print(set(p.keys())&expected)
    #print(expected)
    if set(p.keys()).issuperset(expected):
        #print('true')
        valid += 1

print(valid)
