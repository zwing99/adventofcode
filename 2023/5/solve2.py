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
    section.sort(key=lambda x: x[1])
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

ranges = [[]]
for i in range(len(start_seeds)//2):
    p = tuple(start_seeds[i*2:i*2+2])
    ranges[0].append((p[0], p[0] + p[1]))

ranges[0].sort(key=lambda x: x[0])

print(ranges)

for i, section in enumerate(mappings):
    print(80*"-")
    print(i)
    print(80*"-")
    next_ranges = []
    for s, e in ranges[i]:
        to_remove = []
        for ds, ss, se, _ in section:
            inter = max(s, ss), min(e, se)
            offset = -ss + ds
            print(s, e, "|", ss, se, "|", inter)
            if inter[0] <= inter[1]:
                to_remove.append(inter)
                next_ranges.append((inter[0] + offset, inter[1] + offset))
        to_remove.sort(key=lambda x: x[0])
        print("to_remove", to_remove)
        while len(to_remove) > 0:
            rs, re = to_remove.pop(0)
            if s != rs:
                next_ranges.append((s, rs))
            s = re
        if s != e:
            next_ranges.append((s, e))

    next_ranges.sort(key=lambda x: x[0])
    print("next_ranges", next_ranges)
    ranges.append(next_ranges)

print(min([x[0] for x in ranges[-1]]))