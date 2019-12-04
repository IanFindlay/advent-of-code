"""Advent of Code 2019 Day 4 - Secure Container."""


def number_matching_criteria(part_two=False):
    """Return number of numbers mathching criteria."""
    num_matched = 0
    for n in range(145852, 616943):
        digits = [int(x) for x in list(str(n))]
        adjacent = False
        increase = False
        if digits == sorted(digits):
            increase = True
        else:
            pass

        for digit in digits:
            if part_two:
                if digits.count(digit) == 2:
                    adjacent = True
                    break
            else:
                if digits.count(digit) > 1:
                    adjacent = True
                    break

        if adjacent and increase:
            num_matched += 1

    return num_matched


# Answer One
print("Matches under first criteria:", number_matching_criteria())

# Answer Two
print("Matches under second criteria:", number_matching_criteria(True))
