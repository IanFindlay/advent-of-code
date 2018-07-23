"""Advent of Code Day 12 - Digital Plumber"""

import re


def make_dict():
    """Create a dictionary of pipes and their connections."""
    with open('input.txt') as f:
        survey = [line for line in f.readlines()]
    pipes = {}
    for info in survey:
        pipe, *connections = re.findall(r'\d+', info)
        pipes[pipe] = connections

    return pipes


def find_groups(pipe_list, part_two=False):
    """Use connection information to form and count groups."""
    groups = 0
    while pipe_list:
        to_process = []
        to_process.append(pipe_list[0])
        members = set()
        while to_process:
            connects = pipes[to_process.pop()]
            for connect in connects:
                if connect not in members:
                    to_process.append(connect)
                    members.add(connect)

        if not part_two and '0' in members:
            return len(members)
        [pipe_list.remove(member) for member in members]
        groups += 1

    return groups


if __name__ == '__main__':

    pipes = make_dict()
    pipe_list = [pipe for pipe in pipes]

    # Answer One
    print("Number of programs in group containing 0:", find_groups(pipe_list))

    # Answer Two
    print("Number of groups:", find_groups(pipe_list, part_two=True))
