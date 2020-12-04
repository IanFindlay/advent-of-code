#!/usr/bin/env python3

"""Advent of Code 2020 Day 04 - Passport Processing."""

import re


with open ('input.txt', 'r') as batch_file:
    passports = [passport for passport in batch_file.read().split('\n\n')]

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid = 0
passport_regex = re.compile('\w*:\S*')
for passport in passports:
    fields = set()
    for data in passport_regex.findall(passport):
        fields.add(data.split(':')[0])

    if required_fields - fields == set():
        valid += 1

# Answer One
print("Number of valid passports:", valid)

# Part Two

def validate_date_field(value: str, min: int, max: int) -> bool:
    """."""
    try:
        value = int(value)
    except ValueError:
        return False

    if value >= min and value <= max:
        return True
    else:
        return False


def validate_height_field(value: str,) -> bool:
    """."""
    unit = value[-2:]
    if unit == "cm":
        height = value[:3]
    else:
        height = value[:2]

    try:
        height = int(height)
    except ValueError:
        return False

    if unit == "cm" and height >=150 and height <= 193:
        return True

    if unit == "in" and height >=59 and height <= 76:
        return True

    return False


def validate_hair_field(value: str) -> bool:
    """."""
    hair_regex = re.compile('#{1}[0-9 a-f]{6}')
    if hair_regex.match(value):
        return True
    else:
        return False


def validate_eye_field(value: str) -> bool:
    """."""
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False


def validate_pid_field(value: str) -> bool:
    """."""
    pid_regex = re.compile('[0-9]{9}')
    if pid_regex.match(value) and len(value) == 9:
        return True
    else:
        return False

valid_and_verified = 0
passport_regex = re.compile('\w*:\S*')
for passport in passports:
    fields = set()
    for data in passport_regex.findall(passport):
        field, value = data.split(':')
        if field == "byr" and validate_date_field(value, 1920, 2002):
            fields.add(field)

        elif field == "iyr" and validate_date_field(value, 2010, 2020):
            fields.add(field)

        elif field == "eyr" and validate_date_field(value, 2020, 2030):
            fields.add(field)

        elif field == "hgt" and validate_height_field(value):
            fields.add(field)

        elif field == "hcl" and validate_hair_field(value):
            fields.add(field)

        elif field == "ecl" and validate_eye_field(value):
            fields.add(field)

        elif field == "pid" and validate_pid_field(value):
            fields.add(field)

    if required_fields - fields == set():
        valid_and_verified += 1

print("Number of valid, verified passwords:", valid_and_verified)
