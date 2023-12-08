#!/usr/bin/env python

import sys
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

i = 0
z = {'L': 0, 'R': 1}
current = 'AAA'
while True:
    lr = z[rules[i%len(rules)]]
    #print(lr, guide[current], rules[i%len(rules)])
    current = guide[current][lr]
    i += 1
    #print(current)
    if current == 'ZZZ':
        break

print(i)

