import os
from  pathlib import Path


# expect input file in same dir
input_file = Path(__file__).resolve().parent.joinpath('input.txt')

with open(input_file) as fh:
    contents = fh.read().splitlines()

ints = [''.join(filter(str.isdigit, x)) for x in contents]
total = sum([int(x[0] + x[-1]) for x in ints])

print(total)
