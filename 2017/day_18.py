"""Advent of Code Day 18 - Duet"""

import re
import collections


def is_num(string):
    """Return whether or not a string can be interpreted as an integer."""
    try:
        int(string)
    except ValueError:
        return False
    return True


def duet(instructions, registers, position, part_two=False, program_id=None):
    """Return the final recovered note of a list of instructions."""
    sent = 0
    sound = 0
    recovered = 0
    processed = 0
    i = position
    while i < len(instructions):
        instruction = instructions[i]
        mod, target, *change = re.findall(r'-?\w+', instruction)

        if mod == 'snd' and not part_two:
            if is_num(target):
                sound = target
            else:
                sound = registers[target]

        elif mod == 'snd' and part_two:
            if is_num(target):
                if program_id == 0:
                    queue_1.append(int(target))
                else:
                    queue_0.append(int(target))
                    sent += 1
            else:
                if program_id == 0:
                    queue_1.append(registers[target])
                else:
                    queue_0.append(registers[target])
                    sent += 1

        elif mod == 'set':
            if is_num(change[0]):
                registers[target] = int(change[0])
            else:
                registers[target] = registers[change[0]]

        elif mod == 'add':
            if is_num(change[0]):
                registers[target] += int(change[0])
            else:
                registers[target] += registers[change[0]]

        elif mod == 'mul':
            if is_num(change[0]):
                registers[target] *= int(change[0])
            else:
                registers[target] *= registers[change[0]]

        elif mod == 'mod':
            if is_num(change[0]):
                registers[target] = registers[target] % int(change[0])
            else:
                registers[target] = registers[target] % registers[change[0]]

        elif mod == 'rcv' and not part_two:
            if is_num(target):
                if int(target) != 0:
                    recovered = sound
                    break
            else:
                if registers[target] != 0:
                    recovered = sound
                    break

        elif mod == 'rcv' and part_two:
            if program_id == 0:
                if queue_0:
                    registers[target] = queue_0.popleft()
                else:
                    break
            if program_id == 1:
                if queue_1:
                    registers[target] = queue_1.popleft()
                else:
                    break

        elif mod == 'jgz':
            if is_num(change[0]):
                if is_num(target):
                    if int(target) > 0:
                        i += int(change[0])
                        continue
                else:
                    if registers[target] > 0:
                        i += int(change[0])
                        continue
            else:
                if is_num (target):
                    if int(target) > 0:
                        i += int(registers[change[0]])
                        continue
                else:
                    if registers[target] > 0:
                        i += registers[change[0]]
                        continue
        i += 1
        processed += 1

    if not part_two:
        return recovered

    elif program_id == 0:
        return (i, processed)

    elif program_id == 1:
        return (i, sent, processed)


def coord_progs():
    """Coordinate the running of two programs until they both stall."""
    pos_0 = 0
    pos_1 = 0
    registers_0 = collections.defaultdict(int,)
    registers_1 = collections.defaultdict(int,)
    registers_0['p'] = 0
    registers_1['p'] = 1
    sent = 0
    stalled = False

    while not stalled:
        position, processed_0 = duet(instructions, registers_0, pos_0,
                                     part_two=True, program_id=0)
        pos_0 = position
        position, add_sent, processed_1 = duet(instructions, registers_1, pos_1,
                                               part_two=True, program_id=1)
        pos_1 = position
        sent += add_sent

        if processed_0 == 0 and processed_1 == 0:
            stalled = True

    return sent


if __name__ == '__main__':

    with open('input.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    registers = collections.defaultdict(int,)

    # Answer One
    print("First non-zero recovered frequency:", duet(instructions, registers, 0))

    queue_0 = collections.deque()
    queue_1 = collections.deque()

    # Answer Two
    print("Number of signals sent by program 1:", coord_progs())
