#!/usr/bin/env python

import dataclasses
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


@dataclasses.dataclass
class Machine:
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_button(s: str) -> tuple[int, int]:
    c = [a.strip() for a in s.split(":")[1].strip().split(",")]
    return tuple([int(x.split("+")[1]) for x in c])


def parse_prize(s: str) -> tuple[int, int]:
    c = [a.strip() for a in s.split(":")[1].strip().split(",")]
    return tuple([int(x.split("=")[1]) for x in c])


total_cost = 0
while True:
    a = lines.pop(0)
    b = lines.pop(0)
    p = lines.pop(0)
    m = Machine(parse_button(a), parse_button(b), parse_prize(p))
    print(m)
    a_presses = [(m.button_a[0] * i, m.button_a[1] * i) for i in range(0, 101)]
    b_presses = [(m.button_b[0] * i, m.button_b[1] * i) for i in range(0, 101)]

    options = []
    for i, a_press in enumerate(a_presses):
        for j, b_press in enumerate(b_presses):
            if (
                a_press[0] + b_press[0] == m.prize[0]
                and a_press[1] + b_press[1] == m.prize[1]
            ):
                options.append((i, j))
    if options:
        costs = [a * 3 + b * 1 for a, b in options]
        # print(costs)
        best = sorted(costs)[0]
        # print(best)
        total_cost += best
    if len(lines) <= 1:
        break
    lines.pop(0)

print(total_cost)

# 36022 That's not the right answer; your answer is too low.
# 36718 That's not the right answer; your answer is too high.
