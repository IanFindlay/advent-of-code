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
                    yield "Waiting on input"

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


def move_paddle(tiles_dict):
    """Input move that brings the paddle closer to the ball if both found."""
    paddle_x = 'Missing'
    ball_x = 'Missing'
    for coords, tile in tiles_dict.items():
        if tile == 3:
            paddle_x = coords[0]
        elif tile == 4:
            ball_x = coords[0]

    if paddle_x == 'Missing' or ball_x == 'Missing':
        return
    if paddle_x > ball_x:
        cabinet.inputs.append(-1)
    elif paddle_x < ball_x:
        cabinet.inputs.append(1)
    else:
        cabinet.inputs.append(0)
    return


intcode_dict = defaultdict(int)
with open('inputs/day_13.txt', 'r') as f:
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
tiles = {}
block_count = 0
i = 0
while i < num_outputs:
    tile_id = outputs[i+2]
    tiles[(outputs[i], outputs[i+1])] = tile_id
    if tile_id == 2:
        block_count += 1
    i += 3

# Answer One
print("Number of block tiles:", block_count)

game_2_code = intcode_dict.copy()
game_2_code[0] = 2

cabinet = ArcadeCabinet(game_2_code, [])
game_2 = cabinet.run_intcode()

score = 0
tiles = {}
while True:
    try:
        output = []
        for _ in range(3):
            output.append(next(game_2))

        x, y, tile_id = output
        if x == -1 and y == 0:
            score = tile_id
        elif "Waiting on input" in output:
            move_paddle(tiles)
        else:
            tiles[(x, y)] = tile_id

        if tile_id == 4:
            move_paddle(tiles)

    except StopIteration:
        break

# Answer Two
print("Final Score:", score)
