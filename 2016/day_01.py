""" Advent of Code Day 1 - No Time for a Taxicab"""


def grid_walk(directions, part_two=False):
    """Return Manhattan distance of destination or first revisited place."""
    x = 0
    y = 0
    orientation = 0
    visited = [[0, 0],]
    for direction in directions:
        turn = direction[0]
        steps = int(direction[1:])

        if turn == 'R':
            orientation = (orientation + 1) % 4
        else:
            orientation = (orientation - 1) % 4

        for _ in range(steps):

            if orientation == 0:
                y += 1
            elif orientation == 1:
                x += 1
            elif orientation == 2:
                y -= 1
            else:
                x -= 1

            if part_two:
                if [x, y] in visited:
                    return abs(x) + abs(y)
                else:
                    visited.append([x, y])

    return abs(x) + abs(y)


with open('inputs/day_01.txt') as f:
    instructions = f.read().split(', ')

# Answer Part One
print("Easter Bunny HQ is", grid_walk(instructions), "Blocks Away.")

# Answer Part Two
print("First Revisited House is", grid_walk(instructions, part_two=True), "Blocks Away.")
