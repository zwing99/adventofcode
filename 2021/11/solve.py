#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [[int(x) for x in line.strip()] for line in fh.readlines()]

height = len(lines)
width = len(lines[0])
all_directs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def pop_it(x, y):
    pop_more = set()
    for m,n in all_directs:
        a = x + m
        b = y + n
        if 0 <= a and a < width and 0 <= b and b < height:
            lines[b][a] += 1
            if lines[b][a] >= 10:
                #print (a, b)
                pop_more.add((a,b))
    return pop_more


f = []
for _ in range(100):
    for j in range(height):
        for i in range(width):
            lines[j][i] += 1

    to_pop = set()
    for j in range(height):
        for i in range(width):
            if lines[j][i] >= 10:
                to_pop.add((i, j))

    popped = set()
    while len(to_pop) > 0:
        x, y = to_pop.pop()
        if (x, y) in popped:
            print('huh?')
            continue
        popped.add((x, y))
        moar = pop_it(x, y)
        to_pop.update(moar - popped)

    flashes = 0
    for j in range(height):
        for i in range(width):
            if lines[j][i] >= 10:
                lines[j][i] = 0
                flashes += 1
    f.append(flashes)
    #print (_ + 1, sum(f))
    #for line in lines:
    #    print(' '.join([str(x) for x in line]))
    #print("----------------------------")
    
    #if _ >= 2:
    #    break

print(sum(f))
    


