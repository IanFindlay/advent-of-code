"""Advent of Code Day 12 - Subterranean Sustainability"""


def generations(pots, notes):
    """Return next generation of pots after rules in notes."""
    next_gen = []
    for pot in pots.keys():
        pattern = ''
        for i in range(-2, 3):
            pattern += pots.get(pot + i, '.')

        next_gen.append((pot, notes[pattern]))

    # Check edges for new pots
    left = min(pots)
    pattern = ''
    for i in range(left - 3, left + 2):
        pattern += pots.get(i, '.')
    if notes[pattern] == '#':
        pots[left - 1] = '#'

    right = max(pots)
    pattern = ''
    for i in range(right - 1, right + 4):
        pattern += pots.get(i, '.')
    if notes[pattern] == '#':
        pots[right + 1] = '#'

    for change in next_gen:
        pots[change[0]] = change[1]


with open('input.txt') as f:
    lines = f.readlines()

initial_state = list(lines[0].split()[2])
pots = dict(zip(range(0, len(initial_state)), initial_state))

notes_parse = [line.strip().split() for line in lines[2:]]
notes = {}
for note in notes_parse:
    pattern, __, result = note
    notes[pattern] = result

differences = [0, 0, 0, 0, 1]
prev_plants = 0
i = 1
while i < 1000:
    generations(pots, notes)
    plants = 0
    for pot, state in pots.items():
        if state == '#':
            plants += pot

    if i == 20:
        # Answer One
        print("Plants after 20:", plants)

    # Check if differences between generations has stabilised
    difference = plants - prev_plants
    del differences[0]
    differences.append(difference)

    if len(set(differences)) == 1:
        remaining = 5*10**10 - i
        total_plants = plants + difference * remaining
        # Answer Two
        print("Plants after 50 billion:", total_plants)
        break

    prev_plants = plants
    i += 1
