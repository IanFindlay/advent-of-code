""" Advent of Code Day 13 - A Maze of Twisty Little Cubicles"""

import collections


def build_maze(rows, columns, fav_num):
    """Calculate, contruct and return a dictionary of the cubicle maze."""
    locations = {}
    for y in range(rows):
        for x in range(columns):

            bined = bin(x*x + 3*x + 2*x*y + y + y*y + fav_num)
            if bined.count('1') % 2 == 0:
                locations[x,y] = '.'
            else:
                locations[x,y] = '#'

    return locations


def possible_moves(node):
    """Given a location return all of the possible adjacent moves."""
    x = node[0]
    y = node[1]
    adjacent = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    possible = []
    for cubicle in adjacent:
        if cubicle in locations and locations[cubicle] == '.':
            possible.append(cubicle)
    return possible


def main(root, target, part_two=False):
    """Orchestrate the BFS returning steps taken when target is reached."""
    prev = set()
    prev.add(root)

    to_process = collections.deque(possible_moves(root))
    [prev.add(node) for node in to_process]

    steps = 1

    while True:
        children = []
        while to_process:
            [children.append(child) for child in possible_moves(to_process.pop())
                if child not in prev]

        steps += 1

        for child in children:
            if child == target and not part_two:
                return steps

            prev.add(child)

        if part_two and steps == 50:
            return len(prev)

        to_process = collections.deque(children)


if __name__ == '__main__':

    locations = build_maze(40, 35, 1362)
    # Answer One
    print("Least number of steps to get to target:", main((1, 1), (31, 39)))

    # Answer Two
    print("Number of unique locations visited after 50 steps:",
           main((1, 1), (31, 39), part_two=True ))
