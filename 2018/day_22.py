"""Advent of Code Day 22 - Mode Maze"""


def map_cave(target, depth):
    """Calculate and map the cave coordinates with padding around target."""
    target_x, target_y = target
    cave = {}
    for y in range(target_y + 50):
        for x in range(target_x + 50):
            erosion_level = calculate_erosion((x, y), depth, target, cave)
            cave[(x, y)] = erosion_level

    # Calculated erosion to make calculation easy then convert to type
    for coords, erosion_level in cave.items():
        cave[coords] %= 3

    return cave


def calculate_erosion(coords, depth, target, cave):
    """Return the erosion level of a coordinate."""
    x, y = coords
    if (x, y) == (0, 0):
        return (0 + depth) % 20183
    elif (x, y) == target:
        return (0 + depth) % 20183
    elif y == 0:
        return (x * 16807 + depth) % 20183
    elif x == 0:
        return (y * 48271 + depth) % 20183
    else:
        return (cave[(x-1, y)] * cave[(x, y-1)] + depth) % 20183


def find_path(target, cave):
    """Return quickest path to target- Dijkstra with (coords, tool) nodes."""
    tools = {0: ('c', 't'), 1: ('c', 'n'), 2:('t', 'n')}
    distances = {((0, 0), 't'): 0}
    initial_node = ((0, 0), 't')
    visited = set((initial_node))
    nodes = []
    node = initial_node
    while True:
        coords, tool = node
        visited.add((coords, tool))
        x, y = coords
        adjacent = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbour in adjacent:
            if neighbour not in cave or neighbour in visited:
                continue

            node_distance = distances[node]
            distance = distances.get((neighbour, tool), 1000000)
            neighbour_tools = tools[cave[neighbour]]

            if tool in neighbour_tools:
                if node_distance + 1 < distance:
                    distances[(neighbour, tool)] = node_distance + 1
                    nodes.append((neighbour, tool))
                continue

            current_tools = tools[cave[coords]]

            # Change tool, update node and add it to nodes if quicker
            if current_tools[0] in neighbour_tools:
                updated_node = (coords, current_tools[0])
                distance = distances.get(updated_node, 1000000)
                if node_distance + 7 < distance:
                    distances[updated_node] = node_distance + 7
                    nodes.append(updated_node)

            elif current_tools[1] in neighbour_tools:
                updated_node = (coords, current_tools[1])
                distance = distances.get(updated_node, 1000000)
                if node_distance + 7 < distance:
                    distances[updated_node] = node_distance + 7
                    nodes.append(updated_node)

        # Add to visited
        visited.add((node))

        # Choose next node
        nodes = sorted(nodes, key=lambda x: distances[x], reverse=True)
        node = nodes.pop()

        # Check if target reached add tool switch time if required
        if node[0] == target:
            if node[1] == 't':
                return distances[node]
            else:
                return distances[node] + 7


def main():
    """Map cave, evaluate risk level and find quickest path to target."""
    target = (13, 726)
    depth = 3066
    cave = map_cave(target, depth)

    # Answer One
    risk_level = 0
    for coords, terrain in cave.items():
        if coords[0] <= target[0] and coords[1] <= target[1]:
            risk_level += terrain
    print("Risk level:", risk_level)

    # Answer Two
    quickest_path = find_path(target, cave)
    print("Quickest Path:", quickest_path)


if __name__ == '__main__':
    main()
