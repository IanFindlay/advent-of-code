#!/usr/bin/env python3

"""Advent of Code 2020 Day 02 - Password Philosophy."""

import re


with open ('inputs/2020_02.txt', 'r') as password_database:
    lines = [line for line in password_database.readlines()]

line_regex = re.compile('(\d*)-(\d*)\s(\w):\s(\w*)')
part_one_valid = 0
part_two_valid = 0
for line in lines:
    first_num, second_num, char, password = line_regex.findall(line)[0]
    first_num = int(first_num)
    second_num = int(second_num)

    # Part One
    char_count = password.count(char)
    if char_count >= first_num and char_count <= second_num:
        part_one_valid += 1

    # Part Two
    if password[first_num - 1] == char and password[second_num - 1] != char:
        part_two_valid += 1
    elif password[first_num - 1] != char and password[second_num - 1] == char:
        part_two_valid += 1

# Answer One
print("Number of valid passwords according to first policy:", part_one_valid)

# Answer Two
print("Number of valid passwords according to second policy:", part_two_valid)
