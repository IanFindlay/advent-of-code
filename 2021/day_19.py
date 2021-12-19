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
        beacon_x_vals = [coords[0] for coords in self.beacons.keys()]
        beacon_x_vals.append(0)
        beacon_y_vals = [coords[1] for coords in self.beacons.keys()]
        beacon_y_vals.append(0)
        scan = []
        for y in range(max(beacon_y_vals), min(beacon_y_vals) - 1, -1):
            row = []
            for x in range(min(beacon_x_vals), max(beacon_x_vals) + 1):
                if (x, y) in self.beacons.keys():
                    row.append(self.beacons[(x,y)])
                elif (x, y) == (0, 0):
                    row.append('S')
                else:
                    row.append('.')

            scan.append(row)

        return scan

    def print_scan(self):
        print(f'Scan of Scanner {self.number}:\n')
        for row in self.scan:
            print(''.join(['B' if isinstance(x, Beacon) else x for x in row]))



class Beacon:

    def __init__(self, relative_coords):
        self.relative_x, self.relative_y = relative_coords

    def __str__(self):
        return f'{self.relative_x}, {self.relative_y}'


with open('../inputs/day_19.txt', 'r') as aoc_input:
    scan_in = [x.strip().split('\n') for x in aoc_input.read().split('\n\n')]

scanners = []
for scanner in scan_in:
    num = int(scanner[0].strip(' --').split(' ')[-1])
    beacons = []
    for beacon in scanner[1:]:
        x, y = [int(x) for x in beacon.split(',')]
        beacons.append(((x, y)))

    scanners.append(Scanner(num, beacons))

for scanner in scanners:
    print(scanner)
    scanner.print_scan()
