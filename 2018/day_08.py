"""Advent of Code Day 8 - Memory Maneuver"""


def process_node(node, data):
    """Determine and process the next node in data."""
    nodes[node] = None
    child_nums = None
    children = data[0]
    num_meta = data[1]
    data = data[2:]

    if children:
        data, child_nums = process_children(children, data)

    nodes[node] = (data[:num_meta], child_nums)
    return data[num_meta:]


def process_children(children, data):
    """Process next node in data until no children remain."""
    child_nums = []
    while children:
        node = len(nodes)
        child_nums.append(node)
        nodes[node] = None
        data = process_node(node, data)
        children -= 1

    return (data, child_nums)


def node_value(node):
    """Recursively calculate a nodes value from its children's values."""
    indexed, children = nodes[node]
    if not children:
        return sum(nodes[node][0])

    value = 0
    for index in indexed:
        try:
            value += node_value(children[index-1])
        except IndexError:
            continue

    return value


if __name__ == '__main__':

    with open('inputs/day_08.txt') as f:
        data = [int(x) for x in f.read().split()]

    # Process nodes from root and map nodes to their metadata and children
    nodes = {}
    process_node(0, data)

    metadata_sum = 0
    for node, info in nodes.items():
        for metadata in info[0]:
            metadata_sum += metadata

    # Answer One
    print("Sum of metadata:", metadata_sum)

    # Answer Two
    print("Root value:", node_value(0))
