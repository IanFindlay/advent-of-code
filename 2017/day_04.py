"""Advent of Code Day 4 - High-Entropy Passphrases"""

import os

# Open list, read it and split by newline
pass_txt = open('{0}/4-input.txt'.format(os.getcwd()))
lines = pass_txt.read()
pass_list = lines.split('\n')


def dupe_check(passphrase):
    """Return only if input has no duplicate words in it."""
    words = passphrase.split(' ')
    unique = set(words)
    if words != ['']:
        return len(words) == len(unique)


def anagram_check(passphrase):
    """Return only if input has no anagram pairs in it."""
    words = passphrase.split(' ')
    word_list = []
    for word in words:
        # Make all words have their letters in alphabetical order
        letters = list(word)
        ordered = ('').join(sorted(letters))
        word_list.append(ordered)
    unique = set(word_list)
    if words != ['']:
        return len(words) == len(unique)


# Answer One
dupeless = 0
for passphrase in pass_list:
    if dupe_check(passphrase):
        dupeless += 1

print("Number of passwords without duplicates:", dupeless)

# Answer Two
anagramless = 0
for passphrase in pass_list:
    if anagram_check(passphrase):
        anagramless += 1

print("Number of passwords without anagram pairs:", anagramless)
