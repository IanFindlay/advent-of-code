#!/usr/bin/env python3

"""Advent of Code 2021 Day 20 - Trench Map"""


with open('inputs/day_20.txt', 'r') as aoc_input:
    algo, image = [x.strip() for x in aoc_input.read().split('\n\n')]

def print_image(image_coords):
    min_x, max_x, min_y, max_y = get_image_ranges(image_coords)
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            row += '#' if (x, y) in image_coords else '.'
        print(row)
    print()

    print("Number of lit:", len(image_coords))


def get_image_ranges(image_coords):
    x_values = sorted([coords[0] for coords in image_coords])
    y_values = sorted([coords[1] for coords in image_coords])
    min_x, max_x = x_values[0] - 1, x_values[-1] + 1
    min_y, max_y = y_values[0] - 1, y_values[-1] + 1

    return (min_x, max_x, min_y, max_y)


image_coords = set()
for row_num, row in enumerate(image.split('\n')):
    for col_num, value in enumerate(row):
        if value == '#':
            image_coords.add((col_num, row_num))

"""Actual input has algo[0] mapped to # so the infinite matters"""
explored = set()
for step in range(2):
    min_x, max_x, min_y, max_y = get_image_ranges(image_coords)

    new_image = set()
    for y in range(min_y, max_y + 1):

        for x in range(min_x, max_x + 1):

            if not step % 2:
                explored.add((x, y))

            pixels = [
                    (x - 1, y - 1), (x, y - 1 ), (x + 1, y - 1),
                    (x - 1, y), (x, y), (x + 1, y),
                    (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            ]

            binary = ''
            for pixel in pixels:
                if step % 2 and pixel not in explored:
                    binary += '1'
                else:
                    binary += '1' if pixel in image_coords else '0'

            new_value = algo[int(binary, 2)]
            if new_value == '#':
                new_image.add((x, y))

    image_coords = new_image

# Answer One
print("Number of pixels lit in resulting image:", len(image_coords))
