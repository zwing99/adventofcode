#!/usr/bin/env python

from encodings.punycode import T
import sys
import re

sys.setrecursionlimit(100_000)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

floors = []


for line in lines[:-1]:
    print(line)
    a, b = line.split("contains")
    items = [i.strip().lstrip("a").strip() for i in re.split(r"and|,|and,", b)]
    floors.append(items)


def is_safe(floor):
    gens = set()
    chips = set()
    for item in floor:
        if "generator" in item:
            gens.add(item.split()[0])
        elif "microchip" in item:
            chips.add(item.split("-")[0])
    if not gens:
        return True
    for chip in chips:
        if chip not in gens:
            return False
    return True


def process(floors, elevator, steps, visited):
    state = (elevator, tuple(tuple(sorted(floor)) for floor in floors))
    if state in visited:
        if visited[state] <= steps:
            return float("inf")
    visited[state] = steps

    if all(len(floor) == 0 for floor in floors[:-1]):
        print("All items on top floor in", steps, "steps")
        return steps

    min_steps = float("inf")
    for item in floors[elevator]:
        for direction in [-1, 1]:
            new_elevator = elevator + direction
            if 0 <= new_elevator < len(floors):
                new_floors = [list(floor) for floor in floors]
                new_floors[elevator].remove(item)
                new_floors[new_elevator].append(item)

                if is_safe(new_floors[elevator]) and is_safe(new_floors[new_elevator]):
                    result = process(new_floors, new_elevator, steps + 1, visited)
                    min_steps = min(min_steps, result)
    if len(floors[elevator]) >= 2:
        for i in range(len(floors[elevator])):
            for j in range(i + 1, len(floors[elevator])):
                item1 = floors[elevator][i]
                item2 = floors[elevator][j]
                for direction in [-1, 1]:
                    new_elevator = elevator + direction
                    if 0 <= new_elevator < len(floors):
                        new_floors = [list(floor) for floor in floors]
                        new_floors[elevator].remove(item1)
                        new_floors[elevator].remove(item2)
                        new_floors[new_elevator].append(item1)
                        new_floors[new_elevator].append(item2)

                        if is_safe(new_floors[elevator]) and is_safe(
                            new_floors[new_elevator]
                        ):
                            result = process(
                                new_floors, new_elevator, steps + 1, visited
                            )
                            min_steps = min(min_steps, result)

    return min_steps


result = process(floors, 0, 0, {})
print("Minimum steps required:", result)
