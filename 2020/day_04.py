#!/usr/bin/env python3

"""Advent of Code 2020 Day 04 - Passport Processing."""

import re


with open ('input.txt', 'r') as batch_file:
    passports = [passport for passport in batch_file.read().split('\n\n')]

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid = 0
passport_regex = re.compile('\w*:\.*')
for passport in passports:
    fields = set()
    for data in passport_regex.findall(passport):
        fields.add(data.split(':')[0])

    if required_fields - fields == set():
        valid += 1

# Answer One
print("Number of valid passports:", valid)
