"""
Day 2 - tldr;

Pt. 1 - Find total lines where adjacent value in the line is 1 => and <= 3
Pt. 2 -
"""

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

# foo = []
# bar = []

# with open(input_file) as fh:
#     for line in fh.readlines():
#         values = [int(x) for x in line.strip().split()]
#         diffs = list(map(lambda x, y: y - x, values[:-1], values[1:]))

#         if all([1 <= x <= 3 for x in diffs]):
#             foo.append(values)

safe = []
unsafe = []

# print(len(foo))
# exit()

with open(input_file) as fh:
    for line in fh.readlines():
        values = [int(x) for x in line.strip().split()]

        if values[0] > values[-1]:
            # sort descending reports to make logic easier
            values = values[::-1]

        errors = 0

        # print(values)
        # # print()
        # # exit()

        # 1 2 3 4 8

        for idx, val in enumerate(values):
            if idx == len(values) - 1:
                # hit the end
                # safe.append(values)
                # break
                if errors > 1:
                    unsafe.append(values)
                else:
                    safe.append(values)
                break

            if not 1 <= values[idx + 1] - val <= 3:
                # current diff not in safe range

                if idx == len(values) - 2:
                    # hit the 2nd to last with an unsafe diff to last,
                    # test this edge case if removed if it makes it safe
                    if not 1 <= values[idx + 1] - values[idx - 1] <= 3:
                        unsafe.append(values)
                    else:
                        errors += 1
                        # break

                elif not 1 <= values[idx + 2] - val <= 3:
                    # look ahead to next item if we can omit one error
                    unsafe.append(values)
                    errors += 1
                    # break

                # errors += 1

        # if idx == len(values) - 1:
        #     if errors > 1:
        #         unsafe.append(values)
        #     else:
        #         safe.append(values)

print(f"pt. 2 answer: {len(safe)}")
