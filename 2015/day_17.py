"""Advent of Code Day 17 - No Such Thing as Too Much"""

import itertools

with open('input.txt') as f:
    containers = [int(container) for container in f]

num_needed = len(containers)
total = 0
min_combos = 0
for i in range(len(containers)):
    for combination in itertools.combinations(containers, i):
        if sum(combination) == 150:
            total += 1

            if i <= num_needed:
                num_needed = i
                min_combos += 1

# Answer Part One
print("Number of Valid Combinations =", total)

# Answer Part Two
print("Number of Valid Minimum Container Combinations =", min_combos)
