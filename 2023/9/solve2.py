#!/usr/bin/env python

import sys
from pprint import pprint
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

total = 0
for line in lines:
    z = []
    v = [int(x) for x in line.split()]
    #print(v)
    z.append(v)
    n = []
    while True:
        for i in range (len(v)-1):
            n.append(v[i+1]-v[i])
        v = n[:]
        z.append(v)
        #print(n)
        if all([x == 0 for x in n]):
            break
        n = []
    #pprint(z)
    #print()

    z[-1].insert(0, 0)
    for i in range(len(z) - 2, -1, -1):
        last_row_first = z[i+1][0]
        current_row_first = z[i][0]
        #print(current_row_last, last_row_last)
        next_val = current_row_first - last_row_first
        #print(next_val)
        z[i].insert(0, next_val)
    
    print(z[0][0])
    total += z[0][0]

    #print()

    #for row in z:
    #    print(row)

    #print()
    #print('----')
    #print()

print(total)

