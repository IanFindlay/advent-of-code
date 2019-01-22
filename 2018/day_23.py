"""Advent of Code Day 23 - Experimental Emergency Teleportation"""

import re


def parse_bots():
    """Return dictionary of Nanobots (coords mapped to radii)."""
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    nano_regex = re.compile(r'<(-?\d+),(-?\d+),(-?\d+)>,\s+r=(\d+)')
    nanobots = {}
    for line in lines:
        x, y, z, radius = [int(x) for x in nano_regex.search(line).groups()]
        nanobots[(x, y, z)] = radius

    return nanobots


def distance_between(coords_1, coords_2):
    """Return the distance between two coordinate tuples."""
    paired_coords = zip(coords_1, coords_2)
    return sum([abs(coord[0] - coord[1]) for coord in paired_coords])


def split_box(low, high):
    """Split box into octants (lowest_corner, highest_corner) and return."""
    half_length = (high[0] - low[0]) // 2
    centre = tuple([coord + half_length for coord in low])
    octants = [
        (centre, high),
        (low, centre),
        ((low[0], centre[1], low[2]), (centre[0], high[1], centre[2])),
        ((low[0], centre[1], centre[2]), (centre[0], high[1], high[2])),
        ((centre[0], centre[1], low[2]), (high[0], high[1], centre[2])),
        ((low[0], low[1], centre[2]), (centre[0], centre[1], high[2])),
        ((centre[0], low[1], low[2]), (high[0], centre[1], centre[2])),
        ((centre[0], low[1], centre[2]), (high[0], centre[1], high[2]))
    ]

    return octants


def bots_in_range(low, high, nanobots):
    """Return how many nanobots are in range of the box."""
    # Low of one box can be high of another - adjusted_high avoids this overlap
    adjusted_high = (high[0] - 1, high[1] - 1, high[2] - 1)
    in_range = 0
    for bot in nanobots.items():
        # If the bot is in box the distances between the bots coords and each
        # of the corners will sum to the distance between the corners
        coords, radius = bot
        dist_to_low = distance_between(coords, low)
        dist_to_high = distance_between(coords, adjusted_high)
        dist_low_high = distance_between(low, adjusted_high)

        if dist_low_high == dist_to_low + dist_to_high:
            in_range += 1
            continue

        # Check if radius brings bot into range - idea behind formula:
        # Nearest point on box from bot position satisfies, by definition of
        # being within the box, the condition used above.
        # Therefore, the distance to the nearest point can be found using
        # the bots distance to the corners minus the corner to corner distance
        # (as you only need the closest points distance).
        # This distance will be twice the answer due to using both corners.
        distance = (dist_to_low + dist_to_high - dist_low_high) // 2
        if radius >= distance:
            in_range += 1

    return in_range


def main():
    """Parse nanobots and explore the depth of coverage of the area."""
    nanobots = parse_bots()

    max_radius = 0
    coords_of_max = None
    for coords, radius in nanobots.items():
        if radius > max_radius:
            max_radius = radius
            coords_of_max = coords

    in_range_of_max = 0
    # Find how many nanobots are in range of bot with largest radius
    for nanobot in nanobots:
        distance = distance_between(coords_of_max, nanobot)
        if distance <= max_radius:
            in_range_of_max += 1

    # Answer One
    print("Nanobots in range:", in_range_of_max)

    # Find furthest coord that needs to be covered and then, for ease of
    # divisiblity, find the power of 2 length needed to reach it
    furthest_coord = 0
    for coords, radius in nanobots.items():
        high_abs = max([abs(coord) for coord in coords])
        if high_abs + radius > furthest_coord:
            furthest_coord = high_abs + radius

    half_side_length = 1
    while half_side_length <= furthest_coord:
        half_side_length *= 2
    side_length = half_side_length * 2

    # Coords of opposite corners are enough to define the boxes geometry
    low = (-half_side_length, -half_side_length, -half_side_length)
    high = (half_side_length, half_side_length, half_side_length)

    # Boxes: (bots in range, box size, -distance from origin, low, high)
    # Distance is negative so box closest to origin is popped in case of ties
    in_range = len(nanobots)
    initial_distance = -side_length * 3
    boxes = [(in_range, side_length, initial_distance, low, high)]

    while True:
        # Sort boxes by nanobots in range, size, distance from origin order
        boxes.sort(key=lambda box: (box[0], box[1], box[2]))
        __, size, distance_from_origin, low, high = boxes.pop()

        # If box size == 1 low corner is the answer as sorting ensures that
        # there is no larger box with the same or more bots in range and
        # any 1x1x1 bots with the same number of bots in range must be
        # further away from the origin
        if size == 1:
            distance_from_origin *= -1
            break

        # Split box into octants, calculate needed info for each and append
        oct_size = size // 2
        new_boxes = split_box(low, high)
        for octant in new_boxes:
            oct_low, oct_high = octant
            oct_in_range = bots_in_range(oct_low, oct_high, nanobots)
            oct_dist = -distance_between(oct_low, (0, 0, 0))
            boxes.append((oct_in_range, oct_size, oct_dist, oct_low, oct_high))

    # Answer Two
    print("Best covered point's distance from origin:", distance_from_origin)


if __name__ == '__main__':
    main()
