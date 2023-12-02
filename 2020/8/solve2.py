#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip().split() for line in fh.readlines()]
    lines = [(inst, int(v)) for inst, v in lines]

#print(lines)


def find_it():
    for j in range(len(lines)):
        if lines[j][0] in ('jmp','nop'):
            new_lines = lines[:j]
            #print(new_lines)
            if lines[j][0] == 'jmp':
                new_lines.append(('nop',lines[j][1]))
            elif lines[j][0] == 'nop':
                new_lines.append(('jmp',lines[j][1]))
            #print(new_lines)
            new_lines.extend(lines[j+1:])
            #print(new_lines)
        
            #print(len(new_lines), len(lines))
            assert len(new_lines) == len(lines)
            accum = 0
            i = 0
            visited = set()
            while True:
                if i in visited:
                    break
                if i >= len(new_lines):
                    return accum
                visited.add(i)
                inst, v = new_lines[i]
                #print(inst, v, visited)
                if inst == 'nop':
                    i += 1
                elif inst == 'acc':
                    i += 1
                    accum += v
                elif inst == 'jmp':
                    i += v

print(find_it())
