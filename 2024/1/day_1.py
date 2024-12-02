import os
from pathlib import Path

# expect input file in same dir
input_file = Path(__file__).resolve().parent.joinpath("input.txt")

all_left = []
all_right = []

with open(input_file) as fh:
    for line in fh.readlines():
        left, right = line.strip().split()
        all_left.append(int(left))
        all_right.append(int(right))

print(sum([abs(l - r) for l, r in zip(sorted(all_left), sorted(all_right))]))
