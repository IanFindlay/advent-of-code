#!/usr/bin/env python3

"""Advent of Code 2020 Day 02 - Password Philosophy."""


with open ('input.txt', 'r') as password_database:
    lines = [line for line in password_database.readlines()]

valid_passwords = 0
for line in lines:
    policy, password = line.split(':')
    range_must_appear, character = policy.split(' ')
    lowest_repeat, highest_repeat = range_must_appear.split('-')
    char_count = password.count(character)
    if char_count >= int(lowest_repeat) and char_count <= int(highest_repeat):
        valid_passwords += 1

# Answer One
print("Number of valid passwords:", valid_passwords)
