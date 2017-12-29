"""Answers to Advent of Code Day 9."""


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
            if skip:           # If ! previously then skip this character
                skip = False

            elif character == '!':     # Turn on skip for !
                skip = True

            elif character == '>':     # End of garbage phase reached
                garbage = False

            else:                # Track other characters remove from garbage
                cleaned += 1

        # Not in garbage phase so looking for depth of groups
        else:
            if character == '{':       # Start of group - level increased
                level += 1

            elif character == '}':   # End of group so update total with level
                total += level
                level -= 1

            elif character == '<':       # Start of garbage phase reached
                garbage = True

    print('Challenge 1 Answer = ', total)
    print('Challenge 2 Answer = ', cleaned)


with open('input.txt') as f:
    STREAM = f.read()
    clean(STREAM)
