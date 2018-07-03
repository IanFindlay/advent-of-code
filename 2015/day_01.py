""" Advent of Code Day 1 - Not Quite Lisp"""

def direction(part_two=False):
    with open('input.txt') as f:
        instructions = f.read()
    
    level = 0
    position = 0
    for char in instructions:
        if char == '(':
            level += 1
        elif char ==')':
            level -= 1
        position += 1

        if part_two:
            if level <= -1:
                print("First time in Basement =", position)
                return
    print("Final Floor =", level)

# Answer to Part One
direction()

# Answer to Part Two
direction(part_two=True)
