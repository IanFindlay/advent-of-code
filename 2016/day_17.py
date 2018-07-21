"""Advent of Code Day 17 - Two Steps Forward"""

import hashlib
import collections


def make_layout(rows, columns):
    """Create a layout of rooms represented by a set of coordinates."""
    locations = set()
    for y in range(rows):
        for x in range(columns):
            locations.add((x, y))

    return locations


def find_open(room, seed, prev):
    """Find all open doors in room and return paths not previously traversed."""
    hexed = hashlib.md5('{}'.format(seed).encode('utf-8')).hexdigest()[:5]
    opened = []
    open_indicators = 'bcdef'

    if hexed[0] in open_indicators:
        opened.append(((room[0], room[1] - 1), seed + 'U'))

    if hexed[1] in open_indicators:
        opened.append(((room[0], room[1] + 1), seed + 'D'))

    if hexed[2] in open_indicators:
        opened.append(((room[0] - 1, room[1]), seed + 'L'))

    if hexed[3] in open_indicators:
        opened.append(((room[0] + 1, room[1]), seed + 'R'))

    return [door for door in opened if door[0] in rooms and door[1] not in prev]


def main(passcode, part_two=False):
    """Orchestrate DFS returning shortest route or longest if part two."""
    origin = (0, 0)
    target = (3, 3)
    routes = set()
    prev_paths = set()
    next_info = find_open(origin, passcode, ())

    to_process = collections.deque()
    while True:
        [to_process.append(info) for info in next_info]
        if to_process:
            info = to_process.pop()
            next_node = info[0]
            path = info[1]
            prev_paths.add(path)
            if next_node == target:
                routes.add(info[1].strip(passcode))
                next_info = []
                continue
            next_info = find_open(next_node, path, prev_paths)
        else:
            if not part_two:
                return min(routes, key=len)
            return len(max(routes, key=len))


if __name__ == '__main__':

    rooms = make_layout(4, 4)

    # Answer One
    print("Shortest path:", main('dmypynyp'))

    # Answer Two
    print("Length of longest path:", main('dmypynyp', part_two=True))
