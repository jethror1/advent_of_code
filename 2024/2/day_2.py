import os
from pathlib import Path

# expect input.txt file in same dir
input_file = Path(__file__).resolve().parent.joinpath("input.txt")

safe = []
unsafe = []

with open(input_file) as fh:
    for line in fh.readlines():
        values = [int(x) for x in line.strip().split()]

        if values[0] > values[-1]:
            # sort descending reports to make logic easier
            values = values[::-1]

        for idx, val in enumerate(values):
            if idx == len(values) - 1:
                # hit the end => safe
                safe.append(values)
                break

            if not 1 <= values[idx + 1] - val <= 3:
                unsafe.append(values)
                break

print(f"pt. 1 answer: {len(safe)}")
