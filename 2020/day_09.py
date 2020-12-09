#!/usr/bin/env python3

"""Advent of Code 2020 Day 09 - Encoding Error."""


from itertools import combinations


with open ('input.txt', 'r') as xmas:
    numbers = [int(number.strip()) for number in xmas.readlines()]

for index, number in enumerate(numbers[25:], 25):
    prev_25 = numbers[index - 25 : index]
    valid_next = set([sum(combo) for combo in combinations(prev_25, 2)])
    if number not in valid_next:
        break

# Answer One
print("First number that is not the sum of two numbers in the previous 25:",
      numbers[index])
