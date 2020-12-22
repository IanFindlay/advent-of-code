"""Advent of Code Day 8 - Matchsticks"""


def literal_memory(lines):
    literal = 0
    memory = 0
    for line in lines:
        # Remove outer "
        line = line.strip()[1:-1]
        literal += len(line) + 2
        line_memory = 0

        i = 0
        while i < len(line):
            line_memory += 1
            # Skip over the escaped characters by the appropriate number
            if line[i] == '\\':
                if line[i + 1] == 'x':
                    i += 4
                else:
                    i += 2
            else:
                i += 1

        memory += line_memory

    return literal - memory


def encoded_literal(lines):
    literal = 0
    encoded = 0
    for line in lines:
        literal += len(line)

        # Starts at 2 due to the outer " needed to be encoded
        line_encoded = 2
        for character in line:
            if character in ('\\', '"'):
                line_encoded += 2
            else:
                line_encoded += 1

        encoded += line_encoded

    return encoded - literal


with open('inputs/day_08.txt') as f:
    lines_list = f.readlines()

# Answer One
print("Answer One =", literal_memory(lines_list))

# Answer Two
print("Answer Two =", encoded_literal(lines_list))
