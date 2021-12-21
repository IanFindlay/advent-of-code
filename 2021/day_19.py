#!/usr/bin/env python3

"""Advent of Code 2021 Day 19 - Beacon Scanner"""


class Scanner:

    def __init__(self, number, beacon_coords, copy=False):
        self.number = number
        self.marker = (1, 2, 3)
        self.coords = (0, 0, 0)
        self.create_beacons(beacon_coords)
        self.beacons_set = self.create_beacons_set()
        if not copy:
            self.orientations = self.generate_orientations()

    def __str__(self):
        printout = f'Scanner - {self.number}:\n\n'

        for beacon in self.beacons:
            printout += f'{beacon}\n'

        return printout + '\n'

    def create_beacons(self, coord_tuples):
        beacons = []
        for tup in coord_tuples:
            beacons.append(Beacon(tup))

        self.beacons = beacons

    def create_beacons_set(self):
        return set([x.actual_coords for x in self.beacons])

    def generate_orientations(self):
        def x_axis():
            new_beacons_set = set()
            for beacon in self.beacons_set:
                x, y, z = beacon
                new_beacons_set.add((x, -z, y))
            self.beacons_set = new_beacons_set
            self.create_beacons(new_beacons_set)
            x, y, z = self.marker
            self.marker = (x, -z, y)

        def y_axis():
            new_beacons_set = set()
            for beacon in self.beacons_set:
                x, y, z = beacon
                new_beacons_set.add((-z, y, x))
            self.beacons_set = new_beacons_set
            self.create_beacons(new_beacons_set)
            x, y, z = self.marker
            self.marker = (-z, y, x)

        def z_axis():
            new_beacons_set = set()
            for beacon in self.beacons_set:
                x, y, z = beacon
                new_beacons_set.add((y, -x, z))
            self.beacons_set = new_beacons_set
            self.create_beacons(new_beacons_set)
            x, y, z = self.marker
            self.marker = (y, -x, z)

        orientations = []
        orientations.append(
                Scanner(self.number, self.beacons_set, copy=True)
        )

        for _ in range(3):
            z_axis()
            orientations.append(
                    Scanner(self.number, self.beacons_set, copy=True)
            )
            orientations[-1].marker = self.marker

            for _ in range(3):
                y_axis()
                orientations.append(
                        Scanner(self.number, self.beacons_set, copy=True)
                )
                orientations[-1].marker = self.marker

            y_axis()

            for _ in range(3):
                x_axis()
                orientations.append(
                        Scanner(self.number, self.beacons_set, copy=True)
                )
                orientations[-1].marker = self.marker

                for _ in range(3):
                    y_axis()
                    orientations.append(
                            Scanner(self.number, self.beacons_set, copy=True)
                    )
                    orientations[-1].marker = self.marker

                # Reset y
                y_axis()

            # Reset x
            x_axis()

        # Back to original
        z_axis()

        unique_orientations = []
        marker_set = set()
        for orientation in orientations:
            marker = orientation.marker
            if marker in marker_set:
                continue
            marker_set.add(marker)
            unique_orientations.append(orientation)

        return unique_orientations

    def update_position(self, new_coords):
        self.coords = new_coords
        for beacon in self.beacons:
            beacon.scanner_position = new_coords
            beacon.calculate_actual_coords()
        self.beacons_set = self.create_beacons_set()

    def compare_to_other_scanner(self, other_scanner):

        for orientation in other_scanner.orientations:
            for beacon in self.beacons:
                x, y, z = beacon.actual_coords

                for other_beacon in orientation.beacons:

                    other_x, other_y, other_z = other_beacon.relative_coords

                    # Move scanner so beacons align
                    orientation.update_position(
                            (x - other_x, y - other_y, z - other_z)
                    )

                    match = self.beacons_set.intersection(
                            orientation.beacons_set
                    )

                    if len(match) >= 12:
                        other_beacons = orientation.beacons
                        rel_coords = [x.relative_coords for x in other_beacons]
                        scanner_copy = Scanner(orientation.number,
                                rel_coords)
                        scanner_copy.update_position(orientation.coords)
                        return scanner_copy


class Beacon:

    def __init__(self, relative_coords):
        self.relative_coords = relative_coords
        self.scanner_position = (0, 0, 0)
        self.calculate_actual_coords()

    def __str__(self):
        printout = f'Relative to Scanner: {self.relative_coords}\n'
        printout += f'Actual Coords: {self.actual_coords}\n\n'

        return printout

    def calculate_actual_coords(self):
        scanner_x, scanner_y, scanner_z = self.scanner_position
        relative_x, relative_y, relative_z = self.relative_coords

        actual_x = scanner_x + relative_x
        actual_y = scanner_y + relative_y
        actual_z = scanner_z + relative_z

        self.actual_coords = (actual_x, actual_y, actual_z)


with open('inputs/day_19.txt', 'r') as aoc_input:
    scan_in = [x.strip().split('\n') for x in aoc_input.read().split('\n\n')]

scanners = []
for scanner in scan_in:
    num = int(scanner[0].strip(' --').split(' ')[-1])
    beacons = []
    for beacon in scanner[1:]:
        x, y, z = [int(x) for x in beacon.split(',')]
        beacons.append(((x, y, z)))

    scanners.append(Scanner(num, beacons))

located_scanner_numbers = set([0])
located_scanners = [scanners[0]]
num_scanners = len(scanners)
print(f'Progress: {len(located_scanners)}/{num_scanners}\n')
while len(located_scanner_numbers) != num_scanners:
    for scanner in located_scanners:

        for other_scanner in scanners:

            if scanner == other_scanner:
                continue

            if other_scanner.number in located_scanner_numbers:
                continue

            comparison = scanner.compare_to_other_scanner(other_scanner)
            if not comparison:
                continue

            located_scanner_numbers.add(other_scanner.number)
            located_scanners.append(comparison)
            print(f'Progress: {len(located_scanners)}/{num_scanners}\n')

unique_beacons = set()
for scanner in located_scanners:
         unique_beacons = unique_beacons.union(scanner.beacons_set)

# Answer One
print("Number of beacons:", len(unique_beacons))

largest_distance = 0
for scanner in located_scanners:

    x, y, z = scanner.coords

    for other_scanner in located_scanners:

        other_x, other_y, other_z = other_scanner.coords

        manhattan_distance = x - other_x + y - other_y + z - other_z

        if manhattan_distance > largest_distance:

            largest_distance = manhattan_distance

# Answer Two
print("Largest Manhattan distance between two scanners:", largest_distance)
