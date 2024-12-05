#!/usr/bin/env python

import sys
import itertools
import re
import math
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

dots = re.compile(r"\.+")


def d_print (*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

solved = 0

def DFS(stuff, goal_numbers, v):
    s = stuff[:]
    if v:
        s = s.replace("?", v, 1)
        s = s.strip('.')
    #global solved
    if s.count("?") == 0:
        # d_print("\nchecking s=", s)
        lens = [len(i) for i in s.split(".") if i]
        #solved += 1
        #if solved > 100 == 0:
        #    exit()
        if lens == goal_numbers:
            # d_print(f"#1 good {v}: {lens} == {goal_numbers}")
            return 1
        # d_print(f"#1 bad {v}: {lens} != {goal_numbers}")
        return 0
    else:
        # d_print("\neliminating s=", s)
        # d_print("------------------")
        # d_print("#3\n------------------")
        if s.count("?") + s.count("#") < sum(goal_numbers):
            # d_print(f"#6.1 {s.count('?')} + {s.count('.')} < {sum(goal_numbers)}")
            return 0
        elif s.count("#") > sum(goal_numbers):
            # d_print(f"#6.3 {s.count('#')} > {sum(goal_numbers)}")
            return 0
        # d_print(s)
        parts = [i for i in s.split(".") if i]
        lens = [len(i) for i in parts]
        # d_print(parts)
        # d_print(lens)
        # d_print(goal_numbers)
        in_the_qs = False
        for i in range(min(len(lens), len(goal_numbers))):
            in_the_qs |= parts[i].count("?") > 0
            # d_print(f"i={i}, in_the_qs={in_the_qs}")
            if in_the_qs:
                break
            else:
                if lens[i] != goal_numbers[i]:
                    # d_print(f"#5 [{i}] {lens[i]} != {goal_numbers[i]}")
                    return 0
        if not in_the_qs:
            # d_print('easy find')
            return 1

        if len(goal_numbers) == 1 and lens[0] > goal_numbers[0]:
            # d_print('easy find2')
            total = 0
            for i in range(len(lens)):
                if lens[i] > goal_numbers[0]:
                    total += lens[i] - goal_numbers[0]
            return total
        
        if len(lens) == len(goal_numbers) and "".join(parts).count("#") == 0:
            total = 0
            for i in range(len(lens)):
                if lens[i] < goal_numbers[i]:
                    # d_print('bad fact')
                    return 0
                total += math.factorial(lens[i])//(math.factorial(lens[i]-goal_numbers[i])*math.factorial(goal_numbers[i]))
            # d_print("Factorial:", total)
            return total

        if i > 0:
            p1 = lens[:i]
            p1_sum = sum(p1) + len(p1)
            gn = goal_numbers[len(p1):]
            s1 = s[p1_sum:]
            # d_print(f"i={i}, p1={p1}, p1_sum={p1_sum}, gn={gn}, s1={s1}")
            # d_print(s, goal_numbers)
        else:
            s1 = s
            gn = goal_numbers
        # d_print("#7")
        return DFS(s1, gn, "#") + DFS(s1, gn, ".")
        

DEBUG = True
DEBUG = False
total = 0
for z,line in enumerate(lines):
    #print(z+1)
    if DEBUG and z+1 not in [8]:
        continue
    stuff, numbers = line.split(" ")
    stuff = "?".join([stuff]*5)
    numbers = numbers + "," + numbers + "," + numbers + "," + numbers + "," + numbers
    numbers = [int(n) for n in numbers.split(",")]
    #qs = stuff.count("?")
    qs = stuff.count("?")
    # d_print(stuff, numbers)
    stuff = stuff.strip(".")
    stuff = dots.sub(".", stuff)
    print(stuff.strip("."))
    print(numbers)
    count = DFS(stuff.strip("."), numbers, "")
    print(z+1, count)
    total += count
print(total)

#for i in range(7733408):
#    if i % 1000 == 0:
#        print(i)


        

    

    