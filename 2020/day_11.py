#!/usr/bin/env python3

"""Advent of Code 2020 Day 11 - Seating System."""


with open ('inputs/2020_11.txt', 'r') as f:
    floorplan = [row.strip() for row in f.readlines()]

num_rows = len(floorplan)
num_cols = len(floorplan[0])
floorplan_dict = {}
for row in range(num_rows):
    for col in range(num_cols):
        floorplan_dict[(row, col)] = floorplan[row][col]

floorplan_dict_copy = floorplan_dict.copy()

while True:
    new_states = {}
    for coords, state in floorplan_dict.items():
        if state == '.':
            new_states[coords] = state
            continue

        adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0),
                    (-1, -1), (-1, 1), (1, 1), (1, -1)]
        occupied = 0
        for seat in adjacent:
            new_coords = (coords[0] + seat[0], coords[1] + seat[1])
            if floorplan_dict.get(new_coords, '.') == '#':
                occupied += 1

        if  occupied == 0 and state == 'L':
            new_states[coords] = '#'
        elif occupied >= 4 and state == '#':
            new_states[coords] = 'L'
        else:
            new_states[coords] = state

    if floorplan_dict == new_states:
        break

    floorplan_dict = new_states

occupied = sum(1 for value in new_states.values() if value == '#')

# Answer One
print("Number of seats that end up occupied:", occupied)

floorplan_dict = floorplan_dict_copy
while True:
    new_states = {}
    for coords, state in floorplan_dict.items():
        if state == '.':
            new_states[coords] = state
            continue

        adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0),
                    (-1, -1), (-1, 1), (1, 1), (1, -1)]

        occupied = 0
        for seat in adjacent:
            new_coords = coords
            while True:
                new_coords = (new_coords[0] + seat[0], new_coords[1] + seat[1])
                if new_coords[0] < 0 or new_coords[1] < 0:
                    break
                if new_coords[0] == num_rows or new_coords[1] == num_cols:
                    break

                adj_state = floorplan_dict.get(new_coords, '.')
                if adj_state == 'L':
                    break

                if adj_state == '#':
                    occupied += 1
                    break

        if occupied == 0 and state == 'L':
            new_states[coords] = '#'
        elif occupied >= 5 and state == '#':
            new_states[coords] = 'L'
        else:
            new_states[coords] = state

    if floorplan_dict == new_states:
        break

    floorplan_dict = new_states

occupied = sum(1 for value in new_states.values() if value == '#')

# Answer Two
print("Number of seats that end up occupied:", occupied)
