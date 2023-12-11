with open(0) as file:
    f = file.read().splitlines()

empty_rows = [j for j, l in enumerate(f) if l == len(l) * "."]
empty_cols = [i for i, c in enumerate(zip(*f)) if "".join(c) == len(c) * "."]

stars = [(j, i) for j, l in enumerate(f) for i, c in enumerate(l) if c == "#"]

EXPANSE = 1000000

total = 0
for n, (j1, i1) in enumerate(stars[:-1]):
    for j2, i2 in stars[n + 1 :]:
        for j in range(min(j1, j2), max(j1, j2)):
            total += EXPANSE if j in empty_rows else 1
        for i in range(min(i1, i2), max(i1, i2)):
            total += EXPANSE if i in empty_cols else 1

print(total)
