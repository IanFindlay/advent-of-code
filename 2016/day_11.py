""" Advent of Code Day 11 - Radioisotope Thermoelectric Generators"""

import re
import itertools


def main(part_two=False):
    """Orchestrate the BFS search."""
    with open('inputs/day_11.txt') as f:
        info = [line.strip() for line in f]

    # Initialise starting node
    prev_states = set()
    floors = set_initial(info)
    if part_two:
        [floors[0].append(item) for item in ('eg', 'em', 'dg', 'dm')]

    e = 0
    prev_states.add(make_tuple(floors, e))

    # Find first generation of children then enter do_level/get_next loop
    to_process = get_next(floors, e)
    steps = 0
    while True:
        children = do_level(to_process, prev_states)
        steps += 1

        if not children:
            return steps

        to_process = []
        for child in children:
            [to_process.append(move) for move in get_next(child[0], child[1])]


def set_initial(layout):
    """Process given layout info and generate a representative list."""
    micro_regex = re.compile(r'a (\w)\w+-compatible microchip')
    gen_regex = re.compile(r'a (\w)\w+ generator')
    floors = []
    for floor in layout:
        chips = micro_regex.findall(floor)
        gens = gen_regex.findall(floor)
        floor_items = []
        [floor_items.append(chip + 'm') for chip in chips]
        [floor_items.append(gen + 'g') for gen in gens]
        floors.append(floor_items)

    return floors


def make_tuple(floor_list, elevator):
    """Takes a list and returns a generalised (no element) tuple version."""
    generalised = []
    for floor in floor_list:
        items = tuple([item[1] for item in floor])
        generalised.append(items)

    return tuple(generalised)


def get_next(state, curr_floor):
    """Find all possible moves for a given state."""
    next_moves = []
    for chosen in state[curr_floor]:
        pot_moves = item_moves(state, chosen, curr_floor)
        if pot_moves:
            [next_moves.append((state, chosen, curr_floor, move)) for move in pot_moves]

    combos = itertools.combinations(state[curr_floor], 2)
    for combo in combos:
        pot_moves = item_moves(state, combo, curr_floor, multi_items=True)
        if pot_moves:
            [next_moves.append((state, [combo[0], combo[1]], curr_floor, move))
                for move in pot_moves]

    return next_moves


def item_moves(state, chosen, origin, multi_items=False):
    """Return a list of floors adjacent to origin a given item/s could move to."""
    valid = []
    remaining = [item for item in state[origin] if item != chosen]

    if not check_fried(remaining):
        return False

    if origin != len(state) -1:
        floor_up = list(state[origin + 1])
        if multi_items:
            floor_up.append(chosen[0])
            floor_up.append(chosen[1])
        else:
            floor_up.append(chosen)
        if check_fried(floor_up):
            valid.append(origin + 1)

    if origin != 0:
        floor_down = list(state[origin - 1])
        if multi_items:
            floor_down.append(chosen[0])
            floor_down.append(chosen[1])
        else:
            floor_down.append(chosen)
        if check_fried(floor_down):
            valid.append(origin - 1)

    if valid:
        return valid


def check_fried(floor_items):
    """Check if an item combination results in frying, if not return True."""
    chips = []
    gens = []
    for item in floor_items:
        if item.endswith('m'):
            chips.append(item)
        else:
            gens.append(item)

    if gens:
        for chip in chips:
            partner = "{}g".format(chip[0])
            if partner not in gens:
                return False

    return True


def do_level(variations, prev_states):
    """Carry out variations, test state is unique, update previous."""
    to_try = variations
    children = []
    while to_try:
        # Parse variations and do them
        to_do = to_try.pop()
        mod_state = [list(floor) for floor in to_do[0]]

        chosen = to_do[1]
        ele_pos = to_do[2]
        move_to = to_do[3]

        if type(chosen) == list:
            for item in chosen:
                mod_state[ele_pos].remove(item)
                mod_state[move_to].append(item)

        else:
            mod_state[ele_pos].remove(chosen)
            mod_state[move_to].append(chosen)

        # Check for all items on level 3 solved condition
        if not mod_state[0] and not mod_state[1] and not mod_state[2]:
            return False

        # Format new state, check against previous and if unique add to previous
        curr_mod = make_tuple(mod_state, ele_pos)
        if curr_mod in prev_states:
            continue

        prev_states.add(curr_mod)
        children.append((mod_state, move_to))

    return children


if __name__ == '__main__':
    # Answer One
    print("Minimum steps:", main())

    # Answer Two
    print("Minimum steps with Additional Items:", main(part_two=True))
