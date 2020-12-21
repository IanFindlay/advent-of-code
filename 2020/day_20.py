#!/usr/bin/env python3

"""Advent of Code 2020 Day 20 - Jurassic Jigsaw."""


from math import isqrt


class image_tile:
    """."""

    def __init__(self, id_num, tile):
        """."""
        self.id_num = id_num
        self.tile = tile
        self.patterns = generate_patterns(tile)

        self.pattern_to_edges = self.map_pattern_to_edges()

    def map_pattern_to_edges(self):
        """."""
        pattern_to_edges = {}
        for index, pattern in enumerate(self.patterns):
            top = pattern[0]
            right = [row[-1] for row in pattern]
            bottom = pattern[-1]
            left = [row[0] for row in pattern]
            pattern_to_edges[index] = {'top': top, 'right': right,
                                       'bot': bottom, 'left': left
            }

        return pattern_to_edges


def generate_patterns(pattern):
    """."""
    patterns = [pattern]
    new_patterns = []
    flipped_patterns = pattern_flips(pattern)
    for pattern in flipped_patterns:
        new_patterns.extend(pattern_rotations(pattern))
        new_patterns.extend([pattern])

    for pattern in new_patterns:
        if pattern not in patterns:
            patterns.append(pattern)

    return patterns


def pattern_flips(pattern):
    """."""
    horizontal = pattern[::-1]
    vertical = [row[::-1] for row in pattern if row]
    both = [row[::-1] for row in pattern[::-1] if row]

    return [horizontal] + [vertical] + [both]


def pattern_rotations(pattern):
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

        if len(used_tiles) == len(tiles):
            return image

        current_index = len(used_tiles)
        x, y = divmod(current_index, size)

        above_pattern = None
        left_pattern = None

        if x != 0:
            above_tile, index = image[current_index - size]
            above_pattern = above_tile.pattern_to_edges[index]['bot']

        if y != 0:
            left_tile, index = image[current_index - 1]
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


def remove_border(pattern):
    """."""
    pattern = pattern[1:-1]
    trimmed_pattern = []
    for row in pattern:
        trimmed_pattern.append(row[1:-1])

    return trimmed_pattern


def find_all_monsters(seas):
    """."""
    # Using leftmost part of monster, come up with coords relative to it
    mon_coords = [(1, 1), (1, 4), (0, 5), (0, 6), (1, 7),
                  (1, 10), (0, 11), (0, 12), (1, 13), (1, 16),
                  (0, 17), (0, 18), (-1, 18), (0, 19)
    ]
    monsters = 0
    num_hashes = 0
    for x, row in enumerate(seas):
        for y, char in enumerate(row):
            if char == '#':
                if check_for_monster(x, y, mon_coords, seas):
                    monsters += 1
                num_hashes += 1
    if monsters:
        return (num_hashes, monsters)


def check_for_monster(x, y, mon_coords, seas):
    """."""
    for coord in mon_coords:
        check_x, check_y = (x + coord[0], y + coord[1])
        try:
            if seas[check_x][check_y] != '#':
                return False
        except IndexError:
            return False

    return True

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

final_image = []
for tile in reassembled_image:
    image_tile, pattern_index = tile
    pattern = image_tile.patterns[pattern_index]
    borderless = remove_border(pattern)
    final_image.append(borderless)

joined_image = []
index = 0
while index < size**2:
    for i in range(len(borderless[0])):
        row = []
        for j in range(size):
            row.extend(final_image[j + index][i])
        joined_image.append(row)
    index += size

joined_image_patterns = generate_patterns(joined_image)
for sea in joined_image_patterns:
    monsters_found = find_all_monsters(sea)
    if monsters_found:
        break

num_hashes, num_monsters = monsters_found

# Answer Two
print("Water roughness:", num_hashes - (num_monsters * 15))
