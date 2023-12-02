#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

games = {}
for line in lines:
    game, results = line.split(":")
    game_num = int(game.split(" ")[1])
    results = [x.strip() for x in results.split(";")]
    y = []
    for r in results:
        z = {}
        parts = [x.strip() for x in r.split(",")]
        for p in parts:
            num, color = p.split(" ")
            num = int(num)
            z[color] = num
        y.append(z)
    games[game_num] = y

total = 0
for game_num, g in games.items():
    #print(game_num, g)
    good = True
    round_maxes = {}
    for r in g:
        for color, num in r.items():
            if color not in round_maxes:
                round_maxes[color] = num
            elif num > round_maxes[color]:
                round_maxes[color] = num
    pwr = 1
    for v in round_maxes.values():
        pwr *= v
    #print (game_num, pwr)
    total += pwr
            
print(total)
        


        