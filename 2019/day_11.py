"""Advent of Code 2019 Day 11 - Space Police."""


from collections import defaultdict


class EHPR:
    """Class for the Emergency Hull Painting Robot."""

    def __init__(self, code, inputs):
        """Initialises the EHPR with code (dict) and inputs (list)."""
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


def paint_hull(intcode, starting_colour):
    """Paint hull by running robot's (EHPR) intcode with starting_colour."""
    robot_painter = EHPR(intcode, [])
    painting_intcode = robot_painter.run_intcode()
    robot_coords = (0, 0)
    robot_facing = 0
    hull = {(0,0): starting_colour,}
    while True:
        try:
            if robot_coords in hull:
                current_colour = hull[robot_coords]
            else:
                current_colour = '.'
            current_colour = 0 if current_colour == '.' else 1
            robot_painter.inputs.append(current_colour)

            paint_colour = next(painting_intcode)
            turn = next(painting_intcode)

            hull[robot_coords] = '#' if paint_colour else '.'
            if turn:
                robot_facing = (robot_facing + 1)  % 4
            else:
                robot_facing = (robot_facing - 1)  % 4

            curr_x, curr_y = robot_coords
            if robot_facing == 0:
                robot_coords = (curr_x, curr_y - 1)
            elif robot_facing == 1:
                robot_coords = (curr_x + 1, curr_y)
            elif robot_facing == 2:
                robot_coords = (curr_x, curr_y + 1)
            else:
                robot_coords = (curr_x - 1, curr_y)

        except StopIteration:
            break

    return hull


# Create defaultdict out of input for memory access
intcode_dict = defaultdict(int)
with open('input.txt', 'r') as f:
    i = 0
    for instruction in f.read().split(','):
        intcode_dict[i] = int(instruction)
        i += 1

# Answer One:
print("Panels painted:", len(paint_hull(intcode_dict.copy(), '.')))

# Find dimensions of painted area
painted_panels = paint_hull(intcode_dict.copy(), '#')
min_x = min_y = max_x = max_y = None
for coord in painted_panels:
    x, y = coord
    if not min_x or x < min_x:
        min_x = x
    if not min_y or y < min_y:
        min_y = y
    if not max_x or x > max_x:
        max_x = x
    if not max_y or y > max_y:
        max_y = y

# Compose image for printing
panels = []
for row in range(min_y - 1, max_y + 1):
    curr_row = []
    for col in range(min_x - 1, max_x + 1):
        coords = (col, row)
        if coords in painted_panels and painted_panels[(coords)] == '#':
            curr_row.append('#')
        else:
            curr_row.append(' ')
    panels.append(curr_row)

# Answer Two
for row in panels:
    print(''.join(row))
