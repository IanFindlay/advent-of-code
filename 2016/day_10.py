""" Advent of Code Day 10 - Balance Bots"""

import re


with open('inputs/day_10.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

target_1 = 61
target_2 = 17
comp_bot = None
outputs = {}
bots = {}
while instructions:
    to_delete = []
    for row, instruction in enumerate(instructions):
        bot_regex = re.search(r'bot (\d+) gives low to bot (\d+) and high to bot (\d+)', instruction)
        output_regex = re.search(r'bot (\d+) gives low to output (\d+) and high to output (\d+)', instruction)
        mixed_regex = re.search(r'bot (\d+) gives low to output (\d+) and high to bot (\d+)', instruction)

        if instruction.startswith('value'):
            split_instr = instruction.split(' ')
            if split_instr[-1] not in bots:
                bots[split_instr[-1]] = [int(split_instr[1])]
            else:
                bots[split_instr[-1]].append(int(split_instr[1]))

            to_delete.append(row)


        elif bot_regex and bot_regex.group(1) in bots:
            if len(bots[bot_regex.group(1)]) != 2:
                continue

            low = min(bots[bot_regex.group(1)])
            high = max(bots[bot_regex.group(1)])

            if low == target_2 and high == target_1:
                comp_bot = bot_regex.group(1)

            if bot_regex.group(2) not in bots:
                bots[bot_regex.group(2)] = [low]
            else:
                bots[bot_regex.group(2)].append(low)

            if bot_regex.group(3) not in bots:
                bots[bot_regex.group(3)] = [high]
            else:
                bots[bot_regex.group(3)].append(high)

            bots[bot_regex.group(1)] = []

            to_delete.append(row)


        elif output_regex and output_regex.group(1) in bots:
            if len(bots[output_regex.group(1)]) != 2:
                continue

            low = min(bots[output_regex.group(1)])
            high = max(bots[output_regex.group(1)])

            if low == target_2 and high == target_1:
                comp_bot = output_regex.group(1)

            outputs[output_regex.group(2)] = low

            outputs[output_regex.group(3)] = high

            bots[output_regex.group(1)] = []

            to_delete.append(row)


        elif mixed_regex and mixed_regex.group(1) in bots:
            if len(bots[mixed_regex.group(1)]) != 2:
                continue

            low = min(bots[mixed_regex.group(1)])
            high = max(bots[mixed_regex.group(1)])

            if low == target_2 and high == target_1:
                comp_bot = mixed_regex.group(1)

            outputs[mixed_regex.group(2)] = low

            if mixed_regex.group(3) not in bots:
                bots[mixed_regex.group(3)] = [high]
            else:
                bots[mixed_regex.group(3)].append(high)

            bots[mixed_regex.group(1)] = []

            to_delete.append(row)

    for line in reversed(to_delete):
        del instructions[line]

# Answer One
print("Desired Comparison Bot:", comp_bot)

# Answer Two
print("Product of outputs 0, 1 and 2:", outputs['0'] * outputs['1'] * outputs['2'])
