"""Advent of Code Day 7 - Recursive Circus"""

import collections
import re


def base_dict(tower_data):
    """Build weight and holding dictionaries and identify the base program."""
    holding = {}
    weights = {}
    base = []
    for tower in tower_data:
        program, weight, *held = re.findall(r'\w+', tower)
        base.append(program)
        weights[program] = int(weight)
        holding[program] = list(held)

    for __, values in holding.items():
        [base.remove(value) for value in values]

    return (holding, weights, base[0])


def find_fix(program):
    """Traverse structure and find mismatched weight and the fix required."""
    above = [find_fix(held) for held in holding[program]]

    if len(set(above)) == 2:
        # Imbalanced so find most common (correct) weight and aberrant one
        mismatch = collections.Counter(above).most_common()
        desired = mismatch[0][0]
        wrong = mismatch[1][0]
        # Find imbalanced program and the weight it should be
        imbalanced = holding[program][above.index(wrong)]
        corrected = weights[imbalanced] + (desired - wrong)

        # Answer Two
        print("Corrected weight:", corrected)

        # Return corrected weight so upstream imbalances don't trigger
        return weights[program] + sum(above) + desired - wrong

    return weights[program] + sum(above)


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = f.readlines()

        initial_info = base_dict(data)
        holding = initial_info[0]
        weights = initial_info[1]
        base = initial_info[2]

        # Answer One
        print("Bottom program:", base)

        # Answer Two
        find_fix(base)
