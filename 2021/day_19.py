#!/usr/bin/env python3

"""Advent of Code 2021 Day 19 - Beacon Scanner"""


class Scanner:

    def __init__(self, number, beacon_coords):
        self.number = number
        self.beacons = self.create_beacons(beacon_coords)
        self.beacons_set = self.create_beacon_set()

    def __str__(self):
        printout = f'Scanner - {self.number}:\n\n'

        for beacon in self.beacons:
            printout += f'{beacon}\n'

        return printout + '\n'

    def create_beacons(self, coord_tuples):
        beacons = []
        for tup in coord_tuples:
            beacons.append(Beacon(tup))

        return beacons

    def create_beacon_set(self):
        return set([x.actual_coords for x in self.beacons])

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


class Beacon:

    def __init__(self, relative_coords):
        self.relative_coords = relative_coords
        self.scanner_position = (0, 0, 0)
        self.actual_coords = self.calculate_actual_coords()

    def __str__(self):
        printout = f'Relative to Scanner: {self.relative_coords}\n\n'
        printout += f'Actual Coords: {self.actual_coords}'

        return printout

    def calculate_actual_coords(self):
        scanner_x, scanner_y, scanner_z = self.scanner_position
        relative_x, relative_y, relative_z = self.relative_coords

        actual_x = scanner_x + relative_x
        actual_y = scanner_y + relative_y
        actual_z = scanner_z + relative_z

        return (actual_x, actual_y, actual_z)


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

for scanner in scanners[:1]:
    print(scanner)
    scanner.print_scan()
