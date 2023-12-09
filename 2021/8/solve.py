#! /usr/bin/env python
import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

parts = []
for line in lines:
    i, o = line.split('|')
    parts.append((i.strip().split(),o.strip().split()))

known = { 2:1, 4:4, 3:7, 7:8 }

# part 1
count = 0
for i, o in parts:
    for p in o:
        if len(p) in known:
            count += 1

print(count)

# part 2

def string_sort(s):
    return ''.join(sorted(s))


nums = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
nums_map = {
    string_sort(n): i
    for i, n in enumerate(nums)
}
lens_map = {
    len(n): string_sort(n)
    for n in nums
}
del lens_map[5]
print()
print(f"lens_map: {lens_map}")
print("-----")

total = 0
for i, o in parts:
    remaining = set(i)
    i_lens_map = {
        len(n): n
        for n in i
    }
    mappings = {}
    rev_map = {}
    d_1_7_4 = set()
    d_1_7 = set()
    for l, n in known.items():
        mappings[i_lens_map[l]] = n
        rev_map[n] = i_lens_map[l]
        remaining.remove(i_lens_map[l])
        if n in (1,7,4):
            d_1_7_4 |= set([x for x in i_lens_map[l]])
        if n in (1,7):
            d_1_7 |= set([x for x in i_lens_map[l]])
    magic = set([_ for _ in rev_map[7]]) - set([_ for _ in rev_map[1]])
    d_4_sub_1 = set([_ for _ in rev_map[4]]) - set([_ for _ in rev_map[1]])

    
    
    # find 9
    for a in filter(lambda x: len(x) == 6, remaining):
        inter = set([_ for _ in a]) - d_1_7_4
        if len(inter) == 1:
            mappings[a] = 9
            rev_map[9] = a
            break
    d_9 = set([_ for _ in a])

    # find 6
    d_1_7_4_9 = set() | set(rev_map[9])
    found = False
    for a in filter(lambda x: len(x) == 6, remaining):
        if a in mappings:
            continue
        inter = set([_ for _ in a]) - d_4_sub_1
        if len(inter) == 4:
            mappings[a] = 6
            rev_map[6] = a
        elif len(inter) == 5:
            mappings[a] = 0
            rev_map[0] = a

    d_6 = set([_ for _ in a])
    
    # find 0:
    a = set(list(filter(lambda x: len(x) == 6, remaining))) - set([rev_map[6], rev_map[9]])
    a = a.pop()
    mappings[a] = 0
    rev_map[0] = a
    d_0 = set([_ for _ in a])

    # find 2:
    for a in filter(lambda x: len(x) == 5, remaining):
        inter = set([_ for _ in a]) - d_9
        if len(inter) == 1:
            mappings[a] = 2
            rev_map[2] = a

    d_1_7_4_2 = set([_ for _ in a]) | d_1_7_4_9

    d_4 = set([_ for _ in rev_map[4]])
    for a in filter(lambda x: len(x) == 5, remaining):
        if a in mappings:
            continue
        inter = set([_ for _ in a]) - d_1_7
        if len(inter) == 3:
            mappings[a] = 5
            rev_map[5] = a
        if len(inter) == 2:
            mappings[a] = 3
            rev_map[3] = a
    
    #print(f"mappings: {mappings}")
        
    set_mappping = {}
    for k, v in mappings.items():
        set_mappping[tuple(sorted([_ for _ in k]))] = v

    #print(f"set_mappping: {set_mappping}")
    
    num = ''
    for v in o:
        v_ = tuple(sorted([_ for _ in v]))
        #print(v_)
        num += str(set_mappping[v_])
        #print(num)
    print(f"num: {num}")
    total += int(num)

print(total)





# ab: 1
# 
# dab: 7
# .
# eafb: 4
# . .
# 
# acedgfb: 8
# 
# gcdfa: 2

# cdfbe: 5
# fbcad: 3

# cfe: 5
# fc: 3
# 
# cefabd: 9   (1)
# X.....
# cdfgeb: 6   (2)
# ...X..
# cagedb: 0   (3)
