#!/usr/bin/env python

import dataclasses
import sys
import pulp
import numpy as np

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
    # return tuple([int(x.split("=")[1]) for x in c])
    return tuple([int(x.split("=")[1]) + 10000000000000 for x in c])


total_cost = 0
while True:
    a = lines.pop(0)
    b = lines.pop(0)
    p = lines.pop(0)
    m = Machine(parse_button(a), parse_button(b), parse_prize(p))
    print(m)
    # c = 3* a + b
    # p1 = a1 * a + b1 * b
    # p2 = a2 * a + b2 * b
    A = [
        [m.button_a[0], m.button_b[0], 0],
        [m.button_a[1], m.button_b[1], 0],
        [3, 1, -1],
    ]
    B = [m.prize[0], m.prize[1], 0]
    x = np.linalg.solve(A, B)
    print(x)
    a = int(round(x[0], 0))
    b = int(round(x[1], 0))
    if (
        a * m.button_a[0] + b * m.button_b[0] == m.prize[0]
        and a * m.button_a[1] + b * m.button_b[1] == m.prize[1]
    ):
        total_cost += 3 * a + b

    # problem = pulp.LpProblem("str(m)", pulp.LpMinimize)
    # a = pulp.LpVariable("a", lowBound=0, cat="Integer")
    # b = pulp.LpVariable("b", lowBound=0, cat="Integer")
    # problem += 3 * a + b
    # problem += m.button_a[0] * a + m.button_b[0] * b == m.prize[0]
    # problem += m.button_a[1] * a + m.button_b[1] * b == m.prize[1]
    # status = problem.solve()
    # print(
    #     "*********************************************************************************"
    # )
    # print(status)
    # print(a.value(), b.value())
    # if status == 1:
    #     total_cost += 3 * int(a.value()) + int(b.value())

    if len(lines) <= 1:
        break
    lines.pop(0)

print(total_cost)

# 1762329637000 That's not the right answer; your answer is too low.
# 59262024772463 That's not the right answer; your answer is too low
# 875318608908
