#!/usr/bin/env python

from collections import defaultdict, deque
import enum
from itertools import chain, combinations, permutations, product
from re import M
import sys

import test

sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

vals: dict[str, int] = {}
while True:
    line = lines.pop(0)
    if line == "":
        break
    key, val = line.split(":")
    vals[key.strip()] = int(val)


def andfun(a: int, b: int) -> int:
    return 1 if a and b else 0


def orfun(a: int, b: int) -> int:
    return 1 if a or b else 0


def xorfun(a: int, b: int) -> int:
    return 1 if a ^ b else 0


# print(xorfun(1, 1))
# print(xorfun(1, 0))
# print(xorfun(0, 1))
# print(xorfun(0, 0))
# exit()

swaps0 = {
    "wss": "z18",
    "z18": "wss",
    "bmn": "z23",
    "z23": "bmn",
    "rds": "jss",
    "jss": "rds",
    "mvb": "z08",
    "z08": "mvb",
    # "nhn": "pvc",
    # "pvc": "nhn",
    # "z14": "z15",
    # "z15": "z14",
    # "dcv": "tsg",
    # "tsg": "dcv",
    # "rds": "jss",
    # "tsg": "dcv",
    # "rbp": "bdd",
    # "bdd": "rbp",
    # "pdq": "nfq",
    # "nfq": "pdq",
}
# swaps0 = {}
graph = defaultdict(list)
equations = deque()
for line in lines:
    v1, o, v2, _, out = line.split(" ")
    if out in swaps0:
        out = swaps0[out]
    if o == "AND":
        op = andfun
    elif o == "OR":
        op = orfun
    elif o == "XOR":
        op = xorfun
    else:
        print("Unknown operator", o)
        exit()
    equations.append((op, v1, v2, out))
    graph[v1].append((out, o))
    graph[v2].append((out, o))


def run(equations, x, y, swaps):
    vals = {}
    x = str(bin(x)[2:])
    y = str(bin(y)[2:])
    for i in range(45):
        # print(i)
        vals[f"x{i:02}"] = int(x[-i - 1]) if i < len(x) else 0
        vals[f"y{i:02}"] = int(y[-i - 1]) if i < len(y) else 0
    cnt = 0
    while equations:
        cnt += 1
        eq = equations.popleft()
        op, v1, v2, out = eq
        if v1 in vals and v2 in vals:
            if out in swaps:
                vals[swaps[out]] = op(vals[v1], vals[v2])
            else:
                vals[out] = op(vals[v1], vals[v2])
        else:
            equations.append(eq)
        if cnt > 4000:
            print("too many")
            return "0"
    # print(f"cnt: {cnt}")

    keys = sorted([x for x in vals.keys() if x.startswith("z")], reverse=True)
    num = "".join([str(vals[key]) for key in keys])
    return num


def find_ends(node, graph, depth, max_depth) -> set:
    if node not in graph:
        return {node}
    if depth == max_depth:
        return set()
    ends = set()
    for n, op in graph[node]:
        ends |= find_ends(n, graph, depth + 1, max_depth)
    return set(sorted(ends))


def find_all(node, path, graph, depth, max_depth) -> set:
    if node not in graph:
        return [path]
    if depth == max_depth:
        return [path]
    all_paths = []
    for n, op in graph[node]:
        all_paths.extend(find_all(n, path + [(op, n)], graph, depth + 1, max_depth))
    return all_paths


starts = sorted([x for x in graph.keys() if x.startswith("x") or x.startswith("y")])

bad_options = set()
for s in starts:
    ends = find_ends(s, graph, 0, 3)
    stuff = find_all(s, [s], graph, 0, 5)
    if len(ends) < 2 or [e for e in ends if e[0] != "z"]:
        # bad_options |= stuff
        print("mark")
    print(s)
    # print(ends)
    for path in sorted(stuff, key=lambda x: len(x)):
        # pass
        if len(path) > 2:
            if len(path) == 4:
                if path[1][0] != "AND" or path[2][0] != "OR" != path[3][0] == "XOR":
                    print("foo")
            print(path)

bad_options = set(
    [x for x in bad_options if not x.startswith("y") and not x.startswith("x")]
)

print(bad_options)
print(len(bad_options))

x_keys = sorted([x for x in vals.keys() if x.startswith("x")], reverse=True)
x_num = "".join([str(vals[key]) for key in x_keys])
x_num = int(x_num, 2)

y_keys = sorted([x for x in vals.keys() if x.startswith("y")], reverse=True)
y_num = "".join([str(vals[key]) for key in y_keys])
y_num = int(y_num, 2)


def test_swaps(x, y, swaps):
    z_num = run(equations.copy(), x, y, swaps)
    print(len(z_num.lstrip("0")) - 1)
    print(z_num)
    z_num = eval(f"0b{z_num}")
    print(f"{x} + {y} = {z_num}")
    return x + y == z_num


print(test_swaps(x_num, y_num, {}))
v = 0
for i in range(44):
    v += 2**i
print(test_swaps(v, 1, {}))
print(test_swaps(11111, 11111, {}))
print(",".join(sorted(swaps0.keys())))


# tested = set()
# c = list(combinations(bad_options, 8))
# for i, s in enumerate(c):
#     # i want all sets of 4 pairs of the 8 numbers in s
#     pairs = [sorted(x) for x in list(combinations(s, 2))]
#     for pair_set in combinations(pairs, 4):
#         ordered = tuple(chain(*sorted(pair_set, key=lambda x: x[0])))
#         if ordered in tested:
#             continue
#         tested.add(ordered)
#         swaps = {}
#         swaps[ordered[0]] = ordered[1]
#         swaps[ordered[1]] = ordered[0]
#         swaps[ordered[2]] = ordered[3]
#         swaps[ordered[3]] = ordered[2]
#         swaps[ordered[4]] = ordered[5]
#         swaps[ordered[5]] = ordered[4]
#         swaps[ordered[6]] = ordered[7]
#         swaps[ordered[7]] = ordered[6]
#         if test_swaps(x_num, y_num, swaps):
#             print(swaps)
#             print(ordered)
#             print("found")
#             exit()
#
#     print(f"{len(tested)} {i}/{len(c)}")
