#!/usr/bin/env python3

"""Advent of Code 2020 Day 20 - Jurassic Jigsaw."""


with open('inputs/2020_21.txt') as f:
    rows = [line.strip() for line in f.readlines()]

allergens = {}
ingredients_list = []
for row in rows:
    ingredients, contains = row.split('(')
    ingredients = ingredients.split()
    ingredients_list.extend(ingredients)
    contains = [
            x.strip(',') for x in contains[:-1].split() if x != 'contains'
    ]
    for contained in contains:
        if contained not in allergens:
            allergens[contained] = set(ingredients)
        else:
            allergens[contained] = allergens[contained] & set(ingredients)

num_allergens = len(allergens)
matched = set()
while True:
    for allergen, ingredients in allergens.items():
        if len(ingredients) == 1:
            matched.update(ingredients)
            continue

        allergens[allergen] = allergens[allergen].difference(matched)

    if len(matched) == num_allergens:
        break

non_allergen = 0
for ingredient in ingredients_list:
    if ingredient not in matched:
        non_allergen += 1

# Answer One
print("Number of times non-allergen ingredients appear:", non_allergen)
