"""Answers to Advent of Code Day 11."""


def path(steps_string):
    """Find how far from the centre of a hex grid a list of steps takes you."""
    # Strip and split file into a iterable list
    steps_list = steps_string.strip().split(',')

    # Break hexagon neighbours into cube coordinates
    x = 0
    y = 0
    z = 0
    furthest = 0
    for step in steps_list:
        # Match step with movement in cube coordinate terms
        if step == 'n':
            x += 1
            y -= 1

        elif step == 's':
            y += 1
            x -= 1

        elif step == 'ne':
            z += 1
            y -= 1

        elif step == 'sw':
            y += 1
            z -= 1

        elif step == 'nw':
            x += 1
            z -= 1

        elif step == 'se':
            z += 1
            x -= 1

        # Keep running track of largest value (furthest distance from centre)
        if max(x, y, z) > furthest:
            furthest = max(x, y, z)

    # Find biggest cube coordinate (shortest path)
    shortest_path = max(x, y, z)

    # Challenge Answer 1
    print('The shortest path is', shortest_path, 'step long.')

    # Challenge Answer 2
    print('The furthest from the centre reached was', furthest, 'steps away.')


with open('input.txt') as f:
    steps_string = f.read()
    path(steps_string)
