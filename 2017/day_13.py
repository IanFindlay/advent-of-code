"""Advent of Code Day 13 - Packet Scanners"""


def severity(layers, delay):
    """Calculate cost of getting caught when traversing a Firewall."""
    layers_list = layers.strip().split('\n')

    severity = 0
    for layer in layers_list:
        layer_parts = (str(layer).split(':'))
        layer_num = int(layer_parts[0])
        layer_range = int(str(layer_parts[1]).strip())

        if (layer_num + delay) % ((layer_range - 1) * 2) == 0:
            severity += layer_num * layer_range
            if layer_num == 0:
                severity += 1   # Prevents being caught on 0 not counting

    if delay == 0:
        print('Bypassing with no delay results in overall severity of '
              + str(severity - 1))

    if severity == 0:
        return delay


with open('input.txt') as f:
    firewall = f.read()

delay = 0
while severity(firewall, delay) is None:
    delay += 1

# Answer One
print('The smallest delay that would bypass the firewall is:', delay, 'picoseconds.')
