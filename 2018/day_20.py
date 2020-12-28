"""Advent of Code Day 20 - A Regular Map"""


def cardinal_moves(coords, char, facility):
    """Process basic cardinal moves and update facility."""
    x, y = coords
    if char == 'N':
        facility[(x, y-1)] = '-'
        facility[(x, y-2)] = '.'
        new_coords = (x, y-2)

    elif char == 'E':
        facility[(x+1, y)] = '|'
        facility[(x+2, y)] = '.'
        new_coords = (x+2, y)

    elif char == 'S':
        facility[(x, y+1)] = '-'
        facility[(x, y+2)] = '.'
        new_coords = (x, y+2)

    elif char == 'W':
        facility[(x-1, y)] = '|'
        facility[(x-2, y)] = '.'
        new_coords = (x-2, y)

    return new_coords


def main():
    """Generate facility through regex, tracking distance to each room."""
    with open('inputs/day_20.txt') as f:
        regex = f.read().strip()

    coords = (0, 0)
    facility = {coords: 'X'}
    sections = []
    distances = {}
    distance = 0
    for char in regex[1:-1]:

        if char in ('N', 'E', 'S', 'W'):
            coords = cardinal_moves(coords, char, facility)
            distance += 1

            current_distance = distances.get(coords, 1000000)
            if current_distance > distance:
                distances[coords] = distance

        elif char == '(':
            sections.append(coords)

        elif char == '|':
            coords = sections[-1]
            distance = distances[coords]

        elif char == ')':
            sections.pop()


    # Answer One
    print("Doors to furthest:", max(distances.values()))

    # Answer Two len
    over_1000 = len([x for x in distances.values() if x >= 1000])
    print("Rooms 1000 doors away:", over_1000)


if __name__ == '__main__':
    main()
