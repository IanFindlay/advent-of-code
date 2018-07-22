"""Advent of Code Day 7 - Recursive Circus"""

import re
import pyperclip


def tower_info(structure, balance_fix=False):
    """Find base program of structure and how to fix the tower imbalance."""
    # Isolate the program names
    names_regex = re.compile(r'[^0-9\s()->]\w*')
    programs = names_regex.findall(structure)

    # Find the base (has no parents so program is referenced only once)
    for program in programs:
        base_regex = re.compile(r'{0}'.format(program))
        mentions = base_regex.findall(structure)
        if len(mentions) == 1:
            base = program

    # Return Base Program
    if not balance_fix:
        return base

    # Split structure into program name: weight dictionary
    dict_regex = re.compile(r'([^0-9\s()->]\w*)\s\((\d*)')
    weights = dict_regex.findall(structure)
    prog_weight = {}
    for program in weights:
        name = program[0]
        weight = program[1]
        prog_weight[name] = weight
    print(prog_weight)


# Answer One
print("Base Program:", tower_info(pyperclip.paste()))

# Answer Two
print(tower_info(pyperclip.paste(), balance_fix='yes'))
