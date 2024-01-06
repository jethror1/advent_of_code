from math import prod
import os
from  pathlib import Path
import re


# expect input file in same dir
input_file = Path(__file__).resolve().parent.joinpath('input.txt')

with open(input_file) as fh:
    contents = fh.read().splitlines()


# part 1
games = []

for line in contents:
    game, values = line.split(':', 1)
    game = int(re.search(r'[\d]+', game).group())
    valid = True

    for subset in values.split(';'):
        red = int(re.sub(r'[^0-9]', '', re.search(r'\d+ red|$', subset).group()) or 0)
        blue = int(re.sub(r'[^0-9]', '', re.search(r'\d+ blue|$', subset).group()) or 0)
        green = int(re.sub(r'[^0-9]', '', re.search(r'\d+ green|$', subset).group()) or 0)

        if not all([red <= 12, green <= 13, blue <=14]):
            valid = False
            break

    if valid:
        games.append(game)

print(f"Part 1: {sum(games)}")

# part 2
power = 0

for line in contents:
    game, values = line.split(':', 1)
    game = int(re.search(r'[\d]+', game).group())
    valid = True

    colours = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for subset in values.split(';'):
        for colour in colours.keys():
            value = int(re.sub(r'[^0-9]', '', re.search(rf'\d+ {colour}|$', subset).group()) or 0)
            if value > colours.get(colour):
                colours[colour] = value

    power += prod([x for x in colours.values() if x])

print(f"Part 2: {power}")
