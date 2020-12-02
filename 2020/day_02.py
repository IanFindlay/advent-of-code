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


valid_passwords = 0
for line in lines:
    policy, password = line.split(':')
    password = password.lstrip()
    indicies, char = policy.split(' ')
    lowest_index, highest_index = indicies.split('-')
    lowest_index = int(lowest_index) - 1
    highest_index = int(highest_index) - 1

    if password[lowest_index] == char and password[highest_index] != char:
        valid_passwords += 1
    elif password[lowest_index] != char and password[highest_index] == char:
        valid_passwords += 1

# Answer Two
print("Number of valid passwords:", valid_passwords)
