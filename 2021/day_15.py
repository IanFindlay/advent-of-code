#!/usr/bin/env python3

"""Advent of Code 2021 Day 15 - Chiton"""


def dijkstra(map_dict, end_coords):
    unvisited = set(map_dict.keys())
    node_dict = {(0, 0): 0}
    current_node = (0, 0)
    while node_dict:
        x, y = current_node
        risk = node_dict[current_node]

        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for next_to in adjacent:
            if next_to not in unvisited:
                continue

            current_risk = node_dict.get(next_to, None)
            new_risk = risk + map_dict[next_to]
            if not current_risk or new_risk < current_risk:
                node_dict[next_to] = new_risk

        unvisited.remove(current_node)
        del node_dict[current_node]

        lowest_risk = min(node_dict.values())
        for coords, risk in node_dict.items():
            if risk == lowest_risk:
                current_node = coords
                break

        if current_node == end_coords:
            return node_dict[end_coords]

    return None


with open('inputs/day_15.txt', 'r') as aoc_input:
    lines = [line.strip() for line in aoc_input.readlines()]

map_dict = {}
for y, row in enumerate(lines):
    for x, risk_level in enumerate(row):
        map_dict[(x, y)] = int(risk_level)

end_coords = (len(lines) - 1, len(lines[0]) - 1)

# Answer One
print("Lowest total risk of any path:", dijkstra(map_dict, end_coords))

# Build full map
full_map = map_dict.copy()
for coords, risk in map_dict.items():
    x, y = coords
    for i in range(1, 5):
        new_risk = (risk + i) % 9
        new_risk = 9 if new_risk == 0 else new_risk

        new_x = x + ((end_coords[0] + 1) * i)
        full_map[(new_x, y)] = new_risk

map_dict = full_map.copy()
for coords, risk in map_dict.items():
    x, y = coords
    for i in range(1, 5):
        new_risk = (risk + i) % 9
        new_risk = 9 if new_risk == 0 else new_risk

        new_y = y + ((end_coords[1] + 1) * i)
        full_map[(x, new_y)] = new_risk

new_end_coords = ((end_coords[0] + 1) * 5 - 1, (end_coords[1] + 1) * 5 - 1)

# Answer Two
print("Lowest total risk on full map:", dijkstra(full_map, new_end_coords))
