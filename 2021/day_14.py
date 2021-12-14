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
print("Quantity of most common element minus least common:", most_minus_least)

pairs = {}
polymer = template.strip()
for index, element in enumerate(polymer[:-1]):
    pair = f'{element}{polymer[index + 1]}'
    pairs[pair] = pairs.get(pair, 0) + 1

for _ in range(40):
    new_pairs = {}
    for pair in pairs:
        if pairs[pair] == 0:
            continue

        element_one, element_two = pair
        to_insert = reactions[pair]
        first_new = f'{element_one}{to_insert}'
        second_new = f'{to_insert}{element_two}'

        new_pairs[first_new] = pairs[pair] + new_pairs.get(first_new, 0)
        new_pairs[second_new] = pairs[pair] + new_pairs.get(second_new, 0)

    pairs = new_pairs

element_count = {}
for pair, count in pairs.items():
    element_one, element_two = pair
    element_count[element_one] = element_count.get(element_one, 0) + count

# Last element stays same throughout but isn't counted in above
element_count[polymer[-1]] += 1

most_minus_least = max(element_count.values()) - min(element_count.values())

# Answer Two
print("Quantity of most common element minus least common:", most_minus_least)
