#!/usr/bin/env python3

"""Advent of Code 2021 Day 23 - Amphipod"""


with open('inputs/day_23.txt', 'r') as aoc_input:
    lines = [line.strip('\n') for line in aoc_input.readlines()]

open_space = set()
walls = set()
rooms = []
amphipods = {'A': [], 'B': [], 'C': [], 'D': []}
for y, line in enumerate(lines):
    for x, value in enumerate(line):
        if value == '#':
            walls.add((x, y))
            continue
        if value in ('A', 'B', 'C', 'D'):
            rooms.append((x, y))
            amphipods[value].append((x, y))
        else:
            open_space.add((x, y))

rooms.sort()

target_rooms = {
        'A': (rooms[0], rooms[1]), 'B': (rooms[2], rooms[3]),
        'C': (rooms[4], rooms[5]), 'D': (rooms[6], rooms[7])
}

rooms_set = set(rooms)

doorways = set()
for room in target_rooms.values():
    x, y = room[0]
    doorways.add((x, y - 1))

# Form 9 d tuple representing initial state
initial_state = []
for kind in ('A', 'B', 'C', 'D'):
    sorted_coords = sorted(amphipods[kind])
    initial_state.extend(sorted_coords)

initial_state = tuple(initial_state)

index_to_kind = {
        0: 'A', 1: 'A', 2: 'B', 3:'B',
        4: 'C', 5: 'C', 6: 'D', 7: 'D'
}

def calculate_cost(start, end, kind):
    energy_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    x, y = start
    other_x, other_y = end
    distance = abs(x - other_x) + abs(y - other_y)

    return distance * energy_cost[kind]


def print_state(state, lines):
    for y in range(len(lines)):
        row = ''
        for x in range(len(lines[0])):
            coords = (x, y)
            if coords in state:
                row += index_to_kind[state.index(coords)]
            elif coords in open_space or coords in rooms:
                row += '.'
            else:
                row += '#'
        print(row)
    print()


def path_to_target(state, start, end):
    visited = set()
    visited.add(start)
    moves = [start]
    while moves:
        x, y = moves.pop()
        for move in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if move in visited:
                continue
            if move in state:
                continue
            if move == end:
                return True
            if move in walls:
                continue
            visited.add(move)
            moves.append(move)

    return False


lowest_energy = None
states_seen = {initial_state: 0}
stack = [[initial_state, 0]]
counter = 0
while stack:

    state, cost = stack.pop()

    if lowest_energy and cost > lowest_energy:
        continue

    # Check if completed
    completed = True
    for num, amphipod in enumerate(state):
        targets = target_rooms[index_to_kind[num]]
        if amphipod not in targets:
            completed = False
            break

    if completed:
        if not lowest_energy or cost < lowest_energy:
            lowest_energy = cost
            continue

    for num, amphipod in enumerate(state):

        kind = index_to_kind[num]

        # Already finished
        if amphipod == target_rooms[kind][1]:
            continue
        if amphipod == target_rooms[kind][0]:
            if index_to_kind[state.index(target_rooms[kind][1])] == kind:
                continue

        moves = []
        # Already in open_space so only final position
        if amphipod in open_space:

            open_slot = None
            # Check lowest coord as that is preferential
            if target_rooms[kind][1] not in state:
                open_slot = target_rooms[kind][1]
            elif target_rooms[kind][0] not in state:
                occupier = state.index(target_rooms[kind][1])
                if index_to_kind[occupier] == kind:
                    open_slot = target_rooms[kind][0]

            if open_slot:
                if not path_to_target(state, amphipod, open_slot):
                    continue
                else:
                    moves.append(open_slot)

        else:

            for space in open_space:

                if space in state or space in doorways:
                    continue

                if not path_to_target(state, amphipod, space):
                    continue

                moves.append(space)

        if not moves:
            continue

        # Make moves
        for move in moves:
            state_copy = list(state)
            state_copy[num] = move
            state_copy = tuple(state_copy)

            new_cost = cost + calculate_cost(amphipod, move, kind)

            check_new = states_seen.get(state_copy, False)
            if check_new and check_new <= new_cost:
                continue

            states_seen[state_copy] = new_cost
            stack.append([state_copy, new_cost])

    stack.sort(key=lambda x: x[1])
    counter += 1

# Answer One
print(f'Least energy required to organise the amphipods: {lowest_energy}')
