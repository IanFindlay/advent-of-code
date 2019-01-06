"""Advent of Code Day 15 - Beverage Bandits"""


def build_units(to_open, elf_power):
    """Build Unit objects for units in arena and place them in the arena."""
    with open(to_open) as f:
        arena = [list(row.strip()) for row in f.readlines()]
    units = []
    for row in range(len(arena)):
        for col in range(len(arena[0])):
            if arena[row][col] == 'E':
                unit = Unit('E', (row, col), elf_power)
                units.append(unit)
                arena[row][col] = unit
            elif arena[row][col] == 'G':
                unit = Unit('G', (row, col), 3)
                units.append(unit)
                arena[row][col] = unit

    return (arena, units)


class Unit:
    """Object representing a fighter(unit)."""

    def __init__(self, race, coords, attack):
        """Initialise Unit object with race, coords and attack power."""
        self.race = race
        self.coords = coords
        self.health = 200
        self.attack = attack

    def update_coords(self, new_coords, arena):
        """Update a unit's coordinates and move them in the arena."""
        row, col = self.coords
        arena[row][col] = '.'
        new_row, new_col = new_coords
        arena[new_row][new_col] = self
        self.coords = new_coords

    def get_open(self, arena):
        """Check adjacent spaces of unit and return any open spaces."""
        open_spaces = set()
        row, col = self.coords
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for space in adjacent:
            value = arena[space[0]][space[1]]
            if value == '.':
                open_spaces.add(space)

        return open_spaces

    def check_attack(self, arena):
        """Check adjacent spaces of unit and return coords of any enemies."""
        enemies = []
        row, col = self.coords
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for space in adjacent:
            value = arena[space[0]][space[1]]
            if type(value) is Unit and value.race != self.race:
                enemies.append(value)

        return enemies

    def take_damage(self, damage):
        """Decrease health by damage amount."""
        self.health -= damage

    def kill_unit(self, arena):
        """Remove unit from the arena map as it has been killed."""
        row, col = self.coords
        arena[row][col] = '.'


def make_attack(attackable, attacker):
    """Choose best target from attackable, attack then return if killed."""
    # Sort units by reading order
    attackable.sort(key=lambda unit: (unit.coords[0], unit.coords[1]))

    lowest = (201, None)
    for unit in attackable:
        if unit.health < lowest[0]:
            lowest = (unit.health, unit)
        # Ties go to previous due to sorting by reading order

    to_attack = lowest[1]
    to_attack.take_damage(attacker.attack)

    return to_attack if to_attack.health <= 0 else False


def make_move(start, open_spaces, arena):
    """Dijkstra to find closest open space(s) then sorting to find move."""
    visited = set()
    distances = {}
    first_steps = {}
    for i in range(len(arena)):
        for j in range(len(arena[0])):
            distances[(i, j)] = (float('inf'))
            first_steps[(i, j)] = []

    distances[start] = 0
    shortest = []
    nearest = None
    node = (start, None)
    while True:
        node_coords, node_first_step = node
        row, col = node_coords
        adjacent = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for square in adjacent:
            if square in visited:
                continue

            if arena[square[0]][square[1]] != '.':
                continue

            first_step = node_first_step if node_first_step else square
            current_distance = distances[square]
            new_distance = distances[node_coords] + 1
            if new_distance < current_distance:
                distances[square] = new_distance
                first_steps[square] = [first_step]

            elif new_distance == current_distance:
                first_steps[square].append(first_step)

        visited.add(node)

        # Construct new potential nodes from distances, creating a new
        # node for each first step listed in first_steps under that
        # coordinate as each is as valid as the other as distance is same
        nodes = []
        for coords in distances:
            for step in first_steps[coords]:
                new_node = (coords, step)
                if new_node not in visited:
                    nodes.append(new_node)

        if not nodes:
            break

        nodes.sort(key=lambda new_node: distances[new_node[0]], reverse=True)
        node = nodes.pop()
        new_coords, first_step = node

        if nearest and distances[new_coords] > nearest:
            break
        if distances[new_coords] == float('inf'):
            break

        if new_coords in open_spaces:
            if not shortest:
                shortest = [(new_coords, first_step)]
            else:
                shortest.append((new_coords, first_step))
            nearest = distances[new_coords]

    if not shortest:
        return False

    # Sort by target square (in reading order)
    shortest.sort(key=lambda x: (x[0][0], x[0][1]))
    target = shortest[0][0]
    # Filter out all other targets and extract first_steps list for sorting
    to_target = [x[1] for x in shortest if x[0] == target]
    to_target.sort(key=lambda x: (x[0], x[1]))
    move = to_target[0]

    return move


def battle(arena, units, part_two=False):
    """Battle the units in the arena until one side is eliminated."""
    elves = len([unit for unit in units if unit.race == 'E'])
    goblins = len(units) - elves
    rounds = 0
    while elves and goblins:
        # Clear dead then Sort units by reading order
        units = [unit for unit in units if unit.health > 0]
        units.sort(key=lambda unit: (unit.coords[0], unit.coords[1]))
        for unit in units:
            if unit.health <= 0:
                continue

            # If final blow wasn't the last units attack rounds needs fixed
            if not elves or not goblins:
                rounds -= 1
                break

            # Check for enemies and attack if found
            attackable = unit.check_attack(arena)
            if attackable:
                unit_killed = make_attack(attackable, unit)

            # Move, recheck for enemies and attack if found
            else:
                open_spaces = set()
                for other in units:
                    if other.race != unit.race and other.health > 0:
                        open_spaces = open_spaces | other.get_open(arena)

                if not open_spaces:
                    continue

                move = make_move(unit.coords, open_spaces, arena)

                if not move:
                    continue

                unit.update_coords(move, arena)

                attackable = unit.check_attack(arena)
                if attackable:
                    unit_killed = make_attack(attackable, unit)
                else:
                    unit_killed = False

            # If kill clear from arena, check both sides remain
            if unit_killed:
                unit_killed.kill_unit(arena)
                race = unit_killed.race

                if race == 'E':
                    elves -= 1
                    if part_two:
                        return False
                else:
                    goblins -= 1

        rounds += 1

    remaining_health = sum([unit.health for unit in units if unit.health > 0])
    return rounds * remaining_health


def main():
    """Find outcome of battle then attack boosted one where no elves die."""
    to_open = 'input.txt'
    arena, units = build_units(to_open, 3)

    # Answer One
    outcome = battle(arena, units)
    print("Initial outcome:", outcome)

    attack_power = 4
    while True:
        arena, units = build_units(to_open, attack_power)
        outcome = battle(arena, units, part_two=True)
        if outcome:
            break
        attack_power += 1

    # Answer Two
    print("Outcome of first no death elf victory:", outcome)


if __name__ == '__main__':
    main()
