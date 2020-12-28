""" Advent of Code Day 6 - Signals and Noise"""


with open('inputs/day_06.txt', 'r') as f:
    rows = [row.strip() for row in f.readlines()]

flipped = zip(*rows)

message = ''
mod_message = ''
for chars in flipped:
    most_freq = ''
    least_freq = ''
    highest = 0
    lowest = 100
    for char in chars:
        if chars.count(char) > highest:
            highest = chars.count(char)
            most_freq = char
        if chars.count(char) < lowest:   # Part Two
            lowest = chars.count(char)
            least_freq = char
    message += most_freq
    mod_message += least_freq

# Answer One
print("Error Corrected Message:", message)

# Answer Two
print("Modified Message:", mod_message)
