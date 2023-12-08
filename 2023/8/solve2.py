#!/usr/bin/env python

import sys
import math
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

rules = lines.pop(0)
lines.pop(0)

guide = {}
for line in lines:
    key, z = line.split(" = ") 
    a, b = [x.strip("()") for x in z.split(", ")]
    guide[key] = (a, b)

#print (rules)
#print(guide)

z = {'L': 0, 'R': 1}
current = [x for x in guide.keys() if x[2] == 'A']
print(current)
v = []
for c in current:
    i = 0
    while True:
        lr = z[rules[i%len(rules)]]
        #print(lr, guide[current], rules[i%len(rules)])
        #current = [guide[c][lr] for c in current]
        c = guide[c][lr]
        i += 1
        #print(current)
        if c[2] == 'Z':
            break

    print(i)
    v.append(i)

asdf = math.lcm(*v)
print(asdf)