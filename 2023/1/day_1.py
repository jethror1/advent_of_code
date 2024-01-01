import os
from  pathlib import Path


# expect input file in same dir
input_file = Path(__file__).resolve().parent.joinpath('input.txt')

with open(input_file) as fh:
    contents = fh.read().splitlines()

# part 1
ints = [''.join(filter(str.isdigit, x)) for x in contents]
total = sum([int(x[0] + x[-1]) for x in ints])

print(f"Part 1: {total}")


# part 2
mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

ints = []

for line in contents:
    line_ints = []

    for idx, char in enumerate(line, 1):
        if str.isdigit(char):
            line_ints.append(int(char))

        # int as a word can only be 3, 4 or 5 letters
        selected = [
            mapping.get(x) for x in [
                line[:idx][-3:], line[:idx][-4:], line[:idx][-5:]
            ]
        ]
        if any(selected):
            # found a word int, add it and reset word builder
            line_ints.append(max([x for x in selected if x]))

    ints.append(int(f"{line_ints[0]}{line_ints[-1]}"))

print(f"Part 2: {sum(ints)}")
