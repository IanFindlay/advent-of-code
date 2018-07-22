"""Advent of Code Day 24 - Air Duct Spelunking"""

import collections


def create_map():
    """Create a coordinate dictionary and find the origin and numbers to cross."""
    with open('input.txt') as f:
        data = [line.strip() for line in f.readlines()[1:-1]]

    layout = {}
    num_list = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            value = is_num(data[y][x])
            if type(value) is int:
                num_list.append(value)
            layout[(x, y)] = value
            if value == 0:
                origin = ((x, y), [0,])

    return (layout, origin, num_list)


def is_num(string):
    """Check if a string is a valid integer and if so return it as one."""
    try:
        int(string)
    except ValueError:
        return string
    return int(string)


def get_moves(state):
    """Given a location return all of the possible adjacent moves."""
    x = state[0][0]
    y = state[0][1]
    adjacent = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    moves = []

    for location in adjacent:
        nums = list(state[1])
        if location in locations and locations[location] != '#':
            if type(locations[location]) is int and locations[location] not in nums:
                nums.append(locations[location])
            moves.append((location, nums))
    return moves


def main(origin, num_list, part_two=False):
    """Run a BFS returning steps taken when target condition is reached."""
    prev_states = set()
    prev_states.add((origin[0], tuple(origin[1])))
    to_process = collections.deque(get_moves(origin))
    nums_crossed = False
    steps = 1
    while True:
        steps += 1
        layer = []
        while to_process:
            for state in get_moves(to_process.pop()):
                if set(state[1]) == set(num_list) and not part_two:
                    return steps

                if set(state[1]) == set(num_list) and part_two:
                    if not nums_crossed:
                        nums_crossed = True
                    elif nums_crossed and state[0] == origin[0]:
                        return (steps)

                to_check = (state[0], tuple(state[1]))
                if to_check not in prev_states:
                    prev_states.add(to_check)
                    layer.append(state)

        to_process = collections.deque(layer)


if __name__ == '__main__':

    info = create_map()
    locations = info[0]

    # Answer One
    print("Fewest steps to visit all numbers:", main(info[1], info[2]))

    # Answer Two
    print("Fewest steps to then return robot:", main(info[1], info[2], part_two=True))
