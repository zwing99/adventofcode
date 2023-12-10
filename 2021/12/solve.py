#!/usr/bin/env python

import sys, re
from collections import defaultdict
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

UPPERS = re.compile('[A-Z]+')
LOWERS = re.compile('[a-z]+')

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

starts = []
mappings = defaultdict(list)
for line in lines:
    a, b = line.split('-')
    is_lower_b = LOWERS.search(b) is not None
    is_lower_a = LOWERS.search(a) is not None
    if a == 'start':
        starts.append((b, is_lower_b))
    else:
        mappings[a].append((b, is_lower_b))
        mappings[b].append((a, is_lower_a))

print(starts, mappings)

def goto_nexts(current, visited_minis, paths):
    nexts = mappings[current[0]]
    print(f"current: {current}, nexts: {nexts}")
    for n in nexts:
        #print (n)
        if n[0] == 'end':
            return 1
        if n[1]:
            if n[0] in visited_minis:
                continue
            visited_minis.add(n[0])
        paths += goto_nexts(n[0], visited_minis, paths)
    return paths
    
        

for start in starts:
    current = start
    p = goto_nexts(current, set(), 0)
    print(p)
    

