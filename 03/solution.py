from typing import Tuple, List
import re

with open(0) as file:
    f = file.read().splitlines()

# f = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".split()

non_symbols = [str(n) for n in range(10)]
non_symbols.append(".")
symbols = set()

for l in f:
    for c in l:
        if c not in non_symbols:
            symbols.add(c)


def get_boundary_coords(
    current_line: int, max_lines: int, line_length: int, span: Tuple[int, int]
) -> List[Tuple[int, int]]:
    coords = []

    # UP
    if current_line != 0:
        for i in range(span[0], span[1]):
            coords.append((current_line - 1, i))

        # UP LEFT
        if span[0] > 0:
            coords.append((current_line - 1, span[0] - 1))

        # UP RIGHT
        if span[1] < line_length:
            coords.append((current_line - 1, span[1]))

    # DOWN
    if current_line != max_lines - 1:
        for i in range(span[0], span[1]):
            coords.append((current_line + 1, i))

        # DOWN LEFT
        if span[0] > 0:
            coords.append((current_line + 1, span[0] - 1))

        # DOWN RIGHT
        if span[1] < line_length:
            coords.append((current_line + 1, span[1]))

    # LEFT
    if span[0] > 0:
        coords.append((current_line, span[0] - 1))

    # RIGHT
    if span[1] < line_length:
        coords.append((current_line, span[1]))

    return coords


total = 0

for curr, l in enumerate(f):
    result = re.finditer(r"\d+", l)

    for r in result:
        coords = get_boundary_coords(curr, len(f), len(l), r.span())

        for coord in coords:
            if f[coord[0]][coord[1]] in symbols:
                total += int(r.group())
                break

print(total)

spans = []

for curr, l in enumerate(f):
    result = re.finditer(r"\d+", l)
    for r in result:
        spans.append([curr, r.span()])

total = 0

for r, l in enumerate(f):
    for c, ch in enumerate(l):
        if ch != "*":
            continue

        nums = set()
        coords = get_boundary_coords(r, len(f), len(l), (c, c + 1))

        for coord in coords:
            if f[coord[0]][coord[1]].isdigit():
                for i, s in enumerate(spans):
                    if s[0] == coord[0] and s[1][0] <= coord[1] and coord[1] < s[1][1]:
                        num = int(f[s[0]][s[1][0] : s[1][1]])
                        nums.add(num)

        if len(nums) == 2:
            nums = list(nums)
            total += nums[0] * nums[1]

print(total)
