#!/usr/bin/env python3

"""Advent of Code 2021 Day 12 - Passage Pathing"""


with open('inputs/day_12.txt', 'r') as aoc_input:
    lines = [line.strip().split('-') for line in aoc_input.readlines()]

connections = {}
for line in lines:
    from_cave, to_cave = line
    if from_cave not in connections.keys():
        connections[from_cave] = set()
    if to_cave not in connections.keys():
        connections[to_cave] = set()

    connections[from_cave].add(to_cave)
    connections[to_cave].add(from_cave)

paths = set()
current_paths = []
for to_cave in connections['start']:
    current_paths.append(('start', to_cave))

while current_paths:
    path = current_paths.pop()
    current_cave = path[-1]
    for connected_cave in connections[current_cave]:

        # Can't revisit small caves
        if connected_cave in path and connected_cave.lower() == connected_cave:
            continue

        new_path = path + (connected_cave,)

        # Check if at end and unique path
        if connected_cave == 'end' and new_path not in paths:
            paths.add(new_path)
            continue

        current_paths.append(new_path)

# Answer One
print("Number of paths through cave system visiting small caves only once:",
        len(paths))
