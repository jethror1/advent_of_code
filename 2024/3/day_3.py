"""
Day 3 - tldr;

Pt. 1 - sum all matches of the `mul(\d+,\d+)` evaluated in the input string
Pt. 2 - same as above but only select from between do() and don't() matches
"""

from operator import mul
import os
from pathlib import Path
import re

# expect input.txt file in same dir
input_file = Path(__file__).resolve().parent.joinpath("input.txt")

total = sum(
    eval(x)
    for x in re.findall(r"mul\(\d+,\d+\)", Path(input_file).read_text())
)

print(f"pt. 1 answer: {total}")

# pt. 2
text = Path(input_file).read_text().replace("\n", " ")

initial_muls = re.findall(
    r"mul\(\d+,\d+\)", re.match(r"^.+?(?=don't\(\)|do\(\)|$)", text).group()
)
rest_of_muls = re.findall(
    r"mul\(\d+,\d+\)", "".join(re.findall(r"do\(\).+?(?=don't\(\)|$)", text))
)

total = sum(eval(x) for x in initial_muls + rest_of_muls)

print(f"pt. 2 answer: {total}")
