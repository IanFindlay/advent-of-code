#!/usr/bin/env python3

"""Advent of Code 2021 Day 7 - The Treachery of Wales"""


with open('inputs/day_07.txt', 'r') as aoc_input:
    crabs = [int(x) for x in aoc_input.read().strip().split(',')]

least_fuel = None
for horizontal_position in range(max(crabs)):

    alignment_cost = sum([abs(x - horizontal_position) for x in crabs])
    if not least_fuel or alignment_cost < least_fuel:
        least_fuel = alignment_cost

# Part One
print("Fuel cost to align to least expensive position:", least_fuel)
