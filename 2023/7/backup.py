#!/usr/bin/env python

import sys
import re
from itertools import product
from pprint import pprint
from dataclasses import dataclass

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

card_rank = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
card_rank_back = {v: k for k, v in card_rank.items()}
cards = "AKQJT98765432"
pairs = list(product(cards, cards))


@dataclass
class Hand:
    cards: str
    rank: list[int]
    bet: int
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.rank < other.rank
        if self.rank[0] == other.rank[0]:
            for i in range(1, len(self.rank)):
                if self.rank[i] != other.rank[i]:
                    return self.rank[i] < other.rank[i]
        return self.rank[0] < other.rank[0]

@dataclass
class CardCntPair:
    card: int
    cnt: int
    def __lt__(self, other):
        if self.cnt == other.cnt:
            return self.card < other.card
        return self.cnt < other.cnt 


hands = []
for line in lines:
    hand, bet = line.split()
    r = []
    for c in cards:
        cnt = hand.count(c)
        if cnt > 0:
            r.append(CardCntPair(card_rank[c], cnt))
    r.sort(reverse=True)
    #print(hand, r)
    h = {x.card: x.cnt for x in r}
    new_hand = ''
    for x in r:
        new_hand += card_rank_back[x.card] * x.cnt
    if len(h) == 1:
        rank = 7 # must be 5 of kind
    elif len(h) == 2:
        if 4 in h.values():
            rank = 6 # must be 4 of kind
        else:
            rank = 5 # must be full house
    elif len(h) == 3:
        if 3 in h.values():
            rank = 4 # must be 3 of kind
        else:
            rank = 3 # must be 2 pairs
    elif len(h) == 4:
        rank = 2 # must be 1 pair
    else:
        rank = 1 # must be high card
    hand_rank = [rank] + [x.card for x in r]
    #print("Hand: {}, Bet: {}, Rank: {}".format(hand, bet, hand_rank))
    hands.append(Hand(new_hand, hand_rank, int(bet)))

#print()
#pprint(hands)
#print()
hands.sort()
# pprint(hands)

total = 0
for i, h in enumerate(hands):
    total += (i + 1) * h.bet
    print(i+1, h)

print(len(hands))
print(total)
    
    
# 247614666 That's not the right answer; your answer is too high
# 246602932 That's not the right answer; your answer is too high.