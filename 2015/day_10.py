"""Advent of Code Day 10 - Elves Look, Elves Say"""

           
def say(number):
    """Returns a numbers 'say' equivalent."""
    numbers = []
    spans = []

    i = 0
    repeats = 1
    while i < len(number) - 1:
        if number[i] == number[i + 1]:
            repeats += 1
        else:
            numbers.append(number[i])
            spans.append(str(repeats))
            repeats = 1
        i += 1

    if number[-1] != number[-2]:
        numbers.append(number[-1])
        spans.append('1')

    said_list = list(zip(spans, numbers))
    said = ''
    for pair in said_list:
        said += pair[0]
        said += pair[1]

    return said
    

puzzle_input = '3113322113'

look = puzzle_input
cycles = 0
while cycles < 50:             # 40 for Answer One 50 for Answer Two
    new_number = say(look)
    look = new_number
    cycles += 1

print(len(new_number))
