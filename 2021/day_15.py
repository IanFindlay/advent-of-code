#!/usr/bin/env python3

"""Advent of Code 2021 Day 15 - Chiton"""


def dijkstra(map_dict, end_coords):
    """."""
    unvisited = set(map_dict.keys())
    node_dict = {}
    node_dict[(0, 0)] = 0

    current_node = (0, 0)
    while True:
        x, y = current_node
        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for next_to in adjacent:
            if next_to not in unvisited:
                continue

            risk = node_dict[current_node] + map_dict[next_to]
            if not node_dict.get(next_to, None) or risk < node_dict[next_to]:
                node_dict[next_to] = risk

        unvisited.remove((x, y))
        del node_dict[(x, y)]

        next_node = None
        for coords, risk in node_dict.items():
            if not next_node or node_dict[next_node] > risk:
                next_node = coords

        if next_node == end_coords or not next_node:
            return node_dict[end_coords]

        current_node = next_node


with open('inputs/day_15.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

map_dict = {}
for y, row in enumerate(lines):
    for x, risk_level in enumerate(row):
        map_dict[(x, y)] = int(risk_level)

end_coords = (len(lines) - 1, len(lines[0]) - 1)

# Answer One
print("Lowest total risk of any path:", dijkstra(map_dict, end_coords))

# Build extended map
extended_map = map_dict.copy()
for coords, risk in map_dict.items():

    x, y = coords

    for i in range(1, 5):
        new_risk = (risk + i) % 9
        if new_risk == 0:
            new_risk = 9

        new_x = x + ((end_coords[0] + 1) * i)
        extended_map[(new_x, y)] = new_risk

map_dict = extended_map.copy()
for coords, risk in map_dict.items():

    x, y = coords

    for i in range(1, 5):
        new_risk = (risk + i) % 9
        if new_risk == 0:
            new_risk = 9

        new_y = y + ((end_coords[1] + 1) * i)
        extended_map[(x, new_y)] = new_risk

new_end_coords = ((end_coords[0] + 1) * 5 - 1, (end_coords[1] + 1) * 5 - 1)

# Answer Two
print("Lowest total risk of any path on full map:",
       dijkstra(extended_map, new_end_coords)
)
