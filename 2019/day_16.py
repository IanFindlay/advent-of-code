"""Advent of Code 2019 Day 16 - Flawed Frequency Transmission."""


def fft_phase(numbers):
    """Perform a phase of flawed frequency transmission."""
    num_list_length = len(numbers)
    master_pattern = [0, 1, 0, -1]
    output = []
    for pos, __ in enumerate(numbers, 1):
        generating_pattern = True
        pattern = []
        while generating_pattern:
            for value in master_pattern:
                pattern += [value] * pos

                if len(pattern) > num_list_length:
                    generating_pattern = False
                    break

        pattern = pattern[1: num_list_length + 1]
        output.append(abs(sum([a * b for a, b in zip(numbers, pattern)])) % 10)

    return output


with open('input.txt') as f:
    num_list = [int(x) for x in list(f.read().strip())]

for _ in range(100):
    num_list = fft_phase(num_list)

# Answer One
print("Last eight digits after 100 rounds:",
      ''.join([str(x) for x in num_list[0:8]]))
