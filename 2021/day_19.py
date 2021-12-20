#!/usr/bin/env python3

"""Advent of Code 2021 Day 19 - Beacon Scanner"""


class Scanner:

    def __init__(self, number, beacon_coords):
        self.number = number
        self.coords = (0, 0, 0)
        self.create_beacons(beacon_coords)
        self.beacons_set = self.create_beacons_set()
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
        orientations = []
        orientations.append(self.beacons_set)

        def clockwise(coords):
            x, y, z = coords
            return (y, -x, z)

        def right_rotation(coords):
            x, y, z = coords
            return (z, y, -x)

        def backwards_rotation(coords):
            x, y, z = coords
            return (x, z, -y)

        for _ in range(4):

            for _ in range(3):
                for beacon in self.beacons:
                    beacon.actual_coords = clockwise(beacon.actual_coords)

                orientations.append(self.create_beacons_set())

            # Reset to start then turn it and run through it again
            for beacon in self.beacons:
                beacon.actual_coords = clockwise(beacon.actual_coords)

            for beacon in self.beacons:
                beacon.actual_coords = right_rotation(beacon.actual_coords)

            orientations.append(self.create_beacons_set())

        # Reset to start
        for beacon in self.beacons:
            beacon.actual_coords = right_rotation(beacon.actual_coords)

        # Backwards and rotations but some aren't needed...

        for beacon in self.beacons:
            beacon.actual_coords = backwards_rotation(beacon.actual_coords)
        orientations.append(self.create_beacons_set())

        # All 3 right rotations should still be needed from here
        for _ in range(3):
            for beacon in self.beacons:
                beacon.actual_coords = right_rotation(beacon.actual_coords)
            orientations.append(self.create_beacons_set())

        # Reset right
        for beacon in self.beacons:
            beacon.actual_coords = right_rotation(beacon.actual_coords)

        # Next backward as it's same as 1st right rotations
        for beacon in self.beacons:
            beacon.actual_coords = backwards_rotation(beacon.actual_coords)

        for beacon in self.beacons:
            beacon.actual_coords = backwards_rotation(beacon.actual_coords)
        orientations.append(self.create_beacons_set())

        # Final three rights
        for _ in range(3):
            for beacon in self.beacons:
                beacon.actual_coords = right_rotation(beacon.actual_coords)
            orientations.append(self.create_beacons_set())

        return orientations

    def print_scan(self):
        self.find_scan_borders()
        for d, z in enumerate(range(self.min_z, self.max_z + 1), self.min_z):
            print(f'Current Depth: {d}\n')
            for y in range(self.max_y, self.min_y - 1, -1):
                row = ''
                for x in range(self.min_x, self.max_x + 1):
                    if (x, y, z) in self.beacons_set:
                        row += 'B'
                    elif (x, y, z) == (0, 0, 0):
                        row += 'S'
                    else:
                        row += '.'
                print(row)
            print()

    def find_scan_borders(self):
        beacon_x_vals = [beacon.actual_coords[0] for beacon in self.beacons]
        beacon_x_vals.append(0)
        self.min_x, self.max_x = min(beacon_x_vals), max(beacon_x_vals)

        beacon_y_vals = [beacon.actual_coords[1] for beacon in self.beacons]
        self.min_y, self.max_y = min(beacon_y_vals), max(beacon_y_vals)
        beacon_y_vals.append(0)

        beacon_z_vals = [beacon.actual_coords[2] for beacon in self.beacons]
        self.min_z, self.max_z = min(beacon_z_vals), max(beacon_z_vals)

    def update_position(self, new_coords):
        self.coords = new_coords
        for beacon in self.beacons:
            beacon.scanner_position = new_coords
            beacon.calculate_actual_coords()
        self.beacons_set = self.create_beacons_set()

    def compare_to_other_scanner(self, other_scanner):

        for orientation in self.orientations:

            # Load orientation
            self.create_beacons(orientation)

            # Set this scanner position to 0
            self.update_position((0, 0, 0))

            # Set other beacon to match beacon
            for beacon in self.beacons:
                x, y ,z = beacon.actual_coords

                for other_beacon in other_scanner.beacons:

                    other_x, other_y, other_z = other_beacon.relative_coords

                    other_scanner.update_position(
                            (x - other_x, y - other_y, z - other_z)
                    )

                    match = self.beacons_set.intersection(
                            other_scanner.beacons_set
                    )

                    if len(match) >= 12:
                        for coords in match:
                            print(coords)
                        print("Scanner Position", other_scanner.coords)
                        return True

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

scanners[0].compare_to_other_scanner(scanners[1])
