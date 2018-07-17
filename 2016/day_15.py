""" Advent of Code Day 15 - Timing is Everything"""

with open('input.txt') as f:
    disc_info = [line.strip() for line in f.readlines()]

discs = []
for info in disc_info:
    parse = info.split(' ')
    discs.append([int(parse[3]), int(parse[-1][:-1])])

discs.append([11, 0])  # Delete this for part one

time = 0
while True:
    passed = True
    for delay, disc in enumerate(discs, 1):
        if (disc[1] + time + delay) % disc[0] != 0:
            passed = False
            break

    if passed:
        break

    time += 1

# Answer One / Answer Two
print("Time to wait before pressing button:", time)
