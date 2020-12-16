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


def potential_fields(rules_dict: dict, number: int) -> set:
    """."""
    valid_fields = set()
    for field, range_tuples in rules_dict.items():
        for num_range in range_tuples:
            lower, upper = num_range
            if number >= lower and number <= upper:
                valid_fields.add(field)

    return valid_fields


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

valid_tickets = []
for number_row in numbers:
    ticked_valid = True
    for number in number_row:
        if not number_valid(rules_dict, number):
            ticked_valid = False
            break
    if ticked_valid:
        valid_tickets.append(number_row)

my_fields = [set()] * len(rules_dict)
assigned_fields = set()
while True:
    for number_row in valid_tickets:
        for index, number in enumerate(number_row):
            valid_fields = potential_fields(rules_dict, number)
            if len(my_fields[index]) != 1:
                valid_fields = valid_fields.difference(assigned_fields)
            if not my_fields[index]:
                my_fields[index] = valid_fields
            else:
                my_fields[index] = my_fields[index].intersection(valid_fields)

            if len(my_fields[index]) == 1:
                assigned_fields.update(my_fields[index])
    if len(assigned_fields) == len(my_fields):
        break


my_fields = [list(x)[0] for x in my_fields]
my_ticket = [[int(x) for x in row.split(',')] for row in my_ticket.split('\n')[1:]][0]
departure_product = 1
for index, field in enumerate(my_fields):
    if field.startswith('departure'):
        departure_product *= my_ticket[index]

# Answer Two
print("Product of the six 'departure' field values on my ticket:",
      departure_product)
