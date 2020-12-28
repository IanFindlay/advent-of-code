"""Advent of Code 2019 Day 10 - Monitoring Station."""


from math import atan2, degrees, pi


with open("inputs/day_10.txt", "r") as f:
    space = [list(row) for row in f.read().strip().split('\n')]

space_dict = {}
y = 0
for row in space:
    x = 0
    for col in row:
        value = space[y][x]
        if value == '#':
            space_dict[(x, y)] = space[y][x]
        x += 1
    y += 1

detection_dict = {}
for coords, value in space_dict.items():
    los = {}
    for location, item in space_dict.items():
        if location == coords:
            continue
        x, y = location
        dx = coords[0] - x
        dy = coords[1] - y
        angle = atan2(dy, dx)
        if angle < 0:
            angle += 2 * pi
        los[location] = degrees(angle)

    detection_dict[coords] = los

most_detected = None
for asteroid, los_dict in detection_dict.items():
    num_detected = len(set(los_dict.values()))
    if not most_detected or num_detected > most_detected[1]:
        most_detected = (asteroid, num_detected)

# Answer One
print("Other asteroids detected from the best location:", most_detected[1])

station_coords = most_detected[0]
station = detection_dict[station_coords]
for asteroid, angle in station.items():
    ast_x, ast_y = asteroid
    distance = (
        abs(station_coords[0] - ast_x) + abs(station_coords[1] - ast_y)
    )
    angle = (angle + 270) % 360   # Rotate so angles start at 12 O'Clock
    station[asteroid] = (angle, distance)

# Sort asteroids by angle, then distance
sorted_asteroids = dict(
    sorted(station.items(), key=lambda item: (item[1][0], item[1][1]))
)

vaporised_coords = set()
last_angle = None
vaporised = 0
while vaporised != 200:
    for asteroid, info in sorted_asteroids.items():
        angle = info[0]
        if angle == last_angle or asteroid in vaporised_coords:
            continue
        last_angle = angle
        vaporised_coords.add(asteroid)
        vaporised += 1
        if vaporised == 200:
            break

# Answer Two
print("Coordinates for 200th vaporised asteroid:", asteroid)
