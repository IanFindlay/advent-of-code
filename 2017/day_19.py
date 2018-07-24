"""Advent of Code Day 19 - A Series of Tubes"""


def traverse_maze(network, part_two=False):
    """Traverse the maze collecting letters and counting the steps taken."""
    x = network[0].index('|')
    y = 0
    direction = 'D'
    letters = []
    steps = 0
    while network[y][x] != ' ':
        if direction == 'D':
            y += 1
        elif direction == 'U':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1

        if network[y][x] == '+':
            if direction in ('L', 'R'):
                if y != len(network) - 1 and network[y+1][x] != ' ':
                    direction = 'D'
                else:
                    direction = 'U'
            else:
                if x != len(network[0]) - 1 and network[y][x+1] != ' ':
                    direction = 'R'
                else:
                    direction = 'L'

        elif network[y][x].isalpha():
            letters.append(network[y][x])

        steps += 1

    if not part_two:
        return ''.join(letters)

    return steps


if __name__ == '__main__':

    with open('input.txt') as f:
        network = [line.strip('\n') for line in f.readlines()]

    # Answer One
    print("Letters along the path:", traverse_maze(network))

    # Answer Two
    print("Length of the path:", traverse_maze(network, part_two=True))
