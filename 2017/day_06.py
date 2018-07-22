"""Advent of Code Day 6 - Memory Reallocation"""


def mem_stats(num_list, cycle_count=None):
    """Return how many redistribution cycles occur before an infinite loop."""
    # Split into list of memory banks and save config for uniqueness check
    current = num_list.split()
    current = [int(x) for x in current]
    configs = []
    configs.append(tuple(current))

    finite = True
    while finite is True:
        # Find the bank with the most blocks in it
        highest = 0
        for bank in current:
            if bank > highest:
                highest = bank
                position = current.index(bank)

        # Redistribute the blocks to all memory banks
        current[position] = 0
        while highest > 0:
            if position < len(current) - 1:
                current[position + 1] = current[position + 1] + 1

            else:
                current[0] = int(current[0]) + 1
                position = -1

            highest -= 1
            position += 1

        # If current not in configs list return pertient value
        if tuple(current) in configs:
            finite = False
            if cycle_count is None:
                return 'Cycles until infinite loop: ' + str(len(configs))
            else:
                return ('Loops between repetitions: '
                        + str(len(configs) - configs.index(tuple(current))))

        else:
            configs.append(tuple(current))


PUZZLE_INPUT = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'

# Answer One
print("Number of redistribution cycles:", mem_stats(PUZZLE_INPUT))

# Answer Two
print("Number of loops between repetitions:", mem_stats(PUZZLE_INPUT, cycle_count='yes'))
