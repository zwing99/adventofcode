#!/usr/bin/env python

from collections import defaultdict
import sys

sys.setrecursionlimit(10000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [[x for x in line.strip()] for line in fh.readlines()]

x_range = len(lines[0])
y_range = len(lines)

for y in range(y_range):
    for x in range(x_range):
        if lines[y][x] == "E":
            E = (x, y)
        elif lines[y][x] == "S":
            S = (x, y)

dir = (1, 0)


def turn_cw(dir):
    return (dir[1], -dir[0])


def turn_ccw(dir):
    return (-dir[1], dir[0])


def dfs(
    node: tuple[tuple[int, int], tuple[int, int]],
    current_route: list,
    steps,
    visited: dict,
    route_to: dict,
    can_turn=True,
):
    if node in visited:
        if steps >= visited[node]:
            if steps == visited[node]:
                route_to[node].append(current_route)
            return
    route_to[node] = [current_route]
    visited[node] = steps
    # forward step
    straight_route = current_route.copy()
    straight_route.append(node)
    x, y = node[0]
    dx, dy = node[1]
    if lines[y + dy][x + dx] in [".", "E", "S"]:
        dfs(((x + dx, y + dy), (dx, dy)), straight_route, steps + 1, visited, route_to)
    # turn cw
    if not can_turn:
        return
    cw_route = current_route.copy()
    cw_route.append(node)
    dfs(((x, y), turn_cw((dx, dy))), cw_route, steps + 1000, visited, route_to, False)
    # turn ccw
    ccw_route = current_route.copy()
    ccw_route.append(node)
    dfs(((x, y), turn_ccw((dx, dy))), ccw_route, steps + 1000, visited, route_to, False)


visited = {}
route_to = {}

dfs((S, dir), [], 0, visited, route_to)

dir = (1, 0)
smallest = 9e99
for i in range(4):
    dir = turn_cw(dir)
    if (E, dir) in visited:
        if visited[(E, dir)] < smallest:
            smallest = visited[(E, dir)]
            best_end = (E, dir)
print(smallest)
# print(best_routes)


def check(node, touched, checked):
    checked.add(node)
    best_routes = route_to[node]
    for route in best_routes:
        for n in route:
            x, y = n[0]
            touched.add((x, y))
            if n not in checked:
                check(n, touched, checked)


touched = set()
checked = set()
check(best_end, touched, checked)


# print("\n".join(["".join(x) for x in lines]))
# print()
#
# for x, y in touched:
#     lines[y][x] = "O"
#
# print("\n".join(["".join(x) for x in lines]))

print(len(touched) + 1)
print(best_end)

# for r, routes in route_to.items():
#     print(r)
#     print(routes)
# print(len(route_to))
# print(cnt)

# #################
# #...#...#...#..O#
# #.#.#.#.#.#.#.#O#
# #.#.#.#...#...#O#
# #.#.#.#.###.#.#O#
# #OOO#.#.#.....#O#
# #O#O#.#.#.#####O#
# #O#O..#.#.#OOOOO#
# #O#O#####.#O###O#
# #O#O#..OOOOO#OOO#
# #O#O###O#####O###
# #O#O#OOO#..OOO#.#
# #O#O#O#####O###.#
# #O#O#OOOOOOO..#.#
# #O#O#O#########.#
# #O#OOO..........#
# #################
