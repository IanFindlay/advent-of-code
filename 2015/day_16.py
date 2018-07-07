"""Advent of Code Day 16 - Aunt Sue"""

import re


with open('input.txt') as f:
    sue_list = f.readlines()


mfcsam_dict = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
               'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
               'cars': 2, 'perfumes': 1,}

wrong_aunt = []
for num, aunt in enumerate(sue_list, 1):
    for key in mfcsam_dict:
        info_regex = re.compile(r'{}: (\d+)'.format(key))
        info_point = info_regex.search(aunt)
        if info_point:
            if int(info_point.group(1)) != mfcsam_dict[key]:
                wrong_aunt.append(num)
                break

for number in range(1, len(sue_list)):
    if number not in wrong_aunt:
        print("Aunt One =", number)
        break

# Part Two

wrong_aunt = []
for num, aunt in enumerate(sue_list, 1):
    for key in mfcsam_dict:
        info_regex = re.compile(r'{}: (\d+)'.format(key))
        info_point = info_regex.search(aunt)
        if info_point and key not in ('cats', 'trees', 'pomeranians', 'goldfish'):
            if int(info_point.group(1)) != mfcsam_dict[key]:
                wrong_aunt.append(num)
                break
        elif info_point and key in ('cats', 'trees'):
            if int(info_point.group(1)) <= mfcsam_dict[key]:
                wrong_aunt.append(num)
                break

        elif info_point and key in ('pomeranians', 'goldfish'):
            if int(info_point.group(1)) >= mfcsam_dict[key]:
                wrong_aunt.append(num)
                break


for number in range(1, len(sue_list)):
    if number not in wrong_aunt:
        print("Aunt Two =", number)
        break
