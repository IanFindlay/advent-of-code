"""Advent of Code Day 10 - The Stars Align"""

import re


def stars_gathered(stars):
    """Return whether or not the stars are gathered together."""
    for point in stars:
        alone = True
        x, y = point
        close_to = [
            (x-1, y), (x+1, y), (x, y-1), (x, y+1),
            (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)
        ]
        for close in close_to:
            if (close[0], close[1]) in stars:
                alone = False
                break
        if alone:
            return False

    return True


def plot_stars(stars):
    """Return a table representation of the stars."""
    xs = sorted([position[0] for position in stars])
    ys = sorted([position[1] for position in stars])
    min_x, max_x = xs[0], xs[-1]
    min_y, max_y = ys[0], ys[-1]

    sky = []
    for y in range(min_y - 1, max_y + 2):
        row = []
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in stars:
                row.append('#')
            else:
                row.append('.')
        sky.append(''.join(row))

    return sky


if __name__ == '__main__':

    with open('input.txt') as f:
        lines = f.readlines()

    min_x, min_y = 0, 0
    point_regex = re.compile(r'<\s?(-?\d+),\s+?(-?\d+)>')
    positions = {}
    velocities = {}
    for index, line in enumerate(lines):
        position, velocity = point_regex.findall(line)
        x, y = int(position[0]), int(position[1])
        vel_x, vel_y = int(velocity[0]), int(velocity[1])
        positions[index] = (x, y)
        velocities[index] = (vel_x, vel_y)
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    # Adjust star coordinates relative to minimums
    for index, position in positions.items():
        x = position[0] + abs(min_x)
        y = position[1] + abs(min_y)
        positions[index] = (x, y)

    seconds = 0
    while True:
        stars = set(positions.values())
        if stars_gathered(stars):
            sky = plot_stars(stars)

            # Answer One
            for row in sky:
                print(row)

            # Just in case some inputs have false positive
            response = input("Message appeared? (y/n): ")
            if response.lower() in ('n', 'no'):
                continue

            # Answer Two
            print("Seconds until message:", seconds)
            break

        # Move stars
        for index, position in positions.items():
            x = position[0] + velocities[index][0]
            y = position[1] + velocities[index][1]
            positions[index] = (x, y)

        seconds += 1
