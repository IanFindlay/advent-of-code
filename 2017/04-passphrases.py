"""Answers to Advent of Code Day 4."""

import os

# Open list, read it and split by newline
pass_txt = open('{0}/4-input.txt'.format(os.getcwd()))
lines = pass_txt.read()
pass_list = lines.split('\n')


# Challenge 1 - only passphrases with no duplicates are valid
def dupe_check(passphrase):
    """Return only if input has no duplicate words in it."""
    words = passphrase.split(' ')
    unique = set(words)
    if words != ['']:
        return len(words) == len(unique)


# Challenge 2 - only passphrases with no anagram pairs are valid
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


# Challenge 1 Answer
dupeless = 0
for passphrase in pass_list:
    if dupe_check(passphrase):
        dupeless += 1

print(dupeless)

# Challenge 2 Answer
anagramless = 0
for passphrase in pass_list:
    if anagram_check(passphrase):
        anagramless += 1

print(anagramless)
