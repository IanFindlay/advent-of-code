"""Advent of Code Day 10 - Knot Hash"""


def hashed(lengths):
    """Carry out a simulation of a knot tying hash given length inputs. """
    skip = 0
    pos = 0

    notches = list(range(256))

    for length in lengths:

        if length + pos < len(notches):
            notches[pos: pos + length] = reversed(notches[pos: pos + length])

        # For cases that span over the end of the knot range
        else:
            value = length
            to_reverse = []

            # Seperate affected notches into their own list
            for notch in notches[pos: pos + length]:
                to_reverse.append(notch)

            overlap = (pos + length) % len(notches)

            count = 0
            while overlap > 0:
                to_reverse.append(notches[count])
                count += 1
                overlap -= 1

            # Replace affected notches in 'notches' with 'reversed' ones
            count = 0
            while count + pos < len(notches):
                notches[pos + count] = to_reverse[-(count + 1)]
                count += 1
                value -= 1

            # End flip done
            count_2 = 0
            while value > 0:
                notches[0 + count_2] = to_reverse[-(count + 1)]
                count += 1
                count_2 += 1
                value -= 1

        pos = (pos + length + skip) % len(notches)
        skip += 1

    return notches[0] * notches[1]


PUZZLE_INPUT = [230, 1, 2, 221, 97, 252, 168, 169, 57, 99, 0, 254, 181,
                255, 235, 167]

# Answer One
print("Product of first two numbers in hash:", hashed(PUZZLE_INPUT))
