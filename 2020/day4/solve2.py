#!/usr/bin/env python

import sys
import re
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

expected = {
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",# "cid",
}

pps = []
p = {}
for line in lines:
    if line == '':
        pps.append(p)
        p = {}
    else:
        p.update(dict([[x.strip() for x in z.split(':')] for z in line.split(' ')]))
pps.append(p)



def valid_props(d:dict):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    byr = re.search(r'^(\d{4})$', d['byr'])
    if not byr: return False
    byr = int(byr.group(1))
    if byr < 1920 or byr > 2002: return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = re.match(r'^(\d{4})$', d['iyr'])
    if not iyr: return False
    iyr = int(iyr.group(1))
    if iyr < 2010 or iyr > 2020: return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = re.match(r'^(\d{4})$', d['eyr'])
    if not eyr: return False
    eyr = int(eyr.group(1))
    if eyr < 2020 or eyr > 2030: return False

    # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
    hgt = re.match(r'^(((\d{3})cm)|((\d{2})in))$', d['hgt'])
    if not hgt: return False
    if hgt.group(1).count('in') > 0 and int(hgt.group(5)) < 59 and int(hgt.group(5)) > 76: return False
    if hgt.group(1).count('cm') > 0 and int(hgt.group(3)) < 150 and int(hgt.group(3)) > 193: return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if d['ecl'] not in ('amb','blu','brn','gry','grn','hzl','oth'):
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = re.match(r'^(#[\da-f]{6})$', d['hcl'])
    if not hcl: return False


    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = re.match(r'^(\d{9})$', d['pid'])
    if not pid: return False

    # cid (Country ID) - ignored, missing or not.

    return True



valid = 0
for p in pps:
    if set(p.keys()).issuperset(expected):
        if valid_props(p):
            valid += 1
        else:
            ...
            # print(p)

print(valid)


# 227 -  That's not the right answer; your answer is too high
# 200 - That's not the right answer; your answer is too low