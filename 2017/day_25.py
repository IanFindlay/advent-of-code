"""Advent of Code Day 25 - The Halting Problem"""

import re

def make_dict():
    """Create a nested dictionary representing state and actions to take."""
    states = {}
    for section in sections[1:]:
        lines = section.split('\n')

        state = lines[0][-2]
        value_0 = lines[2][-2]
        dir_0 = re.search(r'(right|left)', lines[3]).group(1)
        cont_0 = lines[4][-2]
        value_1 = lines[6][-2]
        dir_1 = re.search(r'(right|left)', lines[7]).group(1)
        cont_1 = lines[8][-2]

        states[state + '0'] = {'write': value_0, 'dir': dir_0, 'cont': cont_0}
        states[state + '1'] = {'write': value_1, 'dir': dir_1, 'cont': cont_1}

    return states


def run_turing(start_state, steps):
    """Use blueprint to run turing machine and generate diagnostic checksum."""
    tape = {0: '0'}
    tape_pos = 0
    state = start_state
    for __ in range(steps):
        value = tape[tape_pos]
        write = states['{}{}'.format(state, value)]['write']
        direction = states['{}{}'.format(state, value)]['dir']
        new_state = states['{}{}'.format(state, value)]['cont']
        tape[tape_pos] = write

        if direction == 'right':
            tape_pos += 1
        else:
            tape_pos -= 1
        tape[tape_pos] = tape.get(tape_pos, '0')

        state = new_state

    checksum = 0
    for __, value in tape.items():
        if value == '1':
            checksum += 1

    return checksum


if __name__ == '__main__':

    with open('inputs/day_25.txt') as f:
        blueprints = f.read()

    sections = blueprints.strip().split('\n\n')
    begin = re.search(r'state (\w)', sections[0]).group(1)
    steps = int(re.search(r'(\d+)', sections[0]).group(1))

    states = make_dict()

    # Answer
    print("Diagnostic checksum:", run_turing(begin, steps))
