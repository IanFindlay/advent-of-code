"""Advent of Code Day 2 - No Matter How You Slice It"""

import re


def coordinate_cloth(side_length):
    """Create a coordinate dictionary representing cloth of specified size."""
    cloth = {}
    row = 0
    while row < side_length:
        col = 0
        while col < side_length:
            cloth[(row, col)] = set()
            col += 1
        row += 1

    return cloth


def map_claims(claims, cloth):
    """Map ids to their claims on the cloth's coordinates."""
    claim_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    for claim in claims:
        info = re.match(claim_regex, claim)
        id_num = int(info.group(1))
        start_col, start_row = int(info.group(2)), int(info.group(3))
        width, height = int(info.group(4)), int(info.group(5))

        row = start_row
        while row < start_row + height:
            col = start_col
            while col < start_col + width:
                cloth[row, col].add(id_num)
                col += 1
            row += 1


def overlaps_and_intact(mapped_cloth):
    """Take mapped cloth return No. of overlaps and fully intact claim id."""
    ids, unintact_ids = set(), set()
    overlapped = 0
    for value in mapped_cloth.values():
        if len(value) > 1:
            ids.update(value)
            unintact_ids.update(value)
            overlapped += 1
        else:
            ids.update(value)

    intact = (ids - unintact_ids).pop()
    return (overlapped, intact)


if __name__ == '__main__':

    cloth = coordinate_cloth(1000)

    with open('input.txt') as f:
        claims = f.readlines()

    map_claims(claims, cloth)
    overlapped, intact = overlaps_and_intact(cloth)

    # Answer One
    print("Number of overlapping sections:", overlapped)

    # Answer Two
    print("Intact area id:", intact)
