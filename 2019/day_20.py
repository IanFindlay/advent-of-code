"""Advent of Code 2019 Day 20 - Donut Maze."""


from collections import defaultdict, deque


def maze_bfs(maze, start, end, portals, recursive=False):
    """BFS from entrance to exit of maze with portals.

        Args:
            maze (dict): {Coords: Value} dictionary representing the maze.
            entrance (str): Coords of entrance (x, y).
            exit (str): Coords of exit (x, y).
            portals (dict): Dictionary mapping portals to their destinations.
            recursive (bool): Treat portals like recursive mazes.

        Returns:
            Length of the shortest path (int).

    """
    x_edges = (2, max([x for x, y in maze.keys()]) - 2)
    y_edges = (2, max([y for x, y in maze.keys()]) - 2)
    visited = set()
    visited.add((start, 0))
    queue = deque()
    queue.append((start, 0, 0))
    while queue:
        coords, steps, level = queue.popleft()

        if coords in portals:
            warp_to = portals[coords]
            if coords[0] in x_edges or coords[1] in y_edges:
                new_level = level - 1
            else:
                new_level = level + 1

            if (warp_to, new_level) not in visited and new_level >= 0:
                visited.add((warp_to, new_level))
                queue.append((warp_to, steps + 1, new_level))

        x, y = coords
        next_nodes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for node in next_nodes:
            if (node, level) in visited:
                continue

            if node == end:
                if not recursive or level == 0:
                    return steps + 1
                else:
                    queue.append((node, steps + 1, level))

            tile_value = maze.get(node)

            if tile_value == '.':
                visited.add((node, level))
                queue.append((node, steps + 1, level))

    return False


with open('inputs/day_20.txt') as f:
    input_map = [line.strip('\n') for line in f.readlines()]

maze_dict = {}
for y in range(len(input_map)):
    for x in range(len(input_map[0])):
        maze_dict[(x, y)] = input_map[y][x]

portal_locations = defaultdict(list)
for coords, tile in maze_dict.items():
    if tile in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        portal_code = tile
        x, y = coords
        neighbours = {
            'l': (x - 1, y), 'r': (x + 1, y),
            'd': (x, y + 1), 'u': (x, y - 1)
        }
        for direction, new_coords in neighbours.items():
            portal_coords = None
            value = maze_dict.get(new_coords, '#')
            if value in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if direction == 'l':
                    portal_code = value + portal_code
                elif direction == 'r':
                    portal_code += value
                elif direction == 'u':
                    portal_code = value + portal_code
                elif direction == 'd':
                    portal_code += value

            elif value == '.':
                portal_coords = new_coords

            else:
                continue

            if not portal_coords:
                new_x, new_y = new_coords
                adjacents = [
                    (new_x - 1, new_y), (new_x + 1, new_y),
                    (new_x, new_y - 1), (new_x, new_y + 1)
                ]
                for adjacent in adjacents:
                    value = maze_dict.get(adjacent)
                    if value == '.':
                        portal_coords = adjacent
                        break

                if portal_coords not in portal_locations[portal_code]:
                    if portal_coords:
                        portal_locations[portal_code].append(portal_coords)

portal_links = {}
for code, coords in portal_locations.items():
    if code == 'AA':
        entrance = coords[0]
    elif code == 'ZZ':
        maze_exit = coords[0]
    else:
        portal_links[coords[0]] = coords[1]
        portal_links[coords[1]] = coords[0]

# Answer One
fewest_steps = maze_bfs(maze_dict, entrance, maze_exit, portal_links)
print("Fewest steps required to navigate the maze:", fewest_steps)

# Answer Two
fewest_steps = maze_bfs(maze_dict, entrance, maze_exit, portal_links, True)
print("Fewest steps required to navigate the recursive maze:", fewest_steps)
