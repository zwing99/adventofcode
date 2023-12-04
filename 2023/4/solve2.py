#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

card_counts = {k: 1 for k in range(1, len(lines) + 1)}

for line in lines:
    a, b = line.split(":")
    n = int(a.split()[1])
    winners, numbers = b.split("|")
    winners = set([int(i) for i in winners.strip().split()])
    numbers = set([int(i) for i in numbers.strip().split()])
    matching = len(winners & numbers)
    num_cards = card_counts[n]
    for i in range(n+1, n+matching+1):
        card_counts[i] += num_cards


print(sum(card_counts.values()))