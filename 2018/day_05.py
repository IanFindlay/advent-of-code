"""Advent of Code Day 5 - Alchemical Reduction"""


def react_polymer(polymer):
    """Return polymer after all unit reactions have taken place."""
    prev_poly = None
    while prev_poly != polymer:
        prev_poly = polymer
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            upper = letter.upper()
            polymer = polymer.replace('{}{}'.format(letter, upper), '')
            polymer = polymer.replace('{}{}'.format(upper, letter), '')

    return polymer


if __name__ == '__main__':

    with open('inputs/day_05.txt') as f:
        polymer = f.read()

    reduced_polymer = react_polymer(polymer)
    reacted_length = len(reduced_polymer)

    # Answer One
    print("Length after reduction:", reacted_length)

    shortest = reacted_length
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        new_polymer = reduced_polymer.replace(letter, '')
        new_polymer = new_polymer.replace(letter.upper(), '')

        reacted_length = len(react_polymer(new_polymer))
        if reacted_length < shortest:
            shortest = reacted_length

    # Answer Two
    print("Shortest polymer:", shortest)
