#!/usr/bin/env python3

"""Advent of Code 2020 Day 16 - Ticket Translation."""


def number_valid(rules_dict: dict, number: int) -> bool:
    """Run number against dictionary of rules and return if valid or not."""
    for range_tuples in rules_dict.values():
        for num_range in range_tuples:
            lower, upper = num_range
            if number >= lower and number <= upper:
                return True
    return False


with open('input.txt', 'r') as f:
    rules, my_ticket, nearby = [row.strip() for row in f.read().split('\n\n')]

rules_dict = {}
for rule in rules.split('\n'):
    field, num_ranges = rule.split(':')
    num_ranges = [num_range.strip() for num_range in num_ranges.split('or')]
    range_tuples = []
    for num_range in num_ranges:
        lower, upper = num_range.split('-')
        range_tuples.append((int(lower), int(upper)))
    rules_dict[field] = range_tuples

numbers = [[int(x) for x in row.split(',')] for row in nearby.split('\n')[1:]]
invalid = 0
for number_row in numbers:
    for number in number_row:
        if not number_valid(rules_dict, number):
            invalid += number

# Answer One
print("Ticket scanning error rate:", invalid)
