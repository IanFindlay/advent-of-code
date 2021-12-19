#!/usr/bin/env python3

"""Advent of Code 2021 Day 19 - Beacon Scanner"""


class Scanner:

    def __init__(self, number, beacon_coords):
        self.number = number
        self.beacons = self.create_beacons(beacon_coords)

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
