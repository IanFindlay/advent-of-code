"""Advent of Code 2019 Day 16 - Flawed Frequency Transmission."""


def fft_phase(numbers, offset=0):
    """Perform a phase of flawed frequency transmission."""
    output = [0 for __ in numbers]

    if offset > len(numbers) // 2:
        num_sum = sum(numbers[offset:])
        for n in range(offset, len(numbers)):
            output[n] = num_sum % 10
            num_sum -= numbers[n]
    else:
        for i, __ in enumerate(numbers, offset):
            repeat = i + 1
            pattern_value = 1
            for n in range(repeat - 1, len(numbers), repeat * 2):
                output[i] += sum(numbers[n: n + repeat]) * pattern_value
                if pattern_value == 1:
                    pattern_value = -1
                else:
                    pattern_value = 1

            output[i] = abs(output[i]) % 10

    return output


with open('input.txt') as f:
    input_list = [int(x) for x in list(f.read().strip())]

num_list = input_list.copy()
for _ in range(100):
    num_list = fft_phase(num_list)

# Answer One
last_eight = ''.join([str(n) for n in num_list[:8]])
print("Last eight digits after 100 rounds:", last_eight)

offset = int("".join([str(n) for n in input_list[:7]]))

num_list = input_list.copy() * 10000
for __ in range(100):
    num_list = fft_phase(num_list, offset)

# Answer Two
message = ''.join([str(n) for n in num_list[offset: offset + 8]])
print("Eight digit embedded message:", message)
