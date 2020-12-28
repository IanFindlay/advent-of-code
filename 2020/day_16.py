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
    """Check number against each field and return set of valid ones."""
    valid_fields = set()
    for field, range_tuples in rules_dict.items():
        for num_range in range_tuples:
            lower, upper = num_range
            if number >= lower and number <= upper:
                valid_fields.add(field)

    return valid_fields


with open('inputs/day_16.txt', 'r') as f:
    rules, my_ticket, nearby = [row.strip() for row in f.read().split('\n\n')]

# Parse Field Rules
rules_dict = {}
for rule in rules.split('\n'):
    field, num_ranges = rule.split(':')
    num_ranges = [num_range.strip() for num_range in num_ranges.split('or')]
    range_tuples = []
    for num_range in num_ranges:
        lower, upper = num_range.split('-')
        range_tuples.append((int(lower), int(upper)))
    rules_dict[field] = range_tuples

# Parse Nearby Tickets
numbers = [[int(x) for x in row.split(',')] for row in nearby.split('\n')[1:]]

invalid = 0
valid_tickets = []
for number_row in numbers:
    ticket_valid = True
    for number in number_row:
        if not number_valid(rules_dict, number):
            invalid += number
            ticket_valid = False
    if ticket_valid:
        valid_tickets.append(number_row)

# Answer One
print("Ticket scanning error rate:", invalid)

num_fields = len(rules_dict)
my_fields = [set()] * num_fields
assigned_fields = set()
num_assigned = 0
all_assigned = False
while True:
    for number_row in valid_tickets:
        for index, number in enumerate(number_row):
            valid_fields = potential_fields(rules_dict, number)
            prev_fields = my_fields[index]
            if len(prev_fields) != 1:
                valid_fields = valid_fields.difference(assigned_fields)
            if not prev_fields:
                prev_fields = valid_fields
            else:
                prev_fields = prev_fields.intersection(valid_fields)

            my_fields[index] = prev_fields

            if len(prev_fields) == 1:
                field = list(prev_fields).pop()
                if field not in assigned_fields:
                    assigned_fields.update(prev_fields)
                    num_assigned += 1

            if num_assigned == num_fields:
                all_assigned = True
                break

    if all_assigned:
        break

my_fields = [list(x)[0] for x in my_fields]
my_ticket = [[int(x) for x in row.split(',')]
              for row in my_ticket.split('\n')[1:]][0]

departure_product = 1
for index, field in enumerate(my_fields):
    if field.startswith('departure'):
        departure_product *= my_ticket[index]

# Answer Two
print("Product of the six 'departure' field values on my ticket:",
      departure_product)
