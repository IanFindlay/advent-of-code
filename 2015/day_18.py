"""Advent of Code Day 18 - Like a GIF For Your Yard"""


def light_show(part_two=False):
    lights = {}
    for num, line in enumerate(light_lines):
        for pos, light in enumerate(line):
            lights['{},{}'.format(pos, num)] = light
    steps = 0
    while steps < 100:
        new_lights = {}
        for light, state in lights.items():

            coords = light.split(',')
            x = int(coords[0])
            y = int(coords[1])

            adjacent = [str(x - 1) + ',' + str(y), str(x + 1) + ',' + str(y),
                    str(x) + ',' + str(y - 1), str(x) + ',' + str(y + 1),
                    str(x - 1) + ',' + str(y - 1), str(x - 1) + ',' + str(y + 1),
                    str(x + 1) + ',' + str(y - 1), str(x + 1) + ',' + str(y + 1),]

            adjacent_on = 0
            for to_check in adjacent:
                if lights.get(to_check, '.') == '#':
                    adjacent_on += 1

            if state == '#':
                if adjacent_on in (2, 3):
                    new_lights['{},{}'.format(x, y)] = '#'

                else:
                    new_lights['{},{}'.format(x, y)] = '.'

            elif state == '.':
                if adjacent_on == 3:
                    new_lights['{},{}'.format(x, y)] = '#'
                else:
                    new_lights['{},{}'.format(x, y)] = '.'

        if part_two:
            for coords in ('0,0', '0,99', '99,0', '99,99',):
                new_lights[coords] = '#'

        lights = new_lights

        steps += 1

    on = 0
    for state in lights.values():
        if state == '#':
            on += 1

    return on


with open('input.txt') as f:
    light_lines = [line.strip() for line in f]

# Answer One
print(light_show())

# Answer Two
print(light_show(part_two=True))
