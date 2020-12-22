""" Advent of Code Day 9 - Explosives in Cyberspace"""

import re


def simple_decomp(compressed):
    """Decompress string skipping markers within the scope of a previous one."""
    decompressed = 0
    i = 0
    while i < len(compressed):
        if compressed[i] == '(':
            marker = ''
            in_marker = True
            j = 1
            while in_marker:
                if compressed[i + j] == ')':
                    in_marker = False
                else:
                    marker += compressed[i + j]
                j += 1

            split_marker = marker.split('x')
            repeated, reps = int(split_marker[0]), int(split_marker[1])
            decompressed += repeated * reps
            i += (len(marker) + 2) + repeated

        else:
            decompressed += 1
            i += 1

    return decompressed


def adv_decomp(compressed):
    """Decompress string including nested markers."""
    # For each marker track how many repetitions it causes of downstream markers
    marker_regex = re.findall(r'(\d+)x(\d+)', compressed)
    markers = []
    for pair in marker_regex:
        markers.append([int(pair[0]), int(pair[1]), 1])

    tracker = 0
    i = 0
    while i < len(compressed):
        if compressed[i] == '(':
            while compressed[i] != ')':
                i += 1
            marker_splice = compressed[i + 1 : i + markers[tracker][0] + 1]
            marker_regex = re.findall(r'(\(\d+x\d+\))', marker_splice)
            # Use length of all markers in splice to find chars to be repeated
            embedded = 0
            to_repeat = markers[tracker][0]
            for found in marker_regex:
                embedded += 1
                to_repeat -= len(found)
            markers[tracker].append(to_repeat)

            for marker in markers[tracker + 1 : tracker + embedded + 1]:
                marker[2] *= markers[tracker][1]

            tracker += 1

        i += 1

    # Remove markers then carry out decompression using gathered marker info
    decompressed = len(compressed)
    all_markers = re.findall(r'(\(\d+x\d+\))', compressed)
    for found in all_markers:
            decompressed -= len(found)

    for marker in markers:
        decompressed += (marker[1] - 1) * marker[2] * marker[3]

    return decompressed


with open('inputs/day_09.txt') as f:
    data = f.read()

# Answer One
print("Decompressed Sequence Length:", simple_decomp(data))

# Answer Two
print("Version Two Decompression Length:", adv_decomp(data))
