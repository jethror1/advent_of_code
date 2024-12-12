"""
Day 2 - tldr;

Pt. 1 - Find total lines where adjacent value in the line is 1 => and <= 3
Pt. 2 -
"""

import os
from pathlib import Path

# expect input.txt file in same dir
input_file = Path(__file__).resolve().parent.joinpath("input.txt")

safe = 0

with open(input_file) as fh:
    for line in fh.readlines():
        values = [int(x) for x in line.strip().split()]

        if values[0] > values[-1]:
            # sort descending reports to make logic easier
            values = values[::-1]

        for idx, val in enumerate(values):
            if idx == len(values) - 1:
                # hit the end => safe
                safe += 1
                break

            if not 1 <= values[idx + 1] - val <= 3:
                break

print(f"pt. 1 answer: {safe}")

# part 2
safe = 0

with open(input_file) as fh:
    for line in fh.readlines():
        values = [int(x) for x in line.strip().split()]

        if values[0] > values[-1]:
            # sort descending reports to make logic easier
            values = values[::-1]

        all_diffs = []

        for idx, val in enumerate(values):
            # find all diffs between adjacent numbers for all permutations
            # of the line with one number missing, if any of these are valid
            # then this one is safe
            values_without_val = values.copy()
            values_without_val.pop(idx)

            all_diffs.append(
                list(
                    map(
                        lambda x, y: y - x,
                        values_without_val[:-1],
                        values_without_val[1:],
                    )
                )
            )

        if any(
            [all([1 <= x <= 3 for x in sub_diffs]) for sub_diffs in all_diffs]
        ):
            safe += 1

print(f"pt. 2 answer: {safe}")
