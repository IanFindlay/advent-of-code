"""Advent of Code 2019 Day 14 - Space Stoichiometry"""

from collections import defaultdict
import math


def create_fuel(reactions, fuel_wanted):
    """Create wanted amount of fuel from reactions, return material dict."""
    needed = defaultdict(int)
    needed['FUEL'] = fuel_wanted
    queue = ['FUEL']
    while queue:
        target = queue.pop()

        for product, reactants in reactions.items():
            if product[1] == target:
                quantity_produced = product[0]
                required = math.ceil(needed[target] / quantity_produced)

                for reactant in reactants:
                    needed[reactant[1]] += required * reactant[0]

                    if needed[target] > 0:
                        queue.append(reactant[1])

                needed[target] -= required * product[0]

    return needed


with open('inputs/day_14.txt') as f:
    recipies = [line.strip() for line in f.readlines()]

reactions = {}
for recipie in recipies:
    reactants, product = [material.strip() for material in recipie.split('=>')]
    product = product.split()
    product = (int(product[0]), product[1])

    reactants_list = []
    reactants = reactants.split(', ')
    for reactant in reactants:
        amount, material = reactant.split(' ')
        reactants_list.append((int(amount), material))

    reactions[product] = reactants_list

# Answer One
ore_needed = create_fuel(reactions, 1)['ORE']
print("Minimum amount of ore:", ore_needed)

# Binary search for maxiumum fuel amount
trillion_ore = 10 ** 12
low = trillion_ore // ore_needed
high = trillion_ore - 1
while low <= high:
    mid = (low + high) // 2
    if low == mid:
        break

    ore_needed = create_fuel(reactions, mid)['ORE']
    if ore_needed < trillion_ore:
        low = mid + 1
    else:
        high = mid - 1

# Answer Two
print("Most fuel that can be made from 1 trillion ore:", low)
