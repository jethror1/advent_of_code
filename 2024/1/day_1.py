"""
Day 1 - tldr

Pt. 1 - Find the summed pairwise diff of 2 lists
Pt. 2 - Find the summed count of left items in right multiplied by the item value
"""

import os
from pathlib import Path

# expect input.txt file in same dir
input_file = Path(__file__).resolve().parent.joinpath("input.txt")

all_left = []
all_right = []

with open(input_file) as fh:
    for line in fh.readlines():
        left, right = line.strip().split()
        all_left.append(int(left))
        all_right.append(int(right))

total = sum([abs(l - r) for l, r in zip(sorted(all_left), sorted(all_right))])

print(f"pt. 1 answer: {total}")

similarity = sum([(all_right.count(i) * i) for i in all_left])

print(f"pt. 2 answer: {similarity}")
