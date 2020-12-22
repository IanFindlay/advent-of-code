"""Advent of Code Day 4 - The Ideal Stocking Stuffer"""

import hashlib

def mine_adventcoins(part_two=False):
    """Calculates and returns MD5 Hash with five leading zeroes."""
    number = 0
    while True:
        hexed = hashlib.md5('{}{}'.format(key, number).encode('utf-8')).hexdigest()

        if part_two:
            if str(hexed)[0:6] == '000000':
                return number

        else:
            if str(hexed)[0:5] == '00000':
                return number

        number += 1


with open('inputs/day_04.txt', 'r') as f:
    key = f.read().strip()

# Answer Part One
print("Five leading zeroes with =", mine_adventcoins())

# Answer Part Two
print("Six leading zeroes with =", mine_adventcoins(part_two=True))
