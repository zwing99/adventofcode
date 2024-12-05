#!/usr/bin/env python

import sys
import itertools
import re
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

dots = re.compile(r"\.+")


total = 0
for z,line in enumerate(lines):
    stuff, numbers = line.split(" ")
    numbers = [int(n) for n in numbers.split(",")]
    qs = stuff.count("?")
    replacement_pattern = list(itertools.product(*([(".","#")] * qs)))
    count = 0
    # print("======================================================")
    # print("======================================================")
    # print(z+1)
    # print(numbers)
    # print("======================================================")
    for rn in replacement_pattern:
        part = stuff
        for i in rn:
            part = part.replace("?", i, 1)
        part = part.strip('.')
        lens = [len(i) for i in dots.split(part)]
        # print(f"{part}\t-> {lens}")
        #if len(lens) == len(numbers):
        #    print(lens, numbers)
        if lens == numbers:
            #print("found")
            count += 1
    total += count
    break
print(total)

#for i in range(7733408):
#    if i % 1000 == 0:
#        print(i)
