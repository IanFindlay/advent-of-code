"""Advent of Code Day 25 - Let It Snow"""


def find_code(code, row, column):
    first = True
    while coords['row'] != row or coords['col'] != column:

        if first:
            coords['highest_row'] += 1
            coords['row'] = coords['highest_row']
            coords['col'] = 1
            code = (code * 252533) % 33554393
            first = False

        else:
            mid_fill = coords['highest_col'] - 2
            while mid_fill >= 0:
                coords['row'] -= 1
                coords['col'] += 1
                code = (code * 252533) % 33554393
                mid_fill -= 1

                if coords['row'] == row and coords['col'] == column:
                    return code

            coords['row'] -= 1
            coords['col'] += 1
            code = (code * 252533) % 33554393

            if coords['row'] == row and coords['col'] == column:
                return code

            coords['highest_col'] += 1

            first = True

    return code


coords = {'row': 1, 'col': 1, 'highest_row': 1, 'highest_col': 1}

# Answer One
print("Weather Machine Code =", find_code(20151125, 2981, 3075))
