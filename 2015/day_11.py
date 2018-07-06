"""Advent of Code Day 11 - Corporate Policy"""

import re


puzzle_input = 'hxbxwxba'           # Change to Part One Solution for Part Two 
old_pass = puzzle_input
old_rev = list(reversed(old_pass))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
valid = False

while not valid:
    for pos, letter in enumerate(old_rev):
        if letter == 'z':
            old_rev[pos] = 'a'
        else:
            old_rev[pos] = alphabet[alphabet.find(letter) + 1]
            new_pass = ''.join(old_rev)[-1::-1]
            break
    
    # Check Validity
    confusing_regex = re.compile(r'i|o|l')
    if confusing_regex.search(new_pass):
        continue

    doubles_regex = re.compile(r'(.)\1')
    if len(doubles_regex.findall(new_pass)) < 2:
        continue

    straight = False
    for pos, letter in enumerate(new_pass[:-2]):
        if (new_pass[pos] not in ('y', 'z') 
                and new_pass[pos + 1] == alphabet[alphabet.find(letter) + 1]
                and new_pass[pos + 2] == alphabet[alphabet.find(letter) + 2]):

            straight = True

    if not straight:
        continue

    valid = True

print("New Password =",new_pass)
