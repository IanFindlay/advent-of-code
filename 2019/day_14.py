"""Advent of Code 2019 Day 14 - Space Stoichiometry"""

from collections import defaultdict


def create_fuel(reactions, fuel_wanted):
    """Return amount of ore needed to create wanted amount of fuel."""
    extra_materials = defaultdict(int)
    ore_needed = 0
    build_queue = [(fuel_wanted, 'FUEL')]
    while build_queue:
        quantity_needed, target = build_queue.pop()
        for product, reactants in reactions.items():
            if product[1] == target:
                while extra_materials[target] < quantity_needed:
                    for reactant in reactants:
                        if reactant[1] == 'ORE':
                            ore_needed += reactant[0]
                        build_queue.append(reactant)
                    extra_materials[target] += product[0]

                extra_materials[target] -= quantity_needed

    return ore_needed


with open('input.txt') as f:
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
ore_needed = create_fuel(reactions, 1)
print("Minimum amount of ore:", ore_needed)
