#!/usr/bin/env python3

"""Advent of Code 2021 Day 19 - Beacon Scanner"""


class Scanner:

    def __init__(self, number, beacon_coords):
        self.number = number
        self.beacons = self.create_beacons(beacon_coords)
        self.scan = self.create_scan()

    def __str__(self):
        printout = f'Scanner - {self.number}:\n\n'

        for beacon in self.beacons:
            printout += f'{beacon}\n'

        return printout + '\n'

    def create_beacons(self, coord_tuples):
        beacons = {}
        for tup in coord_tuples:
            beacons[tup] = Beacon(tup)

        return beacons

    def create_scan(self):
        self.find_scan_borders()
        scan = {}
        for z in range(self.min_z, self.max_z + 1):
            for y in range(self.max_y, self.min_y - 1, -1):
                for x in range(self.min_x, self.max_x + 1):
                    if (x, y, z) in self.beacons.keys():
                        scan[(x, y, z)] = self.beacons[(x, y, z)]
                    elif (x, y, z) == (0, 0, 0):
                        scan[(x, y, z)] = 'S'
                    else:
                        scan[(x, y, z)] = '.'

        return scan

    def find_scan_borders(self):
        beacon_x_vals = [coords[0] for coords in self.beacons.keys()]
        beacon_x_vals.append(0)
        self.min_x, self.max_x = min(beacon_x_vals), max(beacon_x_vals)

        beacon_y_vals = [coords[1] for coords in self.beacons.keys()]
        self.min_y, self.max_y = min(beacon_y_vals), max(beacon_y_vals)
        beacon_y_vals.append(0)

        beacon_z_vals = [coords[2] for coords in self.beacons.keys()]
        self.min_z, self.max_z = min(beacon_z_vals), max(beacon_z_vals)


    def print_scan(self):
        for d, z in enumerate(range(self.min_z, self.max_z + 1), self.min_z):
            print(f'Current Depth: {d}\n')
            for y in range(self.max_y, self.min_y - 1, -1):
                row = ''
                for x in range(self.min_x, self.max_x + 1):
                    if (x, y, z) in self.beacons.keys():
                        row += 'B'
                    elif (x, y, z) == (0, 0, 0):
                        row += 'S'
                    else:
                        row += '.'

                print(row)

            print()


class Beacon:

    def __init__(self, relative_coords):
        self.relative_x, self.relative_y, self.relative_z = relative_coords

    def __str__(self):
        return f'{self.relative_x}, {self.relative_y}, {self.relative_z}'


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
