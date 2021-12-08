#!/usr/bin/env python3

"""Advent of Code 2021 Day 8 - Seven Segment Search"""


with open('inputs/day_08.txt', 'r') as aoc_input:
    displays = {}
    for num, line in enumerate(aoc_input.readlines()):
        patterns, outputs = line.split('|')
        patterns = patterns.strip().split(' ')
        outputs = outputs.strip().split(' ')
        displays[num] = (patterns, outputs, None)


unique = 0
for key, value in displays.items():
    outputs = value[1]
    for output in outputs:
        if len(output) in (2, 3, 4, 7):
            unique += 1

# Answer One
print("Number of times 1, 4, 7 or 8 appear in output values:", unique)
