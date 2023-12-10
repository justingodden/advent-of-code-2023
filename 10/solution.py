with open(0) as file:
    f = file.read().splitlines()


for j, l in enumerate(f):
    for i, ch in enumerate(l):
        if ch == "S":
            sj, si = j, i

loop = [(sj, si), (sj + 1, si)]
coords = sj + 1, si
prev_dir = "UP"
steps = 1

while True:
    curr = f[coords[0]][coords[1]]
    match curr:
        case "|":
            if prev_dir == "UP":
                coords = coords[0] + 1, coords[1]  # down
                prev_dir = "UP"
            else:
                coords = coords[0] - 1, coords[1]  # up
                prev_dir = "DOWN"
        case "-":
            if prev_dir == "LEFT":
                coords = coords[0], coords[1] + 1  # right
                prev_dir = "LEFT"
            else:
                coords = coords[0], coords[1] - 1  # left
                prev_dir = "RIGHT"
        case "L":
            if prev_dir == "UP":
                coords = coords[0], coords[1] + 1  # right
                prev_dir = "LEFT"
            else:
                coords = coords[0] - 1, coords[1]  # up
                prev_dir = "DOWN"
        case "J":
            if prev_dir == "UP":
                coords = coords[0], coords[1] - 1  # left
                prev_dir = "RIGHT"
            else:
                coords = coords[0] - 1, coords[1]  # up
                prev_dir = "DOWN"
        case "7":
            if prev_dir == "DOWN":
                coords = coords[0], coords[1] - 1  # left
                prev_dir = "RIGHT"
            else:
                coords = coords[0] + 1, coords[1]  # down
                prev_dir = "UP"
        case "F":
            if prev_dir == "DOWN":
                coords = coords[0], coords[1] + 1  # right
                prev_dir = "LEFT"
            else:
                coords = coords[0] + 1, coords[1]  # down
                prev_dir = "UP"
        case "S":
            break
    loop.append(coords)
    steps += 1

print(steps // 2)

for j, l in enumerate(f):
    f[j] = [*l]

f[sj][si] = "7"  # by inspections

for j, l in enumerate(f):
    for i, ch in enumerate(l):
        if (j, i) not in loop:
            f[j][i] = "."

for j, l in enumerate(f):
    l = "".join([ch for ch in l if ch != "-"])
    l = l.replace("L7", "|")
    l = l.replace("LJ", "")
    l = l.replace("F7", "")
    l = l.replace("FJ", "|")
    f[j] = l

outside = 0

for j, l in enumerate(f):
    for i, ch in enumerate(l):
        if ch == ".":
            if i != len(l) - 1:
                crosses = 0
                for k in l[i + 1 :]:
                    if k != ".":
                        crosses += 1
                if crosses % 2 != 0:
                    outside += 1

print(outside)
