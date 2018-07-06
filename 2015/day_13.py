"""Advent of Code Day 13 - Knights of the Dinner Table"""

import itertools
import re


def calc_happiness(person, neighbour):
    """Returns the overall hapiness of a pair of people."""
    if person == 'me' or neighbour == 'me':
        return 0

    pair_happiness = 0
    p_regex = re.compile(r'{} would (gain|lose) (\d+) .* {}'.format(person, neighbour))
    n_regex = re.compile(r'{} would (gain|lose) (\d+) .* {}'.format(neighbour, person))
    effect_1 = p_regex.search(data).group(1)
    amount_1 = p_regex.search(data).group(2)
    effect_2 = n_regex.search(data).group(1)
    amount_2 = n_regex.search(data).group(2)

    if effect_1 == 'gain':
        pair_happiness += int(amount_1)
    else:
        pair_happiness -= int(amount_1)

    if effect_2 == 'gain':
        pair_happiness += int(amount_2)
    else:
        pair_happiness -= int(amount_2)

    return pair_happiness


with open('input.txt') as f:
    data = f.readlines()

# Find all guests for iteration
guests = []
for line in data:
    guest = line.split(' ')[0]
    if guest not in guests:
        guests.append(guest)
# guests.append('me')  # Uncomment this for Part Two

perms = list(itertools.permutations(guests))
# Evaluate Hapiness for Each Perm
data = ','.join(data)  # Convert to string for regex reasons
happiest = 0
for perm in perms:
    happiness = 0

    i = 0
    while i < len(perm) - 1:
        person = perm[i]
        neighbour = perm[i + 1]
        happiness += calc_happiness(person, neighbour)
        i += 1

    happiness += calc_happiness(perm[0], perm[-1])

    if happiness > happiest:
        happiest = happiness

print(happiest)
