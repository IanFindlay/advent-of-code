"""Advent of Code Day 5 - Doesn't He Have Intern-Elves For This?"""

import re

with open('inputs/day_05.txt') as f:
    strings = f.readlines()

# Answer One Regexes
naughty_regex = re.compile(r'ab|cd|pq|xy')
vowel_regex = re.compile(r'([aeiou].*){3,}')
double_regex = re.compile(r'(.)\1')
# Answer Two Regexes
repeated_regex = re.compile(r'(..).*\1')
gapped_regex = re.compile(r'(.).\1')

nice = 0
nice_2 = 0
for string in strings:

    if (vowel_regex.search(string) and double_regex.search(string)
            and not naughty_regex.search(string)):
        nice += 1

    if repeated_regex.search(string) and gapped_regex.search(string):
        nice_2 += 1


print("Answer One =", nice)
print("Answer Two =", nice_2)
