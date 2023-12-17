from collections import deque

with open(0) as file:
    f = file.read().splitlines()


def func(j: int, i: int, dj: int, di: int) -> int:
    seen = set()
    q = deque([(j, i, dj, di)])
    while q:
        j, i, dj, di = q.popleft()

        j += dj
        i += di

        if j < 0 or len(f) <= j or i < 0 or len(f[0]) <= i:
            continue

        ch = f[j][i]

        if ch == "." or (ch == "-" and di != 0) or (ch == "|" and dj != 0):
            if (j, i, dj, di) not in seen:
                seen.add((j, i, dj, di))
                q.append((j, i, dj, di))

        elif ch == "\\":
            # -> v (0, 1) (1, 0)
            # ^ <- (-1, 0) (0, -1)
            # <- ^ (0, -1) (-1, 0)
            # v -> (1, 0) (0, 1)
            dj, di = di, dj
            if (j, i, dj, di) not in seen:
                seen.add((j, i, dj, di))
                q.append((j, i, dj, di))

        elif ch == "/":
            # -> ^ (0, 1) (-1, 0)
            # ^ -> (-1, 0) (0, 1)
            # <- v (0, -1) (1, 0)
            # v <- (1, 0) (0, -1)
            dj, di = -di, -dj
            if (j, i, dj, di) not in seen:
                seen.add((j, i, dj, di))
                q.append((j, i, dj, di))

        elif ch == "|":
            for dj, di in [(1, 0), (-1, 0)]:
                if (j, i, dj, di) not in seen:
                    seen.add((j, i, dj, di))
                    q.append((j, i, dj, di))

        elif ch == "-":
            for dj, di in [(0, 1), (0, -1)]:
                if (j, i, dj, di) not in seen:
                    seen.add((j, i, dj, di))
                    q.append((j, i, dj, di))

    return len({(j, i) for (j, i, _, _) in seen})


print(func(0, -1, 0, 1))


all_starting = (
    [(n, -1, 0, 1) for n in range(len(f))]  # from left
    + [(-1, n, 1, 0) for n in range(len(f[0]))]  # from top
    + [(n, len(f[0]), 0, -1) for n in range(len(f))]  # from right
    + [(len(f), n, -1, 0) for n in range(len(f[0]))]  # from bottom
)

lens = []

for j, i, dj, di in all_starting:
    lens.append(func(j, i, dj, di))

print(max(lens))
