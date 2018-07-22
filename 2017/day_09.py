"""Advent of Code Day 9 - Stream Processing"""


def clean(stream):
    """Filter garbage and find total 'score' of all group in a given input."""
    # Open input file
    stream = stream.read()

    # Set up logic for moving through text and evaluating situation
    total = 0
    cleaned = 0
    skip = False
    level = 0
    garbage = False

    for character in stream:
        # If currently within a garbage phase i.e. < previously reached
        if garbage:
            if skip:
                skip = False

            elif character == '!':
                skip = True

            elif character == '>':
                garbage = False

            else:
                cleaned += 1

        # Not in garbage phase so looking for depth of groups
        else:
            if character == '{':
                level += 1

            elif character == '}':
                total += level
                level -= 1

            elif character == '<':
                garbage = True

    print('Answer One:', total)
    print('Answer Two:', cleaned)


with open('input.txt') as f:
    stream = f.read()
    clean(stream)
