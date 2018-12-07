"""Advent of Code Day 8 - I Heard You Like Registers"""

import re


def run_register(instructions, highest_ever=None):
    """Run the instructions and return value of largest register."""
    # Parse instructions for all of the values and set in dictionary to 0
    value_regex = re.compile(r'(\w*)\s* inc|dec$')
    found = value_regex.findall(instructions)

    registers = {}
    for register in found:
        registers[register] = 0

    # Split instructions into a list to iterate through
    jumps = instructions.split('\n')

    # List of highest value after each jump for Challenge 2
    highs = []

    # Split each instruction into pertient parts
    for instruction in jumps:
        parser_regex = re.compile(r'''(
        ^(\w*)                            # Register name
        \s
        (inc|dec)                         # Action
        \s
        (-?\d*)                           # Change
        \s
        (if)                              # Test start
        \s
        (\w*)                             # Test register
        \s
        (.*)                              # Comparison type
        \s
        (-?\d*)                           # Comparison number
        )''', re.VERBOSE)

        parsed = parser_regex.search(instruction)
        register = parsed.group(2)
        change = int(parsed.group(4))

        # Determine which comparison is needed
        valid = None

        if parsed.group(7) == '>':
            if registers[parsed.group(6)] > int(parsed.group(8)):
                valid = True
            else:
                valid = False

        elif parsed.group(7) == '<':
            if registers[parsed.group(6)] < int(parsed.group(8)):
                valid = True
            else:
                valid = False

        elif parsed.group(7) == '<=':
            if registers[parsed.group(6)] <= int(parsed.group(8)):
                valid = True
            else:
                valid = False

        elif parsed.group(7) == '>=':
            if registers[parsed.group(6)] >= int(parsed.group(8)):
                valid = True
            else:
                valid = False

        elif parsed.group(7) == '==':
            if registers[parsed.group(6)] == int(parsed.group(8)):
                valid = True
            else:
                valid = False

        elif parsed.group(7) == '!=':
            if registers[parsed.group(6)] != int(parsed.group(8)):
                valid = True
            else:
                valid = False

        if valid is True:

            if parsed.group(3) == 'inc':
                new_value = registers[register] + change
                registers.update({register: new_value})

            else:
                new_value = registers[register] - change
                registers.update({register: new_value})

            # Challenge 2 branch - Get highest value after instructions done
            if highest_ever is True:
                highest = max(registers, key=lambda i: registers[i])
                high = registers[highest]
                highs.append(high)

    # Return challenge 2 answer - Highest ever register value
    if highest_ever is True:
        return max(highs)

    # Return challenge 1 answer - Highest final register value
    else:
        highest = max(registers, key=lambda i: registers[i])
        return(registers[highest])


with open('input.txt') as f:
    registers = f.read()

# Answer One:
print('Highest value at end: ' + str(run_register(registers)))

# Answer Two:
print('Highest value: ' + str(run_register(registers, highest_ever=True)))
