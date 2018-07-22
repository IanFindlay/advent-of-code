"""Advent of Code Day 5 - A Maze of Twisty Trampolines, All Alike"""


import pyperclip


def steps_taken(offsets):
    """Calculate the steps needed to traverse an offset maze."""
    # Put the offsets in a list
    value_list = offsets.split('\n')

    # Starting at [0] follow the offsets, adding one to each when used
    list_position = 0
    steps = 0

    while list_position > 0 and list_position < len(value_list):
        offset = int(value_list[list_position])
        value_list[list_position] = int(value_list[list_position]) + 1
        steps += 1
        list_position += offset

    return steps


def jumps_taken(offsets):
    """Calculate the steps needed to traverse a modified offset maze."""
    # Put the offsets in a list
    value_list = offsets.split('\n')

    # Follow offsets, adding one if < 3 and taking 1 if not until maze end
    list_position = 0
    steps = 0

    while list_position > 0 and list_position < len(value_list):
        offset = int(value_list[list_position])
        # Change offset ot the appropriate new value
        if offset < 3:
            value_list[list_position] = int(value_list[list_position]) + 1
        else:
            value_list[list_position] = int(value_list[list_position]) - 1

        steps += 1
        list_position += offset

    return steps


# Answer One
print("Number of steps to reach the exit:", steps_taken(pyperclip.paste()))

# Answer Two
print("Number of steps to reach the exit:", jumps_taken(pyperclip.paste()))
