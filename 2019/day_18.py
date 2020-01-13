"""Advent of Code 2019 Day 18 - Many-Worlds Interpretation."""


from collections import defaultdict, deque


def path_to_key(area_map, start, target_key):
    """Find shortest path, ignoring obstacles, from start key to target key."""
    visited = set()
    queue = deque()
    queue.append((start, 0, set()))
    while queue:
        coords, step, doors = queue.popleft()
        x, y = coords
        adjacents = [(x + 1, y), (x - 1 , y), (x, y + 1), (x, y - 1)]
        for adjacent in adjacents:
            if adjacent in visited:
                continue
            visited.add(adjacent)
            value = area_map[adjacent]

            if value == '#':
                continue

            if value == target_key:
                return (target_key, step + 1, doors)

            if value in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                doors_copy = doors.copy()
                doors_copy.add(value.lower())
                queue.append((adjacent, step + 1, doors_copy))
            else:
                queue.append((adjacent, step + 1, doors))


def navigate_tunnels(start, key_paths):
    """Use key paths to DFS collecting all keys and return fewest steps."""
    num_keys = len(key_paths) - 1
    shortest = None
    seen = set()
    seen_steps = {}
    stack = [(start, set(), 0)]
    while stack:
        tile, keys, steps = stack.pop()

        if shortest and steps >= shortest:
            continue

        cache = (tile, frozenset(keys))
        if cache in seen and seen_steps[cache] <= steps:
            continue
        seen.add(cache)
        seen_steps[cache] = steps

        for path in key_paths[tile]:
            key_name, distance, doors = path

            if doors & keys != doors:
                continue

            if key_name in keys:
                continue

            if len(keys) == num_keys - 1:
                if not shortest or steps + distance < shortest:
                    shortest = steps + distance

            keys_copy = keys.copy()
            keys_copy.add(key_name)

            stack.append((key_name, keys_copy, steps + distance))

    return shortest


def navigate_split(key_paths):
    """DFS to return fewest steps needed to collect all keys in split maze."""
    num_keys = len(key_paths) - 4
    shortest = None
    seen = set()
    seen_steps = {}
    stack = [(('0', '1', '2', '3'), set(), 0)]
    while stack:
        robots, keys, steps = stack.pop()

        if shortest and steps >= shortest:
            continue

        cache = (robots, frozenset(keys))
        if cache in seen and seen_steps[cache] <= steps:
            continue
        seen.add(cache)
        seen_steps[cache] = steps

        for pos in range(4):
            for path in key_paths[robots[pos]]:
                key_name, distance, doors = path

                if doors & keys != doors:
                    continue

                if key_name in keys:
                    continue

                if len(keys) == num_keys - 1:
                    if not shortest or steps + distance < shortest:
                        shortest = steps + distance

                keys_copy = keys.copy()
                keys_copy.add(key_name)

                new_robots = list(robots)
                new_robots[pos] = key_name
                new_robots = tuple(new_robots)

                stack.append((new_robots, keys_copy, steps + distance))

    return shortest


with open('input.txt') as f:
    input_map = [[value for value in row.strip()] for row in f.read().split()]

scan = {}
keys = []
key_coords = {}
for y in range(len(input_map)):
    for x in range(len(input_map[0])):
        scan[(x, y)] = input_map[y][x]
        tile = input_map[y][x]
        if tile in "@abcdefghijklmnopqrstuvwxyz":
            keys.append(tile)
            key_coords[tile] = (x, y)

key_paths = defaultdict(list)
for key in keys:
    for key_name in keys:
        if key == key_name or key_name == '@':
            continue
        key_paths[key].append((path_to_key(scan, key_coords[key], key_name)))

# Answer One
print("Fewest steps needed to get all keys:", navigate_tunnels('@', key_paths))

x, y = key_coords['@']
dx = [-1, 0, 1]
dy = [-1, 0, 1]
robot_num = 0
for col in dx:
    for row in dy:
        new_coords = (x + col, y + row)
        if (col, row) in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
            scan[new_coords] = str(robot_num)
            key_coords[str(robot_num)] = new_coords
            robot_num += 1
        else:
            scan[new_coords] = '#'

key_paths = defaultdict(list)
keys = 'abcdefghijklmnopqrstuvwxyz0123'
for key in keys:
    for key_name in keys:
        if key == key_name or key_name in ('0', '1', '2', '3'):
            continue
        try:
            paths = path_to_key(scan, key_coords[key], key_name)
            if paths:
                key_paths[key].append(paths)
        except KeyError:
            pass

# Answer Two
print("Fewest steps to get keys in split tunnels:", navigate_split(key_paths))
