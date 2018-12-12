"""Advent of Code Day 11 - Chronal Charge"""


def max_square(size, grid):
    """Find square (with size side length) with highest power total."""
    grid_size = len(grid)
    max_power, max_coord = 0, None
    for row in range(1, grid_size - size + 1):
        for col in range(1, grid_size - size + 1):
            a = grid[row - 1][col - 1]
            b = grid[row - 1][col + size - 1]
            c = grid[row + size - 1][col - 1]
            d = grid[row + size - 1][col + size - 1]
            power_sum = a + d - b - c
            if power_sum > max_power:
                max_power = power_sum
                max_coord = (col, row)

    return (max_power, (max_coord))


serial = 7672
end_cell = 301

# Cell power grid - 0's on left/top makes conversion to summed-area easier
grid = [[0 for __ in range(end_cell)] for __ in range(end_cell)]
for row in range(1, end_cell):
    for col in range(1, end_cell):
        rack_id = col + 10
        power = (rack_id * row + serial) * rack_id
        power = int(list(str(power))[-3]) - 5
        grid[row][col] = power

# Transform grid into summed_area grid
for row in range(1, end_cell):
    for col in range(1, end_cell):
       grid[row][col] = (grid[row][col] + grid[row - 1][col]
                         + grid[row][col - 1] - grid[row - 1][col - 1])

# Answer One
print("Coord for 3x3 square with most power:", max_square(3, grid)[1])

max_power = 0
for size in range(1, end_cell):
    power, coord = max_square(size, grid)
    if power > max_power:
        max_power, max_coord = power, coord
        max_size = size

# Answer Two
print("Coord and size with most power:", max_coord, max_size)
