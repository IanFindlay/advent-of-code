#!/usr/bin/env python3

"""Advent of Code 2020 Day 08 - Handheld Halting."""


def run_boot_code(instructions: list) -> tuple:
    """Run boot code in instructions list.

        Args:
            instructions: List of boot code instruction strings in the format
            "operation argument".

        Returns:
            Tuple of (accumulator, boolean). The boolean represents whether
            the code ran to completion - indicatd by trying to access an
            index beyond the instruction list - or not. The accumulator is the
            value of the accumulator at completion or, in the case of an
            infinite loop, prior to entering the loop.
    """
    accumulator = 0
    visited_indicies = set([0])
    current_index = 0
    while True:
        try:
            operation, argument = instructions[current_index].split()
        except IndexError:
            # Indicates program ran to completion
            return (accumulator, True)

        argument = int(argument)
        if operation == "acc":
            current_index += 1
            accumulator += argument
        elif operation == 'jmp':
            current_index += argument
        elif operation == 'nop':
            current_index += 1

        if current_index in visited_indicies:
            return (accumulator, False)
        visited_indicies.add(current_index)


with open ('inputs/day_08.txt', 'r') as boot_code:
    instructions = [instruction for instruction in boot_code.readlines()]

# Answer One
print("Value in the accumulator before infinite loop:",
      run_boot_code(instructions)[0])

current_index = 0
while True:
    operation, argument = instructions[current_index].split()
    if operation in ('jmp', 'nop'):
        mod_instructions = instructions.copy()
        if operation == 'jmp':
            mod_instructions[current_index] = "{} {}".format('nop', argument)
        elif operation == 'nop':
            mod_instructions[current_index] = "{} {}".format('jmp', argument)

        accumulator, program_fixed = run_boot_code(mod_instructions)
        if program_fixed:
            break

    current_index += 1

# Answer Two
print("Value of the accumulator after the program terminates:", accumulator)
