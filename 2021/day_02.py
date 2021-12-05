#!/usr/bin/env python3

"""Advent of Code 2021 Day 2 - Dive!"""


with open('inputs/day_02.txt', 'r') as aoc_input:
    input_lines = [line.strip().split(' ') for line in aoc_input.readlines()]
    input_lines = [(x, int(y)) for [x, y] in input_lines]

horizontal_position = 0
depth = 0

for move, amount in input_lines:
    if move == 'forward':
        horizontal_position += amount
    elif move == 'up':
        depth -= amount
    elif move == 'down':
        depth += amount

# Answer One
print("Product of final horizontal position and final depth:",
        horizontal_position * depth)


horizontal_position = 0
depth = 0
aim = 0

for move, amount in input_lines:
    if move == 'forward':
        horizontal_position += amount
        depth += aim * amount
    elif move == 'up':
        aim -= amount
    elif move == 'down':
        aim += amount

# Answer Two
print("Product of final horizontal position and final depth:",
        horizontal_position * depth)
