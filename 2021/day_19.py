#!/usr/bin/env python3

"""Advent of Code 2021 Day 19 - Beacon Scanner"""


class Scanner:

    def __init__(self, number, beacon_coords):
        self.number = number
        self.coords = (0, 0, 0)
        self.create_beacons(beacon_coords)
        self.beacons_set = self.create_beacons_set()

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

    def reorientate(self):
        def x_axis():
            new_beacons_set = set()
            for beacon in self.beacons_set:
                x, y, z = beacon
                new_beacons_set.add((x, -z, y))
            self.beacons_set = new_beacons_set
            self.create_beacons(new_beacons_set)


        def y_axis():
            new_beacons_set = set()
            for beacon in self.beacons_set:
                x, y, z = beacon
                new_beacons_set.add((-z, y, x))
            self.beacons_set = new_beacons_set
            self.create_beacons(new_beacons_set)

        def z_axis():
            new_beacons_set = set()
            for beacon in self.beacons_set:
                x, y, z = beacon
                new_beacons_set.add((y, -x, z))
            self.beacons_set = new_beacons_set
            self.create_beacons(new_beacons_set)

        # Initial state is an orientation
        yield

        for _ in range(3):
            z_axis()
            yield
            for _ in range(3):
                x_axis()
                yield

                for _ in range(3):
                    y_axis()
                    yield

                # y back to normal
                y_axis()

            # Back to original
            x_axis()

    def update_position(self, new_coords):
        self.coords = new_coords
        for beacon in self.beacons:
            beacon.scanner_position = new_coords
            beacon.calculate_actual_coords()
        self.beacons_set = self.create_beacons_set()

    def compare_to_other_scanner(self, other_scanner):

        for _ in other_scanner.reorientate():
            for beacon in self.beacons:
                x, y, z = beacon.actual_coords

                for other_beacon in other_scanner.beacons:

                    other_x, other_y, other_z = other_beacon.relative_coords

                    # Move scanner so beacons align
                    other_scanner.update_position(
                            (x - other_x, y - other_y, z - other_z)
                    )

                    match = self.beacons_set.intersection(
                            other_scanner.beacons_set
                    )

                    if len(match) >= 12:
                        other_beacons = other_scanner.beacons
                        rel_coords = [x.relative_coords for x in other_beacons]
                        scanner_copy = Scanner(other_scanner.number,
                                rel_coords)
                        scanner_copy.update_position(other_scanner.coords)
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


with open('../inputs/day_19.txt', 'r') as aoc_input:
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
for scanner in scanners:

    if scanner.number not in located_scanner_numbers:
        continue

    for other_scanner in scanners:

        if scanner == other_scanner:
            continue

        if other_scanner.number in located_scanner_numbers:
            continue

        comparison = scanner.compare_to_other_scanner(other_scanner)
        if not comparison:
            continue

        print("Matched")
        located_scanner_numbers.add(other_scanner.number)
        located_scanners.append(comparison)

unique_beacons = set()
for scanner in located_scanners:
         unique_beacons = unique_beacons.union(scanner.beacons_set)

print(len(unique_beacons))
