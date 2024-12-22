#!/usr/bin/env python

from hmac import new
import sys
import itertools

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


keypad_starts_ends_map = {}
for s, e in keypad_start_ends:
    s_node = starts_keypad[s]
    e_node = starts_keypad[e]
    paths = {}
    visited = {}
    dfs(keypad.split("\n"), s_node, 0, [], paths, visited, e_node)
    keypad_starts_ends_map[(s, e)] = ["".join(x) for x in paths[e_node]]

print(keypad_starts_ends_map)

dpad_starts_ends_map = dict()
dpad_start_ends = itertools.permutations("^v<>A", 2)
for s, e in dpad_start_ends:
    s_node = starts_dpad[s]
    e_node = starts_dpad[e]
    paths = {}
    visited = {}
    dfs(dpad.split("\n"), s_node, 0, [], paths, visited, e_node)
    dpad_starts_ends_map[(s, e)] = ["".join(x) for x in paths[e_node]]

print(dpad_starts_ends_map)

# print(keypad_starts_ends_map)


def score_path(path):
    s = 0
    for i in range(len(path) - 1):
        if path[i] == path[i + 1]:
            s += 1
        else:
            s += len(dpad_starts_ends_map[(path[i], path[i + 1])][0])

    return s


def all_full_path_options(full_path_options):
    all_full_path_next_options = []
    for full_path_r1 in full_path_options:
        full_path_next_options = ["A"]
        for i in range(len(full_path_r1) - 1):
            new_full_path_next_options = []
            for full_path_next in full_path_next_options:
                if full_path_r1[i] == full_path_r1[i + 1]:
                    new_full_path_next_options.append(full_path_next + "A")
                else:
                    for option in dpad_starts_ends_map[
                        (full_path_r1[i], full_path_r1[i + 1])
                    ]:
                        new_full_path_next_options.append(full_path_next + option + "A")
            full_path_next_options = new_full_path_next_options
        all_full_path_next_options.extend(new_full_path_next_options)

    scores_next = {
        full_path_next: score_path(full_path_next)
        for full_path_next in all_full_path_next_options
    }
    best_score_next = min(scores_next.values())
    all_full_path_next_options = [
        x for x in all_full_path_next_options if scores_next[x] == best_score_next
    ]

    return all_full_path_next_options


total = 0
for line in lines:
    full_line = "A" + line
    full_path_r1_options = ["A"]
    for i in range(len(full_line) - 1):
        new_full_path_r1_options = []
        for full_path_r1 in full_path_r1_options:
            if full_line[i] == full_line[i + 1]:
                new_full_path_r1_options.append(full_path_r1 + "A")
            else:
                for option in keypad_starts_ends_map[(full_line[i], full_line[i + 1])]:
                    new_full_path_r1_options.append(full_path_r1 + option + "A")
        full_path_r1_options = new_full_path_r1_options
    # print()
    # print(full_path_r1_options)
    # print()

    steps = full_path_r1_options[:]
    for i in range(2):
        steps = all_full_path_options(steps)

    min_len = min([len(x) for x in steps]) - 1

    print(min_len, int(full_line.strip("A")))
    total += min_len * int(full_line.strip("A"))

print(total)
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
