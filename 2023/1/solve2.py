#!/usr/bin/env python

import sys
import re
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

num_map = {
    "1": 1,
    "one": 1,
    "2": 2,
    "two": 2,
    "3": 3,
    "three": 3,
    "4": 4,
    "four": 4,
    "5": 5,
    "five": 5,
    "6": 6,
    "six": 6,
    "7": 7,
    "seven": 7,
    "8": 8,
    "eight": 8,
    "9": 9,
    "nine": 9,
    "0": 0,
    "zero": 0,
}


MATCH_NUMBER = r"(\d|one|two|three|four|five|six|seven|eight|nine|zero)"
re_1 = r"^\D*?" + MATCH_NUMBER
re_2 = r".*" + MATCH_NUMBER + r"\D*?$"


total = 0
for line in lines:
    m1 = num_map[re.match(re_1, line).group(1)]
    m2 = num_map[re.match(re_2, line).group(1)]
    v = m1 * 10 + m2
    total += v

print(total)