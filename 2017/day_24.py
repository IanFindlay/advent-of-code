"""Advent of Code Day 24 - Electromagnetic Moat"""


def extend(join, unused, strength, length):
    """Try to extend a bridge by adding an unused, matching part to it."""
    info.append((strength, length))
    for to_try in unused:
        if join in to_try:
            updated_unused = [part for part in unused if part != to_try]
            left, right = to_try
            if left == join:
                new_join = right
            else:
                new_join = left

            extend(new_join, updated_unused, strength + sum(to_try), length + 1)


def start_bridges(part_two=False):
    """Find all parts with a 0 connection to use as the start of a bridge."""
    for component in parts:
        if 0 in component:
            left, right = component
            unused = [part for part in parts if part != component]
            if left == 0:
                join = right
            else:
                join = left

            extend(join, unused, sum(component), 1)

    if not part_two:
        return max([strength[0] for strength in info])

    longest = max([length[1] for length in info])
    return max([strength[0] for strength in info if strength[1] == longest])


if __name__ == '__main__':

    with open('input.txt') as f:
        parts = [tuple(map(int, line.split("/"))) for line in f]

    info = []   # Keep track of bridge strengths and lengths

    # Answer One
    print("Strength of the strongest bridge:", start_bridges())

    # Answer Two
    print("Strength of the strongest of the longest:", start_bridges(part_two=True))
