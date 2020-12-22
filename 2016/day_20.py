"""Advent of Code Day 20 - Firewall Rules"""

with open('inputs/day_20.txt') as f:
    ip_ranges = [line.strip() for line in f.readlines()]

blacklisted = []
for ip_range in ip_ranges:
    parse = ip_range.split('-')
    start, end = int(parse[0]), int(parse[1])
    blacklisted.append((start, end))

lowest = None
allowed = 0
target = 0
while target <= 4294967295:
    unblocked = True
    for listed in blacklisted:
        if target >= listed[0] and target <= listed[1]:
            target = listed[1]
            unblocked = False
            break

    if unblocked:
        allowed += 1
        if not lowest:
            lowest = target

    target += 1

# Answer One
print("Lowest unblocked IP:", lowest)

# Answer Two
print("Unblocked IPs:", allowed)
