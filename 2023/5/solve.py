#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

start_seeds = [int(x) for x in lines.pop(0).split(":")[1].strip().split(" ")]
lines.pop(0)

mappings = []

def process_grouping(grouping):
    section = []
    for line in grouping[1:]:
        ds, ss, l = [int(x) for x in line.split()]
        section.append([ds, ss, ss + l, l])
    mappings.append(section)


grouping = []
for line in lines:
    if line != "":
        grouping.append(line)
    else:
        process_grouping(grouping)
        grouping = []

if len(grouping) > 0:
    process_grouping(grouping)

final = []
for seed in start_seeds:
    path = []
    current = seed
    path.append((0, current))
    for i, section in enumerate(mappings):
        found = False
        for ds, ss, se, _ in section:
            if current >= ss and current <= se:
                current = current - ss + ds
                path.append((i+1, current))
                found = True
                break
        if not found:
            path.append((i+1, current))
    #print(path)
    final.append(current)

print(min(final))

