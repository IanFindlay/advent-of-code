#!/usr/bin/env python3

"""Advent of Code 2021 Day 16 - Packet Decoder"""


class Packet:

    def __init__(self, binary):
        self.binary = binary
        self.version = int(self.binary[0:3], 2)
        self.type = int(self.binary[3:6], 2)

        if self.type == 4:
            self.value = self.process_literal()
        else:
            self.subs = self.process_subpackets()
            self.value = self.calculate_value()

        self.version_sum = self.sum_versions()

    def process_literal(self):
        binary_value = ''
        i = 6
        while True:
            group_indicator = self.binary[i]
            binary_value += self.binary[i + 1: i + 5]
            i += 5
            if group_indicator == '0':
                break

        self.length = i
        return int(binary_value, 2)

    def process_subpackets(self):
        subpackets = []

        length_type = self.binary[6]
        if length_type == '0':
            index = 22
            subpacket_length = int(self.binary[7: index], 2)
            self.length = subpacket_length + index
            to_process = self.binary[index: self.length]

            while True:
                subpackets.append(Packet(to_process))
                index = subpackets[-1].length
                if index == len(to_process):
                    break
                to_process = to_process[index :]

        else:
            index = 18
            subpacket_count = int(self.binary[7: index], 2)

            self.length = index
            to_process = self.binary[index:]
            while len(subpackets) != subpacket_count:
                subpackets.append(Packet(to_process))
                self.length += subpackets[-1].length
                index = subpackets[-1].length
                to_process = to_process[index:]

        return subpackets

    def sum_versions(self):
        version_sum = self.version
        if self.type == 4:
            return version_sum

        for subpacket in self.subs:
            version_sum += subpacket.sum_versions()

        return version_sum

    def calculate_value(self):
        if self.type == 0:
            return sum(sub.value for sub in self.subs)

        elif self.type == 1:
            value = 1
            for subpacket in self.subs:
                value *= subpacket.value
            return value

        elif self.type == 2:
            return min(sub.value for sub in self.subs)

        elif self.type == 3:
            return max(sub.value for sub in self.subs)

        elif self.type == 5:
            return 1 if self.subs[0].value > self.subs[1].value else 0

        elif self.type == 6:
            return 1 if self.subs[0].value < self.subs[1].value else 0

        elif self.type == 7:
            return 1 if self.subs[0].value == self.subs[1].value else 0


with open('inputs/day_16.txt', 'r') as aoc_input:
    transmission = aoc_input.read().strip()

hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

binary = ''.join([hex_to_bin[char] for char in transmission])

processed_transmission = Packet(binary)

# Answer One
print("Sum of version numbers:", processed_transmission.version_sum)


# Answer Two
print("Value of BITS transmission:", processed_transmission.value)
