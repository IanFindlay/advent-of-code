#!/usr/bin/env python3

"""Advent of Code 2021 Day 15 - Chiton"""


with open('inputs/day_15.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

map_dict = {}
for y, row in enumerate(lines):
    for x, risk_level in enumerate(row):
        map_dict[(x, y)] = int(risk_level)

end_coords = (len(lines) - 1, len(lines[0]) - 1)

unvisited = set(map_dict.keys())
node_dict = {}
for coords in unvisited:
    node_dict[coords] = None
node_dict[(0, 0)] = 0

lowest_risk = None
current_node = (0, 0)
while True:

    x, y = current_node
    adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for next_to in adjacent:
        if next_to not in unvisited:
            continue

        risk = node_dict[(x, y)] + map_dict[next_to]
        if not node_dict[next_to] or risk < node_dict[next_to]:
            node_dict[next_to] = risk

    unvisited.remove((x, y))

    next_node = None
    for coords, risk in node_dict.items():
        if not risk or coords not in unvisited:
            continue

        if not next_node or risk < node_dict[next_node]:
            next_node = coords

    if next_node == end_coords or not next_node:
        break

    current_node = next_node

# Answer One
print("Lowest total risk of any path:", node_dict[end_coords])
