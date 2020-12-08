#!/usr/bin/env python3

"""Advent of Code 2020 Day 08 - Handheld Halting."""


with open ('input.txt', 'r') as f:
    instructions = [instruction.strip() for instruction in f.readlines()]

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
