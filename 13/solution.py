with open(0) as file:
    f = [l.split("\n") for l in file.read().strip().split("\n\n")]


def reflection_p1(block: list[str]) -> int:
    for j, _ in enumerate(block[1:], 1):
        curr_d = j
        curr_u = j - 1
        reflection = True
        while curr_d < len(block) and curr_u >= 0:
            if block[curr_u] != block[curr_d]:
                reflection = False
                break
            curr_d += 1
            curr_u -= 1
        if reflection:
            return j
    return 0


def reflection_p2(block: list[str]) -> int:
    for j, _ in enumerate(block[1:], 1):
        curr_d = j
        curr_u = j - 1
        total_dif = 0
        while curr_d < len(block) and curr_u >= 0:
            for pair in zip(block[curr_u], block[curr_d]):
                total_dif += pair[0] != pair[1]
            curr_d += 1
            curr_u -= 1
        if total_dif == 1:
            return j
    return 0


f_transpose = [["".join(l) for l in zip(*block)] for block in f]

total1 = 0
total2 = 0

for block in f:
    total1 += 100 * reflection_p1(block)
    total2 += 100 * reflection_p2(block)

for block in f_transpose:
    total1 += reflection_p1(block)
    total2 += reflection_p2(block)

print(total1)
print(total2)
