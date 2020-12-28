"""Advent of Code Day 21 - Fractal Art"""

import re


def build_dict():
    """Create dictionary version of enhancement book with rotated forms in."""
    with open('inputs/day_21.txt') as f:
        data = [line.strip() for line in f.readlines()]

    dictionary = {}

    for enhancement in data:
        in_rows, out_rows = enhancement.split('=')
        rows = re.findall(r'([#.]+)', in_rows)
        product = re.findall(r'([#.]+)', out_rows)

        # Original
        dictionary[tuple(rows)] = tuple(product)

        # Y-Flip
        dictionary[tuple([row[::-1] for row in rows])] = tuple(product)

        # X-Flip
        dictionary[tuple([row for row in rows[::-1]])] = tuple(product)

        # Rotations
        rows_90 = tuple(zip(*reversed(rows)))
        rows_180 = tuple(zip(*reversed(rows_90)))
        rows_270 = tuple(zip(*reversed(rows_180)))

        dictionary[tuple([''.join(row) for row in rows_90])] = tuple(product)
        dictionary[tuple([''.join(row) for row in rows_180])] = tuple(product)
        dictionary[tuple([''.join(row) for row in rows_270])] = tuple(product)

        # X-Flipped rotations
        dictionary[tuple([''.join(row) for row in rows_90[::-1]])] = tuple(product)
        dictionary[tuple([''.join(row) for row in rows_180[::-1]])] = tuple(product)
        dictionary[tuple([''.join(row) for row in rows_270[::-1]])] = tuple(product)

        # Y-flipped rotations
        dictionary[tuple([''.join(row[::-1]) for row in rows_90])] = tuple(product)
        dictionary[tuple([''.join(row[::-1]) for row in rows_180])] = tuple(product)
        dictionary[tuple([''.join(row[::-1]) for row in rows_270])] = tuple(product)

    return dictionary


def generate_art(iterations):
    """Iteratively partition, enhance (enchancements dict) and reform the picture."""
    picture = ('.#.', '..#', '###')

    for __ in range(iterations):

        if len(picture[0]) % 2 == 0:

            portions = []
            y = 0
            x = 0
            while y < len(picture) - 1:
                x = 0
                while x < len(picture[0]) - 1:
                    portion = []
                    portion.append("{}{}".format(picture[y][x], picture[y][x+1]))
                    portion.append("{}{}".format(picture[y+1][x], picture[y+1][x+1]))
                    portions.append(tuple(portion))
                    x += 2

                y += 2

            new = [enhancements[tuple(portion)] for portion in portions]

            reformed = []
            i = 0
            while i < len(new):
                row_0 = ''
                row_1 = ''
                row_2 = ''
                for j in range(len(picture[0]) // 2):
                    row_0 += new[j+i][0]
                    row_1 += new[j+i][1]
                    row_2 += new[j+i][2]

                reformed.append(row_0)
                reformed.append(row_1)
                reformed.append(row_2)

                i += len(picture) // 2

            picture = tuple(reformed)

        else:
            portions = []
            y = 0
            x = 0

            while y < len(picture) - 2:
                x = 0
                while x < len(picture[0]) - 2:
                    portion = []
                    portion.append("{}{}{}".format(picture[y][x], picture[y][x+1], picture[y][x+2]))
                    portion.append("{}{}{}".format(picture[y+1][x], picture[y+1][x+1], picture[y+1][x+2]))
                    portion.append("{}{}{}".format(picture[y+2][x], picture[y+2][x+1], picture[y+2][x+2]))
                    portions.append(tuple(portion))

                    x += 3

                y += 3

            new = [enhancements[tuple(portion)] for portion in portions]

            reformed = []
            i = 0
            while i < len(new):
                row_0 = ''
                row_1 = ''
                row_2 = ''
                row_3 = ''
                for j in range(len(picture[0]) // 3):
                    row_0 += new[j+i][0]
                    row_1 += new[j+i][1]
                    row_2 += new[j+i][2]
                    row_3 += new[j+i][3]

                reformed.append(row_0)
                reformed.append(row_1)
                reformed.append(row_2)
                reformed.append(row_3)

                i += len(picture) // 3

            picture = tuple(reformed)

    return ''.join(picture).count('#')


if __name__ == '__main__':

    enhancements = build_dict()

    # Answer One
    print("Pixels on after five iterations:", generate_art(5))

    # Answer Two
    print("Pixels on after eighteen iterations:", generate_art(18))
