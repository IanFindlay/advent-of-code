#!/usr/bin/env python3

"""Advent of Code 2021 Day 18 - Snailfish"""


import json


class Pair:

    def __init__(self, pair, depth, parent, index):
        self.depth = depth
        self.parent = parent
        self.index_in_parent = index
        self.value = self.process_pair(pair)

    def __str__(self):
        if self.value == 0:
            return '0'
        return f'[{self.value[0].__str__()}, {self.value[1].__str__()}]'

    def process_pair(self, pair):
        values = []
        for index, element in enumerate(pair):
            if type(element) is list:
                value = Pair(element, self.depth + 1, self, index)
            else:
                value = int(element)

            values.append(ItemOfPair(self, value, index))

        if type(values[1].value) is int:
            self.rightmost = values[1]
        else:
            self.rightmost = values[1].value.rightmost

        if type(values[0].value) is int:
            self.leftmost = values[0]
        else:
            self.leftmost = values[0].value.leftmost

        return values

    def explode(self):

        if type(self.value) is int:
            return False

        left_item, right_item = self.value
        left_value = left_item.value
        right_value = right_item.value

        if type(left_value) is int and type(right_value) is int:

            if self.depth < 4:
                return False

            left = left_item.on_left()
            if left:
                left.try_addition(left_value)

            right = right_item.on_right()
            if right:
                right.try_addition(right_value)

            new_item = ItemOfPair(self.parent, 0, self.index_in_parent)
            self.parent.value[self.index_in_parent] = new_item
            return True

        if isinstance(left_value, Pair):
            if left_value.explode():
                return True

        if isinstance(right_value, Pair):
            return right_value.explode()

        return False

    def try_to_split(self):

        if type(self.value) is int:
            return False

        for item in self.value:
            if type(item.value) is int and item.value >= 10:
                item.split_item()
                return True

            else:
                if isinstance(item.value, Pair):
                    if item.value.try_to_split():
                        return True

        return False

    def get_magnitude(self):
        left, right = self.value
        if type(left.value) is not int:
            left = left.value.get_magnitude()
        else:
            left = left.value
        if type(right.value) is not int:
            right = right.value.get_magnitude()
        else:
            right = right.value

        return 3 * left + 2 * right


class ItemOfPair:

    def __init__(self, pair, value, index_in_pair):
        self.value = value
        self.pair = pair
        self.index_in_pair = index_in_pair

    def __str__(self):
        if type(self.value) is int:
            return f'{self.value}'
        else:
            return f'{self.value.__str__()}'

    def on_left(self):
        current_pair = self.pair
        if current_pair.index_in_parent == 1:
            if type(current_pair.parent.value[0].value) is int:
                return current_pair.parent.value[0]
            return current_pair.parent.value[0].value.rightmost

        index = 0
        while True:
            index = current_pair.index_in_parent
            if index == 1:
                break

            current_pair = current_pair.parent
            if not current_pair:
                return None

        if type(current_pair.parent.value[0].value) is int:
            return current_pair.parent.value[0]

        return current_pair.parent.value[0].value.rightmost


    def on_right(self):
        current_pair = self.pair
        if current_pair.index_in_parent == 0:
            if type(current_pair.parent.value[1].value) is int:
                return current_pair.parent.value[1]
            return current_pair.parent.value[1].value.leftmost

        index = 1
        while True:
            index = current_pair.index_in_parent
            if index == 0:
                break

            current_pair = current_pair.parent
            if not current_pair:
                return None

        if type(current_pair.parent.value[1].value) is int:
            return current_pair.parent.value[1]

        return current_pair.parent.value[1].value.leftmost

    def try_addition(self, num_to_add):
        if type(self.value) is not int:
            return False

        self.value += num_to_add
        return True

    def split_item(self):
        if type(self.value) is not int:
            return False
        divided = self.value / 2
        if self.value % 2:
            new_value = [divided, divided + 1]
        else:
            new_value = [divided, divided]

        new_parent = self.pair

        self.value = Pair(
                new_value, self.pair.depth + 1, new_parent, self.index_in_pair)


def reduce_number(number):
    while True:
        number = json.loads(number.__str__())
        number = Pair(number, 0, None, None)

        if number.explode():
            continue

        if not number.try_to_split():
            break

    return number


with open('inputs/day_18.txt', 'r') as aoc_input:
    numbers = [json.loads(line.strip()) for line in aoc_input.readlines()]

summed_number = numbers[0]
for number in numbers[1:]:
    summed_number = Pair([summed_number, number], 0, None, None)
    summed_number = reduce_number(summed_number)
    summed_number = json.loads(summed_number.__str__())

summed_number = Pair(summed_number, 0, None, None)

# Answer One
print("Magnitude of final sum:", summed_number.get_magnitude())

biggest_magnitude = 0
for num_one in numbers:

    for num_two in numbers:

        if num_one == num_two:
            continue

        added = reduce_number(Pair([num_one, num_two], 0, None, None))
        magnitude = added.get_magnitude()
        if magnitude > biggest_magnitude:
            biggest_magnitude = magnitude

# Answer Two
print("Largest magnitude of the sum of any two snailfish numbers",
        biggest_magnitude)
