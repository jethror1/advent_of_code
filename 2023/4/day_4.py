import re
import sys

with open(sys.argv[1]) as fh:
    contents = fh.read().rstrip("\n").splitlines()

total = 0

# pt 1
for line in contents:
    winning, selected = line.split("|")
    winning = set(re.findall(r"\d+", winning.split(":")[1]))
    selected = set(re.findall(r"\d+", selected))
    won = len(winning - (winning - selected))

    if won == 0:
        continue
    elif won == 1:
        total += 1
    else:
        total += 2 ** (won - 1)
