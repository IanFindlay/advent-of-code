#!/usr/bin/env python3

"""Advent of Code 2021 Day 14 - Extended Polymerization"""


with open('inputs/day_14.txt', 'r') as aoc_input:
    template, pairs = aoc_input.read().split('\n\n')

reactions = {}
for pair in pairs.strip().split('\n'):
    reactants, insertion = pair.split(' -> ')
    reactions[reactants] = insertion

polymer = template.strip()
for _ in range(10):
    new_polymer = ''
    for index, element in enumerate(polymer[:-1]):
        to_insert = reactions[f'{element}{polymer[index + 1]}']
        new_polymer += f'{element}{to_insert}'

    new_polymer += template.strip()[-1]
    polymer = new_polymer

element_count = {}
for element in polymer:
     element_count[element] = element_count.get(element, 0) + 1


most_minus_least = max(element_count.values()) - min(element_count.values())
# Answer One
print("Quantity of most common elemnet minus least common:", most_minus_least)
