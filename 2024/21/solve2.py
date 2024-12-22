#!/usr/bin/env python

import sys
import itertools
import functools

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]


keypad = """
#####
#789#
#456#
#123#
##0A#
#####
""".strip()

starts_keypad = {}
for y, line in enumerate(keypad.split("\n")):
    for x, c in enumerate(line):
        if c != "#":
            starts_keypad[c] = (x, y)

dpad = """
#####
##^A# 
#<v># 
#####""".strip()

starts_dpad = {}
for y, line in enumerate(dpad.split("\n")):
    for x, c in enumerate(line):
        if c != "#":
            starts_dpad[c] = (x, y)

d_keys_to_dir = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
dir_to_d_keys = {v: k for k, v in d_keys_to_dir.items()}
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

keys = "123456789ABC"
dkeys = ">v<^"

keypad_start_ends = set()
for y, line in enumerate(lines):
    keypad_start_ends.add(("A", line[0]))
    for i in range(len(line) - 1):
        keypad_start_ends.add((line[i], line[i + 1]))


def dfs(
    grid: list[str],
    node: tuple[int, int],
    steps: int,
    path: list[tuple[int, int]],
    paths: dict,
    visited: dict[tuple[int, int], int],
    end: tuple[int, int],
):
    if steps > visited.get(node, float("inf")):
        return
    if steps < visited.get(node, float("inf")):
        paths[node] = []
    visited[node] = steps
    paths[node].append(path)
    if node == end:
        return
    for d in directions:
        new_node = (node[0] + d[0], node[1] + d[1])
        if grid[new_node[1]][new_node[0]] != "#":
            dfs(
                grid,
                new_node,
                steps + 1,
                path + [dir_to_d_keys[d]],
                paths,
                visited,
                end,
            )


starts_ends_map = dict()
dpad_start_ends = itertools.permutations("^v<>A", 2)
for s, e in dpad_start_ends:
    s_node = starts_dpad[s]
    e_node = starts_dpad[e]
    paths = {}
    visited = {}
    dfs(dpad.split("\n"), s_node, 0, [], paths, visited, e_node)
    starts_ends_map[(s, e)] = ["".join(x) + "A" for x in paths[e_node]]

for x in "v^<>A":
    starts_ends_map[(x, x)] = ["A"]


for s, e in keypad_start_ends:
    s_node = starts_keypad[s]
    e_node = starts_keypad[e]
    paths = {}
    visited = {}
    dfs(keypad.split("\n"), s_node, 0, [], paths, visited, e_node)
    starts_ends_map[(s, e)] = ["".join(x) + "A" for x in paths[e_node]]


print("----------------")
start_ends_lengths = {}
for k, v in starts_ends_map.items():
    print(k, starts_ends_map[k])
    start_ends_lengths[k] = len(v[0]) if v else 0
    print(start_ends_lengths[k])

print("----------------")


@functools.cache
def compute(seq, depth, max_depth):
    if depth >= max_depth - 1:
        s = sum(start_ends_lengths[(x, y)] for x, y in zip("A" + seq, seq))
        return s
    m = 0
    for x, y in zip("A" + seq, seq):
        options = starts_ends_map[(x, y)]
        # print(x, y, options)
        m += min([compute(o, depth + 1, max_depth) for o in options])
    return m


total = 0
for line in lines:
    asdf = [starts_ends_map[(x, y)] for x, y in zip("A" + line, line)]
    options = ["".join(x) for x in itertools.product(*asdf)]
    print(options)
    t = min([compute(o, 0, 25) for o in options])
    v = int(line.strip("A"))
    print(line, t, v)
    total += t * v
print(total)


# 154115708116294 That's not the right answer; your answer is too low.
# 383382168568300 That's not the right answer; your answer is too high.

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
