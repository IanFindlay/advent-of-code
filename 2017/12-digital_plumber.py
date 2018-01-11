"""Answers to Advent of Code Day 12."""

import re


def pipes(links, seed):
    """Return the group size of all pipes with a connection to 0."""
    # Split input into list of pipes and their connections
    link_list = links.strip().split('\n')

    # Create regex to isolate pipe name from its connections
    pipe_regex = re.compile(r'(\d*)\s*<->\s*(.*)')

    grouped = [seed]

    # Brute force cycling to get all connections because I'm shit at coding
    cycles = 0
    while cycles < 10:
        for pipe in link_list:
            pipe_num = pipe_regex.search(pipe).group(1)
            pipe_links = pipe_regex.search(pipe).group(2)

            links_split = re.split(', |, ', pipe_links)

            # Check if pipe_num is already in group and append its links if so
            if pipe_num in grouped:

                for number in links_split:
                    strip_num = number.strip()
                    grouped.append(strip_num)
                    pipe = ''

            else:
                # Check if any of the links are in the group
                for number in links_split:
                    strip_num = number.strip()

                    if strip_num in grouped:
                        grouped.append(pipe_num)
                        pipe = ''

                        for number in links_split:
                            strip_num = number.strip()
                            grouped.append(strip_num)

        cycles += 1

    # Challenge 1 Answer
    print(len(set(grouped)))


with open('input.txt') as f:
    survey = f.read()
    pipes(survey, '0')
