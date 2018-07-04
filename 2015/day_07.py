"""Advent of Code Day 7 - Some Assembly Required"""

import re


def attempt(instruction):
    """Parses and attempts instruction returning True only if successful."""
    # Parse instruction
    target_regex = re.compile(r'-> (\w+)')
    target_wire = target_regex.search(instruction).group(1)

    not_regex = re.compile(r'NOT (\w+) ->')
    connection_regex = re.compile(r'(\S+) ->')
    gapped_regex = re.compile(r'(\w+) (AND|OR|LSHIFT|RSHIFT) (\S+) ->')


    if not_regex.search(instruction):
        wire_value = wires[not_regex.search(instruction).group(1)]
        binary_value = bin(wire_value)[2:].zfill(16)
        not_binary = ''
        for bit in binary_value:
            if bit == '1':
                not_binary += '0'
            else:
                not_binary += '1'
        value = int(not_binary, 2)

    elif gapped_regex.search(instruction):
        first = gapped_regex.search(instruction).group(1)
        operation = gapped_regex.search(instruction).group(2)
        second = gapped_regex.search(instruction).group(3)

        if first.isnumeric():
            first_comp = int(first)
        else:
            first_comp = wires[first]

        if second.isnumeric():
            second_comp = int(second)
        else:
            second_comp = wires[second]

        if operation == 'LSHIFT':
            value = first_comp << second_comp

        elif operation == 'RSHIFT':
            value = first_comp >> second_comp

        elif operation == 'AND':
            value = first_comp & second_comp

        elif operation == 'OR':
            value = first_comp | second_comp


    elif connection_regex.search(instruction):
        new_value = connection_regex.search(instruction).group(1)
        if new_value.isnumeric():
            value = new_value
        else:
            value = wires[new_value]

    try:
        wires[target_wire] = int(value)
    except:
        return

    return True


with open('input.txt') as f:
    instructions = f.readlines()

wires = {}
while instructions:
    completed = []
    for instruction in instructions:
        # Catch instructions that aren't yet possible and continue past them
        try:
            if attempt(instruction):
                completed.append(instruction)
        except:
            continue

    # Remove completed instructions after cycle so iteration works properly
    for done in completed:
        instructions.remove(done)

# Answer One
print("Answer One =", wires['a'])

# Part Two
new_b = wires['a']
wires = {'b': new_b,}

with open('input.txt') as f:
    instructions = f.readlines()

while instructions:
    completed = []
    for instruction in instructions:
        # Override the instruction which sets wire b to keep it at required value
        if instruction == "14146 -> b\n":
            completed.append(instruction)
            continue
        try:
            if attempt(instruction):
                completed.append(instruction)
        except:
            continue

    for done in completed:
        instructions.remove(done)


# Answer Two
print("Answer Two =", wires['a'])
