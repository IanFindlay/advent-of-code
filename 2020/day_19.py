#!/usr/bin/env python3

"""Advent of Code 2020 Day 19 - Monster Messages."""

import re

def cycle_rules(rules: dict, resolved_parts: dict) -> dict:
    """."""
    for rule_num, rule in rules.items():
        for index, char in enumerate(rule):

            if type(char) != list and char in resolved_parts:
                rules[rule_num][index] = resolved_parts[char]

            elif char == '"a"':
                resolved_parts[rule_num] = 'a'
                rules[rule_num] = 'a'

            elif char == '"b"':
                resolved_parts[rule_num] = 'b'
                rules[rule_num] = 'b'

        if check_rule_solved(resolved_parts, rule):
            resolved_parts[rule_num] = rule

    return (rules, resolved_parts)


def check_rule_solved(resolved_parts: list, rule: list):
    """."""
    for char in rule:
        if type(char) == list:
            if not check_rule_solved(resolved_parts, char):
                return False
        elif char not in ('a', 'b', '|') and char not in resolved_parts:
            return False

    return True


def convert_list_to_regex(to_conv: list):
    """."""
    regex = ''
    for char in to_conv:
        if type(char) == list:
            regex += '('
            regex += convert_list_to_regex(char)
            regex += ')'
        else:
            regex += char

    return regex


with open('inputs/2020_19.txt', 'r') as f:
    rows = [row.split() for row in f.readlines()]

rules = {}
for row in rows:
    if not row:
        break

    rule_num = row[0][:-1]
    rules[rule_num] = row[1:]

resolved_parts = {}
while True:
    rules, resolved_parts = cycle_rules(rules, resolved_parts)
    if check_rule_solved(resolved_parts, rules['0']):
        break

match = 0
regex = re.compile(convert_list_to_regex(rules['0']))
for message in rows[len(rules) + 1:]:
    if regex.fullmatch(message[0]):
        match += 1

# Answer One
print("Number of messages that completely match rule 0:", match)
