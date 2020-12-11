#!/usr/bin/env python3

"""Advent of Code 2020 Day 11 - Seating System."""


with open ('input.txt', 'r') as f:
    floorplan = [row.strip() for row in f.readlines()]

floorplan_dict = {}
for row in range(len(floorplan)):
    for col in range(len(floorplan[0])):
        floorplan_dict[(row, col)] = floorplan[row][col]

while True:
    new_states = {}
    for coords, state in floorplan_dict.items():
        row, col = coords
        adjacent = [
                (row, col - 1), (row, col + 1),
                (row - 1, col), (row + 1,  col),
                (row - 1, col - 1), (row - 1,  col + 1),
                (row + 1, col + 1), (row + 1,  col - 1)
        ]
        occupied = 0
        for seat in adjacent:
            if floorplan_dict.get(seat, '.') == '#':
                occupied += 1

        if state == 'L' and occupied == 0:
            new_states[coords] = '#'
        elif state == '#' and occupied >= 4:
            new_states[coords] = 'L'
        else:
            new_states[coords] = state

    if floorplan_dict == new_states:
        break

    floorplan_dict = new_states

occupied = 0
for state in new_states.values():
    if state == '#':
        occupied += 1

# Answer One
print("Number of seats that end up occupied:", occupied)
