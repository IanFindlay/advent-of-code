#!/usr/bin/env python3

"""Advent of Code 2021 Day 20 - Trench Map"""


with open('../inputs/day_20.txt', 'r') as aoc_input:
    algo, image = [x.strip() for x in aoc_input.read().split('\n\n')]

def print_image(image_dict):
    min_x, max_x, min_y, max_y = get_image_ranges(image_dict)
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            row += image_dict.get((x, y), '.')
        print(row)
    print()

    lit = [1 for x in image_dict.values() if x == '#']
    print("Number of lit:", sum(lit))


def get_image_ranges(image_dict):
    x_values = sorted([coords[0] for coords in image_dict.keys()])
    y_values = sorted([coords[1] for coords in image_dict.keys()])
    min_x, max_x = x_values[0] - 1, x_values[-1] + 1
    min_y, max_y = y_values[0] - 1, y_values[-1] + 1

    return (min_x, max_x, min_y, max_y)

image_coords = {}
for row_num, row in enumerate(image.split('\n')):
    for col_num, value in enumerate(row):
        if value == '#':
            image_coords[(col_num, row_num)] = value

print_image(image_coords)
input()

for _ in range(2):
    min_x, max_x, min_y, max_y = get_image_ranges(image_coords)

    new_image = {}
    for y in range(min_y, max_y + 1):

        for x in range(min_x, max_x + 1):

            pixels = [
                    (x - 1, y - 1), (x, y - 1 ), (x + 1, y - 1),
                    (x - 1, y), (x, y), (x + 1, y),
                    (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            ]

            binary = ''
            for pixel in pixels:
                value = image_coords.get(pixel, '.')
                binary += '1' if value == '#' else '0'

            new_value = algo[int(binary, 2)]
            new_image[(x, y)] = new_value

    print_image(new_image)
    input()

    image_coords = new_image

lit = [1 for x in image_coords.values() if x == '#']
# Answer One

print("Number of pixels lit in resulting image:", sum(lit))

# 5469 too high
