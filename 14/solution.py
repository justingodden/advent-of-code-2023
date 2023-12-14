with open(0) as file:
    f = file.read().splitlines()


def slide_left(f_T: list[str]) -> list[str]:
    for j, l in enumerate(f_T):
        l = l.split("#")
        segments = []
        for segment in l:
            tmp = ""
            tmp += "O" * segment.count("O")
            tmp += "." * segment.count(".")
            segments.append(tmp)

        f_T[j] = "#".join(segments)
    return f_T


p1 = ["".join(c) for c in zip(*f)]
p1 = slide_left(p1)

total = 0
for i, col in enumerate(zip(*p1)):
    total += (len(f) - i) * col.count("O")

print(total)


p2 = ["".join(c) for c in zip(*f)]
seen = set()
grids = []
i = 0

while True:
    if tuple(p2) in seen:
        break
    seen.add(tuple(p2))
    grids.append(tuple(p2))
    i += 1

    p2 = slide_left(p2)
    p2 = ["".join(c) for c in zip(*p2)]
    p2 = slide_left(p2)
    p2 = ["".join(c)[::-1] for c in zip(*p2)]
    p2 = slide_left(p2)
    p2 = ["".join(c)[::-1] for c in zip(*p2)][::-1]
    p2 = slide_left(p2)
    p2 = ["".join(c) for c in zip(*p2)][::-1]

first_seen = grids.index(tuple(p2))
cycle_length = i - first_seen

cycles = 1000000000
pos = first_seen + ((cycles - first_seen) % cycle_length)

total = 0
for i, col in enumerate(zip(*grids[pos])):
    total += (len(f) - i) * col.count("O")

print(total)
