"""Advent of Code Day 6 - Chronal Coordinates"""

import collections


def largest_bounded(max_side, area_origins):
    """Return size of the largest bounded area."""
    infinite_areas = set()
    area_sizes = collections.defaultdict(int)
    for row in range(max_side+1):
        for col in range(max_side+1):
            closest = closest_origin((row, col), area_origins)
            if closest:
                area_sizes[closest] += 1

                if row in (0, max_side) or col in (0, max_side):
                    infinite_areas.add(closest)

    for infinite_area in infinite_areas:
        del area_sizes[infinite_area]

    return max(area_sizes.values())


def closest_origin(coord, area_origins):
    """Return closest area origin to coord based on Manhattan Distance."""
    closest, min_distance = None, 10000
    for origin in area_origins:
        distance = abs(coord[0] - origin[0]) + abs(coord[1] - origin[1])
        if distance < min_distance:
            closest, min_distance = area_origins[origin], distance
            shared = False

        elif distance == min_distance:
            shared = True

    return False if shared else closest


def all_close(max_side, area_origins, limit):
    """Return region size where distance sum of point from origins < limit."""
    close_region_size = 0
    for row in range(max_side+1):
        for col in range(max_side+1):
            distance = limit
            for origin in area_origins:
                distance -= abs(row - origin[0]) + abs(col - origin[1])
                if distance <= 0:
                    distance = False
                    break

            if distance:
                close_region_size += 1

    return close_region_size


if __name__ == '__main__':

    with open('inputs/day_06.txt') as f:
        coordinates = f.readlines()

    # Build origins dict and find required side length to capture all origins
    area_origins = {}
    max_side = 0
    for num, coord in enumerate(coordinates):
        col, row = [int(x) for x in coord.split(',')]
        furthest = max(col, row)
        if furthest > max_side:
            max_side = furthest

        area_origins[(row, col)] = str(num)

    # Answer One
    print("Size of largest area:", largest_bounded(max_side, area_origins))

    # Answer Two
    print("Size of close region:", all_close(max_side, area_origins, 10000))
