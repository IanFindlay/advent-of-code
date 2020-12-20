#!/usr/bin/env python3

"""Advent of Code 2020 Day 20 - Jurassic Jigsaw."""


from math import isqrt


class image_tile:
    """."""

    def __init__(self, id_num, tile):
        """."""
        self.id_num = id_num
        self.tile = tile
        self.patterns = self.generate_patterns()

        # Make dict of pattern: (top, right, bottom, left) edges
        pattern_edges = self.map_pattern_to_edges()

    def generate_patterns(self):
        """."""
        patterns = [self.tile]
        new_patterns = []
        flipped_patterns = self.pattern_flips()
        for pattern in flipped_patterns:
            new_patterns.extend(self.pattern_rotations(pattern))
            new_patterns.extend([pattern])

        for pattern in new_patterns:
            if pattern not in patterns:
                patterns.append(pattern)

        return patterns

    def pattern_flips(self):
        """."""
        horizontal = self.tile[::-1]
        vertical = [list(row[::-1]) for row in tile if row]
        both = [list(row[::-1]) for row in tile[::-1] if row]

        return [horizontal] + [vertical] + [both]

    def pattern_rotations(self, pattern):
        """."""
        rotated = []
        tile = pattern.copy()
        for _ in range(3):
            rotated_tile = zip(*tile[::-1])
            new_tile = []
            for tup in rotated_tile:
                new_tile.append(list(tup))
            rotated.append(new_tile)

        return rotated

    def map_pattern_to_edges(self):
        """."""
        pattern_to_edges = {}
        for index, pattern in enumerate(self.patterns):
            top = pattern[0]
            right = [row[0] for row in pattern]
            bottom = pattern[-1]
            left = [row[-1] for row in pattern]
            pattern_to_edges[index] = (top, right, bottom, left)

        return pattern_to_edges





with open('input.txt') as f:
#with open('inputs/2020_20.txt') as f:
    raw_tiles = f.read().split('\n\n')

size = isqrt(len(raw_tiles))
tiles = []
for tile in raw_tiles:
    tile = tile.split('\n')
    title = int(tile[0].strip("Tile ")[:-1])
    tile = [x for x in tile[1:] if x]
    split_tile = []
    for row in tile:
        split_row = []
        for char in row:
            split_row.append(char)
        split_tile.append(split_row)
    tiles.append(image_tile(title, split_tile))

for tile in tiles:
    print(len(tile.patterns))
