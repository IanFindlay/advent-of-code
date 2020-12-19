#!/usr/bin/env python3

"""Advent of Code 2020 Day 19 - Monster Messages."""


import re


def convert_to_regex(rules_dict: dict, rule_num: int, depth: int=0) -> str:
    """Convert rule to its regex equivalent and return it.

    Args:
        rules_dict: Dictionary of rule_num: rule.
        rule_num: Key for rules_dict corresponding to rule to be converted.
        depth: Number of recursive calls to the function. Defaults to 0 and
               used to set a limit on processing of loops.

    Returns:
        The regex string equivalent of the rule at key rule_num in rules_dict
        (to a capped depth).

    """
    if depth > 15:
        return ''

    if rules_dict[rule_num] in ('a', 'b'):
        return rules_dict[rule_num]

    rules = []
    for branches in rules_dict[rule_num].split('|'):
        branch_answer = ''
        for branch_num in branches.split():
            branch_re = convert_to_regex(rules_dict, branch_num, depth + 1)
            branch_answer += branch_re
        rules.append(branch_answer)

    return '(' + '|'.join(rules) + ')'


rules, messages = open('inputs/2020_19.txt').read().split('\n\n')
rules_dict = {}
for line in rules.split("\n"):
    rule_num, rule = [x.strip() for x in line.split(':')]
    if rule[0] == '"':
        rule = rule.strip('"')
    rules_dict[rule_num] = rule

regex = re.compile(convert_to_regex(rules_dict, '0'))

matches = 0
for message in messages.split():
    if regex.fullmatch(message):
        matches += 1

# Answer One
print("Number of messages that completely match rule 0:", matches)

rules_dict["8"] = "42 | 42 8"
rules_dict["11"] = "42 31 | 42 11 31"

regex = re.compile(convert_to_regex(rules_dict, '0'))

matches = 0
for message in messages.split():
    if regex.fullmatch(message):
        matches += 1

# Answer Two
print("Number of messages that completely match rule 0 after update:",
      matches)
