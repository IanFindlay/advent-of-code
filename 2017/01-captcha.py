"""Answers to Advent of Code Day 1."""

import pyperclip


# Challenge 1 - Sum matching digits of captcha
def captcha_dupes(numbers):
    """Sum only the digits that match the one next in a cyclic string."""
    Total = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers[i - 1]:
            Total += int(numbers[i])
    return Total


# Challenge 1 - Sum digits that match the one halfway around of captcha
def captcha_halfway(numbers):
    """Sum the digits that match the one half way around a cyclic string."""
    total = 0
    for i in range(int(len(numbers) / 2)):
        if numbers[i] == numbers[i + int(len(numbers) / 2)]:
            total += int(numbers[i])

    return total * 2


# Paste the string then run it through the funciton and print the answer
captcha = pyperclip.paste()

# Challenge 1 Answer
try:
    print(captcha_dupes(captcha))
except ValueError:
    print('The string in your clipboard isn\'t just digits')

# Challenge 2 Answer
try:
    print(captcha_halfway(captcha))
except ValueError:
    print('The string in your clipboard isn\'t just digits')
