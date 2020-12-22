"""Advent of Code Day 24 - It Hangs in the Balance"""

import itertools


with open('inputs/day_24.txt') as f:
    weights = [int(num) for num in f]

section_weight = sum(weights) // 4    # Change to 3 for Part One

smallest_section = len(weights)
smallest_combos = []

for i in range(1, len(weights)):
    if i > smallest_section:
        break

    combos = itertools.combinations(weights, i)
    for combo in combos:
        if sum(combo) != section_weight:
            continue

        smallest_combos.append(combo)
        smallest_section = i

smallest_qe = max(weights) ** len(weights)
for combination in smallest_combos[:1]:
    qe = 1
    for weight in combination:
        qe *= weight

    if qe < smallest_qe:
        smallest_qe = qe

# Answer
print("Smallest Quantum Entanglement =", smallest_qe)

