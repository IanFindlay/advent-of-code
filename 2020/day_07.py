#!/usr/bin/env python3

"""Advent of Code 2020 Day 07 - Handy Haversacks."""

import re

class Bag:
    """."""

    def __init__(self, colour, contains):
        """."""
        self.colour = colour
        self.contains = contains
        self.leads_to_shiny_gold = False

        self.contents = self.process_contents()

    def process_contents(self):
        """."""
        contents = {}
        for contained_bag in self.contains:
            number, colour = contained_bag
            if colour == 'shiny gold':
                self.leads_to_shiny_gold = True
            if colour != 'no other':
                contents[colour] = int(number)

        return contents


with open ('input.txt', 'r') as f:
    luggage_rules = [rule.strip() for rule in f.readlines()]

bag_regex = re.compile('(\d)*?\s?(\w*\s\w*)\sbags?')
bags = {}
for rule in luggage_rules:
    parsed_rule = bag_regex.findall(rule)
    subject_bag = parsed_rule[0][1] # [0] is blank
    bags[subject_bag] = Bag(subject_bag, parsed_rule[1:])

bags_that_can_contain_shiny = 0
while True:
    for bag in bags:
        for inner_bag in bags[bag].contents:
            if bags[inner_bag].leads_to_shiny_gold:
                bags[bag].leads_to_shiny_gold = True

    shiny_count = 0
    for bag in bags:
        if bags[bag].leads_to_shiny_gold:
            shiny_count += 1

    if shiny_count == bags_that_can_contain_shiny:
        break
    else:
        bags_that_can_contain_shiny = shiny_count


# Answer One
print("Number of bag colours that can eventually contain shiny:",
       bags_that_can_contain_shiny)
