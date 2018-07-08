"""Advent of Code Day 19 - Medicine for Rudolph"""

import re


with open('input.txt') as f:
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
