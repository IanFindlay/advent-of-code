#!/usr/bin/env python3

"""Advent of Code 2021 Day 13 - Transparent Origami"""


with open('inputs/day_13.txt', 'r') as aoc_input:
    dots, folds = aoc_input.read().split('\n\n')

dot_dict = {}
for dot in dots.split('\n'):
    x, y = dot.strip().split(',')
    dot_dict[(int(x), int(y))] = '#'

part_one = False
for fold in folds.strip().split('\n'):
    axis, index = fold.strip('fold along ').split('=')
    index = int(index)

    folded = {}
    for dot in dot_dict.keys():
        x, y = dot

        if axis == 'y':
            # Distance from fold to dot gives new y value
            difference = index - y
            new_y = index + (index - y) if y > index else y
            folded[(x, new_y)] = '#'

        elif axis == 'x':
            # Distance from fold to dot gives new y value
            difference = index - x
            new_x = index + (index - x) if x > index else x
            folded[(new_x, y)] = '#'

    if not part_one:
        # Answer One
        print("Number of dots visible after first fold:", len(folded))
        part_one = True
