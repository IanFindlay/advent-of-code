""" Advent of Code Day 2 - Bathroom Security"""


def get_code(start_pos, keypad, valid_pos):
    """Returns the code generated from instructions on specified keypad."""
    pos = start_pos
    code = ''
    for line in lines:
        for move in line:
            if move == 'R':
                next_pos = [pos[0], pos[1] + 1]
            elif move == 'L':
                next_pos = [pos[0], pos[1] - 1]
            elif move == 'D':
                next_pos = [pos[0] + 1, pos[1]]
            elif move == 'U':
                next_pos = [pos[0] - 1, pos[1]]

            if next_pos in valid_pos:
                pos = next_pos

        code += keypad[pos[0]][pos[1]]

    return code


basic = [
         ['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9'],
]

advanced = [
         ['', '',   '1', '',   ''],
         ['',  '2', '3', '4',  ''],
         ['5', '6', '7', '8', '9'],
         ['',  'A', 'B', 'C',  ''],
         ['',   '', 'D',  '',  ''],
]

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# Answer Part One
buttons = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
print("Bathroom Code =", get_code([1, 1], basic, buttons))

# Answer Part Two
adv_but = [[0, 2], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3],
           [2, 4], [3, 1], [3, 2], [3, 3],[4, 2]]
print("Advanced Bathroom Code =", get_code([1, 1], advanced, adv_but))
