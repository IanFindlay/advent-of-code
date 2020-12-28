"""Advent of Code Day 19 - Medicine for Rudolph"""

import re


with open('inputs/day_19.txt') as f:
    calibration = [line.strip() for line in f]

mol = calibration[-1]
replacements = calibration[:-2]

new_list = set()
for replacement in replacements:
    info = replacement.split(' ')
    change_from = info[0]
    change_to = info[2]

    i = 0
    while i < len(mol):
        if mol[i: i + len(change_from)] == change_from:
            new_mol = mol[:i] + change_to + mol[i + len(change_from):]
            i += len(change_from)
            new_list.add(new_mol)

        else:
            i += 1

# Answer Part One
print("Number of Distinct Molecules After One Replacement = " + str(len(new_list)))

# Part Two

# Function so it can be fed to re.sub
def replace(rev_chem):
    """Return the appropriate substitution of an element string."""
    return unsynth[rev_chem.group()]


# Reverse to capture Ar subs before other part of the sub are carried out
rev_mol = mol[::-1]

rep_regex = re.compile(r'(\w+) => (\w+)')
reps = rep_regex.findall('\n'.join(replacements))

# Build dict of reversed elements - k = replacement and v = replaced
unsynth = {}
for rep in reps:
    unsynth[rep[1][::-1]] = rep[0][::-1]

count = 0
while rev_mol != 'e':
    rev_mol = re.sub('|'.join(unsynth.keys()), replace, rev_mol, 1)
    count += 1

print("Number of Steps to Synthesise Rudolph Cure =", count)
