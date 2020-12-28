""" Advent of Code Day 7 - Internet Protocol Version 7"""

import re


def check_tls(address):
    """Check address has TLS support - ABBA only found in supernet."""
    abba_regex = re.compile(r'(\w)(?!\1)(\w)\2\1')
    hypernet = re.findall(r'\[[^\]]*\]', address)

    if abba_regex.search(address):
        for found in hypernet:
            if abba_regex.search(found):
                return
        return True


def check_ssl(address):
    """Check address has SLS support - ABA in supernet and related BAB in hypernet."""
    in_squares = False
    supernet = []
    hypernet = ''
    for char in address:
        if char == '[':
            in_squares = True
            supernet.append('|')
        if in_squares:
            hypernet += char
        else:
            supernet.append(char)
        if char == ']':
            in_squares = False

    to_check = ''.join(supernet).split('|')

    for string in to_check:
        i = 0
        abas = []
        while i < len(string) - 2:
            if string[i] == string[i + 2] and string[i] != string[i + 1]:
                abas.append((string[i],string[i + 1]))
            i += 1

        for aba in abas:
            bab_regex = re.findall(r'{}{}{}'.format(aba[1], aba[0], aba[1]), hypernet)

            if bab_regex:
                return True


with open('inputs/day_07.txt') as f:
    addresses = [address.strip() for address in f.readlines()]

tls = 0
ssl = 0
for address in addresses:
    if check_tls(address):
        tls += 1
    if check_ssl(address):
        ssl += 1

# Answer One
print("IPs Supporting TLS:", tls)

# Answer Two
print("IPs Supporting SSL:", ssl)
