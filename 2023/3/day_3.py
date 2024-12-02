import os
from pathlib import Path
import re


# expect input file in same dir
input_file = Path(__file__).resolve().parent.joinpath("input.txt")

with open(input_file) as fh:
    contents = fh.read().splitlines()

prev_symbol_idxs = []
parts = []
# # contents = contents[:3]
# for x in contents:
#     print(x)
# sys.exit()

contents = [
    ".242......276....234............682.................",
    ".............*............................612*......",
    "..........346......................997........923...",
]

for idx, line in enumerate(contents):
    # print(line)
    # indexes of current lines symbols
    curr_symbol_idxs = [
        idx for idx, x in enumerate(line) if re.match("[^\w\s\.]", x)
    ]

    print(f"curr symbol idxs: {curr_symbol_idxs}")

    next_symbol_idxs = []
    if not idx + 1 == len(contents):
        # indexes of symbols in next line
        next_symbol_idxs = [
            idx
            for idx, x in enumerate(contents[idx + 1])
            if re.match("[^\w\s\.]", x)
        ]

    print(f"next symbol idxs: {next_symbol_idxs}")

    # get numbers with flanking symbols in current line
    curr_line_matches = re.findall(r"[^\w\s\.][\d]+|[\d]+[^\w\s\.]", line)

    # replace current line matches with . to ensure we don't double match
    # when checking for diagonal matches
    if curr_line_matches:
        print(curr_line_matches)
        for x in curr_line_matches:
            print(line)
            print(x)
            line = re.sub(re.escape(x), "." * len(x), line)
        # line = [re.sub(x, '.' * len(x), line) for x in curr_line_matches][0]

    print(f"curr line matches: {curr_line_matches}")

    # keep just digits of current line matches
    curr_line_matches = [re.sub(r"[^\d]", "", x) for x in curr_line_matches]

    # print(line)
    # print(list(re.finditer('\d+', line)))

    test = re.finditer("\d+", line)
    print(f"curr line nums: {list(test)}")

    for num in list(re.finditer("\d+", line)):
        num_idxs = list(range(num.start(), num.end() + 1))

        for x in num_idxs:
            if x in prev_symbol_idxs or x in next_symbol_idxs:
                curr_line_matches.append(num.group())

                print(num_idxs)
                print(f"matches diagonal: {num.group()}")

        if [x in prev_symbol_idxs for x in num_idxs]:
            curr_line_matches.append(num.group())

        if [x in next_symbol_idxs for x in num_idxs]:
            curr_line_matches.append(num.group())

        # print(num_idxs)

    # print(curr_line_matches)

    parts.extend(curr_line_matches)

    # for x in line:
    #     print(list(re.finditer('\d+', x)))

    # for char in line:
    #     digits = re.finditer('\d+', char)
    #     print([list(range(x.start() - 1, x.end() + 1)) for x in digits])

    prev_symbol_idxs = curr_symbol_idxs

print(f"Part 1 total: {sum([int(x) for x in parts])}")
