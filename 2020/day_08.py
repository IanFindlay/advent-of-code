#!/usr/bin/env python3

"""Advent of Code 2020 Day 08 - Handheld Halting."""


def acc(argument: int, index: int, accumulator: int) -> int:
    """."""
    accumulator += argument
    return (index + 1, accumulator)


def jmp(argument: int, index: int) -> int:
    """."""
    return index + argument


def nop(index: int) -> int:
    """."""
    return index + 1


with open ('input.txt', 'r') as f:
    instructions = [instruction.strip() for instruction in f.readlines()]

accumulator = 0
visited_indicies = set([0])
current_index = 0
while True:
    operation, argument = instructions[current_index].split()
    argument = int(argument)
    if operation == "acc":
        current_index, accumulator = acc(argument, current_index, accumulator)
    elif operation == 'jmp':
        current_index = jmp(argument, current_index)
    elif operation == 'nop':
        current_index = nop(current_index)

    if current_index in visited_indicies:
        break
    visited_indicies.add(current_index)

# Answer One
print("Value in the accumulator before infinite loop:", accumulator)


def run_until_infinite_or_stopped(instructions: list) -> tuple:
    """."""
    accumulator = 0
    visited_indicies = set([0])
    current_index = 0
    infinite = False
    while True:
        try:
            operation, argument = instructions[current_index].split()
        except IndexError:
            return (accumulator, True)
        argument = int(argument)
        if operation == "acc":
            current_index, accumulator = acc(argument, current_index, accumulator)
        elif operation == 'jmp':
            current_index = jmp(argument, current_index)
        elif operation == 'nop':
            current_index = nop(current_index)

        if current_index in visited_indicies:
            return (accumulator, False)
            break
        visited_indicies.add(current_index)



changed_indicies = set()
current_index = 0
while True:
    operation, argument = instructions[current_index].split()
    if current_index not in changed_indicies and operation != 'acc':
        mod_instructions = instructions.copy()
        changed_indicies.add(current_index)
        if operation == 'jmp':
            mod_instructions[current_index] = "{} {}".format('nop', argument)
        elif operation == 'nop':
            mod_instructions[current_index] = "{} {}".format('jmp', argument)

        accumulator, fixed = run_until_infinite_or_stopped(mod_instructions)
        if fixed:
            break

    current_index += 1

# Answer Two
print("Value of the accumulator after the program terminates:", accumulator)
