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

        self.pattern_to_edges = self.map_pattern_to_edges()

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
            pattern_to_edges[index] = {'top': top, 'right': right,
                                       'bot': bottom, 'left': left
            }

        return pattern_to_edges


def generate_image_dfs(tiles):
    """."""
    size = isqrt(len(tiles))
    image = []
    for _ in range(size**2):
        image.append([])

    stack = []
    for tile in tiles:
        for index, _ in enumerate(tile.patterns):
            image_copy = image.copy()
            image_copy[0] = (tile, index)
            stack.append((image_copy, set([tile])))

    while stack:
        image, used_tiles = stack.pop()

        current_index = len(used_tiles)
        x, y = divmod(current_index, size)

        above_pattern = None
        left_pattern = None

        if x != 0:
            above_tile, index = image[current_index - size]
            if above_tile:
                above_pattern = above_tile.pattern_to_edges[index]['bot']

        if y != 0:
            left_tile, index = image[current_index - 1]
            if left_tile:
                left_pattern = left_tile.pattern_to_edges[index]['right']

        for tile in tiles:
            if tile in used_tiles:
                continue

            for index, _ in enumerate(tile.patterns):

                if above_pattern:
                    if tile.pattern_to_edges[index]['top'] != above_pattern:
                        continue

                if left_pattern:
                    if tile.pattern_to_edges[index]['left'] != left_pattern:
                        continue

                image[current_index] = (tile, index)
                used_tiles.add(tile)
                stack.append((image.copy(), used_tiles))

                if x == size - 1 and y == size - 1:
                    return image




#with open('input.txt') as f:
with open('inputs/2020_20.txt') as f:
    raw_tiles = f.read().split('\n\n')

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

size = isqrt(len(tiles))
reassembled_image = generate_image_dfs(tiles)
corners = [0, -1, 0 + size - 1, (len(tiles) -1) - (size - 1)]
corners_product = 1
for corner in corners:
    corners_product *= reassembled_image[corner][0].id_num

# Answer One
print("Product of corner ids of reassembled_image", corners_product)
