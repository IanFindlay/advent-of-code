"""Advent of Code 2019 Day 13 - Care Package."""


from collections import defaultdict


class ArcadeCabinet:
    """Class representing an intcode running arcade cabinet."""

    def __init__(self, code, inputs):
        """Initialises arcade cabinet with code (dict) and an input list."""
        self.code = code
        self.inputs = inputs

    def run_intcode(self):
        """Run intcode program on code."""
        relative_base = 0
        pointer = 0
        while True:
            opcode = self.code[pointer]

            if 99 < opcode <= 22210:
                opcode, modes = parse_instruction(opcode)
            else:
                modes = [0, 0, 0]

            if opcode == 99:   # halt
                return

            if modes[0] == 0:
                param_1 = self.code[pointer + 1]
            elif modes[0] == 1:
                param_1 = pointer + 1
            else:
                param_1 = self.code[pointer + 1] + relative_base

            if modes[1] == 0:
                param_2 = self.code[pointer + 2]
            elif modes[1] == 1:
                param_2 = pointer + 2
            else:
                param_2 = self.code[pointer + 2] + relative_base

            if modes[2] == 0:
                param_3 = self.code[pointer + 3]
            else:
                param_3 = self.code[pointer + 3] + relative_base

            if opcode == 1:   # addition
                self.code[param_3] = self.code[param_1] + self.code[param_2]
                pointer += 4

            elif opcode == 2:   # multiplication
                self.code[param_3] = self.code[param_1] * self.code[param_2]
                pointer += 4

            elif opcode == 3:   # input
                if self.inputs:
                    self.code[param_1] = self.inputs.pop(0)
                    pointer += 2
                else:
                    yield

            elif opcode == 4:   # output
                pointer += 2
                output = self.code[param_1]
                yield output

            elif opcode == 5:   # jump-if-true
                if self.code[param_1] == 0:
                    pointer += 3
                else:
                    pointer = self.code[param_2]

            elif opcode == 6:   # jump-if-false
                if self.code[param_1] != 0:
                    pointer += 3
                else:
                    pointer = self.code[param_2]

            elif opcode == 7:   # less than
                if self.code[param_1] < self.code[param_2]:
                    self.code[param_3] = 1
                else:
                    self.code[param_3] = 0
                pointer += 4

            elif opcode == 8:   # equals
                if self.code[param_1] == self.code[param_2]:
                    self.code[param_3] = 1
                else:
                    self.code[param_3] = 0
                pointer += 4

            elif opcode == 9:   # adjust relative base
                relative_base += self.code[param_1]
                pointer += 2

            else:
                print("Invalid or incorrectly parsed instruction.")
                return


def parse_instruction(value):
    """Return opcode and mode parsed from instruction value."""
    str_value = str(value)
    opcode = int(str_value[-2:])
    modes = [int(x) for x in list(str_value)[:-2]]
    while len(modes) != 3:
        modes.insert(0, 0)
    return (opcode, list(reversed(modes)))


intcode_dict = defaultdict(int)
with open('input.txt', 'r') as f:
    i = 0
    for instruction in f.read().split(','):
        intcode_dict[i] = int(instruction)
        i += 1

game = ArcadeCabinet(intcode_dict.copy(), []).run_intcode()
outputs = []
while True:
    try:
        outputs.append(next(game))
    except StopIteration:
        break

num_outputs = len(outputs)
tile_ids = {0: 'empty', 1: 'wall', 2: 'block', 3: 'paddle', 4: 'ball'}
tiles = {}
block_count = 0
i = 0
while i < num_outputs:
    tile_id = tile_ids[outputs[i+2]]
    tiles[(outputs[i], outputs[i+1])] = tile_id
    if tile_id == 'block':
        block_count += 1
    i += 3

# Answer One
print("Number of block tiles:", block_count)

game_2_code = intcode_dict.copy()
game_2_code[0] = 2

