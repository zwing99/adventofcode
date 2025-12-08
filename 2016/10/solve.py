#!/usr/bin/env python
import re
from collections import defaultdict
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
target = (2, 5) if filename != "input.txt" else (17, 61)

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

bots = defaultdict(list)
output = defaultdict(list)
rules = {}


def send_to(dest, number, value):
    if dest == "bot":
        bots[number].append(value)
        bots[number].sort()
    elif dest == "output":
        output[number].append(value)
        output[number].sort()


giver = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
)
gotor = re.compile(r"value (\d+) goes to bot (\d+)")

for line in lines:
    if m := gotor.match(line):
        v, b = m.groups()
        v = int(v)
        send_to("bot", b, v)
    elif m := giver.match(line):
        g, s1, p1, s2, p2 = m.groups()
        rules[g] = g, s1, p1, s2, p2


def run_rule(b):
    g, s1, p1, s2, p2 = rules[b]
    low = bots[g].pop(0)
    send_to(s1, p1, low)
    high = bots[g].pop(-1)
    send_to(s2, p2, high)
    if (low, high) == target:
        print(b)


while True:
    didSomething = False
    keys = list(bots.keys())
    for b in keys:
        nums = bots[b]
        if len(nums) == 2:
            run_rule(b)
            didSomething = True
    if not didSomething:
        break


# print(bots)
# print(output)
